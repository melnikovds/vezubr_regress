import time
import allure
import pytest
from pages.request_old_ftl_add_page import FTLAdd
from pages.login_page import Login
from pages.filter_old_ftl_page import OldFTL


@allure.story("Smoke test")
@allure.feature('Создание FTL заявок')
@allure.description('ЛКЭ. Тест создания FTL заявки от ГВ: тип - Город, подача - Сейчас, ТС - Груз 0.5т, '
                    'кузов - Закрытый, адреса - Конкретные, публикация - Тариф')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_ftl_request_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к созданию новой FTL заявки
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_city_button,
                           do_assert=True)

    ftl = FTLAdd(base.driver)
    # Сброс ранее введенных и сохраненных данных
    ftl.click_button(ftl.cancel_button)
    
    # Переход к созданию новой FTL заявки
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_city_button,
                           do_assert=True)
    
    # Выбор владельца заявки
    ftl.dropdown_without_input(ftl.request_owner_select, "Auto LKZ")
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
    ftl.dropdown_with_input(ftl.vehicle_type_select, "до 0.5т")
    # Выбор типа кузова - Закрытый
    ftl.click_button(ftl.vehicle_body_select)
    ftl.click_button(ftl.body_type_closed_checkbox)
    # Выбор первого адреса из списка
    ftl.click_button(ftl.first_address_select, wait="lst")
    ftl.input_in_field(ftl.address_filter, "Свердловская обл, г Верхняя Пышма, Успенский пр-кт, д 103а", wait="lst")
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    time.sleep(3)
    # Выбор второго адреса из списка
    ftl.click_button(ftl.second_address_select, wait="lst")
    ftl.input_in_field(ftl.address_filter, "Свердловская обл, г Березовский, ул Театральная, д 13", wait="lst")
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)

    time.sleep(1)
    ftl.click_and_select_with_arrows(ftl.custom_fields, arrow_presses=1)

    # Ожидание завершения расчета стоимости
    base.get_element(ftl.calculate_finish)
    # Публикация заявки с использованием тарифа
    ftl.click_button(ftl.tariff_button)
    ftl.click_button(ftl.producer_select)
    ftl.click_button(ftl.producer_check_box, index=2)
    ftl.click_button(ftl.producer_select_text)
    ftl.click_button(ftl.publish_button)
    ftl.click_button(ftl.continue_button, do_assert=True)
    ftl.click_button(ftl.confirm_add_button, wait="lst")
    # Конец теста
    
    
