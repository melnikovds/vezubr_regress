import allure
import pytest
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cargo_place_list_page import CargoPlaceList
from pages.history_journal_page import Journal
from pages.filters_gm_lkz_lke_page import GmFilters
from pages.address_list_page import AddressesList
from pages.filter_directory_page import Manual
from pages.request_old_ftl_add_page import FTLAdd
from pages.filters_old_ftl_page import OldFTL


@allure.story("Extended test")
@allure.feature('Журналирование')
@allure.description('ЛКЗ. Проверка журналирования Грузоместа')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_journal_cargo_place_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Выбор нужного грузоместа
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button)
    fltr = GmFilters(base.driver)
    fltr.click_button_option(fltr.reset_filters, skip_if_not_clickable=True)
    fltr.dropdown_without_input(fltr.creation_date, "За все время")
    fltr.input_in_field(fltr.bar_code, value='2448000053332')
    time.sleep(3)
    lst = CargoPlaceList(base.driver)
    lst.click_button(lst.first_cp_link)
    time.sleep(2)
    # Переход в таб 'История'
    jrn = Journal(base.driver)
    jrn.click_button(jrn.tab_history_cargo_place)
    time.sleep(1)
    jrn.dropdown_without_input(jrn.time_event, option_text='За все время')
    time.sleep(10)
    jrn.verify_text_on_page(text='53332')
    jrn.verify_text_on_page(text='24.02.2026')
    jrn.verify_text_on_page(text='19225')
    jrn.verify_text_on_page(text='05.02.2026')


@allure.story("Extended test")
@allure.feature('Журналирование')
@allure.description('ЛКЗ. Проверка журналирования Адреса')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_journal_address_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Выбор нужного адреса
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button)
    fltr2 = Manual(base.driver)
    fltr2.click_button(element_dict=fltr2.reset)
    fltr2.dropdown_without_input(fltr2.filter_date_create, option_text='За все время')
    time.sleep(3)

    fltr = AddressesList(base.driver)
    fltr.input_in_field(fltr.name_filter, value='адресочек', wait="lst")
    fltr.click_button(fltr.first_address_link, wait="form")
    time.sleep(3)
    jrn = Journal(base.driver)
    jrn.click_button(jrn.tab_history_address)
    time.sleep(1)
    jrn.dropdown_without_input(jrn.time_event, option_text='За все время')
    time.sleep(7)
    jrn.verify_text_on_page(text='8283')
    jrn.verify_text_on_page(text='2448')
    jrn.verify_text_on_page(text='1191')
    jrn.verify_text_on_page(text='адресочек')
    jrn.verify_text_on_page(text='Гатчинский р-н')


@allure.story("Extended test")
@allure.feature('Журналирование')
@allure.description('ЛКЗ. Проверка журналирования Рейса')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_journal_order_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к созданию новой FTL заявки
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.new_ftl_city_button,
                           do_assert=True)

    ftl = FTLAdd(base.driver)
    # Сброс ранее введенных и сохраненных данных
    ftl.click_button(ftl.cancel_button)

    # Переход к созданию новой FTL заявки
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.new_ftl_city_button,
                           do_assert=True)

    # Установка даты подачи заявки на сегодня
    ftl.click_button(ftl.start_date_field)
    ftl.click_button(ftl.today_button)
    # Установка времени подачи заявки через 3 часа от текущего времени
    ftl.click_button(ftl.start_time_field)
    new_time = ftl.naw_time_change(180)
    ftl.input_in_field(ftl.start_time_input, new_time)
    time.sleep(1)
    # Выбор категории заявки - Груз
    ftl.click_button(ftl.request_category_select)
    ftl.click_button(ftl.select_freight)
    # Выбор типа ТС - до 0.5т
    ftl.click_button(ftl.vehicle_type_select)
    ftl.dropdown_with_input(ftl.vehicle_type_select, "до 0.5т")
    # Выбор типа кузова - Закрытый
    ftl.click_button(ftl.vehicle_body_select)
    ftl.click_button(ftl.body_type_closed_checkbox)
    # Выбор первого адреса из списка
    ftl.click_button(ftl.first_address_select)
    ftl.input_in_field(ftl.address_filter, "Гатчина, ул Карла Маркса, д 37", wait="lst")
    time.sleep(3)
    ftl.click_button(ftl.select_first_radio)
    time.sleep(1)
    ftl.click_button(ftl.confirm_address_button)
    time.sleep(1)
    # Выбор второго адреса из списка
    ftl.click_button(ftl.second_address_select)
    ftl.input_in_field(ftl.address_filter, "ул Орджоникидзе, д 31 к 2", wait="lst")
    time.sleep(3)
    ftl.click_button(ftl.select_first_radio)
    time.sleep(1)
    ftl.click_button(ftl.confirm_address_button)
    time.sleep(1)

    ftl.scroll_to_element(ftl.tariff_button)

    # Ожидание завершения расчета стоимости
    base.get_element(ftl.calculate_finish)
    # Публикация заявки с использованием тарифа
    ftl.click_button(ftl.tariff_button)
    ftl.click_button(ftl.producer_select)
    ftl.click_button(ftl.select_all_producer)
    time.sleep(1)
    ftl.click_button(ftl.producer_select_text)
    ftl.click_button(ftl.publish_button)
    ftl.click_button(ftl.continue_button, do_assert=True)


    # Находим элемент с сообщением
    wait = WebDriverWait(base.driver, 10)

    modal = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'ant-modal-confirm-content')]")
        )
    )
    text = modal.text.strip()

    # Извлекаем всё после "№" — только допустимые символы
    match = re.search(r'№([A-Za-z0-9\-]+)', text)

    if match:
        application_number = match.group(1)  # например: '25-VZ-494'
        print(f"Номер заявки: {application_number}")
    else:
        raise ValueError(f"Не удалось найти номер заявки в тексте: {text}")


    ftl.click_button(ftl.confirm_add_button, wait="lst")
    time.sleep(1)

    # Переход в раздел Активные FTL-заявки
    base.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_active_list_button,
                        do_assert=True, wait='lst')

    add = OldFTL(base.driver)
    # сброс фильтров
    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    add.click_button(add.start_date)
    time.sleep(1)
    add.click_button(add.all_time)
    time.sleep(1)

    # выбираем созданную заявку
    add.input_in_field(add.request_number, value=application_number, click_first=True)
    time.sleep(3)
    ftl.click_button(ftl.click_on_request)
    time.sleep(2)
    jrn = Journal(base.driver)
    jrn.click_button(jrn.tab_history_old_request)
    time.sleep(1)
    jrn.dropdown_without_input(jrn.time_event, option_text='За все время')
    time.sleep(7)
    jrn.verify_text_on_page(text='Время публикации')
    jrn.verify_text_on_page(text='Отложена Заказчиком')


























