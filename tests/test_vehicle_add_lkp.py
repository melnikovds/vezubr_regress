import time
import allure
import pytest
from pages.transport_add_page import TransportAdd
from pages.transports_list_page import TransportsList


@allure.story("Smoke test")
@allure.feature('Создание и операции с транспортными средствами')
@allure.description('ЛКП. Тест создания ТС ПВ: номер - ТС-timestamp, модель - Монорамник, выпуск - 2023г, собственник '
                    '- Подрядчик, тип - Грузовой, кузов - Тент, грузоподемность/объем/палеты/высота - Рандом, '
                    'добавить/убрать - 2 и 1 водителя, эксплуатация - останавливаем/восстанавливаем/завершаем')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_transport1_add_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку транспортных средств
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")

    transports_list = TransportsList(base.driver)
    # Клик по кнопке добавления транспортного средства
    transports_list.click_button(transports_list.add_transport_button)

    add_ts = TransportAdd(base.driver)
    # Выбор типа транспортного средства
    add_ts.dropdown_without_input(add_ts.vehicle_type_select, "Монорамное ТС")
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ТС-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Монорамник")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_without_input(add_ts.year_select, "2022")
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Грузовая")
    add_ts.dropdown_without_input(add_ts.vehicle_body_types_select, "Тентованный")
    add_ts.input_in_field(add_ts.capacity_input, base.random_value_float_str(0.5, 30.0))
    add_ts.input_in_field(add_ts.volume_input, base.random_value_float_str(0.5, 120.0))
    add_ts.input_in_field(add_ts.pallets_input, base.random_value_float_str(0, 35))
    add_ts.input_in_field(add_ts.height_from_ground_input, base.random_value_float_str(1.0, 4.0))
    vin=add_ts.generate_vin()
    add_ts.input_in_field(add_ts.vin_number, value=str(vin))
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_transport_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Прикрепление водителей
    add_ts.click_button(add_ts.attach_button)
    time.sleep(4)
    add_ts.click_button(add_ts.select_button)
    add_ts.click_button(add_ts.select_button)
    add_ts.click_button(add_ts.assign_selected_button, wait="form")
    time.sleep(3)
    add_ts.click_button(add_ts.attach_button)
    time.sleep(2)
    add_ts.click_button(add_ts.unselect_button)
    add_ts.click_button(add_ts.assign_selected_button, wait="form")
    # Операции с транспортным средством
    time.sleep(1)
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.suspend_button, wait="form")
    add_ts.refresh_page()
    time.sleep(3)
    add_ts.verify_text_on_page(text='Эксплуатация приостановлена')
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.resume_button, wait="form")
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.exploitation_finish_button)
    add_ts.click_button(add_ts.yes_button, do_assert=True)
    add_ts.click_button(add_ts.ok_button)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание и операции с транспортными средствами')
@allure.description('ЛКП. Тест создания ТС ПВ: номер - ТС-timestamp, модель - Монорамник, выпуск - 1996г, собственник '
                    '- Подрядчик, тип - Грузовой, кузов - Изотермический, грузоподемность/объем/палеты/высота - Рандом ')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_transport2_add_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку транспортных средств
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")

    transports_list = TransportsList(base.driver)
    # Клик по кнопке добавления транспортного средства
    transports_list.click_button(transports_list.add_transport_button)

    add_ts = TransportAdd(base.driver)
    # Выбор типа транспортного средства
    add_ts.dropdown_without_input(add_ts.vehicle_type_select, "Монорамное ТС")
    # Заполнение данных о транспортном средстве
    plate=base.get_timestamp()
    add_ts.input_in_field(add_ts.plate_number_input, f"ТС-{plate}")
    add_ts.input_in_field(add_ts.mark_model_input, "Газель")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_without_input(add_ts.year_select, "1996")
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Грузовая")
    add_ts.dropdown_without_input(add_ts.vehicle_body_types_select, "Изотермический")
    add_ts.input_in_field(add_ts.capacity_input, base.random_value_float_str(0.5, 30.0))
    add_ts.input_in_field(add_ts.volume_input, base.random_value_float_str(0.5, 120.0))
    add_ts.input_in_field(add_ts.pallets_input, base.random_value_float_str(0, 35))
    add_ts.input_in_field(add_ts.height_from_ground_input, base.random_value_float_str(1.0, 4.0))
    vin=add_ts.generate_vin()
    add_ts.input_in_field(add_ts.vin_number, value=str(vin))
    time.sleep(5)
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_transport_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    add_ts.verify_text_on_page(text=vin)
    add_ts.verify_text_on_page(text=plate)
    add_ts.verify_text_on_page(text='1996')
    add_ts.verify_text_on_page(text='Газель')
    add_ts.verify_text_on_page(text='Грузовая')
    # Прикрепление водителей
    add_ts.click_button(add_ts.attach_button)
    time.sleep(4)
    add_ts.click_button(add_ts.select_button)
    add_ts.click_button(add_ts.select_button)
    add_ts.click_button(add_ts.assign_selected_button, wait="form")
    time.sleep(3)
    add_ts.click_button(add_ts.attach_button)
    time.sleep(2)
    add_ts.click_button(add_ts.unselect_button)
    add_ts.click_button(add_ts.assign_selected_button, wait="form")
    # Операции с транспортным средством
    time.sleep(1)
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.suspend_button, wait="form")
    add_ts.refresh_page()
    time.sleep(3)
    add_ts.verify_text_on_page(text='Эксплуатация приостановлена')
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.resume_button, wait="form")
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.exploitation_finish_button)
    add_ts.click_button(add_ts.yes_button, do_assert=True)
    add_ts.click_button(add_ts.ok_button)
    # Конец теста


