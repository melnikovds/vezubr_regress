import os

import allure
import time
from typing import Tuple, Optional
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class UploadingDocumentsPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ==================== ОБЩИЕ ЛОКАТОРЫ ====================

    # Кнопка меню (три точки) - общая для всех
    menu_dots = {
        "xpath": "//img[@alt='dotsBlue']",
        "name": "menu_dots"
    }

    # Кнопка "OK" в уведомлении
    export_ok = {
        "xpath": "//button[@id='export-ok']",
        "name": "export_ok"
    }

    # Ссылка на скачивание в уведомлении
    download_link = {
        "xpath": "//a[contains(text(), 'ссылка')]",
        "name": "download_link"
    }

    # Кнопка "Выгрузить в Excel" в окне уведомлений
    download_excel = {
        "xpath": "//button[contains(@class, 'ant-btn ant-btn-default')]",
        "name": "download_excel"
    }
    export_download = {
        "xpath": "//span[contains(text(), 'Выгрузить в Excel')]",
        "name": "export_download"
    }


    insurance_company = {
        "xpath": "//div[@class='cell-text-overflow-content']//a[@class='link-back'][normalize-space()='7705041231']",
        "name": "insurance_company"
    }
    insured_flights = {
        "xpath": "//a[contains(text(),'Застрахованные рейсы')]",
        "name": "insured_flights"
    }

    lkz_requests_download = {
        "xpath": "//div[@class='dashboard-content margin-top-60']//a[2]//li[1]",
        "name": "lkz_requests_download"
    }

    export_menu = {
        "xpath": "//img[@alt='dotsBlue']",
        "name": "lkz_gm_export_menu"
    }

    lkz_export_download = {
        "xpath": "//span[contains(text(), 'Выгрузить в Excel')]",
        "name": "lkz_export_download"
    }

    lkz_export_download_excel = {
        "xpath": "//button[@class='ant-btn ant-btn-default']",
        "name": "lkz_export_download_excel"
    }

    lkz_export_ok = {
        "xpath": "//button[@id='export-ok']",
        "name": "lkz_export_ok"
    }

    lkz_export_link = {
        "xpath": "//a[contains(text(), 'ссылка')]",
        "name": "lkz_export_link"
    }

    lkz_users_button = {
        "xpath": "//a[contains(text(),'Пользователи')]",
        "name": "lkz_users_button"
    }

    lkz_users_export_menu = {
        "xpath": "//button[@id='employees-menu']//img[@alt='dotsBlue']",
        "name": "lkz_users_export_menu"
    }

    # ==================== ОБЩИЕ МЕТОДЫ ====================

    def _get_download_link(self, link_locator: dict = None, timeout: int = 30) -> str:
        """
        Ожидает появления уведомления со ссылкой и возвращает ссылку.

        Parameters
        ----------
        link_locator : dict, optional
            Локатор ссылки. Если не передан, используется стандартный.
        timeout : int
            Таймаут ожидания в секундах
        """
        if link_locator is None:
            link_locator = self.download_link

        with allure.step("Ожидание ссылки на скачивание в уведомлении"):
            link_element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, link_locator["xpath"]))
            )

            href = link_element.get_attribute("href")

            if href and href.startswith("//"):
                current_url = self.driver.current_url
                protocol = "https:" if current_url.startswith("https") else "http:"
                href = protocol + href

            assert href, "Ссылка на скачивание не найдена"

            allure.attach(href, "Ссылка на скачивание", allure.attachment_type.TEXT)
            return href

    # ==================== МЕТОДЫ LKZ ====================

    def export_cargo_delivery_requests_lkz(self) -> Tuple[int, str, bytes]:
        """
        Выгрузка заявок на доставку груза для LKZ.
        """
        with allure.step("Выгрузка заявок на доставку груза (LKZ)"):
            self.click_button(self.menu_dots)
            time.sleep(1)
            self.click_button(self.lkz_requests_download)
            time.sleep(1)
            self.click_button(self.download_excel)
            time.sleep(1)
            self.click_button(self.export_ok)
            time.sleep(2)

            link = self._get_download_link()
            return self.download_file_via_api(link)

    def export_all(self) -> Tuple[int, str, bytes]:
        """
        Выгрузка ГМ (Грузовых модулей) для LKZ.

        Последовательность:
        1. Нажать на меню (три точки)
        2. Выбрать "Выгрузить в Excel"
        3. Нажать на кнопку Excel в уведомлении
        4. Нажать "OK" в уведомлении
        5. Получить ссылку и скачать
        """
        with allure.step("Выгрузка"):
            # 1. Открываем меню (три точки)
            self.click_button(self.export_menu)
            time.sleep(1)

            # 2. Выбираем "Выгрузить в Excel"
            self.click_button(self.lkz_export_download)
            time.sleep(1)

            # 3. Нажимаем на кнопку Excel в уведомлении
            self.click_button(self.lkz_export_download_excel)
            time.sleep(1)

            # 4. Нажимаем "OK" в уведомлении
            self.click_button(self.lkz_export_ok)
            time.sleep(2)

            # 5. Получаем ссылку и скачиваем
            link = self._get_download_link(self.lkz_export_link)
            return self.download_file_via_api(link)

    def export_users_lkz(self) -> Tuple[int, str, bytes]:
        """
        Выгрузка пользователей для LKZ.

        Последовательность:
        1. Нажать на кнопку "Пользователи"
        2. Нажать на меню (три точки)
        3. Выбрать "Выгрузить в Excel"
        4. Нажать на кнопку Excel в уведомлении
        5. Нажать "OK" в уведомлении
        6. Получить ссылку и скачать
        """
        with allure.step("Выгрузка пользователей (LKZ)"):
            # 1. Нажимаем на кнопку "Пользователи"
            self.click_button(self.lkz_users_button)
            time.sleep(1)

            # 2. Открываем меню (три точки)
            self.click_button(self.lkz_users_export_menu)
            time.sleep(1)

            # 3. Выбираем "Выгрузить в Excel"
            self.click_button(self.lkz_export_download)
            time.sleep(1)

            # 4. Нажимаем на кнопку Excel в уведомлении
            self.click_button(self.lkz_export_download_excel)
            time.sleep(1)

            # 5. Нажимаем "OK" в уведомлении
            self.click_button(self.lkz_export_ok)
            time.sleep(2)

            # 6. Получаем ссылку и скачиваем
            link = self._get_download_link(self.lkz_export_link)
            return self.download_file_via_api(link)

    def export_insurance_all(self) -> Tuple[int, str, bytes]:
        """
        Выгрузка ГМ (Грузовых модулей) для LKZ.

        Последовательность:
        1. Нажать на меню (три точки)
        2. Выбрать "Выгрузить в Excel"
        3. Нажать на кнопку Excel в уведомлении
        4. Нажать "OK" в уведомлении
        5. Получить ссылку и скачать
        """
        with allure.step("Выгрузка"):
            # 1. Выбираем страховую компанию
            self.click_button(self.insurance_company)
            time.sleep(1)

            # 2. Переходим в застрахованные рейсы
            self.click_button(self.insured_flights)
            time.sleep(1)

            # 3. Открываем меню (три точки)
            self.click_button(self.export_menu)
            time.sleep(1)

            # 4. Выбираем "Выгрузить в Excel"
            self.click_button(self.lkz_export_download)
            time.sleep(1)

            # 5. Нажимаем на кнопку Excel в уведомлении
            self.click_button(self.lkz_export_download_excel)
            time.sleep(1)

            # 6. Нажимаем "OK" в уведомлении
            self.click_button(self.lkz_export_ok)
            time.sleep(2)

            # 7. Получаем ссылку и скачиваем
            link = self._get_download_link(self.lkz_export_link)
            return self.download_file_via_api(link)

    def export_all_1(self) -> Tuple[int, str, bytes]:
        with allure.step("Выгрузка"):
            # 1. Открываем меню (три точки)
            self.click_button(self.export_menu)
            time.sleep(1)

            # 2. Выбираем "Выгрузить в Excel"
            self.click_button(self.lkz_export_download)
            time.sleep(3)  # Даем время на скачивание

            # 3. Получаем последний скачанный файл
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
            files = [f for f in os.listdir(downloads_path) if f.endswith('.xlsx')]

            if not files:
                raise AssertionError("Файл Excel не был скачан")

            # Берем самый новый файл
            latest_file = max(files, key=lambda f: os.path.getctime(os.path.join(downloads_path, f)))
            file_path = os.path.join(downloads_path, latest_file)

            # Читаем содержимое файла
            with open(file_path, 'rb') as f:
                content = f.read()

            # Возвращаем статус, имя файла и содержимое
            return 200, latest_file, content

    def export_direct_download(self, expected_filename_pattern: str = None) -> Tuple[int, str, bytes]:
        """
        Выгрузка через прямое скачивание в папку Downloads.
        Ищет файл по паттерну в имени.

        Parameters
        ----------
        expected_filename_pattern : str, optional
            Ожидаемый паттерн в имени файла (например, "Список_водителей")
        """
        with allure.step("Прямая выгрузка через браузер"):
            # 1. Открываем меню (три точки)
            self.click_button(self.menu_dots)
            time.sleep(1)

            # 2. Выбираем "Выгрузить в Excel"
            self.click_button(self.export_download)

            # 3. Ждем скачивания
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
            timeout = 30
            start = time.time()
            new_file = None

            # Получаем список файлов до скачивания
            before_files = set(os.listdir(downloads_path))

            while time.time() - start < timeout:
                after_files = set(os.listdir(downloads_path))
                new_files = after_files - before_files

                # Ищем новый файл с нужным паттерном
                for f in new_files:
                    # Исключаем временные файлы
                    if f.endswith('.crdownload') or f.endswith('.tmp'):
                        continue

                    # Если указан паттерн — ищем его в имени
                    if expected_filename_pattern:
                        if expected_filename_pattern in f:
                            new_file = f
                            break
                    # Если паттерн не указан — берем любой .csv или .xlsx
                    elif f.endswith('.csv') or f.endswith('.xlsx'):
                        new_file = f
                        break

                if new_file:
                    break
                time.sleep(1)

            if not new_file:
                raise AssertionError("Файл не был скачан за отведенное время")

            file_path = os.path.join(downloads_path, new_file)

            # Ждем, пока файл полностью запишется
            time.sleep(1)

            # Читаем содержимое файла
            with open(file_path, 'rb') as f:
                content = f.read()

            # Удаляем файл из папки Downloads
            try:
                os.remove(file_path)
                print(f"🗑️ Файл удален из папки Downloads: {new_file}")
            except:
                pass

            return 200, new_file, content


