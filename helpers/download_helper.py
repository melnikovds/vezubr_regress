import os
import re
import time
import requests
from pathlib import Path
from typing import Optional, Tuple, Dict, Any
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from typing import Optional, Tuple, Callable


class DownloadHelper:
    """
    Хелпер для работы с выгрузками файлов.
    Использует куки из браузера для авторизации в API.
    """

    def __init__(self, driver, base: 'Base'):
        """
        Инициализация хелпера.

        Parameters
        ----------
        driver : WebDriver
            Драйвер Selenium
        base : Base
            Экземпляр базового класса (для доступа к методам ожидания)
        """
        self.driver = driver
        self.base = base
        self.session = requests.Session()
        self._copy_cookies_from_driver()

    def _copy_cookies_from_driver(self) -> None:
        """
        Копирует все куки из браузера в requests-сессию.
        Это обеспечивает авторизацию при скачивании.
        """
        for cookie in self.driver.get_cookies():
            self.session.cookies.set(cookie['name'], cookie['value'])

        # Для надежности добавляем common headers
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        })

    def refresh_cookies(self) -> None:
        """
        Обновляет куки в сессии (полезно, если сессия истекла).
        """
        self.session.cookies.clear()
        self._copy_cookies_from_driver()

    def get_download_link_from_notification(
            self,
            notification_text: str = "Выгрузка в файл готова",
            timeout: int = 15,
            wait_for_spinner: bool = True
    ) -> str:
        """
        Ждет появления уведомления и извлекает ссылку на скачивание.

        Parameters
        ----------
        notification_text : str
            Текст уведомления для поиска
        timeout : int
            Максимальное время ожидания в секундах
        wait_for_spinner : bool
            Ждать ли исчезновения спиннера перед поиском уведомления

        Returns
        -------
        str
            Полный URL для скачивания (с протоколом)

        Raises
        ------
        TimeoutException
            Если уведомление не появилось за отведенное время
        AssertionError
            Если ссылка не найдена в уведомлении
        """
        with allure.step(f"Ожидание уведомления '{notification_text}'"):
            # Сначала ждем исчезновения спиннера (если он есть)
            if wait_for_spinner:
                try:
                    self.base.get_element(self.base.loading_form, wait_type="invisibility")
                except:
                    pass  # Игнорируем, если спиннера нет

            # Ищем уведомление по тексту
            notification_xpath = f"//*[contains(text(), '{notification_text}')]"

            # Ждем появления уведомления
            notification = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, notification_xpath))
            )

            # Ищем ссылку внутри уведомления
            try:
                link_element = notification.find_element(By.TAG_NAME, "a")
                href = link_element.get_attribute("href")
            except:
                # Если ссылка не нашлась внутри, ищем её рядом с уведомлением
                link_element = self.driver.find_element(
                    By.XPATH,
                    f"{notification_xpath}/ancestor::div[1]//a"
                )
                href = link_element.get_attribute("href")

            # Нормализуем URL (добавляем протокол если нужно)
            if href and href.startswith("//"):
                # Определяем протокол из текущего URL
                current_url = self.driver.current_url
                protocol = "https:" if current_url.startswith("https") else "http:"
                href = protocol + href

            assert href, "Ссылка на скачивание не найдена в уведомлении"

            allure.attach(href, "Ссылка на скачивание", allure.attachment_type.TEXT)
            return href

    def download_file_via_api(
            self,
            url: str,
            expected_filename_pattern: Optional[str] = None,
            timeout: int = 30,
            min_size_bytes: int = 100
    ) -> Tuple[int, str, bytes]:
        """
        Скачивает файл через requests и проверяет его.

        Parameters
        ----------
        url : str
            URL для скачивания
        expected_filename_pattern : str, optional
            Ожидаемый паттерн в имени файла (например, "Список Заказов")
        timeout : int
            Таймаут на скачивание в секундах
        min_size_bytes : int
            Минимальный размер файла в байтах

        Returns
        -------
        Tuple[int, str, bytes]
            (статус_код, имя_файла, содержимое_файла)

        Raises
        ------
        Exception
            Если скачивание не удалось или файл не прошел проверки
        """
        with allure.step(f"Скачивание файла..."):
            # Обновляем куки перед запросом (на случай, если сессия обновилась)
            self.refresh_cookies()

            # Выполняем запрос
            response = self.session.get(
                url,
                stream=True,
                timeout=timeout,
                allow_redirects=True
            )

            # Проверяем статус
            if response.status_code != 200:
                raise Exception(
                    f"Ошибка скачивания: статус {response.status_code}. "
                    f"URL: {url}"
                )

            # Извлекаем имя файла из Content-Disposition
            filename = self._extract_filename_from_response(response, url)

            # Получаем содержимое
            content = response.content

            # Проверяем, что файл не пустой
            if len(content) < min_size_bytes:
                raise Exception(
                    f"Файл слишком маленький: {len(content)} байт "
                    f"(ожидалось >= {min_size_bytes} байт)"
                )

            # Проверяем, что это Excel файл (по сигнатуре)
            is_excel = self._check_excel_signature(content)
            if not is_excel:
                # Не строгая проверка, только предупреждение
                allure.attach(
                    f"Предупреждение: файл '{filename}' может не быть Excel. "
                    f"Первые 20 байт: {content[:20].hex()}",
                    "Проверка формата",
                    allure.attachment_type.TEXT
                )

            # Проверяем паттерн в имени файла
            if expected_filename_pattern:
                assert expected_filename_pattern in filename, \
                    f"Имя файла '{filename}' не содержит '{expected_filename_pattern}'"

            # Логируем результат
            allure.attach(
                f"Имя файла: {filename}\n"
                f"Размер: {len(content)} байт ({len(content) / 1024:.2f} KB)\n"
                f"Статус: {response.status_code}\n"
                f"Content-Type: {response.headers.get('Content-Type', 'unknown')}",
                "Информация о файле",
                allure.attachment_type.TEXT
            )

            return response.status_code, filename, content

    def _extract_filename_from_response(self, response: requests.Response, url: str) -> str:
        """
        Извлекает имя файла из заголовков или URL.
        """
        # Пробуем из Content-Disposition
        content_disposition = response.headers.get('Content-Disposition', '')
        if 'filename=' in content_disposition:
            # Парсим filename
            match = re.search(r'filename[^;=\n]*=(([\'"]).*?\2|[^;\n]*)', content_disposition)
            if match:
                filename = match.group(1).strip('"\'')
                # Декодируем URL-кодировку если есть
                try:
                    from urllib.parse import unquote
                    filename = unquote(filename)
                except:
                    pass
                return filename

        # Пробуем из URL
        url_filename = url.split('/')[-1].split('?')[0]
        if url_filename and '.' in url_filename:
            return url_filename

        # Генерируем имя по умолчанию
        return f"export_{self.base.get_timestamp()}.xlsx"

    def _check_excel_signature(self, content: bytes) -> bool:
        """
        Проверяет сигнатуру файла на соответствие Excel форматам.
        """
        if len(content) < 8:
            return False

        # Проверка на .xlsx (ZIP)
        if content[:4] in (b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'):
            return True

        # Проверка на .xls (OLE)
        if content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            return True

        return False

    def download_and_save_file(
            self,
            url: str,
            save_path: Optional[str] = None,
            expected_filename_pattern: Optional[str] = None
    ) -> str:
        """
        Скачивает файл и сохраняет его на диск.

        Parameters
        ----------
        url : str
            URL для скачивания
        save_path : str, optional
            Путь для сохранения (если не указан, сохраняет в папку downloads)
        expected_filename_pattern : str, optional
            Ожидаемый паттерн в имени файла

        Returns
        -------
        str
            Полный путь к сохраненному файлу
        """
        status, filename, content = self.download_file_via_api(
            url,
            expected_filename_pattern=expected_filename_pattern
        )

        # Определяем путь для сохранения
        if not save_path:
            # Создаем папку downloads в корне проекта
            project_root = Path(__file__).parent.parent
            download_dir = project_root / "downloads"
            download_dir.mkdir(exist_ok=True)
            save_path = str(download_dir / filename)

        # Сохраняем файл
        with open(save_path, 'wb') as f:
            f.write(content)

        allure.attach.file(
            save_path,
            f"Сохраненный файл: {filename}",
            allure.attachment_type.TEXT
        )

        print(f"💾 Файл сохранен: {save_path}")
        return save_path

    def capture_download_url_from_network(
            self,
            click_action: Callable,
            url_pattern: str = "/download-file/",
            timeout: int = 10
    ) -> str:
        """
        Перехватывает URL скачивания из сетевых запросов через CDP.

        Parameters
        ----------
        click_action : Callable
            Функция, которая выполняет клик по кнопке выгрузки
        url_pattern : str
            Паттерн для поиска URL (по умолчанию "/download-file/")
        timeout : int
            Таймаут ожидания запроса в секундах

        Returns
        -------
        str
            URL для скачивания
        """
        with allure.step(f"Перехват сетевого запроса с паттерном '{url_pattern}'"):
            # Включаем логирование сети
            self.driver.execute_cdp_cmd('Network.enable', {})

            # Создаем JavaScript коллектор для перехвата URL
            self.driver.execute_script("""
                window.__downloadUrls = [];
                window.__originalFetch = window.fetch;
                window.fetch = function(...args) {
                    const url = args[0];
                    if (typeof url === 'string' && url.indexOf(arguments[0]) !== -1) {
                        window.__downloadUrls.push(url);
                    }
                    return window.__originalFetch.apply(this, args);
                };
            """, url_pattern)

            # Также перехватываем XMLHttpRequest
            self.driver.execute_script("""
                window.__originalXHROpen = XMLHttpRequest.prototype.open;
                XMLHttpRequest.prototype.open = function(method, url, ...args) {
                    if (typeof url === 'string' && url.indexOf(arguments[0]) !== -1) {
                        window.__downloadUrls.push(url);
                    }
                    return window.__originalXHROpen.apply(this, [method, url, ...args]);
                };
            """, url_pattern)

            # Выполняем клик
            click_action()

            # Ждем появления запроса
            start = time.time()
            download_urls = []
            while time.time() - start < timeout:
                urls = self.driver.execute_script("return window.__downloadUrls;")
                if urls:
                    download_urls = urls
                    break
                time.sleep(0.5)

            # Восстанавливаем оригинальные функции
            self.driver.execute_script("""
                window.fetch = window.__originalFetch;
                XMLHttpRequest.prototype.open = window.__originalXHROpen;
                delete window.__downloadUrls;
                delete window.__originalFetch;
                delete window.__originalXHROpen;
            """)

            # Отключаем логирование
            self.driver.execute_cdp_cmd('Network.disable', {})

            if not download_urls:
                raise Exception(f"Не перехвачен запрос с паттерном '{url_pattern}'")

            url = download_urls[0]
            if url.startswith('//'):
                protocol = "https:" if self.driver.current_url.startswith("https") else "http:"
                url = protocol + url

            allure.attach(url, "Перехваченный URL скачивания", allure.attachment_type.TEXT)
            return url

