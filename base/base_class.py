import os
import platform
import random
import re
import time
from datetime import datetime, timezone, timedelta
from typing import Any, ClassVar, Dict, Type, NoReturn, Optional

import allure
from selenium import webdriver
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""Variable"""
# Определение пути к драйверам
WINDOWS_DRIVER_PATH = os.path.join('resource', 'windows', 'chromedriver.exe')
LINUX_DRIVER_PATH = '/app/resource/linux/chromedriver'


class Base:
    """
    Базовый класс содержащий методы для взаимодействия с веб-драйвером.
    """
    driver: WebDriver
    loading_form: ClassVar[Dict[str, str]]
    loading_list: ClassVar[Dict[str, str]]

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует экземпляр класса с драйвером.

        Parameters
        ----------
        driver : WebDriver
            Драйвер для управления браузером.
        """
        self.driver = driver

    """ Main locators"""
    loading_form = {
        "xpath": "(//div[@id='loader'])[2]",
        "name": "loading_form"
    }
    loading_list = {
        "xpath": "//span[@class='ant-spin-dot ant-spin-dot-spin']",
        "name": "loading_list"
    }
    sorting_button = {
        "xpath": "//span[@class='ant-table-column-sorter']/div[@title='Сортировка']",
        "name": "sorting_button"
    }
    reset_button = {
        "xpath": "//button[contains(., 'Сбросить')]",
        "name": "reset_button"
    }

    """ Get driver """

    @classmethod
    def get_driver(cls: Type['Base']) -> 'Base':
        """
        Создает и возвращает экземпляр драйвера с нужными настройками в зависимости от операционной системы.

        Returns
        -------
        Base
            Экземпляр класса Base с инициализированным веб-драйвером.
        """
        options = webdriver.ChromeOptions()

        # Настройки драйвера для разных операционных систем
        chrome_driver_path = WINDOWS_DRIVER_PATH if platform.system() == 'Windows' else LINUX_DRIVER_PATH
        # options.add_argument('--headless')
        options.add_argument('--window-size=1920x1080')
        options.add_argument('--force-device-scale-factor=0.8')

        if platform.system() != 'Windows':
            # Дополнительные параметры для Linux
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('--headless')
            options.add_argument('--remote-debugging-port=9222')
            options.add_argument('--disable-software-rasterizer')
            options.add_argument('--disable-setuid-sandbox')

        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(options=options, service=service)

        # Шаг в Allure и вывод в консоль
        with allure.step(title="Start test"):
            print("Start test")

        return cls(driver)

    """ Test finish """

    def test_finish(self) -> None:
        """
        Завершает тест и закрывает браузер.
        """
        # Шаг в Allure и вывод в консоль
        with allure.step(title="Test finish"):
            print("Test finish")
            self.driver.quit()

    """ Get current url """

    def get_current_url(self) -> None:
        """
        Получает и выводит текущий URL адрес в консоль.
        """
        get_url = self.driver.current_url
        # Шаг в Allure и вывод в консоль
        with allure.step(title="Current url: " + get_url):
            print("Current url: " + get_url)

    """ Get element with choosing a method for obtaining an element """

    def get_element(self, element_info: Dict[str, str], wait_type: str = 'clickable') -> Dict[str, Any]:
        """
        Ожидает элемент в зависимости от выбранного типа ожидания и возвращает его.

        Parameters
        ----------
        element_info : dict
            Информация о локаторе элемента.
        wait_type : str, optional
            Тип ожидания: 'clickable', 'visible', 'located', 'find', или 'invisibility'. По умолчанию 'clickable'.

        Returns
        -------
        dict
            Словарь с информацией о найденном элементе.
        """
        try:
            wait_conditions = {
                'clickable': EC.element_to_be_clickable,
                'visible': EC.visibility_of_element_located,
                'located': EC.presence_of_element_located,
                'find': lambda locator: self.driver.find_element(*locator),
                'invisibility': EC.invisibility_of_element_located
            }

            if wait_type not in wait_conditions:
                raise ValueError(f"Unsupported wait type: {wait_type}")

            condition = wait_conditions[wait_type]

            # Определение типа локаторов и его значения
            if 'xpath' in element_info:
                locator = (By.XPATH, element_info['xpath'])
            elif 'css' in element_info:
                locator = (By.CSS_SELECTOR, element_info['css'])
            else:
                raise ValueError("Не указан ни XPath, ни CSS-селектор для элемента")

            if wait_type == 'invisibility':
                # Ожидание невидимости элемента с заданным таймаутом
                WebDriverWait(self.driver, 15).until(condition(locator))
                element = None  # Возвращаем None, так как элемент невидим
            else:
                # Ожидание для остальных типов
                element = WebDriverWait(self.driver, 60).until(condition(locator))

            return {'name': element_info['name'], 'element': element}

        except TimeoutException:
            message = f"Element '{element_info['name']}' is not {wait_type}"
            # Шаг в Allure и вывод в консоль
            with allure.step(message):
                print(message)
            raise TimeoutException(message)

    """ Get timestamp """

    @staticmethod
    def get_timestamp(dot: bool = False, eight: bool = False) -> str:
        """
        Возвращает текущее время в формате UTC с возможностью выбора формата.

        Parameters
        ----------
        dot : bool, optional
            Если True, время будет возвращено с точками в качестве разделителей ("ГГГГ.ММ.ДД.ЧЧ.ММ.СС").
        eight : bool, optional
            Если True, время будет возвращено в формате "ДДЧЧММСС".
            Если оба параметра True, приоритет будет у параметра 'eight'.

        Returns
        -------
        str
            Текущее время в выбранном формате.
        """
        current_time = datetime.now(timezone.utc)  # Используем текущую дату и время с учетом временной зоны UTC

        if eight:
            # Формат с восемью знаками без разделителей
            timestamp = current_time.strftime("%d%H%M%S")
        elif dot:
            # Формат с точками в качестве разделителей
            timestamp = current_time.strftime("%Y.%m.%d.%H.%M.%S")
        else:
            # Формат по умолчанию без разделителей
            timestamp = current_time.strftime("%Y%m%d%H%M%S")

        return timestamp

    """ Assert element text"""

    def assert_element_text(self, element_dict: Dict[str, str], reference_value: Optional[str] = None,
                            wait_type: str = 'clickable') -> None:
        """
        Проверяет, что текст элемента соответствует заданному значению или условию.
        Использует 'reference_xpath' из 'element_dict' для получения текста элемента, если указан.
        Если не указан 'reference_value', используется 'reference' из 'element_dict' для сравнения.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о локаторе элемента. Может включать 'reference_xpath' или 'xpath'.
        reference_value : str, optional
            Ожидаемый текст для сравнения, если указан.
        wait_type : str, optional
            Тип ожидания элемента ('clickable', 'visible', 'located', 'find'). По умолчанию 'clickable'.

        Raises
        ------
        AssertionError
            Если текст элемента не соответствует ожидаемому значению.
        """
        # Проверяем наличие 'reference_xpath' и используем его для получения текста, иначе используем 'xpath'
        if 'reference_xpath' in element_dict:
            element_info = {'name': 'Reference element', 'xpath': element_dict['reference_xpath']}
        else:
            element_info = {'name': element_dict['name'], 'xpath': element_dict['xpath']}

        element = self.get_element(element_info, wait_type=wait_type)['element']
        value_word = element.text or element.get_attribute('value')

        # Определяем ожидаемое значение
        expected_value = reference_value if reference_value else element_dict.get('reference', '')

        # Шаг в Allure и вывод в консоль
        with allure.step(f"Assert \"{value_word}\" == \"{expected_value}\""):
            assert re.fullmatch(expected_value, value_word), f"Expected '{expected_value}', but found '{value_word}'."
            print(f"Assert \"{value_word}\" == \"{expected_value}\"")

    """ Verify text presence on the page """

    def verify_text_on_page(self, text: str, should_exist: bool = True) -> None:
        """
        Проверяет наличие или отсутствие заданного текста на всей странице.

        Parameters
        ----------
        text : str
            Текст для поиска на странице.
        should_exist : bool, optional
            Если True, проверяет, что текст присутствует на странице.
            Если False, проверяет, что текст отсутствует на странице. По умолчанию True.

        Raises
        ------
        AssertionError
            Если текст не найден при should_exist=True или найден при should_exist=False.
        """
        # Формируем сообщение для шага Allure и вывода в консоль
        message = f"Verify that text '{text}' is {'present' if should_exist else 'absent'} on the page"

        with allure.step(message):
            page_source = self.driver.page_source
            text_found = text in page_source

            if should_exist:
                assert text_found, f"Expected text '{text}' to be present on the page, but it was not found."
            else:
                assert not text_found, f"Expected text '{text}' to be absent on the page, but it was found."

            print(message)

    def find_text_on_page(self, text: str, occurrences: int = 1) -> None:
        """
        Проверяет наличие указанного текста на странице и количество его вхождений.

        Parameters
        ----------
        text : str
            Текст, который необходимо найти на странице.
        occurrences : int, optional
            Количество раз, которое текст должен присутствовать на странице (по умолчанию 1).

        Raises
        -------
        AssertionError
            Если количество вхождений текста на странице не совпадает с ожидаемым.
        """

        try:
            page_source = self.driver.page_source
            count = page_source.count(text)

            if count == occurrences:
                with allure.step(f"Text '{text}' found {count} times as expected."):
                    print(f"Text '{text}' found {count} times as expected.")
            else:
                raise AssertionError(
                    f"Expected '{text}' to appear {occurrences} times, but found {count} times."
                )
        except Exception as e:
            message = f"Error finding text on the page: {str(e)}"
            with allure.step(message):
                print(message)
            raise

    """ Get random value float to str"""

    @staticmethod
    def random_value_float_str(of: float, to: float, precision: int = 0) -> str:
        """
        Возвращает случайное вещественное число в виде строки с заданным количеством знаков после запятой.

        Parameters
        ----------
        of : float
            Нижняя граница диапазона.
        to : float
            Верхняя граница диапазона.
        precision : int, optional
            Количество знаков после запятой, по умолчанию 0.

        Returns
        -------
        str
            Строковое представление случайного вещественного числа с заданной точностью.
        """
        # Генерируем случайное число в указанном диапазоне и форматируем с указанной точностью
        random_value = random.uniform(of, to)
        return f'{random_value:.{precision}f}'

    @staticmethod
    def random_value_int(of: int, to: int) -> int:
        """
        Возвращает случайное целое число в заданном диапазоне.

        Parameters
        ----------
        of : int
            Нижняя граница диапазона (включительно).
        to : int
            Верхняя граница диапазона (включительно).

        Returns
        -------
        int
            Случайное целое число в диапазоне [of, to].
        """
        # Генерируем случайное целое число в указанном диапазоне
        return random.randint(of, to)

    """ Get screenshot """

    def get_screenshot(self, test_name: str = None) -> NoReturn:
        """
        Сохраняет скриншот текущего состояния браузера в папку screens внутри проекта.
        Если тест запускается с Allure, прикрепляет скриншот к отчету Allure.

        Parameters
        ----------
        test_name : str, optional
            Название теста, добавляемое к имени скриншота. Если не указано, используется только таймштамп.
        """
        # Определяем путь к папке screens внутри корня проекта
        screenshot_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'screens')

        # Создаем имя файла скриншота с таймштампом и названием теста (если указано)
        name_screenshot = f"{test_name + '_' if test_name else ''}{self.get_timestamp(dot=True)}.png"
        screenshot_path = os.path.join(screenshot_dir, name_screenshot)

        # Проверяем существование папки и создаем ее при необходимости
        os.makedirs(screenshot_dir, exist_ok=True)

        # Сохраняем скриншот
        self.driver.save_screenshot(screenshot_path)

        # Шаг в Allure и вывод в консоль
        message = f"Screenshot saved at: {screenshot_path}"
        with allure.step(title=f"Screen taken: {name_screenshot}"):
            print(message)

            # Прикрепляем файл скриншота только если используется Allure
            if hasattr(self, 'allure_dir') and self.allure_dir:
                allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)

    """Click button with optional assertion and loading wait"""

    def click_button(self, element_dict: Dict[str, str], index: int = 1, do_assert: bool = False,
                     wait: Optional[str] = None, wait_type: str = 'clickable') -> None:
        """
        Кликает по кнопке с заданным типом ожидания и опционально по индексу элемента.
        Опционально выполняет проверку текста элемента после клика и ожидание исчезновения элементов загрузки.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о кнопке для клика.
        index : int, optional
            Индекс элемента в списке однотипных элементов. По умолчанию 1 (первый элемент).
        do_assert : bool, optional
            Если True, выполнит проверку текста элемента после клика.
        wait : str, optional
            Определяет, какой спиннер ожидать после клика ('lst' для списка или 'form' для формы).
        wait_type : str, optional
            Тип ожидания элемента перед кликом ('clickable', 'visible', 'located', 'find'), по умолчанию 'clickable'.

        """
        # Формирование локатора и имени элемента с учётом индекса
        element_name = f"{element_dict['name']} index {index}" if index > 1 else element_dict['name']

        if 'xpath' in element_dict:
            locator = f"({element_dict['xpath']})[{index}]" if index > 1 else element_dict['xpath']
            locator_type = 'xpath'
        elif 'css' in element_dict:
            locator = f"{element_dict['css']}:nth-of-type({index})" if index > 1 else element_dict['css']
            locator_type = 'css'
        else:
            raise ValueError("Не указан ни XPath, ни CSS-селектор для элемента")

        updated_element_dict = {
            "name": element_name,
            locator_type: locator
        }

        # Создаем единое сообщение для Allure шага и консоли
        message = f"Click on {element_name}"

        with allure.step(title=message):
            button_dict = self.get_element(updated_element_dict, wait_type)
            button_dict['element'].click()
            print(message)

            # Ожидание спиннера, если задано
            if wait:
                loading_spinner = self.loading_form if wait == 'form' else self.loading_list
                try:
                    self.get_element(loading_spinner, wait_type="visible")  # Ожидание появления спиннера
                except TimeoutException:
                    with allure.step("Spinner did not appear"):
                        print("Spinner did not appear")
                        return  # Завершаем метод, если спиннер не появился

                try:
                    self.get_element(loading_spinner, wait_type="invisibility")  # Ожидание исчезновения спиннера
                except TimeoutException:
                    with allure.step("Spinner did not disappear"):
                        print("Spinner did not disappear")
                        # Продолжаем выполнение, несмотря на то, что спиннер не исчез

            # Выполнение ассерта текста элемента, если do_assert = True
            if do_assert:
                self.assert_element_text(element_dict)

    def click_button_recaptchav3(self, element_dict: Dict[str, str], index: int = 1, do_assert: bool = False,
                                 wait: Optional[str] = None, wait_type: str = 'clickable', safe: bool = False) -> None:
        """
        Клик с имитацией человеческого поведения
        """
        element_name = f"{element_dict['name']} index {index}" if index > 1 else element_dict['name']

        # Формируем локатор с учетом типа селектора
        if 'xpath' in element_dict:
            locator = f"({element_dict['xpath']})[{index}]" if index > 1 else element_dict['xpath']
            locator_type = 'xpath'
        elif 'css' in element_dict:
            locator = f"{element_dict['css']}:nth-of-type({index})" if index > 1 else element_dict['css']
            locator_type = 'css'
        else:
            raise ValueError("Не указан селектор")

        updated_element_dict = {
            "name": element_name,
            locator_type: locator
        }

        message = f"Human-like click on {element_name}"

        with allure.step(title=message):
            button_dict = self.get_element(updated_element_dict, wait_type)
            element = button_dict['element']

            if safe:
                # Имитация реального поведения
                actions = ActionChains(self.driver)

                # 1. Движение мыши к элементу
                actions.move_to_element(element).perform()
                time.sleep(random.uniform(0.2, 0.5))  # Задержка перед кликом

                # 2. Случайное смещение клика (человек не всегда кликает точно в центр)
                offset_x = random.randint(-10, 10)
                offset_y = random.randint(-10, 10)
                self.driver.execute_script(f"""
                    var elem = arguments[0];
                    var rect = elem.getBoundingClientRect();
                    var x = rect.left + rect.width/2 + {offset_x};
                    var y = rect.top + rect.height/2 + {offset_y};
                    elem.dispatchEvent(new MouseEvent('click', {{clientX: x, clientY: y}}));
                """, element)
            else:
                element.click()

            print(message)
            time.sleep(random.uniform(0.3, 1.0))  # Задержка после клика

            # Обработка спиннеров
            if wait:
                loading_spinner = self.loading_form if wait == 'form' else self.loading_list
                try:
                    self.get_element(loading_spinner, wait_type="visible")
                except TimeoutException:
                    with allure.step("Spinner did not appear"):
                        print("Spinner did not appear")
                        return

                try:
                    self.get_element(loading_spinner, wait_type="invisibility")
                except TimeoutException:
                    with allure.step("Spinner did not disappear"):
                        print("Spinner did not disappear")

            if do_assert:
                self.assert_element_text(element_dict)

    def click_and_select_with_arrows(self, element_info: Dict[str, str], arrow_presses: int) -> None:
        """
        Кликает по указанному элементу, затем нажимает клавишу "стрелка вниз" указанное количество раз
        и завершает выбор нажатием клавиши "Enter".

        Parameters
        ----------
        element_info : dict
            Информация о локаторе элемента (name и xpath).
        arrow_presses : int
            Количество нажатий клавиши "стрелка вниз".
        """
        try:
            # ожидание видимости элемента
            element = self.get_element(element_info, wait_type='visible')['element']

            # клик по элементу
            element.click()
            time.sleep(1)

            # нажатие стрелки вниз указанное количество раз
            actions = ActionChains(self.driver)
            for _ in range(arrow_presses):
                actions.send_keys(Keys.ARROW_DOWN)
                time.sleep(1)

            # подтверждение выбора
            actions.send_keys(Keys.ENTER).perform()
            time.sleep(1)

            # Формируем сообщение для шага Allure и консоли
            with allure.step(f"Clicked on {element_info['name']} and selected with {arrow_presses} arrow presses"):
                print(f"Clicked on {element_info['name']} and selected with {arrow_presses} arrow presses")

        except Exception as e:
            message = f"Error interacting with dropdown on element {element_info['name']}: {str(e)}"
            with allure.step(message):
                print(message)
            raise

    def scroll_to_element(self, element_info: Dict[str, str]) -> None:
        """
        Прокручивает страницу до указанного элемента.

        Parameters
        ----------
        element_info : dict
            Информация о локаторе элемента (name и xpath).
        """
        try:
            element = self.get_element(element_info, wait_type='visible')['element']

            # JS прокрутка до элемента
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

            # Формируем сообщение для шага Allure и консоли
            with allure.step(f"Scrolled to element {element_info['name']}"):
                print(f"Scrolled to element {element_info['name']}")
        except Exception as e:
            message = f"Error scrolling to element {element_info['name']}: {str(e)}"
            with allure.step(message):
                print(message)
            raise

    def refresh_page(self) -> None:
        """
        Обновляет текущую страницу.
        """
        try:
            self.driver.refresh()
            with allure.step("Page refreshed successfully"):
                print("Page refreshed successfully.")

        except Exception as e:
            message = f"Error while refreshing the page: {str(e)}"
            with allure.step(message):
                print(message)
            raise

    def reload_page(self) -> None:
        """
        Перезагружает текущую страницу.
        """
        try:
            self.driver.execute_script("location.reload(true);")
            with allure.step("Page reload successfully"):
                print("Page reload successfully.")

        except Exception as e:
            message = f"Error while performing a reload: {str(e)}"
            with allure.step(message):
                print(message)
            raise

    def click_on_the_cross(self, cross_info: Dict[str, str]) -> None:
        """
        Проверяет наличие крестика в поле, и кликает по нему если он существует.

        Parameters
        ----------
        cross_info : Dict[str, str]
            Словарь с информацией о локаторе элемента (name и xpath).
        """
        try:
            # проверяем наличие крестика
            try:
                cross_element = WebDriverWait(self.driver, timeout=3).until(
                    EC.presence_of_element_located((By.XPATH, cross_info['xpath']))
                )
            except TimeoutException:
                # Формируем сообщение для шага Allure и консоли
                with allure.step(f"Clear button not present, skipping action: {cross_info['name']}"):
                    print(f"Clear button not present, skipping action: {cross_info['name']}")
                return

            # клик по крестику
            ActionChains(self.driver).move_to_element(cross_element).click().perform()

            # Формируем сообщение для шага Allure и консоли
            with allure.step(f"Clicked on clear button: {cross_info['name']}"):
                print(f"Clicked on clear button: {cross_info['name']}")

        except Exception as e:
            message = f"Error clicking clear button: {cross_info['name']}. Error: {str(e)}"
            with allure.step(message):
                print(message)
            raise

    """ In dropdown click, wait, input and enter"""

    def dropdown_with_input(self, element_dict: Dict[str, str], option_text: str, press_enter: bool = True,
                            wait_presence: bool = False, wait_type: str = 'clickable',
                            dd_index: int = 1, index: int = 1) -> None:
        """
        Выбирает текст в выпадающем списке, вводит текст и, опционально, ожидает появления опции,
        после чего может нажимать Enter. Позволяет выбор типа ожидания для элемента.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией об элементе выпадающего списка.
        option_text : str
            Текст опции для выбора.
        press_enter : bool, optional
            Если True, после ввода текста будет выполнено нажатие Enter.
        wait_presence : bool, optional
            Если True, ожидает появления текста перед нажатием Enter.
        wait_type : str, optional
            Тип ожидания элемента ('clickable', 'visible', 'located', 'find'). По умолчанию 'clickable'.
        dd_index : int, optional
            Индекс выпадающего списка для инициации клика, начиная с 1.
        index : int, optional
            Индекс опции в списке, начиная с 1, который нужно выбрать.
        """
        # Формируем единое сообщение для Allure шага и вывода в консоль
        message = f"Select '{option_text}' from dropdown {element_dict['name']}"
        if dd_index != 1:
            message += f" at dropdown index {dd_index}"
        if index != 1:
            message += f" at option index {index}"

        with allure.step(message):
            # Генерация XPath для выпадающего списка
            xpath_dropdown = f"({element_dict['xpath']})[{dd_index}]" if dd_index > 1 else element_dict['xpath']
            dropdown_dict = self.get_element({"name": element_dict['name'], "xpath": xpath_dropdown},
                                             wait_type=wait_type)

            # Клик по выпадающему списку
            dropdown_dict['element'].click()

            # Поиск поля для ввода текста
            option_input = dropdown_dict['element'].find_element(By.XPATH, "./../..//input")
            option_input.send_keys(option_text)

            # XPath для опции, которую нужно выбрать
            option_xpath = f"(.//li[@role='option' and contains(normalize-space(.), '{option_text}')])[{index}]"

            if wait_presence:
                # Ожидание появления опции с использованием get_element
                self.get_element({"name": "Dropdown option", "xpath": option_xpath}, wait_type="visible")

            if press_enter:
                # Нажатие Enter после ввода текста
                option_input.send_keys(Keys.ENTER)
            else:
                # Клик по опции в списке с использованием get_element
                option_element = self.get_element({"name": "Dropdown option", "xpath": option_xpath},
                                                  wait_type="clickable")
                option_element['element'].click()

            # Вывод сообщения в консоль
            print(message)

    """ In dropdown click input + index click """

    def dropdown_without_input(self, element_dict: Dict[str, str], option_text: str, dd_index: int = 1,
                               index: int = 1) -> None:
        """
        Выбирает опцию в выпадающем списке с помощью поиска и клика по найденному элементу.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией об элементе выпадающего списка.
        option_text : str
            Текст опции для поиска и выбора.
        dd_index : int, optional
            Индекс выпадающего списка для инициации клика, начиная с 1.
        index : int, optional
            Индекс опции в списке, начиная с 1, который нужно выбрать.
        """
        # Формируем единое сообщение для Allure шага и вывода в консоль
        message = f"Select '{option_text}' from dropdown {element_dict['name']}"
        if dd_index != 1:
            message += f" at dropdown index {dd_index}"
        if index != 1:
            message += f" at option index {index}"

        with allure.step(message):
            # Генерация XPath для выпадающего списка
            xpath_dropdown = f"({element_dict['xpath']})[{dd_index}]" if dd_index > 1 else element_dict['xpath']
            dropdown_dict = self.get_element({"name": element_dict['name'], "xpath": xpath_dropdown})

            # Клик по выпадающему списку
            time.sleep(1)
            dropdown_dict['element'].click()
            time.sleep(2)

            # XPath для выбора нужной опции
            xpath_expression = f"(.//li[@role='option' and normalize-space(.)='{option_text}'])[{index}]"
            option_to_select = self.get_element({"name": f"Option '{option_text}'", "xpath": xpath_expression})[
                'element']

            # Клик по найденной опции
            time.sleep(1)
            option_to_select.click()
            time.sleep(1)

            # Вывод сообщения в консоль
            print(message)

    """ Move to element"""

    def move_to_element(self, element_dict: Dict[str, str], index: int = 1, wait_type: str = 'clickable') -> None:
        """
        Перемещает курсор мыши к элементу с заданным типом ожидания и опционально по индексу элемента.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией об элементе, к которому необходимо переместить курсор.
        index : int, optional
            Индекс элемента в списке однотипных элементов. По умолчанию 1 (первый элемент).
        wait_type : str, optional
            Тип ожидания элемента ('clickable', 'visible', 'located', 'find', 'invisibility').

        """
        # Формируем единое сообщение для Allure шага и вывода в консоль
        message = f"Move to {element_dict['name']}"
        if index != 1:
            message += f" at index {index}"

        # Обновление локатора с учетом индекса
        locator = f"({element_dict['xpath']})[{index}]" if index > 1 else element_dict['xpath']
        updated_element_dict = {"name": element_dict['name'], "xpath": locator}

        with allure.step(message):
            # Получение элемента с помощью метода get_element
            button_dict = self.get_element(updated_element_dict, wait_type)

            # Перемещение курсора к элементу
            ActionChains(self.driver).move_to_element(button_dict['element']).perform()

            # Вывод сообщения в консоль
            print(message)

    """ Switch to original window """

    def switch_to_original_window(self) -> None:
        """
        Переключается обратно к оригинальному окну браузера.
        """
        # Формируем сообщение для Allure шага и вывода в консоль
        message = "Returned to the original window"

        with allure.step(message):
            # Переключаемся на оригинальное окно
            original_window_handle = self.driver.current_window_handle
            self.driver.switch_to.window(original_window_handle)

            # Вывод сообщения в консоль
            print(message)

    """ Input in field with optional click, enter, index, and wait for loading """

    def input_in_field(self, element_dict: Dict[str, str], value: str, click_first: bool = False,
                       press_enter: bool = False, wait: Optional[str] = None, safe: bool = False,
                       wait_type: str = 'clickable', index: int = 1) -> None:
        """
        Универсальный метод для ввода текста в поле с опциональным кликом перед вводом и нажатием Enter после.
        Поддерживает дополнительные параметры для управления взаимодействием, включая индекс элемента,
        ожидание прогрузки элементов (списки или формы), и выбор типа ожидания доступности элемента.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о поле ввода.
        value : str
            Значение для ввода.
        click_first : bool, optional
            Если True, сначала кликает по полю перед вводом текста.
        press_enter : bool, optional
            Если True, нажимает Enter после ввода текста.
        wait : str, optional
            Указывает, нужно ли ожидать исчезновение элементов загрузки после ввода ('lst' или 'form').
        safe : bool, optional
            Если True, заменяет введенное значение на символы "***" в логах.
        wait_type : str, optional
            Тип ожидания элемента ('clickable', 'visible', 'located', 'find'), по умолчанию 'clickable'.
        index : int, optional
            Индекс элемента в списке однотипных элементов. По умолчанию 1 (первый элемент).

        """
        log_value = "***" if safe else value
        element_name = f"{element_dict['name']} index {index}" if index > 1 else element_dict['name']
        locator = f"({element_dict['xpath']})[{index}]" if index > 1 else element_dict['xpath']
        updated_element_dict = {"name": element_name, "xpath": locator}

        # Формируем сообщение для шага Allure и консоли
        message = f"{'Click and ' if click_first else ''}Input in {element_name}: {log_value}"

        with allure.step(title=message):
            field_dict = self.get_element(updated_element_dict, wait_type)
            if click_first:
                field_dict['element'].click()
            field_dict['element'].send_keys(value)
            if press_enter:
                field_dict['element'].send_keys(Keys.ENTER)
            print(message)

            if wait:
                # Определяем, какой спиннер ожидать
                loading_spinner = self.loading_form if wait == 'form' else self.loading_list
                try:
                    self.get_element(loading_spinner, wait_type="visible")  # Ожидание появления спиннера
                except TimeoutException:
                    with allure.step("Spinner did not appear"):
                        print("Spinner did not disappear")
                        return  # Выходим из метода, так как спиннер не появился

                try:
                    self.get_element(loading_spinner, wait_type="invisibility")  # Ожидание исчезновения спиннера
                except TimeoutException:
                    with allure.step("Spinner did not disappear"):
                        print("Spinner did not disappear")

    """ Backspace num times/all and input with optional click, enter, and wait type"""

    def input_in_field_recaptchav3(self, element_dict: Dict[str, str], value: str, click_first: bool = False,
                                   press_enter: bool = False, wait: Optional[str] = None, safe: bool = False,
                                   wait_type: str = 'clickable', index: int = 1) -> None:
        """
        Универсальный метод для ввода текста с поддержкой имитации человека
        """
        log_value = "***" if safe else value
        element_name = f"{element_dict['name']} index {index}" if index > 1 else element_dict['name']
        locator = f"({element_dict['xpath']})[{index}]" if index > 1 else element_dict['xpath']
        updated_element_dict = {"name": element_name, "xpath": locator}

        message = f"{'Click and ' if click_first else ''}Input in {element_name}: {log_value}"

        with allure.step(title=message):
            field_dict = self.get_element(updated_element_dict, wait_type)
            element = field_dict['element']

            if safe:
                # Имитация реального поведения
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                time.sleep(random.uniform(0.2, 0.5))  # Задержка перед вводом

                if click_first:
                    element.click()
                    time.sleep(random.uniform(0.1, 0.3))

                # Плавный ввод по символам
                for char in value:
                    element.send_keys(char)
                    time.sleep(random.uniform(0.1, 0.3))

                if press_enter:
                    time.sleep(random.uniform(0.2, 0.5))
                    element.send_keys(Keys.ENTER)
            else:
                # Стандартный ввод
                if click_first:
                    element.click()
                element.send_keys(value)
                if press_enter:
                    element.send_keys(Keys.ENTER)

            print(message)

            # Обработка спиннеров
            if wait:
                loading_spinner = self.loading_form if wait == 'form' else self.loading_list
                try:
                    self.get_element(loading_spinner, wait_type="visible")
                except TimeoutException:
                    with allure.step("Spinner did not appear"):
                        print("Spinner did not disappear")
                        return

                try:
                    self.get_element(loading_spinner, wait_type="invisibility")
                except TimeoutException:
                    with allure.step("Spinner did not disappear"):
                        print("Spinner did not disappear")

    def backspace_and_input(self, element_dict: Dict[str, str], value: str, click_first: bool = False,
                            press_enter: bool = False, wait_type: str = 'clickable', num: Optional[int] = None) -> None:
        """
        Выполняет нажатие клавиши Backspace для удаления символов и вводит текст. Если передается num,
        то удаляет указанное количество символов. Если num не передан, удаляет все символы в поле.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о поле ввода.
        value : str
            Значение для ввода.
        click_first : bool, optional
            Если True, сначала кликает по полю перед вводом текста.
        press_enter : bool, optional
            Если True, нажимает Enter после ввода значения.
        wait_type : str, optional
            Тип ожидания элемента. По умолчанию 'clickable'.
            Доступные варианты: 'clickable', 'visible', 'located', 'find', 'invisibility'.
        num : int, optional
            Количество раз для нажатия клавиши Backspace. Если None, удаляет все символы в поле. По умолчанию None.

        """
        element_name = element_dict['name']

        # Формируем сообщение для шага Allure и консоли
        message = (f"{'Click and ' if click_first else ''}"
                   f"Backspace {'all' if num is None else num} times and input in {element_name}: {value}")

        with allure.step(title=message):
            field_dict = self.get_element(element_dict, wait_type=wait_type)

            if click_first:
                field_dict['element'].click()

            # Если num не указан, удаляем все символы, иначе удаляем num символов
            if num is None:
                current_value = field_dict['element'].get_attribute('value')
                num_backspaces = len(current_value)
            else:
                num_backspaces = num

            # Выполняем нажатие Backspace
            field_dict['element'].send_keys(Keys.BACKSPACE * num_backspaces)

            # Вводим новое значение
            field_dict['element'].send_keys(value)

            # Если указано, выполняем нажатие Enter
            if press_enter:
                field_dict['element'].send_keys(Keys.ENTER)

            # Вывод сообщения в консоль
            print(message)

    def backspace_and_input_int(self, element_dict: Dict[str, str], value: int, click_first: bool = False,
                                press_enter: bool = False, wait_type: str = 'clickable',
                                num: Optional[int] = None) -> None:
        """
        Выполняет нажатие клавиши Backspace для удаления символов и вводит целое число.
        Если передается num, то удаляет указанное количество символов.
        Если num не передан, удаляет все символы в поле.

        Parameters
        ----------
        element_dict : dict
            Словарь с информацией о поле ввода.
        value : int
            Целочисленное значение для ввода.
        click_first : bool, optional
            Если True, сначала кликает по полю перед вводом текста.
        press_enter : bool, optional
            Если True, нажимает Enter после ввода значения.
        wait_type : str, optional
            Тип ожидания элемента. По умолчанию 'clickable'.
            Доступные варианты: 'clickable', 'visible', 'located', 'find', 'invisibility'.
        num : int, optional
            Количество раз для нажатия клавиши Backspace. Если None, удаляет все символы в поле. По умолчанию None.

        Raises
        ------
        ValueError
            Если value не является целым числом.
        """
        # Проверяем, что value является целым числом
        if not isinstance(value, int):
            raise ValueError(f"Expected 'value' to be an integer, got {type(value).__name__} instead.")

        element_name = element_dict['name']

        # Формируем сообщение для шага Allure и консоли
        message = (f"{'Click and ' if click_first else ''}"
                   f"Backspace {'all' if num is None else num} times and input in {element_name}: {value}")

        with allure.step(title=message):
            field_dict = self.get_element(element_dict, wait_type=wait_type)

            if click_first:
                field_dict['element'].click()

            # Если num не указан, удаляем все символы, иначе удаляем num символов
            if num is None:
                current_value = field_dict['element'].get_attribute('value')
                num_backspaces = len(current_value)
            else:
                num_backspaces = num

            # Выполняем нажатие Backspace
            field_dict['element'].send_keys(Keys.BACKSPACE * num_backspaces)

            # Вводим новое значение
            field_dict['element'].send_keys(str(value))

            # Если указано, выполняем нажатие Enter
            if press_enter:
                field_dict['element'].send_keys(Keys.ENTER)

            # Вывод сообщения в консоль
            print(message)

    """Move to element and click another element"""

    def move_and_click(self, move_to: Dict[str, str], click_to: Dict[str, str], move_index: int = 1,
                       click_index: int = 1, move_wait_type: str = 'clickable', click_wait_type: str = 'clickable',
                       do_assert: bool = False, wait: Optional[str] = None) -> None:
        """
        Перемещается к одному элементу и кликает по другому, поддерживая настройку индекса, типа ожидания и проверок.

        Parameters
        ----------
        move_to : dict
            Словарь с информацией о элементе для перемещения.
        click_to : dict
            Словарь с информацией о элементе для клика.
        move_index : int, optional
            Индекс элемента для перемещения, по умолчанию 1.
        click_index : int, optional
            Индекс элемента для клика, по умолчанию 1.
        move_wait_type : str, optional
            Тип ожидания элемента для перемещения ('clickable', 'visible', 'located', 'find').
        click_wait_type : str, optional
            Тип ожидания элемента для клика ('clickable', 'visible', 'located', 'find').
        do_assert : bool, optional
            Если True, выполняет проверку текста элемента после клика.
        wait : str, optional
            Если 'lst' или 'form', ожидает исчезновение указанных элементов загрузки после клика.

        """
        # Перемещаемся к указанному элементу
        self.move_to_element(move_to, index=move_index, wait_type=move_wait_type)
        time.sleep(0.1)  # Небольшая задержка перед кликом для надёжности

        # Кликаем по указанному элементу с дополнительными проверками
        self.click_button(click_to, index=click_index, wait_type=click_wait_type, do_assert=do_assert, wait=wait)

    """ Naw time/datetime change"""

    @staticmethod
    def naw_time_change(minutes: int, new: str = 'time') -> str:
        """
        Изменяет текущее время, дату или дату и время, добавляя указанное количество минут и округляя результат.

        Parameters
        ----------
        minutes : int
            Количество минут для добавления к текущему времени.
        new : str, optional
            Формат возвращаемого значения.
            'time' для формата HHMM (по умолчанию),
            'datetime' для формата DDMMYYYY HHMM,
            'date_dot' для формата DD.MM.YYYY.

        Returns
        -------
        str
            Строка с новым временем в формате HHMM, DDMMYYYY HHMM или DD.MM.YYYY, округленным до ближайших 5 минут.

        Raises
        ------
        ValueError
            Если передано неверное значение для параметра new.
        """
        original_time = datetime.now()
        new_time = original_time + timedelta(minutes=minutes)

        # Определяем формат
        if new == 'time':
            time_str = new_time.strftime("%H%M")
        elif new == 'datetime':
            time_str = new_time.strftime("%d%m%Y %H%M")
        elif new == 'date_dot':
            return new_time.strftime("%d.%m.%Y")
        else:
            raise ValueError("Unsupported format. Use 'time', 'datetime', or 'date_dot'.")

        # Округляем время до ближайших 5 минут
        rounded_time_str = str(int(round(int(time_str[-4:]) / 5) * 5)).zfill(4)

        # Возвращаем строку с правильным форматом
        return time_str[:-4] + rounded_time_str if new == 'datetime' else rounded_time_str

    """ Generate INN """

    @staticmethod
    def generate_inn(entity_type: str) -> str:
        """
        Генерирует ИНН для физического лица (individual) или юридического лица (entity).

        Parameters
        ----------
        entity_type : str
            Тип сущности, для которой генерируется ИНН. Допустимые значения: 'individual', 'entity'.

        Returns
        -------
        str
            Сгенерированный ИНН в виде строки.
            Для юридического лица ИНН состоит из 10 цифр, для физического лица - из 12 цифр.

        Raises
        ------
        ValueError
            Если передан неизвестный тип сущности. Допустимые значения параметра entity_type: 'individual', 'entity'.
        """

        def calculate_control_sum(numbers: list[int], local_coeffs: list[int]) -> int:
            """Вычисляет контрольную сумму по заданным коэффициентам."""
            return sum(a * b for a, b in zip(numbers, local_coeffs)) % 11 % 10

        if entity_type == "entity":
            # Генерация ИНН для юридического лица
            base = [random.randint(0, 9) for _ in range(9)]
            entity_coeffs = [2, 4, 10, 3, 5, 9, 4, 6, 8]
            control_sum = calculate_control_sum(base, entity_coeffs)
            inn = ''.join(map(str, base)) + str(control_sum)
        elif entity_type == "individual":
            # Генерация ИНН для физического лица
            base = [random.randint(0, 9) for _ in range(10)]
            individual_coeffs_first = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
            individual_coeffs_second = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 5]
            first_control_sum = calculate_control_sum(base, individual_coeffs_first)
            second_control_sum = calculate_control_sum(base + [first_control_sum], individual_coeffs_second)
            inn = ''.join(map(str, base)) + str(first_control_sum) + str(second_control_sum)
        else:
            raise ValueError("Неизвестный тип сущности. Допустимые значения: 'individual', 'entity'.")

        return inn

    """ Multiple click buttons """

    def click_multiple_buttons(self, button_element: Dict[str, str], num_buttons: int, num_clicks: int = 1,
                               wait: Optional[str] = None, wait_type: str = 'clickable', start_index: int = 1) -> None:
        """
        Нажимает на каждую из N кнопок по num_clicks раз, с опциональным ожиданием прогрузки после каждого клика,
        начиная с заданного индекса.

        Parameters
        ----------
        button_element : dict
            Словарь с информацией о кнопке для клика.
        num_buttons : int
            Количество кнопок, на которые нужно кликнуть.
        num_clicks : int, optional
            Количество кликов на одну кнопку, по умолчанию 1.
        wait : str, optional
            Определяет, какой спиннер ожидать после клика ('lst' для списка или 'form' для формы). Если None,
            ожидание не выполняется.
        wait_type : str, optional
            Тип ожидания элемента перед кликом ('clickable', 'visible', 'located', 'find'). По умолчанию 'clickable'.
        start_index : int, optional
            Начальный индекс кнопки для кликов, по умолчанию 1.
        """
        for i in range(start_index, num_buttons + 1):
            for _ in range(num_clicks):
                try:
                    # Обновляем локатор элемента с учетом индекса
                    element_locator = {"name": f"{button_element['name']} index {i}",
                                       "xpath": f"({button_element['xpath']})[{i}]"}

                    # Получаем элемент с использованием метода get_element
                    element_info = self.get_element(element_locator, wait_type=wait_type)
                    element = element_info['element']

                    # Скроллим к элементу перед кликом
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

                    # Выполняем клик по кнопке
                    if wait:
                        self.click_button(button_element, index=i, wait=wait, wait_type=wait_type)
                    else:
                        self.click_button(button_element, index=i, wait_type=wait_type)
                except ElementClickInterceptedException:
                    print(f"ElementClickInterceptedException: unable to click button at index {i}")