@allure.story("Smoke test")
@allure.feature('Создание FTL заявок')
@allure.description('ЛКЗ. Тест создания FTL заявки: тип - Город, подача - Сейчас, ТС - Груз 0.5т, '
                    'кузов - Закрытый, адреса - Конкретные, публикация - Тариф')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_ftl_request_add_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к созданию новой FTL заявки
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_city_button,
                           do_assert=True)
    
    ftl = FTLAdd(base.driver)
    # Сброс ранее введенных и сохраненных данных
    ftl.click_button(ftl.cancel_button)
    
    # Переход к созданию новой FTL заявки
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_city_button,
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
    ftl.click_button(ftl.first_address_select, wait="lst")
    ftl.input_in_field(ftl.address_filter, "Свердловская обл, г Верхняя Пышма, Успенский пр-кт, д 103а", wait="lst")
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    time.sleep(3)
    # Выбор второго адреса из списка
    ftl.click_button(ftl.second_address_select, wait="lst")
    ftl.input_in_field(ftl.address_filter, "Свердловская обл, г Березовский, ул Театральная, д 13", wait="lst")
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)

    time.sleep(1)
    ftl.click_and_select_with_arrows(ftl.custom_fields, arrow_presses=1)

    # Ожидание завершения расчета стоимости
    base.get_element(ftl.calculate_finish)
    # Публикация заявки с использованием тарифа
    ftl.click_button(ftl.tariff_button)
    ftl.click_button(ftl.producer_select)
    ftl.click_button(ftl.select_all_producer)
    time.sleep(0.5)
    ftl.click_button(ftl.producer_select_text)
    ftl.click_button(ftl.publish_button)
    ftl.click_button(ftl.continue_button, do_assert=True)
    ftl.click_button(ftl.confirm_add_button, wait="lst")
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание и Исполнение FTL заявок')
@allure.description('ЛКЗ. Тест FTL Рейс: тип - Город, подача - Сейчас, ТС - Груз 1.5т, '
                    'кузов - Закрытый, адреса - Конкретные, публикация - Ставка')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_ftl_order_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход в раздел Новая FTL заявка
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_city_button,
                           do_assert=True)

    ftl = FTLAdd(base.driver)
    # Сброс ранее введенных и сохраненных данных
    ftl.click_button(ftl.cancel_button)

    # Создание новой FTL заявки
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_city_button,
                           do_assert=True)

    # Установка даты подачи заявки на сегодня
    ftl.click_button(ftl.start_date_field)
    ftl.click_button(ftl.today_button)
    # Установка времени подачи заявки через час от текущего времени
    ftl.click_button(ftl.start_time_field)
    new_time = ftl.naw_time_change(60)
    ftl.input_in_field(ftl.start_time_input, new_time)
    time.sleep(2)
    # # Выбор категории заявки - Груз
    ftl.click_button(ftl.request_category_select)
    ftl.click_button(ftl.select_freight)
    # Выбор типа ТС - 1.5т
    ftl.click_button(ftl.vehicle_type_select)
    ftl.dropdown_with_input(ftl.vehicle_type_select, "1.5т / 9м3 / 4пал.")
    # Выбор типа кузова - Закрытый
    ftl.click_button(ftl.vehicle_body_select)
    ftl.click_button(ftl.body_type_closed_checkbox)
    time.sleep(1)
    # Выбор первого адреса из списка
    ftl.click_button(ftl.first_address_select, wait="lst")
    ftl.input_in_field(ftl.address_filter, "г Санкт-Петербург, ул Брянцева, д 15 к 2", wait="lst")
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    time.sleep(1)
    # Выбор второго адреса из списка
    ftl.click_button(ftl.second_address_select, wait="lst")
    ftl.input_in_field(ftl.address_filter, "г Санкт-Петербург, ул Маршала Захарова, д 17 к 1", wait="lst")
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    # Добавление грузоместа
    ftl.click_button(ftl.attach_cargoplaces)
    time.sleep(1)
    ftl.click_button(ftl.new_cargoplace)
    time.sleep(1)
    ftl.input_in_field(ftl.number_of_pieces, value='111')
    ftl.click_and_select_with_arrows(ftl.type_of_packaging, arrow_presses=1)
    ftl.input_in_field(ftl.weight, value='111')
    ftl.input_in_field(ftl.volume, value='3')
    ftl.input_in_field(ftl.name_of_cargo, value='бетономешалки')
    ftl.input_in_field(ftl.cost, value='333000')
    ftl.click_and_select_with_arrows(ftl.loading, arrow_presses=0)
    ftl.click_and_select_with_arrows(ftl.unloading, arrow_presses=0)
    time.sleep(1)
    ftl.click_button(ftl.attach)

    # Добавление дополнительных данных
    ftl.click_button(ftl.additional_requirements)
    ide_code = FTLAdd.generate_ide_code()  # вызов метода
    ftl.input_in_field(ftl.order_identifier, value=ide_code)
    time.sleep(1)
    ftl.scroll_to_element(ftl.order_insurance)
    time.sleep(1)
    ftl.click_and_select_with_arrows(ftl.custom_fields, arrow_presses=1)
    ftl.click_button(ftl.order_insurance)
    ftl.dropdown_with_input(ftl.cargo_category, option_text='Оборудование и запчасти')
    ftl.assert_element_text(ftl.estimated_value, reference_value='333 000')

    ftl.click_button(ftl.responsible_employee)
    ftl.click_and_select_with_arrows(ftl.select_employee, arrow_presses=1)
    time.sleep(1)

    # Публикация рейса
    ftl.scroll_to_element(ftl.publish_order)
    time.sleep(1)
    ftl.click_button(ftl.publish_order)
    time.sleep(3)
    ftl.click_button(ftl.radio_button_rate, wait_type='clickable')
    ftl.input_in_field(ftl.rate_for_publication, value='5999')
    ftl.click_button(ftl.selection_of_contractors)
    ftl.click_button(ftl.contractor_checkbox)
    time.sleep(3)
    ftl.click_button(ftl.radio_button_rate, wait_type='visible')
    ftl.click_button(ftl.publish, wait='form')

    # Выход из ЛКЗ
    ftl.click_button(ftl.ok)
    time.sleep(1)
    sidebar.click_button(sidebar.exit_button)
    time.sleep(3)

    # Вход за ЛКП
    login = Login(base.driver, domain)
    login.authorization("lkp")
    time.sleep(10)

    sidebar.click_button(sidebar.sidebar_button)

    # Переход в раздел Активные FTL-заявки
    base.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_active_list_button,
                        do_assert=True, wait='lst')

    add = OldFTL(base.driver)
    # Сброс фильтров
    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    add.input_in_field(add.request_identifier, value=ide_code, click_first=True)
    time.sleep(2)
    # Принятие заявки
    ftl.click_button(ftl.click_on_request)
    time.sleep(2)
    ftl.click_button(ftl.accept_obligations)
    time.sleep(2)
    ftl.click_button(ftl.order_accept)
    time.sleep(2)
    # Назначение водителя
    ftl.input_in_field(ftl.search_driver, value='Фронтов')
    time.sleep(1)
    ftl.click_button(ftl.attach_driver, wait='form')
    ftl.click_button(ftl.order_accepted)
    time.sleep(5)

    ftl.reload_page()

    # Начало исполнения рейса
    ftl.click_button(ftl.burger_menu)
    ftl.click_button(ftl.start_execution)
    time.sleep(3)
    # ftl.click_button(ftl.tab_execution)

    time_one, time_two, time_three, time_four = FTLAdd.get_time_intervals()

    # Простановка времени работы на 1 точке
    ftl.input_in_field(ftl.point_loading_start, value=time_one)
    time.sleep(1)
    ftl.input_in_field(ftl.point_loading_finish, value=time_two)
    time.sleep(1)

    ftl.click_button(ftl.save_changes)
    time.sleep(1)
    ftl.click_button(ftl.approve_changes, wait='form')
    time.sleep(1)
    ftl.click_button(ftl.ok_time)
    time.sleep(3)

    # Простановка времени работы на 2 точке
    ftl.input_in_field(ftl.point_unloading_start, value=time_three)
    time.sleep(1)
    ftl.input_in_field(ftl.point_unloading_finish, value=time_four)
    time.sleep(1)

    ftl.click_button(ftl.complete_order, wait='list')
    time.sleep(1)
    ftl.click_button(ftl.approve_and_complete_order, wait='form')
    time.sleep(1)













