@allure.story("Critical path test")
@allure.feature('Создание и операции с транспортными средствами')
@allure.description('ЛКП. Тест создания ПП ПВ: номер - ПП-timestamp, модель - Полуприцеп, выпуск - 2012г, собственник '
                    '- Подрядчик, тип - Грузовой, кузов - Тент, грузоподемность/объем/палеты/высота - Рандом, '
                    'добавить/заменить - Тягач, эксплуатация - останавливаем/восстанавливаем')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_trailer1_add_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку транспортных средств
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")

    transports_list = TransportsList(base.driver)
    # Клик по кнопке добавления транспортного средства
    transports_list.click_button(transports_list.add_transport_button)

    add_ts = TransportAdd(base.driver)
    # Выбор типа транспортного средства
    add_ts.dropdown_without_input(add_ts.vehicle_type_select, "Полуприцеп")
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ПП-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Полуприцеп")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_without_input(add_ts.year_select, "2012")
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Грузовая")
    add_ts.dropdown_without_input(add_ts.vehicle_body_types_select, "Тентованный")
    add_ts.input_in_field(add_ts.capacity_input, base.random_value_float_str(0.5, 100.0))
    add_ts.input_in_field(add_ts.volume_input, base.random_value_float_str(0.5, 120.0))
    add_ts.input_in_field(add_ts.pallets_input, base.random_value_float_str(0, 35))
    add_ts.input_in_field(add_ts.height_from_ground_input, base.random_value_float_str(1.0, 4.0))
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_trailer_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Прикрепление тягача
    add_ts.click_button(add_ts.attach_button, wait="form")
    time.sleep(4)
    add_ts.click_button(add_ts.select_button, wait="form")
    time.sleep(3)
    add_ts.click_button(add_ts.attach_button, wait="form")
    time.sleep(2)
    add_ts.click_button(add_ts.select_button, wait="form")
    # Операции с транспортным средством
    time.sleep(1)
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.suspend_button, wait="form")
    add_ts.refresh_page()
    time.sleep(3)
    add_ts.verify_text_on_page(text='временно приостановлена')
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.resume_button, wait="form")
    add_ts.refresh_page()
    time.sleep(3)
    add_ts.verify_text_on_page(text='временно приостановлена', should_exist=False)
    # Конец теста


@allure.story("Critical path test")
@allure.feature('Создание и операции с транспортными средствами')
@allure.description('ЛКП. Тест создания ПП ПВ: номер - ПП-timestamp, модель - Полуприцеп, выпуск - 1993г, собственник '
                    '- Аренда, тип - Грузовой, кузов - Фургон, грузоподемность/объем/палеты/высота - Рандом, '
                    'добавить/заменить - Тягач, эксплуатация - останавливаем/восстанавливаем')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_trailer2_add_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку транспортных средств
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")

    transports_list = TransportsList(base.driver)
    # Клик по кнопке добавления транспортного средства
    transports_list.click_button(transports_list.add_transport_button)

    add_ts = TransportAdd(base.driver)
    # Выбор типа транспортного средства
    add_ts.dropdown_without_input(add_ts.vehicle_type_select, "Полуприцеп")
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ПП-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Полуприцеп")
    add_ts.dropdown_without_input(add_ts.year_select, "1993")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Аренда")

    time.sleep(1)
    add_ts.backspace_and_input(add_ts.owner_document_name, value='договор аренды')
    add_ts.backspace_and_input(add_ts.owner_document_number, value='п-111')
    add_ts.backspace_and_input(add_ts.owner_document_inn, value='772070478775')
    add_ts.click_button(add_ts.owner_document_date)
    time.sleep(1)
    add_ts.click_button(add_ts.owner_document_date_today)
    add_ts.backspace_and_input(add_ts.owner_document_organization, value='ИП Володин')

    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Грузовая")
    add_ts.dropdown_without_input(add_ts.vehicle_body_types_select, "Фургон (будка)")
    add_ts.input_in_field(add_ts.capacity_input, base.random_value_float_str(0.5, 100.0))
    add_ts.input_in_field(add_ts.volume_input, base.random_value_float_str(0.5, 120.0))
    add_ts.input_in_field(add_ts.pallets_input, base.random_value_float_str(0, 35))
    add_ts.input_in_field(add_ts.height_from_ground_input, base.random_value_float_str(1.0, 4.0))
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_trailer_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Прикрепление тягача
    add_ts.click_button(add_ts.attach_button, wait="form")
    time.sleep(4)
    add_ts.click_button(add_ts.select_button, wait="form")
    time.sleep(3)
    add_ts.click_button(add_ts.attach_button, wait="form")
    time.sleep(2)
    add_ts.click_button(add_ts.select_button, wait="form")
    # Операции с транспортным средством
    time.sleep(1)
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.suspend_button, wait="form")
    add_ts.refresh_page()
    time.sleep(3)
    add_ts.verify_text_on_page(text='временно приостановлена')
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.resume_button, wait="form")
    add_ts.refresh_page()
    time.sleep(3)
    add_ts.verify_text_on_page(text='временно приостановлена', should_exist=False)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание транспортных средств')
