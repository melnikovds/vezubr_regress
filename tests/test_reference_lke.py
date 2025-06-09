import time

import allure
import pytest

from pages.manual_page import Manual
from pages.reference_page import Filter


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description("ЛКЗ Тест фильтра 'Адреса' в разделе справочники")
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_address_directory_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    with allure.step("Переход к списку адресов"):
        base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                            do_assert=True, wait='lst')

    add = Filter(base.driver)

    with allure.step("сброс фильтров"):
        add.click_button(element_dict=add.refresh)

    with allure.step('проверка фильтра "дата создания"'):
        add.dropdown_without_input(add.creation_date, option_text='За год')
        time.sleep(3)

    with allure.step('проверка фильтра "подтвержденный адрес"'):
        add.input_in_field(add.confirm_address, "Ижевск, ул Дзержинского")
        time.sleep(2)
        add.verify_text_on_page(text='Ижевск, ул Дзержинского')
        add.backspace_and_input(add.confirm_address, value='')

    with allure.step('проверка фильтра "название адреса"'):
        add.input_in_field(add.name_address, "Autotests")
        time.sleep(2)
        add.verify_text_on_page(text='Ижевск, ул Телегина')
        add.backspace_and_input(add.name_address, value='')

    with allure.step('проверка фильтра "отправитель/получатель"'):
        add.input_in_field(add.sender_recipient, "ООО ЭЛЕТЕК")
        time.sleep(2)
        add.verify_text_on_page(text=' Ижевск, ул Крылова')
        add.backspace_and_input(add.sender_recipient, value='')

    with allure.step('проверка фильтра "регион"'):
        add.dropdown_without_input(add.region, option_text='Удмуртская республика')
        time.sleep(1)
        add.verify_text_on_page('Ижевск')

    with allure.step("сброс фильтров"):
        add.click_button(element_dict=add.refresh)

    with allure.step('проверка фильтра "подтвердил"'):
        add.input_in_field(add.confirmed, "auto@LKE.com", wait='lst')
        time.sleep(1)
        add.verify_text_on_page(text='Ижевск')
        add.backspace_and_input(add.confirmed, value='')

    with allure.step('проверка фильтра "Создал"'):
        add.input_in_field(add.created, "auto@LKE.com", wait='lst')
        time.sleep(1)
        add.verify_text_on_page(text='Ижевск')
        add.backspace_and_input(add.created, value='')

    with allure.step('проверка фильтра "ID Адреса Партнёра"'):
        add.input_in_field(add.partner_id, "Autotests")
        time.sleep(2)
        add.verify_text_on_page(text='Ижевск, ул Телегина')
        add.backspace_and_input(add.partner_id, value='')

    with allure.step('проверка фильтра "Владелец Адреса"'):
        add.input_in_field(add.address_owner, "Auto LKE")
        time.sleep(2)
        add.verify_text_on_page(text='Ижевск, ул Телегина')
        add.backspace_and_input(add.address_owner, value='')

    with allure.step("сброс фильтров"):
        add.click_button(element_dict=add.refresh)


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description("ЛКЗ Тест фильтра 'тарифы' в разделе справочники")
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_tariff_directory_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    with allure.step("Переход к списку тарифов"):
        base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                            do_assert=True, wait='lst')

    add = Filter(base.driver)
    with allure.step('проверка фильтра "создал"'):
        add.input_in_field(add.tariff_name, "Autotests")
        time.sleep(1)
        add.verify_text_on_page(text='Autotests FTL')
        add.backspace_and_input(add.confirmed, value='')

    with allure.step('проверка фильтра "статус"'):
        add.dropdown_without_input(add.tariff_status, option_text='Не активный')
        time.sleep(2)
        add.verify_text_on_page(text='Autotests FTL', should_exist=True)
        add.verify_text_on_page(text='Autotests FTL фиксированный', should_exist=False)
        time.sleep(2)


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description("ЛКЭ Тест фильтра 'водители' в разделе справочники")
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_drivers_directory_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    with allure.step("Переход к списку водителей"):
        base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                            do_assert=True, wait='lst')
        add = Filter(base.driver)
    with allure.step('проверка фильтра "Фамилия"'):
        add.input_in_field(add.soname_driver, "Prime")
        time.sleep(1)
        add.verify_text_on_page(text='Avtobot')
        add.backspace_and_input(add.soname_driver, value='')

    with allure.step('проверка фильтра "Имя"'):
        add.input_in_field(add.name_driver, "Avtobot")
        time.sleep(1)
        add.verify_text_on_page(text='Avtobot')
        add.backspace_and_input(add.name_driver, value='')

    with allure.step('проверка фильтра "Отчество"'):
        add.input_in_field(add.surname, "Emecron", wait='lst')
        time.sleep(3)
        add.verify_text_on_page(text='Avtobot')
        add.backspace_and_input(add.surname, value='')

    with allure.step('проверка фильтра "Телефон"'):
        add.input_in_field(add.phone_driver, "70000000001")
        time.sleep(1)
        add.verify_text_on_page(text='Avtobot')
        add.backspace_and_input(add.phone_driver, value='')

    with allure.step('проверка фильтра "подрядчик"'):
        add.input_in_field(add.contractor, "Auto LKE")
        time.sleep(1)
        add.verify_text_on_page(text='Avtobot')
        add.backspace_and_input(add.contractor, value='')

    with allure.step('проверка фильтра "статус в рейсе"'):
        add.dropdown_without_input(add.flight_status, "Назначен на заказ")
        time.sleep(1)
        add.verify_text_on_page(text='Жилиман')
        add.dropdown_without_input(add.flight_status, "На заказе")
        add.verify_text_on_page(text='79655151885')
        add.dropdown_without_input(add.flight_status, "Работа приостановлена")
        add.verify_text_on_page(text='79650084909')


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description("ЛКЭ Тест фильтра 'тягачи' в разделе справочники")
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_tractors_directory_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    with allure.step("Переход к списку тягачей"):
        base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tractors_list_button,
                            do_assert=True, wait='lst')
        add = Filter(base.driver)
    with allure.step('проверка фильтра "госномер тягачей"'):
        add.input_in_field(add.number_of_tractor, "WAHATRACK")
        add.verify_text_on_page(text='KAMAZ')
        add.input_in_field(add.number_of_tractor, "")

    with allure.step('проверка фильтра "подрядчик"'):
        add.input_in_field(add.contractor_tractor, "Auto LKE")
        add.verify_text_on_page(text='WAHATRACK')
        add.input_in_field(add.contractor_tractor, "")

    with allure.step('проверка фильтра "Статус в рейсе"'):
        add.dropdown_without_input(add.flight_status_tractor, "Эксплуатация приостановлена")
        time.sleep(1)
        add.verify_text_on_page(text='Е406НУ')
        add.dropdown_without_input(add.flight_status_tractor, "Нет заказов")
        add.verify_text_on_page(text='WAHATRACK')


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description("ЛКП Тест фильтра 'Полуприцепы' в разделе справочники")
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_trailer_directory_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    with allure.step('переход к списку тягачей'):
        base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.trailers_list_button,
                            do_assert=True, wait='lst')
        add = Filter(base.driver)
    with allure.step('проверка фильтра "Госномер Полуприцепа"'):
        add.input_in_field(add.number_of_trailer, "WAHATRACK")
        add.verify_text_on_page(text='WAHATRACKПРИЦЕП')
        add.input_in_field(add.number_of_trailer, "")

    with allure.step('проверка фильтра "тип автоперевозки грузовая"'):
        add.dropdown_without_input(add.type_of_road_trailer, "Грузовая")
        add.verify_text_on_page(text='WAHATRACKПРИЦЕП')

    with allure.step('проверка фильтра "статус в рейсе"'):
        add.dropdown_without_input(add.flight_status_trailer, "Эксплуатация приостановлена")
        time.sleep(1)
        add.verify_text_on_page(text='ПП20240126103514')
        add.dropdown_without_input(add.flight_status_trailer, "Нет заказов")
        add.verify_text_on_page(text='WAHATRACK')
        add.dropdown_without_input(add.flight_status_trailer, "Назначен на заказ")
        add.verify_text_on_page(text='ПП-20250309203400')


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description("ЛКП Тест фильтра 'ТС' в разделе справочники")
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_vehicle_directory_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    with allure.step('переход к списку ТС'):
        base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                            do_assert=True, wait='lst')
        add = Filter(base.driver)
        com = Manual(base.driver)
    with allure.step('проверка фильтра "госномер ТС"'):
        add.input_in_field(add.number_vehicles, "WH40")
        time.sleep(2)
        add.verify_text_on_page(text='WH400000')
        add.backspace_and_input(add.number_vehicles, "")

    with allure.step('проверка фильтра "имя водителя"'):
        add.input_in_field(add.name_driver_vehicle, "Робаут")
        time.sleep(1)
        add.verify_text_on_page(text='WAHATRACK')
        add.backspace_and_input(add.name_driver_vehicle, "")

    with allure.step('проверка фильтра "фамилия водителя"'):
        add.input_in_field(add.surname_driver_vehicle, "Жилиман")
        time.sleep(2)
        add.verify_text_on_page(text='WAHATRACK')
        add.backspace_and_input(add.surname_driver_vehicle, "")

    with allure.step('проверка фильтра "отчество водителя"'):
        add.input_in_field(add.patronymic_driver_vehicle, "Астартес")
        time.sleep(2)
        add.verify_text_on_page(text='WAHATRACK')
        add.backspace_and_input(add.patronymic_driver_vehicle, "")

    with allure.step('проверка фильтра "отчество водителя"'):
        add.input_in_field(add.contractor_vehicle, "Auto LKP")
        time.sleep(2)
        add.verify_text_on_page(text='WH400000')
        add.backspace_and_input(add.contractor_vehicle, "")

    with allure.step('проверка фильтра "тип авто перевозки"'):
        add.move_to_element(com.type_road_transport_two)
        time.sleep(2)
        add.click_on_the_cross(com.cross_six)
        time.sleep(2)
        add.move_and_click(move_to=com.type_road_transport_two, click_to=com.cargo_transportation)
        time.sleep(15)
        add.verify_text_on_page(text='WH400000', should_exist=True)
        add.verify_text_on_page(text='ТК567У', should_exist=False)
        time.sleep(2)
        add.move_to_element(com.type_road_transport_two)
        time.sleep(2)
        add.click_on_the_cross(com.cross_six)
        time.sleep(2)
        add.move_and_click(move_to=com.type_road_transport_two, click_to=com.cargo_passenger_transportation)
        time.sleep(3)
        add.verify_text_on_page(text='А444АА', should_exist=True)
        add.verify_text_on_page(text='ТС20231229113421', should_exist=False)
        time.sleep(2)
        add.move_to_element(com.type_road_transport_two)
        time.sleep(2)
        add.click_on_the_cross(com.cross_six)
        time.sleep(2)
        add.move_and_click(move_to=com.type_road_transport_two, click_to=com.special_transportation)
        time.sleep(1)
        add.click_button(com.manipulator_truck)
        time.sleep(3)
        add.verify_text_on_page(text='ВТС-20240512231701', should_exist=True)
        add.verify_text_on_page(text='ТС20240110120731', should_exist=False)
        time.sleep(2)
        add.move_to_element(com.type_road_transport_two)
        time.sleep(2)
        add.click_on_the_cross(com.cross_six)
        time.sleep(2)
