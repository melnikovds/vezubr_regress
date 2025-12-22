import time
import allure
import pytest
from pages.filter_directory_page import Manual, Filter


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
        add.dropdown_without_input(add.creation_date, option_text='За все время')
        time.sleep(3)

    with allure.step('проверка фильтра "подтвержденный адрес"'):
        add.input_in_field(add.confirm_address, "Музыкальный")
        time.sleep(2)
        add.verify_text_on_page(text='г Орск, Музыкальный пер, д 14')
        add.backspace_and_input(add.confirm_address, value='')

    with allure.step('проверка фильтра "название адреса"'):
        add.input_in_field(add.name_address, "Autotests")
        time.sleep(2)
        add.verify_text_on_page(text='Ижевск, ул Телегина')
        add.backspace_and_input(add.name_address, value='')

    with allure.step('проверка фильтра "отправитель/получатель"'):
        add.input_in_field(add.sender_recipient, "ООО ЭЛЕТЕК")
        time.sleep(2)
        add.verify_text_on_page(text='Ижевск, ул Крылова')
        add.backspace_and_input(add.sender_recipient, value='')

    with allure.step('проверка фильтра "Статус"'):
        add.click_button(add.status)
        time.sleep(2)
        add.click_button(add.inactive_status)
        time.sleep(2)
        add.verify_text_on_page(text='Ясный, ул Ленина, д 26')
        time.sleep(2)
        add.click_button(element_dict=add.refresh)
        add.dropdown_without_input(add.creation_date, option_text='За все время')
        time.sleep(3)
        add.click_button(add.status)
        time.sleep(2)
        add.click_button(add.active_status)
        time.sleep(2)
        add.verify_text_on_page(text='лплроа')

    with allure.step("сброс фильтров"):
        add.click_button(element_dict=add.refresh)
        add.dropdown_without_input(add.creation_date, option_text='За все время')
        time.sleep(3)

    with allure.step('проверка фильтра "регион"'):
        add.dropdown_without_input(add.region, option_text='Тверская область')
        time.sleep(1)
        add.verify_text_on_page('Вышний Волочек')

    with allure.step("сброс фильтров"):
        add.click_button(element_dict=add.refresh)
        add.dropdown_without_input(add.creation_date, option_text='За все время')
        time.sleep(3)

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
        add.input_in_field(add.partner_id, "тиммейт")
        time.sleep(2)
        add.verify_text_on_page(text='Воскресенск')
        add.backspace_and_input(add.partner_id, value='')

    with allure.step('проверка фильтра "Владелец Адреса"'):
        add.input_in_field(add.address_owner, "Auto LKE")
        add.input_in_field(add.confirm_address, "теле")
        time.sleep(2)
        add.verify_text_on_page(text='Ижевск, ул Телегина')
        add.backspace_and_input(add.address_owner, value='')
        add.backspace_and_input(add.confirm_address, value='')

    with allure.step("сброс фильтров"):
        add.click_button(element_dict=add.refresh)
        add.dropdown_without_input(add.creation_date, option_text='За все время')


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description("ЛКЗ Тест фильтра 'Тарифы' в разделе справочники")
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_tariff_directory_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    with allure.step("Переход к списку тарифов"):
        base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                            do_assert=True, wait='lst')

    add = Filter(base.driver)
    with allure.step('проверка фильтра "Название тарифа"'):
        add.input_in_field(add.tariff_name, "Telemost")
        time.sleep(1)
        add.verify_text_on_page(text='Auto Telemost')
        add.backspace_and_input(add.tariff_name, value='')

    with allure.step('проверка фильтра "Статус"'):
        add.dropdown_without_input(add.tariff_status, option_text='Не активный')
        add.input_in_field(add.tariff_name, "фикс")
        time.sleep(2)
        add.verify_text_on_page(text='Autotests FTL фиксированный', should_exist=True)
        add.verify_text_on_page(text='Auto Telemost', should_exist=False)
        time.sleep(2)
        add.backspace_and_input(add.tariff_name, value='')

    with allure.step('Проверка нескольких фильтров №1'):
        add.input_in_field(add.tariff_name, "26182211")
        add.dropdown_without_input(add.tariff_status, option_text='Активный')
        time.sleep(2)
        add.verify_text_on_page(text='ПРР-20250826182211', should_exist=True)
        add.verify_text_on_page(text='Telemost', should_exist=False)
        add.backspace_and_input(add.tariff_name, value='')

    with allure.step('Проверка нескольких фильтров №2'):
        add.input_in_field(add.tariff_name, "20074639")
        add.dropdown_without_input(add.tariff_status, option_text='Не активный')
        time.sleep(2)
        add.verify_text_on_page(text='ГГ-20250820074639', should_exist=True)
        add.verify_text_on_page(text='ПРР-20250826182211', should_exist=False)
        add.backspace_and_input(add.tariff_name, value='')


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description("ЛКЭ Тест фильтра 'водители' в разделе справочники")
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_drivers_directory_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    time.sleep(2)

    with allure.step("Переход к списку водителей"):
        base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                            do_assert=True, wait='lst')
        add = Filter(base.driver)

        add.move_to_element(add.driver_status)
        add.click_on_the_cross(add.cross_status_in_the_system)

        add.move_to_element(add.flight_status)
        add.click_on_the_cross(add.cross_status_in_flight)

    with allure.step('проверка фильтра "Фамилия"'):
        add.input_in_field(add.surname_driver, "Ролов")
        time.sleep(1)
        add.verify_text_on_page(text='Ролыч')
        add.backspace_and_input(add.surname_driver, value='')

    with allure.step('проверка фильтра "Имя"'):
        add.input_in_field(add.name_driver, "и2023")
        time.sleep(1)
        add.verify_text_on_page(text='о2023')
        add.backspace_and_input(add.name_driver, value='')

    with allure.step('проверка фильтра "Отчество"'):
        add.input_in_field(add.patronymic_driver, "Emecron", wait='lst')
        time.sleep(3)
        add.verify_text_on_page(text='Avtobot')
        add.backspace_and_input(add.patronymic_driver, value='')

    with allure.step('проверка фильтра "Телефон"'):
        add.input_in_field(add.phone_driver, "79652633268")
        time.sleep(1)
        add.verify_text_on_page(text='И-20240427105243')
        add.backspace_and_input(add.phone_driver, value='')

    with allure.step('проверка фильтра "Подрядчик"'):
        # включение доп.фильтра
        add.click_button(add.add_filter)
        time.sleep(1)
        add.click_button(add.default_filter_lke)
        time.sleep(1)
        add.click_button(add.add_filter_contractor)
        time.sleep(1)
        add.click_button(add.apply_add_filter)
        time.sleep(1)

        # проверка фильтра
        add.input_in_field(add.contractor, "Auto LKE")
        add.input_in_field(add.surname_driver, "данов")
        time.sleep(1)
        add.verify_text_on_page(text='Даныч')
        add.backspace_and_input(add.contractor, value='')
        add.backspace_and_input(add.surname_driver, value='')

    with allure.step('проверка фильтра "Статус в рейсе"'):
        add.dropdown_without_input(add.flight_status, "Назначен на заказ")
        time.sleep(1)
        add.verify_text_on_page(text='И-20250311090229')
        add.dropdown_without_input(add.flight_status, "На заказе")
        add.verify_text_on_page(text='Булков')
        add.dropdown_without_input(add.flight_status, "Работа приостановлена")
        add.verify_text_on_page(text='79650084909')

        add.move_to_element(add.flight_status)
        add.click_on_the_cross(add.cross_status_in_flight)

    with allure.step('проверка фильтра "Статус в системе"'):
        add.dropdown_without_input(add.driver_status, "Неактивный")
        add.input_in_field(add.surname_driver, "40427110905")
        time.sleep(1)
        add.verify_text_on_page(text='ВФ-20240427110905')
        add.verify_text_on_page(text='71234567890', should_exist=False)
        time.sleep(1)
        add.backspace_and_input(add.surname_driver, value='')
        add.dropdown_without_input(add.driver_status, "Активный")
        add.input_in_field(add.surname_driver, "531043106")
        time.sleep(1)
        add.verify_text_on_page(text='ВФ-20240531043106')
        add.verify_text_on_page(text='71234567890', should_exist=False)
        time.sleep(1)
        add.backspace_and_input(add.surname_driver, value='')

        add.move_to_element(add.driver_status)
        add.click_on_the_cross(add.cross_status_in_the_system)

        add.move_to_element(add.flight_status)
        add.click_on_the_cross(add.cross_status_in_flight)


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

        add.move_to_element(add.tractor_status)
        add.click_on_the_cross(add.cross_status_in_the_system_tractor)

        add.move_to_element(add.flight_status_tractor)
        add.click_on_the_cross(add.cross_status_in_flight_tractor)

    with allure.step('проверка фильтра "Госномер тягача"'):
        add.input_in_field(add.number_of_tractor, "WAHATRACK")
        time.sleep(1)
        add.verify_text_on_page(text='KAMAZ')
        add.backspace_and_input(add.number_of_tractor, '')
        time.sleep(1)

    with allure.step('проверка фильтра "Подрядчик"'):
        add.move_to_element(add.tractor_status)
        add.click_on_the_cross(add.cross_status_in_the_system_tractor)
        add.input_in_field(add.contractor_tractor, "Auto LKE")
        time.sleep(2)
        add.verify_text_on_page(text='KAMAZ', should_exist=True)
        add.backspace_and_input(add.contractor_tractor, '')
        time.sleep(1)

    with allure.step('проверка фильтра "Статус в рейсе"'):
        add.dropdown_without_input(add.flight_status_tractor, "Эксплуатация приостановлена")
        time.sleep(1)
        add.verify_text_on_page(text='Е406НУ')
        add.dropdown_without_input(add.flight_status_tractor, "Нет заказов")
        time.sleep(1)
        add.input_in_field(add.number_of_tractor, "5938")
        time.sleep(1)
        add.verify_text_on_page(text='ВТЯГ-20240421205938')
        time.sleep(1)
        add.backspace_and_input(add.number_of_tractor, '')
        add.move_to_element(add.flight_status_tractor)
        add.click_on_the_cross(add.cross_status_in_flight_tractor)

    with allure.step('проверка фильтра "Статус в системе"'):
        add.dropdown_without_input(add.tractor_status, "Активный")
        add.input_in_field(add.number_of_tractor, "26185053")
        time.sleep(1)
        add.verify_text_on_page(text='ТЯГ-20250826185053')
        add.backspace_and_input(add.number_of_tractor, '')

        add.move_to_element(add.tractor_status)
        add.click_on_the_cross(add.cross_status_in_the_system_tractor)

        add.move_to_element(add.flight_status_tractor)
        add.click_on_the_cross(add.cross_status_in_flight_tractor)


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description("ЛКП Тест фильтра 'Полуприцепы' в разделе справочники")
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_trailer_directory_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    with allure.step('переход к списку тягачей'):
        base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.trailers_list_button,
                            do_assert=True, wait='lst')
        add = Filter(base.driver)

        add.move_to_element(add.trailer_status)
        add.click_on_the_cross(add.cross_status_in_the_system_trailer)

        add.move_to_element(add.flight_status_trailer)
        add.click_on_the_cross(add.cross_status_in_flight_trailer)

        add.move_to_element(add.type_of_road_trailer)
        add.click_on_the_cross(add.cross_type_of_road_trailer)

        add.backspace_and_input(add.contractor_trailer, '')
        add.backspace_and_input(add.number_of_trailer, '')

    with allure.step('проверка фильтра "Госномер Полуприцепа"'):
        add.input_in_field(add.number_of_trailer, "WAHATRACK")
        time.sleep(1)
        add.verify_text_on_page(text='WAHATRACKПРИЦЕП')
        add.backspace_and_input(add.number_of_trailer, '')

    with allure.step('проверка фильтра "Тип автоперевозки"'):
        # add.dropdown_without_input(add.type_of_road_trailer, "Грузовая")
        add.click_button(add.type_of_road_trailer)
        time.sleep(1)
        add.click_button(add.trailer_cargo_transportation)
        time.sleep(1)
        add.verify_text_on_page(text='АВТО111')

        add.move_to_element(add.type_of_road_trailer)
        add.click_on_the_cross(add.cross_type_of_road_trailer)

    with allure.step('проверка фильтра "Статус в рейсе"'):
        add.dropdown_without_input(add.flight_status_trailer, "Эксплуатация приостановлена")
        time.sleep(1)
        add.verify_text_on_page(text='ПП20240126103514')
        add.dropdown_without_input(add.flight_status_trailer, "Нет заказов")
        add.input_in_field(add.number_of_trailer, "111201")
        time.sleep(1)
        add.verify_text_on_page(text='20240508111201')
        time.sleep(1)
        add.backspace_and_input(add.number_of_trailer, '')
        time.sleep(1)
        add.dropdown_without_input(add.flight_status_trailer, "Назначен на заказ")
        add.verify_text_on_page(text='ПП-20250309203400')

        add.move_to_element(add.trailer_status)
        add.click_on_the_cross(add.cross_status_in_the_system_trailer)

        add.move_to_element(add.flight_status_trailer)
        add.click_on_the_cross(add.cross_status_in_flight_trailer)

        add.move_to_element(add.type_of_road_trailer)
        add.click_on_the_cross(add.cross_type_of_road_trailer)

    with allure.step('проверка фильтра "Подрядчик"'):
        add.input_in_field(add.contractor_trailer, value="яндекс")
        add.input_in_field(add.number_of_trailer, value="5143630")
        time.sleep(1)
        add.verify_text_on_page(text='ВПП-20250705143630')
        add.backspace_and_input(add.contractor_trailer, '')
        add.backspace_and_input(add.number_of_trailer, '')


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
    with allure.step('проверка фильтра "Госномер ТС"'):
        add.del_all_filter_vehicle()
        add.input_in_field(add.number_vehicles, "WH40")
        time.sleep(2)
        add.verify_text_on_page(text='WH400000')
        add.backspace_and_input(add.number_vehicles, "")

    with allure.step('проверка фильтра "Имя водителя"'):
        # включение доп. фильтров
        add.click_button(add.add_filter_vehicle)
        time.sleep(1)
        add.click_button(add.default_filter_vehicle)
        time.sleep(1)
        add.click_button(add.add_vehicle_filter_surname)
        time.sleep(1)
        add.click_button(add.add_vehicle_filter_name)
        time.sleep(1)
        add.click_button(add.add_vehicle_filter_patronymic)
        time.sleep(1)
        add.click_button(add.add_vehicle_filter_contractor)
        time.sleep(1)
        add.click_button(add.apply_filter_vehicle)
        time.sleep(1)

        add.input_in_field(add.name_driver_vehicle, "Дан")
        time.sleep(2)
        add.verify_text_on_page(text='Д404ОН')
        add.backspace_and_input(add.name_driver_vehicle, "")

    with allure.step('проверка фильтра "Фамилия водителя"'):
        add.input_in_field(add.surname_driver_vehicle, "Жилиман")
        time.sleep(2)
        add.verify_text_on_page(text='WAHATRACK')
        add.backspace_and_input(add.surname_driver_vehicle, "")

    with allure.step('проверка фильтра "Отчество водителя"'):
        add.input_in_field(add.patronymic_driver_vehicle, "ВО-20240512121331")
        time.sleep(2)
        add.verify_text_on_page(text='2062626')
        add.backspace_and_input(add.patronymic_driver_vehicle, "")

    with allure.step('проверка фильтра "Подрядчик"'):
        add.input_in_field(add.contractor_vehicle, "Auto LKP")
        time.sleep(2)
        add.input_in_field(add.number_vehicles, "ПРО")
        time.sleep(2)
        add.verify_text_on_page(text='ПРО_СТО')
        add.backspace_and_input(add.contractor_vehicle, "")
        add.backspace_and_input(add.number_vehicles, "")

    with allure.step('проверка фильтра "Тип авто перевозки"'):
        add.move_to_element(com.type_road_transport_two)
        time.sleep(2)
        add.click_on_the_cross(com.cross_six)
        time.sleep(2)
        add.move_and_click(move_to=com.type_road_transport_two, click_to=com.cargo_transportation)
        time.sleep(2)
        add.input_in_field(add.number_vehicles, "WH400000")
        add.verify_text_on_page(text='WH400000', should_exist=True)
        add.verify_text_on_page(text='ТК567У', should_exist=False)
        add.backspace_and_input(add.number_vehicles, "")
        time.sleep(2)
        add.move_to_element(com.type_road_transport_two)
        time.sleep(2)
        add.click_on_the_cross(com.cross_six)
        time.sleep(2)
        add.move_and_click(move_to=com.type_road_transport_two, click_to=com.cargo_passenger_transportation)
        time.sleep(3)
        add.input_in_field(add.number_vehicles, "А444АА")
        add.verify_text_on_page(text='А444АА', should_exist=True)
        add.verify_text_on_page(text='ТС20231229113421', should_exist=False)
        add.backspace_and_input(add.number_vehicles, "")
        time.sleep(2)
        add.move_to_element(com.type_road_transport_two)
        time.sleep(2)
        add.click_on_the_cross(com.cross_six)
        time.sleep(2)
        add.move_and_click(move_to=com.type_road_transport_two, click_to=com.special_transportation)
        time.sleep(1)
        add.click_button(com.manipulator_truck)
        time.sleep(2)
        add.verify_text_on_page(text='ВТС-20240512231701', should_exist=True)
        add.verify_text_on_page(text='ТС20240110120731', should_exist=False)
        time.sleep(2)
        add.move_to_element(com.type_road_transport_two)
        time.sleep(2)
        add.click_on_the_cross(com.cross_six)
        time.sleep(2)
