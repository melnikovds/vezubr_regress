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

    def __init__(self, driver, domain):
        super().__init__(driver)
        self.domain = domain

    # ==================== МЕТОДЫ ДЛЯ ЛОГИНА ====================

    def login_as_admin(self, email: str, password: str):
        """Метод для входа в админку"""
        with allure.step("Вход в админку"):
            self.get_element(self.email_input, wait_type='visible')
            # Для email - safe=False (или опускаем, так как email не критичен)
            self.input_in_field(self.email_input, email, click_first=True, safe=True)
            # Для пароля - safe=True (скрывает значение в логах и Allure)
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
