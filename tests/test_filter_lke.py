import time
import allure
import pytest
from pages.filters_gm_lkz_lke_page import GmFilters


@allure.story("Extended")
@allure.feature('Фильтры')
@allure.description('ЛКЭ, Тестирование: фильтры в разделе "Отправления"')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_filter_departures_lke(base_fixture, domain, request):
    base, sidebar = base_fixture

    with allure.step("Переходим на вкладку 'Задания'"):
        sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.dispatch_list_button)
        add = GmFilters(base.driver)

    with allure.step("Проверка фильтра 'Номер рейса'"):
        add.input_in_field(add.flight_number, "R-25-173-2448-1", wait='lst')
        time.sleep(2)
        add.verify_text_on_page(text="2448445390000")
        add.backspace_and_input(add.flight_number, "")

    with allure.step("Проверка фильтра 'По заданию №'"):
        add.input_in_field(add.according_task, "2448442650000", wait='lst')
        time.sleep(2)
        add.verify_text_on_page(text="R-25-122-2448-1")
        add.backspace_and_input(add.according_task, "")

    with allure.step("Проверка фильтров 'Адрес отправления/доставки'"):
        add.filter_departures_address()

    with allure.step("Проверка фильтра 'Статус'"):
        add.filter_departure_status()


@allure.story("Extended")
@allure.feature('Фильтры')
@allure.description('ЛКЭ, Тестирование: фильтры в разделе "Грузоместа"')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_filter_gm_lke(base_fixture, domain, request):
    base, sidebar = base_fixture

    with allure.step("Переходим на вкладку 'Задания'"):
        sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button)
        add = GmFilters(base.driver)

    with allure.step("сброс фильтров"):
        add.click_button_option(add.reset_filters, skip_if_not_clickable=True)

    with allure.step("Устанавливаем дату создания за все время"):
        add.dropdown_without_input(add.creation_date, "За все время")

    with allure.step("Проверка фильтра 'Номер рейса'"):
        add.input_in_field(add.flight_number, "R-25-173-2448-1")
        time.sleep(2)
        add.verify_text_on_page(text="2448445390000")
        add.backspace_and_input(add.flight_number, "")

    with allure.step("Проверка фильтра 'id ГМ партнера'"):
        add.input_in_field(add.partner_gm_id, "Тестовое ГМ", wait='lst')
        time.sleep(2)
        add.verify_text_on_page(text="2448445650000")
        add.backspace_and_input(add.partner_gm_id, "")

    with allure.step("Проверка фильтра 'Тип ГМ'"):
        add.filter_type_gm()

    with allure.step("Проверка фильтра 'Наименование ГМ'"):
        add.input_in_field(add.name_gm, "Паллета new", wait='lst')
        time.sleep(2)
        add.verify_text_on_page(text="2448445650000")
        add.backspace_and_input(add.name_gm, "")

    with allure.step("Проверка фильтра 'Адрес отправления'"):
        add.input_in_field(add.departure_address_gm, "Дзержинского", wait='lst')
        add.verify_text_on_page(text="2448445650000")
        add.backspace_and_input(add.departure_address_gm, "")

    with allure.step("Проверка фильтра 'Адрес доставки'"):
        add.input_in_field(add.delivery_address_gm, "Крылова", wait='lst')
        add.verify_text_on_page(text="2448445650000")
        add.backspace_and_input(add.delivery_address_gm, "")

    with allure.step("Проверка фильтра 'Номер накладной'"):
        add.input_in_field(add.invoice_number, "000000001", wait='lst')
        time.sleep(2)
        add.verify_text_on_page(text="2448445650000")
        add.backspace_and_input(add.invoice_number, "")

    with allure.step("Проверка фильтра 'Номер WMS'"):
        add.input_in_field(add.wms_number, "000000002", wait='lst')
        time.sleep(2)
        add.verify_text_on_page(text="2448445650000")
        add.backspace_and_input(add.wms_number, "")

    with allure.step("Проверка фильтра 'Bar Code'"):
        add.input_in_field(add.bar_code, "2448445650000", wait='lst')
        time.sleep(2)
        add.verify_text_on_page(text="Паллета new")
        add.backspace_and_input(add.bar_code, "")

    with allure.step("Проверка фильтров 'Регионы'"):
        add.filters_region_gm()
