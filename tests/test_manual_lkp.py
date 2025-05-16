import time

import allure
import pytest

from pages.manual_page import Manual


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description("ЛКП Тест фильтра 'Тарифы' в разделе справочники")
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_tariff_directory_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # переход к списку тарифов
    base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                        do_assert=True, wait='lst')

    add = Manual(base.driver)
    # проверка фильтра "Название тарифа"
    add.input_in_field(add.tariff_name, value='20241204172', click_first=True)
    time.sleep(2)
    add.verify_text_on_page(text='LTL-20241204172745', should_exist=True)
    add.verify_text_on_page(text='ГГ-20241210025702', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.tariff_name, value='')
    time.sleep(2)

    # проверка №1 фильтра "Статус"
    add.dropdown_without_input(add.tariff_status, option_text='Не активный')
    time.sleep(2)
    add.verify_text_on_page(text='ПРР-20250427180750', should_exist=True)
    add.verify_text_on_page(text='ПБ-20241205233932', should_exist=False)
    time.sleep(2)

    # проверка №2 фильтра "Статус"
    add.dropdown_without_input(add.tariff_status, option_text='Активный')
    time.sleep(2)
    add.verify_text_on_page(text='ПЧ-20250430024902', should_exist=True)
    add.verify_text_on_page(text='ПРР-20241205194647', should_exist=False)
    time.sleep(2)

    # проверка №1 фильтра с несколькими значениями
    add.input_in_field(add.tariff_name, value='ПРР-20241209183834', click_first=True)
    add.dropdown_without_input(add.tariff_status, option_text='Не активный')
    time.sleep(2)
    add.find_text_on_page(text='83834', occurrences=3)
    add.verify_text_on_page(text='10.12.2024 01:11', should_exist=True)
    add.verify_text_on_page(text='ПРР-20241209145054', should_exist=False)
    add.verify_text_on_page(text='212151', should_exist=False)
    time.sleep(2)

    # очистка поля "Название тарифа"
    add.backspace_and_input(add.tariff_name, value='')

    # проверка №2 фильтра с несколькими значениями
    add.input_in_field(add.tariff_name, value='ПЧ-20240716214624', click_first=True)
    add.dropdown_without_input(add.tariff_status, option_text='Активный')
    time.sleep(2)
    add.find_text_on_page(text='624', occurrences=3)
    add.verify_text_on_page(text='10.12.2024 00:11', should_exist=False)
    add.verify_text_on_page(text='ПРР-20241209145054', should_exist=False)
    add.verify_text_on_page(text='212151', should_exist=False)
    time.sleep(2)

    # очистка поля "Название тарифа"
    add.backspace_and_input(add.tariff_name, value='')

    # Конец теста


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description("ЛКП Тест фильтра 'Водители' в разделе справочники")
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_driver_directory_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # переход к списку водителей
    base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                        do_assert=True, wait='lst')

    # очистка полей с выпадающими списками
    add = Manual(base.driver)
    add.move_to_element(add.status_in_system)
    time.sleep(2)
    add.click_on_the_cross(add.cross_two)
    time.sleep(2)
    add.move_to_element(add.status_on_flight)
    time.sleep(2)
    add.click_on_the_cross(add.cross_three)
    time.sleep(2)

    # проверка фильтра "Фамилия"
    add.backspace_and_input(add.surname_driver, value='')
    time.sleep(1)
    add.input_in_field(add.surname_driver, value='2205347', click_first=True)
    time.sleep(3)
    add.verify_text_on_page(text='Ф-20241212205347', should_exist=True)
    add.verify_text_on_page(text='Ф-20241211051656', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.surname_driver, value='')
    time.sleep(1)
    add.input_in_field(add.surname_driver, value='Ф-20240531043410', click_first=True)
    time.sleep(2)
    add.find_text_on_page(text='43410', occurrences=3)
    time.sleep(1)
    add.backspace_and_input(add.surname_driver, value='')
    time.sleep(1)

    # проверка №1 фильтра "Статус в системе"
    add.click_and_select_with_arrows(add.status_in_system, arrow_presses=1)
    time.sleep(3)
    add.verify_text_on_page(text='Ф-20241210204128', should_exist=True)
    add.verify_text_on_page(text='Ф-20241209193525', should_exist=False)
    time.sleep(2)

    # проверка №2 фильтра "Статус в системе"
    add.dropdown_without_input(add.status_in_system, option_text='Активный')
    time.sleep(3)
    add.verify_text_on_page(text='Ф-20240320192739', should_exist=True)
    add.verify_text_on_page(text='Ф-20240524143334', should_exist=False)
    time.sleep(2)

    # проверка №1 фильтра "Статус в рейсе"
    add.dropdown_without_input(add.status_on_flight, option_text='Нет заказов')
    time.sleep(3)
    add.verify_text_on_page(text='И-20240110134909', should_exist=True)
    add.verify_text_on_page(text='И-20241211032444', should_exist=False)
    time.sleep(2)

    # проверка №2 фильтра "Статус в рейсе"
    add.dropdown_without_input(add.status_on_flight, option_text='Назначен на заказ')
    time.sleep(3)
    # add.verify_text_on_page(text='Ф-20240515185027', should_exist=True)
    add.verify_text_on_page(text='Ф-20241211051656', should_exist=False)
    time.sleep(2)

    # проверка №3 фильтра "Статус в рейсе"
    add.dropdown_without_input(add.status_on_flight, option_text='На заказе')
    time.sleep(3)
    # add.verify_text_on_page(text='Ф-20241204160029', should_exist=True)
    add.verify_text_on_page(text='Ф-20241209193448', should_exist=False)
    time.sleep(2)

    # проверка №4 фильтра "Статус в рейсе"
    add.dropdown_without_input(add.status_on_flight, option_text='Работа приостановлена')
    time.sleep(3)
    add.verify_text_on_page(text='Ф-20240806185159', should_exist=True)
    add.verify_text_on_page(text='Ф-20241210010831', should_exist=False)
    time.sleep(2)

    add.dropdown_without_input(add.status_in_system, option_text='Активный')
    add.dropdown_without_input(add.status_on_flight, option_text='Нет заказов')

    # проверка фильтра "Имя"
    add.input_in_field(add.name_driver, value='93449', click_first=True)
    time.sleep(1)
    add.verify_text_on_page(text='И-20241209193449', should_exist=True)
    add.verify_text_on_page(text='И-20241210010831', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.name_driver, value='')
    time.sleep(1)
    add.input_in_field(add.name_driver, value='И-20241205221738', click_first=True)
    time.sleep(2)
    add.find_text_on_page(text='79651895827', occurrences=2)
    time.sleep(1)
    add.backspace_and_input(add.name_driver, value='')
    time.sleep(1)

    # проверка фильтра "Отчество"
    add.input_in_field(add.patronymic_driver, value='5235', click_first=True)
    time.sleep(1)
    add.verify_text_on_page(text='О-20241210205235', should_exist=True)
    add.verify_text_on_page(text='О-20241210010752', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.patronymic_driver, value='')
    time.sleep(1)
    add.input_in_field(add.patronymic_driver, value='О-20241209193526', click_first=True)
    time.sleep(2)
    add.find_text_on_page(text='79659326139', occurrences=2)
    time.sleep(1)
    add.backspace_and_input(add.patronymic_driver, value='')
    time.sleep(1)

    # очистка полей с выпадающими списками
    add.move_to_element(add.status_in_system)
    time.sleep(2)
    add.click_on_the_cross(add.cross_two)
    time.sleep(2)
    add.move_to_element(add.status_on_flight)
    time.sleep(2)
    add.click_on_the_cross(add.cross_three)
    time.sleep(2)

    # проверка фильтра "Телефон"
    add.input_in_field(add.telephone_driver, value='18834', click_first=True)
    time.sleep(1)
    add.verify_text_on_page(text='79659218834', should_exist=True)
    add.verify_text_on_page(text='79653420389', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.telephone_driver, value='')
    time.sleep(1)
    add.input_in_field(add.telephone_driver, value='79654648108', click_first=True)
    time.sleep(2)
    add.find_text_on_page(text='79658472612', occurrences=2)
    time.sleep(1)
    add.backspace_and_input(add.telephone_driver, value='')
    time.sleep(1)

    # очистка полей с выпадающими списками
    add.move_to_element(add.status_in_system)
    time.sleep(2)
    add.click_on_the_cross(add.cross_two)
    time.sleep(2)
    add.move_to_element(add.status_on_flight)
    time.sleep(2)
    add.click_on_the_cross(add.cross_three)
    time.sleep(2)

    # проверка №1 фильтра с несколькими значениями
    add.input_in_field(add.surname_driver, value='80111', click_first=True)
    add.input_in_field(add.name_driver, value='180112', click_first=True)
    add.input_in_field(add.patronymic_driver, value='О-20241002180112', click_first=True)
    time.sleep(2)
    add.verify_text_on_page(text='Ф-20241002180111', should_exist=True)
    add.verify_text_on_page(text='Ф-20241002180015', should_exist=False)

    add.backspace_and_input(add.surname_driver, value='')
    add.backspace_and_input(add.name_driver, value='')
    add.backspace_and_input(add.patronymic_driver, value='')

    # проверка №2 фильтра с несколькими значениями
    add.dropdown_without_input(add.status_in_system, option_text='Неактивный')
    add.input_in_field(add.telephone_driver, value='79657063014', click_first=True)
    time.sleep(2)
    add.verify_text_on_page(text='И-20240806184630', should_exist=True)
    add.verify_text_on_page(text='И-20241207114547', should_exist=False)

    add.backspace_and_input(add.telephone_driver, value='')

    # Конец теста


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description("ЛКП Тест фильтра 'ТС' в разделе справочники")
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_transport_directory_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # переход к списку ТС
    base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                        do_assert=True, wait='lst')

    add = Manual(base.driver)
    add.move_to_element(add.type_road_transport_two)
    time.sleep(2)
    add.click_on_the_cross(add.cross_six)
    time.sleep(2)

    # проверка фильтра "Тип автоперевозки"
    add.move_and_click(move_to=add.type_road_transport_two, click_to=add.cargo_transportation)
    time.sleep(4)
    add.verify_text_on_page(text='ТС20231229113421', should_exist=True)
    add.verify_text_on_page(text='ТК567У', should_exist=False)
    add.verify_text_on_page(text='ТС-20240417063916', should_exist=False)
    add.verify_text_on_page(text='ТС-20240515211030', should_exist=False)
    time.sleep(2)

    add.move_to_element(add.type_road_transport_two)
    time.sleep(2)
    add.click_on_the_cross(add.cross_six)
    time.sleep(2)

    add.move_and_click(move_to=add.type_road_transport_two, click_to=add.cargo_passenger_transportation)
    time.sleep(3)
    add.verify_text_on_page(text='ТС-20240417065434', should_exist=True)
    add.verify_text_on_page(text='А444АА', should_exist=True)
    add.verify_text_on_page(text='ТС20231229113421', should_exist=False)
    time.sleep(2)

    add.move_to_element(add.type_road_transport_two)
    time.sleep(2)
    add.click_on_the_cross(add.cross_six)
    time.sleep(2)

    add.move_and_click(move_to=add.type_road_transport_two, click_to=add.special_transportation)
    time.sleep(1)
    add.click_button(add.manipulator_truck)
    time.sleep(3)
    add.verify_text_on_page(text='ТС-20240512232418', should_exist=True)
    add.verify_text_on_page(text='ТС-20240417063916', should_exist=True)
    add.verify_text_on_page(text='ТС20240110120731', should_exist=False)
    time.sleep(2)

    add.move_to_element(add.type_road_transport_two)
    time.sleep(2)
    add.click_on_the_cross(add.cross_six)
    time.sleep(2)

    # проверка фильтра "госномер ТС"
    add.input_in_field(add.transport_number, value='442')
    time.sleep(3)
    add.verify_text_on_page(text='ТС20240116120442', should_exist=True)
    add.verify_text_on_page(text='ТС-20241108044244', should_exist=True)
    add.verify_text_on_page(text='ТС20240116131611', should_exist=False)
    time.sleep(2)

    add.move_to_element(add.transport_number)
    time.sleep(2)
    add.click_on_the_cross(add.cross_seven)
    time.sleep(2)

    # проверка фильтра "Статус в системе"
    add.dropdown_without_input(add.status_in_system_two, option_text='Неактивный')
    time.sleep(3)
    add.verify_text_on_page(text='ТС-20240418133910', should_exist=True)
    add.verify_text_on_page(text='ТС20231229113421', should_exist=False)
    time.sleep(2)

    add.dropdown_without_input(add.status_in_system_two, option_text='Активный')
    time.sleep(3)
    add.verify_text_on_page(text='ТС20240110120731', should_exist=True)
    add.verify_text_on_page(text='ТС-20240419044633', should_exist=False)
    time.sleep(2)

    add.move_to_element(add.status_in_system_two)
    time.sleep(2)
    add.click_on_the_cross(add.cross_two)
    time.sleep(2)

    # проверка №1 фильтра "Статус в рейсе"
    add.dropdown_without_input(add.status_on_flight, option_text='Нет заказов')
    time.sleep(3)
    add.verify_text_on_page(text='ТС20240112133709', should_exist=True)
    add.verify_text_on_page(text='ПРО_СТО', should_exist=False)
    time.sleep(2)

    add.move_to_element(add.status_on_flight)
    time.sleep(2)
    add.click_on_the_cross(add.cross_eight)
    time.sleep(2)

    # проверка №2 фильтра "Статус в рейсе"
    add.dropdown_without_input(add.status_on_flight, option_text='Назначен на заказ')
    time.sleep(3)
    add.verify_text_on_page(text='ТС-20240714234846', should_exist=True)
    add.verify_text_on_page(text='ТС-20240526054013', should_exist=False)
    time.sleep(2)

    add.move_to_element(add.status_on_flight)
    time.sleep(2)
    add.click_on_the_cross(add.cross_eight)
    time.sleep(2)

    # проверка №3 фильтра "Статус в рейсе"
    add.dropdown_without_input(add.status_on_flight, option_text='На заказе')
    time.sleep(3)
    add.verify_text_on_page(text='ТС20240110120731', should_exist=True)
    add.verify_text_on_page(text='ТС20240116131611', should_exist=False)
    time.sleep(2)

    add.move_to_element(add.status_on_flight)
    time.sleep(2)
    add.click_on_the_cross(add.cross_eight)
    time.sleep(2)

    # проверка №4 фильтра "Статус в рейсе"
    add.dropdown_without_input(add.status_on_flight, option_text='Эксплуатация приостановлена')
    time.sleep(3)
    add.verify_text_on_page(text='ТС-20240526052340', should_exist=True)
    add.verify_text_on_page(text='ТС20240116131611', should_exist=False)
    time.sleep(2)

    add.move_to_element(add.status_on_flight)
    time.sleep(2)
    add.click_on_the_cross(add.cross_eight)
    time.sleep(2)

    # проверка фильтра "фамилия водителя"
    add.input_in_field(add.surname_driver_two, value='фро', click_first=True)
    time.sleep(3)
    add.verify_text_on_page(text='ПРО_СТО', should_exist=True)
    add.verify_text_on_page(text='ТС20240112133709', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.surname_driver_two, value='')
    time.sleep(1)
    add.input_in_field(add.surname_driver_two, value='17185241', click_first=True)
    time.sleep(2)
    add.find_text_on_page(text='ТС20240110120731', occurrences=1)
    time.sleep(1)
    add.backspace_and_input(add.surname_driver_two, value='')
    time.sleep(1)

    # проверка фильтра "имя водителя"
    add.input_in_field(add.name_driver_two, value='09164032', click_first=True)
    time.sleep(1)
    add.verify_text_on_page(text='ТС20231229113421', should_exist=True)
    add.verify_text_on_page(text='ТС20240120144803', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.name_driver_two, value='')
    time.sleep(1)
    add.input_in_field(add.name_driver_two, value='И-20241204160030', click_first=True)
    time.sleep(2)
    add.find_text_on_page(text='110120731', occurrences=1)
    time.sleep(1)
    add.backspace_and_input(add.name_driver_two, value='')
    time.sleep(1)

    # проверка фильтра "отчество водителя"
    add.input_in_field(add.patronymic_driver_two, value='24200338', click_first=True)
    time.sleep(1)
    add.verify_text_on_page(text='ТС-20240526053124', should_exist=True)
    add.verify_text_on_page(text='ТС20240110120731', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.patronymic_driver_two, value='')
    time.sleep(1)
    add.input_in_field(add.patronymic_driver_two, value='Пользователь', click_first=True)
    time.sleep(2)
    add.find_text_on_page(text='515211030', occurrences=1)
    time.sleep(1)
    add.backspace_and_input(add.patronymic_driver_two, value='')
    time.sleep(1)

    # Конец теста


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description("ЛКП Тест фильтра 'Тягачи' в разделе справочники")
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_tractor_directory_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # переход к списку тягачей
    base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tractors_list_button,
                        do_assert=True, wait='lst')

    add = Manual(base.driver)
    # проверка фильтра "Госномер тягача"
    add.input_in_field(add.tractor_number, value='832', click_first=True)
    time.sleep(3)
    add.verify_text_on_page(text='ТЯГ-20240708081832', should_exist=True)
    add.verify_text_on_page(text='ТЯГ-20240517055115', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.tractor_number, value='')
    time.sleep(1)
    add.input_in_field(add.tractor_number, value='ТЯГ-20240531061917', click_first=True)
    time.sleep(2)
    add.find_text_on_page(text='1917', occurrences=3)
    time.sleep(1)
    add.backspace_and_input(add.tractor_number, value='')
    time.sleep(1)

    # проверка №1 фильтра "Статус в системе"
    add.dropdown_without_input(add.status_in_system_two, option_text='Неактивный')
    time.sleep(3)
    add.verify_text_on_page(text='ТЯГ-20240126103308', should_exist=False)
    time.sleep(2)

    # проверка №2 фильтра "Статус в системе"
    add.dropdown_without_input(add.status_in_system_two, option_text='Активный')
    time.sleep(3)
    add.verify_text_on_page(text='ТЯГ-20240320203430', should_exist=True)
    time.sleep(2)

    # проверка №1 фильтра "Статус в рейсе"
    add.dropdown_without_input(add.status_on_flight_two, option_text='Нет заказов')
    time.sleep(2)
    add.verify_text_on_page(text='ТЯГ-20240116131200', should_exist=True)
    add.verify_text_on_page(text='ТЯГ-20241212233234', should_exist=False)
    time.sleep(2)

    # проверка №2 фильтра "Статус в рейсе"
    add.dropdown_without_input(add.status_on_flight_two, option_text='Назначен на заказ')
    time.sleep(2)
    # add.verify_text_on_page(text='ТЯГ-20240910131320', should_exist=True)
    add.verify_text_on_page(text='ТЯГ-20240223190811', should_exist=False)
    time.sleep(2)

    # проверка №3 фильтра "Статус в рейсе"
    add.dropdown_without_input(add.status_on_flight_two, option_text='На заказе')
    time.sleep(2)
    # add.verify_text_on_page(text='ТЯГ-20241212233054', should_exist=True)
    add.verify_text_on_page(text='ТЯГ-20240224125553', should_exist=False)
    time.sleep(2)

    # проверка №4 фильтра "Статус в рейсе"
    add.dropdown_without_input(add.status_on_flight_two, option_text='Эксплуатация приостановлена')
    time.sleep(2)
    add.verify_text_on_page(text='ТЯГ-20240714214407', should_exist=True)
    add.verify_text_on_page(text='ТЯГ-20240710212039', should_exist=False)
    time.sleep(2)

    # проверка №1 фильтра с несколькими значениями
    add.input_in_field(add.tractor_number, value='ТЯГ-20240222223726', click_first=True)
    add.dropdown_without_input(add.status_on_flight_two, option_text='Нет заказов')
    time.sleep(2)
    add.find_text_on_page(text='3726', occurrences=3)
    add.verify_text_on_page(text='ТЯГ-20240220122853', should_exist=False)
    time.sleep(2)

    # очистка поля "Госномер тягача"
    add.backspace_and_input(add.tractor_number, value='')

    # проверка №2 фильтра с несколькими значениями
    add.input_in_field(add.tractor_number, value='ТЯГ-20240316202442', click_first=True)
    add.dropdown_without_input(add.status_on_flight_two, option_text='Эксплуатация приостановлена')
    time.sleep(2)
    add.find_text_on_page(text='2442', occurrences=3)
    add.verify_text_on_page(text='ТЯГ-20240112133258', should_exist=False)
    time.sleep(2)

    # очистка поля "Госномер тягача"
    add.backspace_and_input(add.tractor_number, value='')

    # Конец теста


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description("ЛКП Тест фильтра 'Полуприцепы' в разделе справочники")
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_trailer_directory_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # переход к списку тягачей
    base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.trailers_list_button,
                        do_assert=True, wait='lst')

    add = Manual(base.driver)
    add.move_to_element(add.status_on_flight_three)
    time.sleep(2)
    add.click_on_the_cross(add.cross_four)
    time.sleep(2)

    # проверка фильтра "Госномер полуприцепа"
    add.backspace_and_input(add.trailer_number, value='')
    time.sleep(1)
    add.input_in_field(add.trailer_number, value='3058', click_first=True)
    time.sleep(3)
    add.verify_text_on_page(text='ПП20240220123058', should_exist=True)
    add.verify_text_on_page(text='ПП-20241019130545', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.trailer_number, value='')
    time.sleep(1)
    add.input_in_field(add.trailer_number, value='ПП20240126103514', click_first=True)
    time.sleep(5)
    add.find_text_on_page(text='3514', occurrences=3)
    time.sleep(1)
    add.backspace_and_input(add.trailer_number, value='')
    time.sleep(1)

    # проверка фильтра "Тип автоперевозки"
    add.click_button(add.type_road_transport)
    time.sleep(1)
    add.click_button(add.cargo_transportation)
    time.sleep(5)
    add.click_button(add.click_sort)
    time.sleep(2)
    add.verify_text_on_page(text='ПП20240120144445', should_exist=True)
    add.verify_text_on_page(text='ПП-20240910132625', should_exist=False)
    add.verify_text_on_page(text='ПП-20240515211247', should_exist=False)
    add.verify_text_on_page(text='ПП-20240826225850', should_exist=False)
    time.sleep(2)

    add.click_button(add.type_road_transport)
    time.sleep(1)
    add.click_button(add.special_transportation)
    time.sleep(2)
    add.click_button(add.mainline_trawl)
    time.sleep(2)
    add.verify_text_on_page(text='ПП-20240812230958', should_exist=True)
    add.verify_text_on_page(text='ПП-20240812231116', should_exist=False)
    add.verify_text_on_page(text='ПП20240110120526', should_exist=False)

    add.click_button(add.type_road_transport)
    time.sleep(1)
    add.click_button(add.cistern_car)
    time.sleep(2)
    add.verify_text_on_page(text='Н678ГЛ', should_exist=True)
    add.verify_text_on_page(text='ПП-20240417084756', should_exist=False)
    add.verify_text_on_page(text='ПП20240110120526', should_exist=False)

    add.click_button(add.type_road_transport)
    time.sleep(1)
    add.click_button(add.dump_truck)
    time.sleep(2)
    add.verify_text_on_page(text='ПП-20240417124505', should_exist=True)
    add.verify_text_on_page(text='ПП20240116131406', should_exist=False)
    add.verify_text_on_page(text='ПП-20240417062859', should_exist=False)

    add.click_button(add.type_road_transport)
    time.sleep(1)
    add.click_button(add.car_transporter)
    time.sleep(2)
    add.verify_text_on_page(text='ПП-20240417062859', should_exist=True)
    add.verify_text_on_page(text='ПП-20240417124505', should_exist=False)
    add.verify_text_on_page(text='ПП20240202124010', should_exist=False)

    add.click_button(add.type_road_transport)
    time.sleep(1)
    add.click_button(add.container_truck)
    time.sleep(2)
    add.verify_text_on_page(text='ПП-20240417124736', should_exist=True)
    add.verify_text_on_page(text='ПП-20240417082904', should_exist=False)
    add.verify_text_on_page(text='ПП20240112133503', should_exist=False)

    # перезагрузка страницы
    add.move_to_element(add.type_road_transport)
    time.sleep(2)
    add.click_on_the_cross(add.cross_five)
    time.sleep(2)
    add.reload_page()
    time.sleep(2)

    # проверка №1 фильтра "Статус в системе"
    add.dropdown_without_input(add.status_in_system_three, option_text='Неактивный')
    time.sleep(3)
    add.verify_text_on_page(text='ПП20240321042342', should_exist=False)
    time.sleep(2)

    # проверка №2 фильтра "Статус в системе"
    add.dropdown_without_input(add.status_in_system_three, option_text='Активный')
    time.sleep(3)
    add.verify_text_on_page(text='ПП-20240615163933', should_exist=True)
    time.sleep(2)

    # проверка №1 фильтра "Статус в рейсе"
    add.dropdown_without_input(add.status_on_flight_three, option_text='Нет заказов')
    time.sleep(2)
    add.verify_text_on_page(text='ПП20240202124010', should_exist=True)
    add.verify_text_on_page(text='ПП20240126103514', should_exist=False)
    time.sleep(2)

    # проверка №2 фильтра "Статус в рейсе"
    add.dropdown_without_input(add.status_on_flight_three, option_text='Назначен на заказ')
    time.sleep(2)
    # add.verify_text_on_page(text='ПП-20240828215650', should_exist=True)
    add.verify_text_on_page(text='ПП-20240524194437', should_exist=False)
    time.sleep(2)

    # проверка №3 фильтра "Статус в рейсе"
    add.dropdown_without_input(add.status_on_flight_three, option_text='На заказе')
    time.sleep(2)
    # add.verify_text_on_page(text='ПП-20241210035413', should_exist=True)
    add.verify_text_on_page(text='ПП-20240421211400', should_exist=False)
    time.sleep(2)

    # проверка №4 фильтра "Статус в рейсе"
    add.dropdown_without_input(add.status_on_flight_three, option_text='Эксплуатация приостановлена')
    time.sleep(2)
    add.verify_text_on_page(text='ПП20240126103514', should_exist=True)
    add.verify_text_on_page(text='ПП-20240517102825', should_exist=False)
    time.sleep(2)

    # проверка №1 фильтра с несколькими значениями
    add.input_in_field(add.trailer_number, value='ПП-20240524193241', click_first=True)
    add.dropdown_without_input(add.status_on_flight_three, option_text='Нет заказов')
    time.sleep(2)
    add.find_text_on_page(text='3241', occurrences=3)
    add.verify_text_on_page(text='ПП-20240615162454', should_exist=False)
    time.sleep(2)

    # очистка поля "Госномер полуприцепа"
    add.backspace_and_input(add.trailer_number, value='')

    # проверка №2 фильтра с несколькими значениями
    add.input_in_field(add.trailer_number, value='ПП-20240704075915', click_first=True)
    add.dropdown_without_input(add.status_on_flight_two, option_text='Эксплуатация приостановлена')
    time.sleep(2)
    add.find_text_on_page(text='5915', occurrences=3)
    add.verify_text_on_page(text='ПП-20240709213607', should_exist=False)
    time.sleep(2)

    # очистка поля "Госномер полуприцепа"
    add.backspace_and_input(add.trailer_number, value='')

    # Конец теста


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description("ЛКП Тест фильтра 'Специалисты' в разделе справочники")
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_specialist_directory_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # переход к списку специалистов
    base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.loaders_list_button,
                        do_assert=True, wait='lst')

    add = Manual(base.driver)
    # проверка фильтра "Тип специалиаста" одиночное значение
    add.click_button(add.specialist_type)
    time.sleep(2)
    add.click_button(add.specialist_checkbox_one)
    time.sleep(2)
    add.verify_text_on_page(text='Ф-20250116225450', should_exist=True)
    add.verify_text_on_page(text='Ф-20241212211409', should_exist=False)
    add.reload_page()
    time.sleep(2)
    add.move_to_element(add.specialist_type_field)
    time.sleep(2)
    add.click_on_the_cross(add.specialist_type_cross)
    time.sleep(2)
    add.click_button(add.specialist_type)
    time.sleep(2)
    add.click_button(add.specialist_checkbox_two)
    time.sleep(2)
    add.verify_text_on_page(text='Евтушенко', should_exist=True)
    add.verify_text_on_page(text='Ф-20240624000605', should_exist=False)
    add.reload_page()
    time.sleep(2)
    add.move_to_element(add.specialist_type_field)
    time.sleep(2)
    add.click_on_the_cross(add.specialist_type_cross)
    time.sleep(2)
    add.click_button(add.specialist_type)
    time.sleep(2)
    add.click_button(add.specialist_checkbox_three)
    time.sleep(2)
    add.verify_text_on_page(text='Ф-20241210211039', should_exist=True)
    add.verify_text_on_page(text='Евтушенко', should_exist=False)
    add.reload_page()
    time.sleep(2)
    add.move_to_element(add.specialist_type_field)
    time.sleep(2)
    add.click_on_the_cross(add.specialist_type_cross)
    time.sleep(2)
    add.click_button(add.specialist_type)
    time.sleep(2)
    add.click_button(add.specialist_checkbox_four)
    time.sleep(2)
    add.verify_text_on_page(text='Ф-20240622041124', should_exist=True)
    add.verify_text_on_page(text='Ф-20241210211000', should_exist=False)
    add.reload_page()
    time.sleep(2)
    add.move_to_element(add.specialist_type_field)
    time.sleep(2)
    add.click_on_the_cross(add.specialist_type_cross)
    time.sleep(2)
    add.click_button(add.specialist_type)
    time.sleep(2)
    add.click_button(add.specialist_checkbox_five)
    time.sleep(2)
    add.verify_text_on_page(text='Ф-20250118114413', should_exist=True)
    add.verify_text_on_page(text='Ф-20250123040129', should_exist=False)
    add.reload_page()
    time.sleep(2)
    add.move_to_element(add.specialist_type_field)
    time.sleep(2)
    add.click_on_the_cross(add.specialist_type_cross)
    time.sleep(2)
    add.click_button(add.specialist_type)
    time.sleep(2)
    add.click_button(add.specialist_checkbox_six)
    time.sleep(2)
    add.verify_text_on_page(text='Ф-20240622061305', should_exist=True)
    add.verify_text_on_page(text='Ф-20250116225928', should_exist=False)
    add.reload_page()
    time.sleep(2)
    add.move_to_element(add.specialist_type_field)
    time.sleep(2)
    add.click_on_the_cross(add.specialist_type_cross)
    time.sleep(2)
    add.click_button(add.specialist_type)
    time.sleep(2)
    add.click_button(add.specialist_checkbox_seven)
    time.sleep(2)
    add.verify_text_on_page(text='Антонов', should_exist=True)
    add.verify_text_on_page(text='Ф-20240622061305', should_exist=False)
    add.reload_page()
    time.sleep(2)
    add.move_to_element(add.specialist_type_field)
    time.sleep(2)
    add.click_on_the_cross(add.specialist_type_cross)
    time.sleep(2)
    add.click_button(add.specialist_type)
    time.sleep(2)
    add.click_button(add.specialist_checkbox_eight)
    time.sleep(2)
    add.verify_text_on_page(text='Ф-20241204160029', should_exist=True)
    add.verify_text_on_page(text='Антонов', should_exist=False)
    add.reload_page()
    time.sleep(2)
    add.move_to_element(add.specialist_type_field)
    add.click_on_the_cross(add.specialist_type_cross)

    # проверка фильтра "Тип специалиаста" множественное значение
    add.click_button(add.specialist_type)
    time.sleep(2)
    add.click_button(add.specialist_checkbox_one)
    add.click_button(add.specialist_checkbox_two)
    time.sleep(2)
    add.verify_text_on_page(text='Ф-20250118113952', should_exist=True)
    add.verify_text_on_page(text='Ф-20241211053807', should_exist=False)
    add.reload_page()
    time.sleep(2)
    add.move_to_element(add.specialist_type_field)
    time.sleep(2)
    add.click_on_the_cross(add.specialist_type_cross)
    time.sleep(2)
    add.click_button(add.specialist_type)
    time.sleep(2)
    add.click_button(add.specialist_checkbox_three)
    add.click_button(add.specialist_checkbox_four)
    time.sleep(2)
    add.verify_text_on_page(text='Ф-20241028073830', should_exist=True)
    add.verify_text_on_page(text='Ф-20250118113952', should_exist=False)
    add.reload_page()
    time.sleep(2)
    add.move_to_element(add.specialist_type_field)
    time.sleep(2)
    add.click_on_the_cross(add.specialist_type_cross)
    time.sleep(2)
    add.click_button(add.specialist_type)
    time.sleep(2)
    add.click_button(add.specialist_checkbox_five)
    add.click_button(add.specialist_checkbox_six)
    time.sleep(2)
    add.verify_text_on_page(text='Ф-20250116225847', should_exist=True)
    add.verify_text_on_page(text='Ф-20241204161836', should_exist=False)
    add.reload_page()
    time.sleep(2)
    add.move_to_element(add.specialist_type_field)
    time.sleep(2)
    add.click_on_the_cross(add.specialist_type_cross)
    time.sleep(2)
    add.click_button(add.specialist_type)
    time.sleep(2)
    add.click_button(add.specialist_checkbox_seven)
    add.click_button(add.specialist_checkbox_eight)
    time.sleep(2)
    add.verify_text_on_page(text='Ф-20240617185241', should_exist=True)
    add.verify_text_on_page(text='Ф-20241212210832', should_exist=False)
    add.reload_page()
    time.sleep(2)
    add.move_to_element(add.specialist_type_field)
    time.sleep(2)
    add.click_on_the_cross(add.specialist_type_cross)
    time.sleep(2)

    # проверка фильтра "Фамилия"
    add.input_in_field(add.specialist_surname, value='11039', click_first=True)
    time.sleep(3)
    add.verify_text_on_page(text='Ф-20241210211039', should_exist=True)
    add.verify_text_on_page(text='Ф-20241205183937', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.specialist_surname, value='')
    time.sleep(1)
    add.input_in_field(add.specialist_surname, value='Ф-20241107182635', click_first=True)
    time.sleep(2)
    add.find_text_on_page(text='Ф-20241107182635', occurrences=3)
    add.verify_text_on_page(text='Ф-20241205183937', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.specialist_surname, value='')
    time.sleep(1)

    # проверка фильтра "Имя"
    add.input_in_field(add.specialist_name, value='210832', click_first=True)
    time.sleep(1)
    add.verify_text_on_page(text='И-20241212210832', should_exist=True)
    add.verify_text_on_page(text='И-20241211053807', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.specialist_name, value='')
    time.sleep(1)
    add.input_in_field(add.specialist_name, value='И-20241209165826', click_first=True)
    time.sleep(2)
    add.find_text_on_page(text='И-20241209165826', occurrences=3)
    add.verify_text_on_page(text='И-20241211053807', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.specialist_name, value='')
    time.sleep(1)

    # проверка фильтра "Отчество"
    add.input_in_field(add.specialist_patronymic, value='12804', click_first=True)
    time.sleep(1)
    add.verify_text_on_page(text='О-20241019112804', should_exist=True)
    add.verify_text_on_page(text='О-20240828184523', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.specialist_patronymic, value='')
    time.sleep(1)
    add.input_in_field(add.specialist_patronymic, value='О-20240818203746', click_first=True)
    time.sleep(2)
    add.find_text_on_page(text='3746', occurrences=3)
    time.sleep(1)
    add.backspace_and_input(add.specialist_patronymic, value='')
    time.sleep(1)

    # проверка фильтра "Телефон"
    add.input_in_field(add.telephone_driver, value='0793', click_first=True)
    time.sleep(1)
    add.verify_text_on_page(text='78655240793', should_exist=True)
    add.verify_text_on_page(text='78659504025', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.telephone_driver, value='')
    time.sleep(1)
    add.input_in_field(add.telephone_driver, value='78654403548', click_first=True)
    time.sleep(2)
    add.find_text_on_page(text='3548', occurrences=3)
    time.sleep(1)
    add.backspace_and_input(add.telephone_driver, value='')
    time.sleep(1)

    # проверка №1 фильтра с несколькими значениями
    add.input_in_field(add.specialist_telephone, value='78656141729', click_first=True)
    add.click_button(add.specialist_type)
    time.sleep(2)
    add.click_button(add.specialist_checkbox_one)
    time.sleep(2)
    add.find_text_on_page(text='7183112', occurrences=3)
    add.verify_text_on_page(text='Ф-20241207121221', should_exist=False)
    time.sleep(2)

    add.reload_page()
    time.sleep(2)
    add.move_to_element(add.specialist_type_field)
    time.sleep(2)
    add.click_on_the_cross(add.specialist_type_cross)
    time.sleep(2)

    # проверка №2 фильтра с несколькими значениями
    add.input_in_field(add.specialist_name, value='23040631', click_first=True)
    add.input_in_field(add.specialist_telephone, value='23040632', click_first=True)
    time.sleep(2)
    add.find_text_on_page(text='Ф-20250123040631', occurrences=1)
    add.verify_text_on_page(text='Ф-20250123040739', should_exist=False)
    time.sleep(2)

    # Конец теста
