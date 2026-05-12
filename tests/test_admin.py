import allure
import pytest
from pages.admin_page import AdminPage
import time
from selenium.webdriver.common.by import By


@allure.story("Admin Panel Tests")
@allure.feature('Админ панель')
class TestAdminPanel:

    @allure.title("Базовый метод для входа в админку")
    @allure.description("Проверка успешного входа в админ-панель")
    def test_admin_login(self, admin_fixture, domain):
        """Тест: Базовый метод для входа в админку"""
        base = admin_fixture
        admin_page = AdminPage(base.driver, domain)
        admin_page.login()

        # Дополнительно проверяем URL для отчета
        current_url = base.driver.current_url
        allure.attach(current_url, "Admin panel URL", allure.attachment_type.TEXT)

    @allure.title("Поиск по Контрагентам")
    @allure.description("Проверка поиска контрагента LKZ")
    def test_search_counterparties_lkz(self, admin_fixture, domain):
        """Тест: Поиск контрагента LKZ"""
        base = admin_fixture
        admin_page = AdminPage(base.driver, domain)
        admin_page.login()

        # Переход в раздел Контрагенты
        admin_page.go_to_counterparties()
        # Поиск контрагента LKZ
        admin_page.search("LKZ")
        time.sleep(3)
        # Проверяем наличие текста на странице (вместо таблицы)
        page_text = base.driver.page_source
        found = False
        for value in ["2448", "3123625054", "Auto LKZ"]:
            if value in page_text:
                found = True
                allure.attach(f"Найдено значение: {value}", "Результат поиска", allure.attachment_type.TEXT)
                break
        assert found, "Ни одно из значений (2448, 3123625054, Auto LKZ) не найдено в результатах поиска"

    @allure.title("Поиск по Организациям")
    @allure.description("Проверка поиска Организации")
    def test_search_organizations(self, admin_fixture, domain):
        """Тест: Поиск Организации"""
        base = admin_fixture
        admin_page = AdminPage(base.driver, domain)
        admin_page.login()

        # Переход в раздел Организации
        admin_page.go_to_organizations()
        # Поиск организации
        admin_page.search("ООО ЛОГОСОФТ")
        # Небольшая пауза перед проверкой
        time.sleep(3)
        # Проверяем наличие текста на странице
        page_text = base.driver.page_source
        # Ищем значения
        found = False
        search_values = ["7", "5009112893", "500901001", "ООО ЛОГОСОФТ"]
        for value in search_values:
            if value in page_text:
                found = True
                allure.attach(f"Найдено значение: {value}", "Результат поиска", allure.attachment_type.TEXT)
                break
        assert found, f"Ни одно из значений {search_values} не найдено в результатах поиска"

    @allure.title("Поиск по Сотрудникам")
    @allure.description("Проверка поиска сотрудника Робаут")
    def test_search_employees(self, admin_fixture, domain):
        """Тест: Поиск сотрудника Робаут"""
        base = admin_fixture
        admin_page = AdminPage(base.driver, domain)
        admin_page.login()

        admin_page.go_to_employees()
        admin_page.search("Робаут")
        time.sleep(2)
        page_text = base.driver.page_source
        assert "Робаут Жилиман Сотый" in page_text, "Сотрудник не найден"
        assert "13448" in page_text, "ID сотрудника не найден"
        allure.attach("Сотрудник Робаут успешно найден", "Результат", allure.attachment_type.TEXT)

    @allure.title("Поиск по id ПРР")
    @allure.description("Проверка поиска ПРР по идентификатору и проверка деталей рейса")
    def test_search_prr_by_id(self, admin_fixture, domain):
        """Тест: Поиск по id ПРР"""
        base = admin_fixture
        admin_page = AdminPage(base.driver, domain)
        admin_page.login()

        # Используем конкретный ID для поиска
        prr_id = "42263"
        admin_page.click_button(admin_page.orders_prr)
        admin_page.search(prr_id)
        time.sleep(2)
        page_text = base.driver.page_source
        assert prr_id in page_text, f"ПРР с ID {prr_id} не найден"
        admin_page.click_button(admin_page.orders_prr_details)
        time.sleep(2)
        page_text = base.driver.page_source
        assert "26/585/K" in page_text, "Идентификатор '26/585/K' не найден"
        assert "R/26/585/K-01" in page_text, "Идентификатор 'R/26/585/K-01' не найден"
        allure.attach(f"ПРР с ID {prr_id} успешно найден", "Результат", allure.attachment_type.TEXT)

    @allure.title("Поиск по id CDR")
    @allure.description("Проверка поиска CDR по идентификатору и проверка деталей")
    def test_search_cdr_by_id(self, admin_fixture, domain):
        """Тест: Поиск по id CDR"""
        base = admin_fixture
        admin_page = AdminPage(base.driver, domain)
        admin_page.login()

        # ID для поиска
        cdr_id = "9a1dabb1-4fee-4181-ae2d-0522cab9b813"
        # Переход в раздел Cargo Delivery Requests
        admin_page.click_button(admin_page.cargo_delivery_request)
        # Поиск по ID CDR
        admin_page.search(cdr_id)
        time.sleep(2)
        # Проверяем, что CDR найден
        page_text = base.driver.page_source
        assert cdr_id in page_text, f"CDR с ID {cdr_id} не найден"
        assert "[1599] ООО \"Перевозчик\"" in page_text, "Перевозчик [1599] ООО \"Перевозчик\" не найден"
        # Кликаем по найденному CDR для просмотра деталей
        admin_page.click_button(admin_page.cargo_delivery_request_details)
        time.sleep(2)
        # Проверяем детали
        page_text = base.driver.page_source
        assert cdr_id in page_text, f"ID {cdr_id} не найден в деталях"
        assert "[1599] ООО \"Перевозчик\"" in page_text, "Перевозчик не найден в деталях"
        allure.attach(f"CDR с ID {cdr_id} успешно найден, детали проверены",
                      "Результат",
                      allure.attachment_type.TEXT)

    @allure.title("Поиск по id TD")
    @allure.description("Проверка поиска TD по идентификатору и проверка деталей")
    def test_search_td_by_id(self, admin_fixture, domain):
        """Тест: Поиск по id TD"""
        base = admin_fixture
        admin_page = AdminPage(base.driver, domain)
        admin_page.login()

        # ID для поиска
        td_id = "e58ed05c-2ca1-478e-a0d3-74b1af92ce23"
        # Переход в раздел Truck Deliveries
        admin_page.click_button(admin_page.truck_delivery)
        # Поиск по ID TD
        admin_page.search(td_id)
        time.sleep(2)
        # Проверяем, что TD найден
        page_text = base.driver.page_source
        assert td_id in page_text, f"TD с ID {td_id} не найден"
        assert "[1599] ООО \"Перевозчик\"" in page_text, "Перевозчик [1599] ООО \"Перевозчик\" не найден"
        # Кликаем по найденному TD для просмотра деталей
        admin_page.click_button(admin_page.truck_delivery_details)
        time.sleep(2)
        # Проверяем детали
        page_text = base.driver.page_source
        assert td_id in page_text, f"ID {td_id} не найден в деталях"
        assert "[1599] ООО \"Перевозчик\"" in page_text, "Перевозчик не найден в деталях"
        allure.attach(f"TD с ID {td_id} успешно найден, детали проверены",
                      "Результат",
                      allure.attachment_type.TEXT)

    @allure.title("Поиск по id заказов")
    @allure.description("Проверка поиска заказов по идентификатору")
    def test_search_order_by_id(self, admin_fixture, domain):
        """Тест: Поиск по id orders"""
        base = admin_fixture
        admin_page = AdminPage(base.driver, domain)
        admin_page.login()

        # ID для поиска
        order_id = "42260"
        # Переход в раздел Заказы на перевозку
        admin_page.click_button(admin_page.orders_menu)
        # Поиск по ID заказа
        admin_page.search(order_id)
        import time
        time.sleep(2)
        # Проверяем, что заказ найден
        page_text = base.driver.page_source
        assert order_id in page_text, f"Заказ с ID {order_id} не найден"
        # Кликаем по найденному заказу для просмотра деталей
        admin_page.click_button(admin_page.orders_menu_detail)
        time.sleep(2)
        # Проверяем детали заказа
        page_text = base.driver.page_source
        # Проверяем наличие Request и Request Nr на странице
        assert "Request" in page_text, "Текст 'Request' не найден на странице деталей"
        assert "Request Nr" in page_text or "RequestNr" in page_text, "Текст 'Request Nr' не найден на странице деталей"
        assert "26-138-2448" in page_text, "Номер '26-138-2448' не найден в деталях заказа"
        allure.attach(f"Заказ с ID {order_id} успешно найден, детали проверены",
                      "Результат",
                      allure.attachment_type.TEXT)

    @allure.title("Переход из карточки сотрудника в компанию")
    @allure.description("Проверка перехода из карточки сотрудника в карточку компании")
    def test_employee_to_company_transition(self, admin_fixture, domain):
        """Тест: Переход из карточки сотрудника в компанию"""
        base = admin_fixture
        admin_page = AdminPage(base.driver, domain)
        admin_page.login()

        # Переход в раздел Сотрудники
        admin_page.click_button(admin_page.employees_menu)
        # Поиск сотрудника по ID
        admin_page.search("13599")
        time.sleep(2)
        # Проверка что сотрудник найден
        page_text = base.driver.page_source
        assert "13599" in page_text, "Сотрудник с ID 13599 не найден"

        # Кликаем по сотруднику, чтобы открыть его карточку
        admin_page.click_button(admin_page.employees_details)
        time.sleep(2)
        # Переходим в организацию из карточки сотрудника
        admin_page.click_button(admin_page.employees_move_organization)
        time.sleep(2)
        # Проверяем данные организации
        page_text = base.driver.page_source
        assert "2447" in page_text, "ID организации 2447 не найден"
        assert "5178860124" in page_text, "ИНН 5178860124 не найден"
        allure.attach("Переход из сотрудника в компанию успешно выполнен, данные организации проверены",
                      "Результат",
                      allure.attachment_type.TEXT)

    @allure.title("Вход в ЛК Контрагента")
    @allure.description("Проверка возможности входа в личный кабинет контрагента из админки")
    def test_enter_counterparty_lk(self, admin_fixture, domain):
        """Тест: Вход в ЛК Контрагента"""
        base = admin_fixture
        admin_page = AdminPage(base.driver, domain)
        admin_page.login()

        admin_page.click_button(admin_page.counterparties_menu)
        admin_page.search("Auto LKP")
        time.sleep(2)
        # Проверка контрагента
        page_text = base.driver.page_source
        assert "6883106209" in page_text, "ИНН 6883106209 не найден"
        # Открытие карточки и вход в ЛК
        admin_page.click_button(admin_page.counterparties_details)
        time.sleep(2)
        admin_page.click_button(admin_page.counterparties_lkp)
        time.sleep(3)
        # Переключение на новую вкладку
        if len(base.driver.window_handles) > 1:
            base.driver.switch_to.window(base.driver.window_handles[-1])
        # Ждем загрузки страницы ЛК
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        # Ждем пока URL станет producer.vezubr.com
        WebDriverWait(base.driver, 15).until(
            EC.url_contains("producer.vezubr.com")
        )
        # Ждем появления логотипа или контента на странице
        try:
            WebDriverWait(base.driver, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(), 'Auto LKP') or contains(@class, 'logo')]"))
            )
        except:
            pass
        time.sleep(3)
        # Проверка входа в ЛК
        assert "producer.vezubr.com" in base.driver.current_url, "Не удалось войти в ЛК"
        assert "Auto LKP" in base.driver.page_source, "Auto LKP не найден в ЛК"
        allure.attach(f"Успешный вход в ЛК. URL: {base.driver.current_url}",
                      "Результат",
                      allure.attachment_type.TEXT)

    @allure.title("Проверка сортировок во всех разделах админки")
    def test_all_sortings_in_admin_tabs(self, admin_fixture, domain):
        """Тест: Проход по вкладкам админки и проверка сортировок"""
        base = admin_fixture
        admin_page = AdminPage(base.driver, domain)
        admin_page.login()

        tabs = [
            ("Контрагенты", admin_page.counterparties_menu),
            ("Организации", admin_page.organizations_menu),
            ("Сотрудники", admin_page.employees_menu),
            ("ПРР", admin_page.orders_prr),
            ("CDR", admin_page.cargo_delivery_request),
            ("TD", admin_page.truck_delivery),
            ("Заказы на перевозку", admin_page.orders_menu),
            ("Типы ТС", admin_page.vehicle_types),
            ("Справочник портов", admin_page.ports_directory),
            ("Страна", admin_page.country),
            ("Регионы", admin_page.regions),
            ("Населенные пункты", admin_page.localities),
        ]

        for tab_name, tab_locator in tabs:
            print(f"\n=== Раздел: {tab_name} ===")
            admin_page.click_button(tab_locator)
            time.sleep(2)

            # Вызываем метод сортировок для админки
            admin_page.click_sortings_in_admin(num_clicks=2)

            time.sleep(1)

    @allure.title("Проверка фильтров в разделе Контрагенты")
    def test_filters_in_counterparties(self, admin_fixture, domain):
        base = admin_fixture
        admin_page = AdminPage(base.driver, domain)
        admin_page.login()

        filters = [
            ("2308285850", "ООО ИМПУЛЬС ПЛЮС", "2308285850"),  # поиск, ожидание в списке, ожидание в деталке
            ("Auto LKZ", "2448", "Auto LKZ"),
            ("ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ \"ЛИНА\"", "4060",
             "ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ \"ЛИНА\""),
        ]

        for search_value, expected_in_list, expected_in_details in filters:
            admin_page.go_to_counterparties()
            time.sleep(2)
            admin_page.search(search_value)
            time.sleep(2)
            assert expected_in_list in admin_page.driver.page_source, f"Не найдено: {expected_in_list}"

            admin_page.click_button(admin_page.counterparties_details)
            time.sleep(2)
            assert expected_in_details in admin_page.driver.page_source, f"В деталке не найдено: {expected_in_details}"

        allure.attach("Все проверки фильтров в Контрагентах успешно завершены", "Итог", allure.attachment_type.TEXT)

    @allure.title("Проверка фильтров в разделе Сотрудники")
    def test_filters_in_employees(self, admin_fixture, domain):
        base = admin_fixture
        admin_page = AdminPage(base.driver, domain)
        admin_page.login()

        filters = [
            ("13593", "Автотест_LKEФедоров1776436984"),
            ("Жилиман Робаут API", "sovietkirby@tiffincrane.com"),
            ("79540012344", "12210"),
            ("guillemasubstantial@tiffincrane.com", "79550000013"),
        ]

        for search_value, expected_in_details in filters:
            admin_page.go_to_employees()
            time.sleep(2)
            admin_page.search(search_value)
            time.sleep(2)
            assert search_value in admin_page.driver.page_source, f"Сотрудник не найден: {search_value}"

            admin_page.click_button(admin_page.employees_details)
            time.sleep(2)
            assert expected_in_details in admin_page.driver.page_source, f"В деталке не найдено: {expected_in_details}"

        allure.attach("Все проверки фильтров в Сотрудниках успешно завершены", "Итог", allure.attachment_type.TEXT)

    @allure.title("Поиск по Населенным пунктам")
    @allure.description("Проверка поиска населенного пункта Ижевск")
    def test_search_localities(self, admin_fixture, domain):
        """Тест: Поиск населенного пункта Ижевск"""
        base = admin_fixture
        admin_page = AdminPage(base.driver, domain)

        admin_page.login()

        # Переход и поиск
        admin_page.click_button(admin_page.localities)
        admin_page.search("Ижевск")

        time.sleep(2)

        # Проверки
        page_text = base.driver.page_source
        assert "Ижевск" in page_text, "Ижевск не найден"
        assert "Удмуртская республика" in page_text, "Удмуртская республика не найдена"

        allure.attach("Поиск населенного пункта успешно выполнен",
                      "Результат",
                      allure.attachment_type.TEXT)