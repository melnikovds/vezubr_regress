import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.login import admin_credentials


class AdminPage(Base):
    """
    Page Object для админ-панели с полным функционалом
    """

    # ==================== ЛОКАТОРЫ ====================

    # Поля ввода для логина
    email_input = {
        "xpath": "//input[@id='username']",
        "name": "email_input"
    }
    password_input = {
        "xpath": "//input[@id='password']",
        "name": "password_input"
    }
    login_button = {
        "xpath": "//button[@type='submit']",
        "name": "login_button"
    }
    admin_logo = {
        "xpath": "(//span[@class='logo-custom'])[1]",
        "name": "admin_logo"
    }

    # Меню
    counterparties_menu = {
        "xpath": "//span[@class='menu-item-label position-relative'][contains(text(),'Контрагенты')]",
        "name": "counterparties_menu"
    }
    counterparties_details = {
        "xpath": "//td[@data-label='ID']",
        "name": "counterparties_details"
    }
    counterparties_lkp = {
        "xpath": "//span[contains(text(),'Выполнить вход в ЛК контрагента')]",
        "name": "counterparties_lkp"
    }

    employees_menu = {
        "xpath": "//span[@class='menu-item-label position-relative'][contains(text(),'Сотрудники')]",
        "name": "employees_menu"
    }
    employees_details = {
        "xpath": "//td[@data-label='ID']",
        "name": "employees_details"
    }
    employees_move_organization = {
        "xpath": "//a[normalize-space()='[2447] Auto LKE']",
        "name": "employees_move_organization"
    }

    organizations_menu = {
        "xpath": "//span[contains(text(),'Организации')]",
        "name": "organizations_menu"
    }

    orders_menu = {
        "xpath": "//span[contains(text(),'Заказы на перевозку')]",
        "name": "orders_menu"
    }
    orders_menu_detail = {
        "xpath": "//td[@data-label='ID']",
        "name": "orders_menu_detail"
    }

    orders_prr = {
        "xpath": "//span[contains(text(),'Заказы ПРР')]",
        "name": "orders_prr"
    }
    orders_prr_details = {
        "xpath": "//td[@data-label='ID']",
        "name": "orders_prr_details"
    }

    truck_delivery = {
        "xpath": "//span[normalize-space()='Truck Deliveries']",
        "name": "truck_delivery"
    }
    truck_delivery_details = {
        "xpath": "//td[@data-label='ID']",
        "name": "truck_delivery_details"
    }

    cargo_delivery_request = {
        "xpath": "//span[normalize-space()='Cargo Delivery Requests']",
        "name": "cargo_delivery_request"
    }
    cargo_delivery_request_details = {
        "xpath": "//td[@data-label='ID']",
        "name": "cargo_delivery_request_details"
    }

    vehicle_types = {
        "xpath": "//span[contains(text(),'Типы ТС')]",
        "name": "vehicle_types"
    }

    ports_directory = {
        "xpath": "//span[contains(text(),'Справочник портов')]",
        "name": "ports_directory"
    }

    country = {
        "xpath": "//span[contains(text(),'Страна')]",
        "name": "country"
    }

    regions = {
        "xpath": "//span[contains(text(),'Регионы')]",
        "name": "regions"
    }

    localities = {
        "xpath": "//span[contains(text(),'Населенные пункты')]",
        "name": "localities"
    }

    # Поиск
    search_input = {
        "xpath": "//input[@placeholder='Поиск']",
        "name": "search_input"
    }

    # Таблицы результатов
    results_table = {
        "xpath": "//table[contains(@class, 'ant-table')]",
        "name": "results_table"
    }
    table_rows = {
        "xpath": "//table/tbody/tr",
        "name": "table_rows"
    }
    no_data_message = {
        "xpath": "//div[contains(text(), 'Нет данных')]",
        "name": "no_data_message"
    }

    # Создание нового типа ТС
    create_vehicle_type_button = {
        "xpath": "//span[contains(text(),'Создать Тип ТС')]",
        "name": "create_vehicle_type_button"
    }
    create_button = {
        "xpath": "//button[@value='saveAndReturn']//span[@class='action-label'][contains(text(),'Создать')]",
        "name": "create_button"
    }
    status = {
        "xpath": "//div[contains(text(), 'Нет данных')]",
        "name": "status"
    }
    category = {
        "xpath": "//div[@id='VehicleType_category-ts-control']//input[@class='items-placeholder']",
        "name": "category"
    }
    category_search_input = {
        "xpath": "(//input[@type='text'])[3]",
        "name": "category_search_input"
    }
    insurance_limit = {
        "xpath": "//input[@id='VehicleType_insuranceLimit']",
        "name": "insurance_limit"
    }
    body_width = {
        "xpath": "//input[@id='VehicleType_bodyMinWidth']",
        "name": "body_width"
    }
    body_length = {
        "xpath": "//input[@id='VehicleType_bodyMinLength']",
        "name": "body_length"
    }
    body_height = {
        "xpath": "//input[@id='VehicleType_bodyMinHeight']",
        "name": "body_height"
    }
    load_capacity = {
        "xpath": "//input[@id='VehicleType_liftingCapacityMin']",
        "name": "load_capacity"
    }
    capacity_in_pallets = {
        "xpath": "//input[@id='VehicleType_palletsCapacityMin']",
        "name": "capacity_in_pallets"
    }
    volume = {
        "xpath": "//input[@id='VehicleType_volumeMin']",
        "name": "volume"
    }
    number_of_passengers = {
        "xpath": "//input[@id='VehicleType_passengersCapacity']",
        "name": "number_of_passengers"
    }
    boom_lifting_capacity = {
        "xpath": "//input[@id='VehicleType_craneCapacity']",
        "name": "boom_lifting_capacity"
    }
    boom_length = {
        "xpath": "//input[@id='VehicleType_craneLength']",
        "name": "boom_length"
    }
    platform_length = {
        "xpath": "//input[@id='VehicleType_platformLength']",
        "name": "platform_length"
    }
    platform_height = {
        "xpath": "//input[@id='VehicleType_platformHeight']",
        "name": "platform_height"
    }
    number_of_cars = {
        "xpath": "//input[@id='VehicleType_carCount']",
        "name": "number_of_cars"
    }
    number_of_compartments = {
        "xpath": "//input[@id='VehicleType_compartmentCount']",
        "name": "number_of_compartments"
    }
    available_body_types_and_loading = {
        "xpath": "//pre[@role='presentation']",
        "name": "available_body_types_and_loading"
    }
    first_record = {
        "xpath": "//tbody/tr[1]/td[3]",
        "name": "first_record"
    }
    save_button = {
        "xpath": "//button[@value='saveAndReturn']//span[@class='action-label'][contains(text(),'Сохранить')]",
        "name": "save_button"
    }

    # Локаторы для тестов TD (Графики, полилинии, координаты)

    def __init__(self, driver, domain):
        super().__init__(driver)
        self.domain = domain

    # ==================== МЕТОДЫ ДЛЯ ЛОГИНА ====================

    def login_as_admin(self, email: str, password: str):
        """Метод для входа в админку"""
        with allure.step("Вход в админку"):
            self.get_element(self.email_input, wait_type='visible')
            self.input_in_field(self.email_input, email, click_first=True, safe=True)
            self.input_in_field(self.password_input, password, safe=True)

            button = self.driver.find_element(By.XPATH, self.login_button["xpath"])
            button.click()

            WebDriverWait(self.driver, 10).until(
                lambda driver: 'login' not in driver.current_url.lower()
            )

    def login(self):
        """Быстрый вход в админку под администратором"""
        self.login_as_admin(admin_credentials["email"], admin_credentials["password"])

    # ==================== МЕТОДЫ ДЛЯ ПЕРЕХОДА В РАЗДЕЛЫ ====================

    def go_to_counterparties(self):
        with allure.step("Переход в раздел Контрагенты"):
            self.click_button(self.counterparties_menu)

    def go_to_organizations(self):
        with allure.step("Переход в раздел Организации"):
            self.click_button(self.organizations_menu)

    def go_to_employees(self):
        with allure.step("Переход в раздел Сотрудники"):
            self.click_button(self.employees_menu)

    def go_to_orders(self):
        with allure.step("Переход в раздел Заказы на перевозку"):
            self.click_button(self.orders_menu)

    # ==================== МЕТОД ДЛЯ ПОИСКА ====================

    def search(self, text: str):
        """Универсальный поиск (работает во всех разделах)"""
        with allure.step(f"Поиск: '{text}'"):
            self.input_in_field(self.search_input, text, click_first=True, press_enter=True)

    # ==================== ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ ====================

    def wait_for_loader_disappear(self, timeout: int = 30):
        """Ожидает исчезновения лоадера"""
        try:
            self.get_element(self.loading_form, wait_type="invisibility")
            self.get_element(self.loading_list, wait_type="invisibility")
        except:
            pass

    def check_counterparty_filter_by_inn(self, search_value: str, expected_name: str) -> None:
        """Проверка поиска контрагента по ИНН"""
        self.go_to_counterparties()
        time.sleep(2)
        self.search(search_value)
        time.sleep(2)
        page_text = self.driver.page_source
        assert expected_name in page_text, f"При поиске по ИНН {search_value} не найдено {expected_name}"

    def check_counterparty_filter_by_name(self, search_value: str, expected_id: str) -> None:
        """Проверка поиска контрагента по наименованию"""
        self.go_to_counterparties()
        time.sleep(2)
        self.search(search_value)
        time.sleep(2)
        page_text = self.driver.page_source
        assert expected_id in page_text, f"При поиске по наименованию {search_value} не найден ID {expected_id}"

    def check_counterparty_filter_by_full_name(self, search_value: str, expected_id: str) -> None:
        """Проверка поиска контрагента по полному наименованию"""
        self.go_to_counterparties()
        time.sleep(2)
        self.search(search_value)
        time.sleep(2)
        page_text = self.driver.page_source
        assert expected_id in page_text, f"При поиске по полному наименованию не найден ID {expected_id}"

    def check_employee_filter_and_open_details(self, search_value: str, expected_in_details: str) -> None:
        """Проверка поиска сотрудника и проверка данных в деталке"""
        self.go_to_employees()
        time.sleep(2)
        self.search(search_value)
        time.sleep(2)
        page_text = self.driver.page_source
        assert search_value in page_text, f"Сотрудник с {search_value} не найден"

        # Заходим в деталку
        self.click_button(self.employees_details)
        time.sleep(2)
        page_text = self.driver.page_source
        assert expected_in_details in page_text, f"В деталке не найдено '{expected_in_details}'"

    # ==================== МЕТОДЫ ДЛЯ РАБОТЫ С ТИПАМИ ТС ====================

    def create_new_vehicle_type(self) -> str:
        """
        Создает новый тип ТС с заданными параметрами

        Returns:
            str: Название созданного типа ТС (формируется из параметров)
        """
        with allure.step("Создание нового типа ТС"):
            # Переход в раздел Типы ТС
            self.click_button(self.vehicle_types)
            time.sleep(2)

            # Нажимаем кнопку "Создать Тип ТС"
            self.click_button(self.create_vehicle_type_button)
            time.sleep(3)

            # Заполняем форму и получаем имя
            vehicle_type_name = self._fill_vehicle_type_form()

            return vehicle_type_name

    def _fill_vehicle_type_form(self):
        """
        Заполнение формы создания типа ТС (внутренний метод)
        """
        # Ждем, пока форма полностью загрузится
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='VehicleType_category-ts-control']"))
        )
        time.sleep(2)

        # Выбираем категорию "Грузовая"
        # 1. Кликаем по полю категории - открывается список с полем ввода
        self.click_button(self.category)
        time.sleep(1)

        # 2. Вводим текст в поле поиска (которое появилось после клика)
        self.input_in_field(
            element_dict=self.category_search_input,  # Используем новый локатор
            value="Грузовая",
            click_first=True,  # Кликаем для активации
            press_enter=True,  # Нажимаем Enter для выбора
            wait_type='visible'
        )
        time.sleep(1)

        # Поле статус пропускаем - оно автоматически "Актуальный тип ТС"
        # Поле name_input пропускаем - имя генерируется автоматически

        # Заполняем числовые поля
        test_data = {
            "insurance_limit": "250000000",
            "body_width": "175",
            "body_length": "260",
            "body_height": "140",
            "load_capacity": "15000",
            "capacity_in_pallets": "7",
            "volume": "20",
            "number_of_passengers": "4",
            "boom_lifting_capacity": "500",
            "boom_length": "100",
            "platform_length": "1",
            "platform_height": "1",
            "number_of_cars": "1",
            "number_of_compartments": "0"
        }

        fields = [
            (self.insurance_limit, test_data["insurance_limit"]),
            (self.body_width, test_data["body_width"]),
            (self.body_length, test_data["body_length"]),
            (self.body_height, test_data["body_height"]),
            (self.load_capacity, test_data["load_capacity"]),
            (self.capacity_in_pallets, test_data["capacity_in_pallets"]),
            (self.volume, test_data["volume"]),
            (self.number_of_passengers, test_data["number_of_passengers"]),
            (self.boom_lifting_capacity, test_data["boom_lifting_capacity"]),
            (self.boom_length, test_data["boom_length"]),
            (self.platform_length, test_data["platform_length"]),
            (self.platform_height, test_data["platform_height"]),
            (self.number_of_cars, test_data["number_of_cars"]),
            (self.number_of_compartments, test_data["number_of_compartments"])
        ]

        for field, value in fields:
            self.input_in_field(field, value)
            time.sleep(0.2)  # Небольшая пауза между полями

        # Заполняем JSON поле
        self._fill_json_field()

        # Нажимаем кнопку "Создать"
        self.click_button(self.create_button)
        time.sleep(3)

        # Формируем ожидаемое имя типа ТС
        # Имя складывается из: Грузоподъемность / Объем / Вместимость в паллетах
        load_capacity_ton = str(int(test_data["load_capacity"]) // 1000)  # 15000 -> 15
        expected_name = f"{load_capacity_ton}т / {test_data['volume']}м3 / {test_data['capacity_in_pallets']}пал."

        allure.attach(f"Ожидаемое имя типа ТС: {expected_name}",
                      "Информация",
                      allure.attachment_type.TEXT)

        return expected_name

    def _fill_json_field(self):
        """
        Заполнение JSON поля с типами кузова (внутренний метод)
        """
        with allure.step("Заполнение JSON поля"):
            # Используем готовую строку JSON
            json_str = '{ "2": { "1": true, "2": false, "3": false }, "3": { "1": true, "2": true, "3": false }, "4": { "1": true, "2": false, "3": false }, "7": { "1": true, "2": false, "3": false }, "8": { "1": true, "2": false, "3": false } }'

            # Прокручиваем до поля
            self.scroll_to_element(self.available_body_types_and_loading)
            time.sleep(1)

            # Кликаем по полю для открытия JSON редактора
            self.click_button(self.available_body_types_and_loading)
            time.sleep(2)

            # Находим элемент после клика
            element = self.get_element(self.available_body_types_and_loading, wait_type='visible')['element']

            # Кликаем через JavaScript чтобы активировать
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(1)

            # Очищаем через JavaScript
            self.driver.execute_script("arguments[0].textContent = '';", element)
            time.sleep(1)

            # Вставляем JSON через JavaScript
            self.driver.execute_script("arguments[0].textContent = arguments[1];", element, json_str)
            time.sleep(1)

            # Триггерим событие
            self.driver.execute_script("""
                var event = new Event('input', { bubbles: true });
                arguments[0].dispatchEvent(event);
            """, element)

            time.sleep(2)

    def verify_vehicle_type_exists(self, name: str) -> bool:
        """
        Проверяет, что тип ТС с указанным именем существует в списке

        Args:
            name: Название типа ТС для поиска (например: "15т / 20м3 / 7пал.")

        Returns:
            bool: True если найден, иначе False
        """
        with allure.step(f"Проверка наличия типа ТС '{name}' в списке"):
            # Очищаем поле поиска
            search_input = self.get_element(self.search_input, wait_type='clickable')['element']
            search_input.clear()
            time.sleep(0.5)

            # Ищем по имени
            self.input_in_field(self.search_input, name, click_first=True, press_enter=True)
            time.sleep(3)

            page_text = self.driver.page_source

            # Проверяем наличие имени в тексте страницы
            exists = name in page_text

            if exists:
                allure.attach(f"✅ Тип ТС '{name}' найден в списке",
                              "Результат проверки",
                              allure.attachment_type.TEXT)
            else:
                allure.attach(f"❌ Тип ТС '{name}' НЕ найден в списке",
                              "Результат проверки",
                              allure.attachment_type.TEXT)

            return exists

    def edit_vehicle_type(self, search_name: str) -> str:
        """
        Редактирует существующий тип ТС

        Args:
            search_name: Часть имени для поиска (например "15т / 20м3")

        Returns:
            str: Новое имя типа ТС
        """
        with allure.step(f"Редактирование типа ТС с поиском по '{search_name}'"):
            # Ищем тип ТС по части имени
            self.search(search_name)
            time.sleep(3)

            # Кликаем по первой записи в списке (переход в деталку)
            self.click_button(self.first_record)
            time.sleep(3)

            # Меняем только 3 поля
            new_name = self._fill_edit_vehicle_type_form()

            # Кнопка "Сохранить" уже видна, так как мы не скроллили вниз
            # Используем специальный локатор для кнопки "Сохранить"
            self.click_button(self.save_button)
            time.sleep(3)

            return new_name

    def _fill_edit_vehicle_type_form(self) -> str:
        """
        Заполнение формы редактирования типа ТС (внутренний метод)
        Меняем только 3 основных поля: грузоподъемность, объем, вместимость в паллетах

        Returns:
            str: Новое имя типа ТС
        """
        # Ждем, пока форма полностью загрузится
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='VehicleType_category-ts-control']"))
        )
        time.sleep(2)

        # Новые данные для редактирования (только 3 поля)
        test_data = {
            "load_capacity": "19000",  # 19 тонн
            "capacity_in_pallets": "8",  # 8 паллет
            "volume": "13",  # 13 м3
        }

        # Меняем только 3 поля
        fields = [
            (self.load_capacity, test_data["load_capacity"]),
            (self.capacity_in_pallets, test_data["capacity_in_pallets"]),
            (self.volume, test_data["volume"]),
        ]

        for field, value in fields:
            self.backspace_and_input(
                element_dict=field,
                value=value,
                click_first=True,
                wait_type='visible',
                num=None  # Удаляем все содержимое
            )
            time.sleep(0.3)

        # Формируем ожидаемое новое имя типа ТС
        load_capacity_ton = str(int(test_data["load_capacity"]) // 1000)  # 19000 -> 19
        new_expected_name = f"{load_capacity_ton}т / {test_data['volume']}м3 / {test_data['capacity_in_pallets']}пал."

        allure.attach(f"Новое имя типа ТС: {new_expected_name}",
                      "Информация",
                      allure.attachment_type.TEXT)

        return new_expected_name
