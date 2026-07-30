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
from pages.contractor_page import Contractor
from pages.contractor_list_page import ContractorList
from pages.clients_list_page import ClientsList
from pages.filters_new_ftl_page import NewFtlFilters
from pages.cdr_ftl_page import AddCdr


@allure.story("Extended test")
@allure.feature('Журналирование')
@allure.description('ЛКЭ. Проверка журналирования Грузоместа')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_journal_cargo_place_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Выбор нужного грузоместа
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button)
    fltr = GmFilters(base.driver)
    fltr.click_button_option(fltr.reset_filters, skip_if_not_clickable=True)
    fltr.dropdown_without_input(fltr.creation_date, "За все время")
    fltr.input_in_field(fltr.bar_code, value='12093708')
    time.sleep(3)
    lst = CargoPlaceList(base.driver)
    lst.click_button(lst.first_cp_link)
    time.sleep(2)
    # Переход в таб 'История'
    jrn = Journal(base.driver)
    jrn.click_button(jrn.tab_history_cargo_place)
    time.sleep(1)
    jrn.dropdown_without_input(jrn.time_event, option_text='За все время')
    time.sleep(7)
    jrn.verify_text_on_page(text='12.03.2025')
    jrn.verify_text_on_page(text='43852')
    jrn.verify_text_on_page(text='Создано')


@allure.story("Extended test")
@allure.feature('Журналирование')
@allure.description('ЛКЭ. Проверка журналирования Адреса')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_journal_address_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Выбор нужного адреса
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button)
    fltr2 = Manual(base.driver)
    fltr2.click_button(element_dict=fltr2.reset)
    fltr2.dropdown_without_input(fltr2.filter_date_create, option_text='За все время')
    time.sleep(3)

    fltr = AddressesList(base.driver)
    fltr.input_in_field(fltr.name_filter, value='собств2', wait="lst")
    fltr.click_button(fltr.first_address_link, wait="form")
    time.sleep(3)
    jrn = Journal(base.driver)
    jrn.click_button(jrn.tab_history_address)
    time.sleep(1)
    jrn.dropdown_without_input(jrn.time_event, option_text='За все время')
    time.sleep(10)
    jrn.verify_text_on_page(text='05.03.2026')
    jrn.verify_text_on_page(text='28549')
    jrn.verify_text_on_page(text='Пороховая')
    jrn.verify_text_on_page(text='Europe/Moscow')
    jrn.verify_text_on_page(text='собств2')


@allure.story("Extended test")
@allure.feature('Журналирование')
@allure.description('ЛКЭ. Проверка журналирования Рейса')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_journal_order_lke(base_fixture, domain):
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
    time.sleep(3)

    # Выбор владельца заявки
    ftl.dropdown_without_input(ftl.request_owner_select, "Собственный Заказ")

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
    ftl.click_and_select_with_arrows(ftl.vehicle_type_select,arrow_presses=5)
    # Выбор типа кузова - Закрытый
    ftl.click_button(ftl.vehicle_body_select)
    ftl.click_button(ftl.body_type_closed_checkbox)
    ftl.click_outside()
    time.sleep(1)
    # Выбор первого адреса из списка
    ftl.click_button(ftl.first_address_select)
    ftl.input_in_field(ftl.address_filter, "Россия, г Тула, ул Пороховая", wait="lst")
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    time.sleep(3)
    # Выбор второго адреса из списка
    ftl.click_button(ftl.second_address_select)
    ftl.input_in_field(ftl.address_filter, "Россия, г Калуга, ул Кирова", wait="lst")
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)

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
    time.sleep(10)
    jrn.verify_text_on_page(text='Время публикации')
    jrn.verify_text_on_page(text='Отложена Заказчиком')


@allure.story("Extended test")
@allure.feature('Журналирование')
@allure.description('ЛКЭ. Проверка журналирования Контрагента')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_journal_contractor_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    ctr = ContractorList(base.driver)
    cl = ClientsList(base.driver)
    jrn = Journal(base.driver)

    # Выбор нужного контрагента
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")
    time.sleep(2)
    ctr.input_in_field(ctr.contractor_name, value='трейд')
    time.sleep(2)
    cl.click_button(cl.client_inn)
    time.sleep(1)
    jrn.click_button(jrn.tab_history_contractor)
    time.sleep(1)
    jrn.dropdown_without_input(jrn.time_event, option_text='За все время')
    time.sleep(10)
    jrn.verify_text_on_page(text='79551717320')
    jrn.verify_text_on_page(text='8863224672')
    jrn.verify_text_on_page(text='ул. Б. Якиманка, д.72')
    jrn.verify_text_on_page(text='auto@LKE.com')


@allure.story("Extended test")
@allure.feature('Журналирование')
@allure.description('ЛКЭ. Проверка журналирования Договора')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_journal_agreement_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    ctr = ContractorList(base.driver)
    cl = ClientsList(base.driver)
    ct = Contractor(base.driver)
    jrn = Journal(base.driver)

    # Выбор нужного контрагента
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")
    time.sleep(2)
    ctr.input_in_field(ctr.contractor_name, value='трейд')
    time.sleep(2)
    cl.click_button(cl.client_inn)
    time.sleep(1)
    ct.click_button(ct.agreement_link_four)
    jrn.click_button(jrn.tab_history_agreement)
    time.sleep(1)
    jrn.dropdown_without_input(jrn.time_event, option_text='За все время')
    time.sleep(10)
    jrn.verify_text_on_page(text='по новым правилам')
    jrn.verify_text_on_page(text='91233237')
    jrn.verify_text_on_page(text='91-233-237')


@allure.story("Critical test")
@allure.feature('Журналирование')
@allure.description('ЛКЭ. Проверка журналирования FTL Заявки')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_journal_cdr_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    add = NewFtlFilters(base.driver)
    cdr = AddCdr(base.driver)
    jrn = Journal(base.driver)

    # Выбор нужной Заявки
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.cdr_active_list_button,
                           do_assert=True, wait="lst")

    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(1)
    add.input_in_field(add.request_number, value='26-VZ-197')
    time.sleep(3)
    cdr.click_button(cdr.click_first_element)
    time.sleep(1)
    jrn.click_button(jrn.tab_history_ftl_request)
    time.sleep(1)
    jrn.dropdown_without_input(jrn.time_event, option_text='За все время')
    time.sleep(10)
    jrn.verify_text_on_page(text='Статус Заявки')
    jrn.verify_text_on_page(text='auto@LKZ')
    jrn.verify_text_on_page(text='6094')
    jrn.verify_text_on_page(text='ТОРНАДО')