@allure.description('ЛКП. Тест создания Тягача: номер - ТЯГ-timestamp, модель - Тягач, выпуск - 2023г, собственник'
                    ' - Подрядчик, добавить/убрать - 2 и 1 водителя, эксплуатация - останавливаем/восстанавливаем')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_tractor1_add_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку транспортных средств
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")

    transports_list = TransportsList(base.driver)
    # Клик по кнопке добавления транспортного средства
    transports_list.click_button(transports_list.add_transport_button)

    add_ts = TransportAdd(base.driver)
    # Выбор типа транспортного средства
    add_ts.dropdown_without_input(add_ts.vehicle_type_select, "Тягач")
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ТЯГ-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Тягач")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_without_input(add_ts.year_select, "2023")
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_tractor_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Прикрепление водителей
    add_ts.click_button(add_ts.attach_button)
    time.sleep(4)
    add_ts.click_button(add_ts.select_button)
    add_ts.click_button(add_ts.select_button)
    add_ts.click_button(add_ts.assign_selected_button, wait="form")
    time.sleep(3)
    add_ts.click_button(add_ts.attach_button)
    time.sleep(2)
    add_ts.click_button(add_ts.unselect_button)
    add_ts.click_button(add_ts.assign_selected_button, wait="form")
    # Операции с транспортным средством
    time.sleep(1)
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.suspend_button, wait="form")
    add_ts.refresh_page()
    time.sleep(3)
    add_ts.verify_text_on_page(text='временно приостановлена')
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.resume_button, wait="form")
    add_ts.refresh_page()
    time.sleep(3)
    add_ts.verify_text_on_page(text='временно приостановлена', should_exist=False)
    # Конец теста


@allure.story("Critical path test")
@allure.feature('Создание транспортных средств')
@allure.description('ЛКП. Тест создания Тягача ПВ": номер - ТЯГ-timestamp, модель - Тягач, выпуск - 2023г, собственник'
                    ' - Подрядчик, добавить/заменить - ПП, эксплуатация - останавливаем/восстанавливаем')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_tractor2_add_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку транспортных средств
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")

    transports_list = TransportsList(base.driver)
    # Клик по кнопке добавления транспортного средства
    transports_list.click_button(transports_list.add_transport_button)

    add_ts = TransportAdd(base.driver)
    # Выбор типа транспортного средства
    add_ts.dropdown_without_input(add_ts.vehicle_type_select, "Тягач")
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ТЯГ-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Тягач")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_without_input(add_ts.year_select, "2023")
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_tractor_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Прикрепление полуприцепа
    add_ts.click_button(add_ts.attach_button, index=2, wait="form")
    time.sleep(4)
    add_ts.click_button(add_ts.select_button, wait="form")
    time.sleep(3)
    add_ts.click_button(add_ts.attach_button, index=2, wait="form")
    time.sleep(2)
    add_ts.click_button(add_ts.select_button, wait="form")
    # Операции с транспортным средством
    time.sleep(1)
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.suspend_button)
    time.sleep(1)
    add_ts.refresh_page()
    time.sleep(3)
    add_ts.verify_text_on_page(text='временно приостановлена')
    add_ts.click_button(add_ts.action_menu_button)
    add_ts.click_button(add_ts.resume_button)
    time.sleep(1)
    add_ts.refresh_page()
    time.sleep(4)
    add_ts.verify_text_on_page(text='временно приостановлена', should_exist=False)
    # Конец теста
