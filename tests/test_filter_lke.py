import time
import allure
import pytest
from pages.filters_gm_lkz_lke_page import GmFilters
from pages.contractor_list_page import ContractorList
from pages.profile_page import *
from pages.user_add_page import *


@allure.story("Extended")
@allure.feature('Фильтры')
@allure.description('ЛКЭ, Тестирование: фильтры в разделе "Задания"')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_filter_assignment_lke(base_fixture, domain, request):
    base, sidebar = base_fixture

    with allure.step("Переходим на вкладку 'Задания'"):
        sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.tasks_list_button)
        add = GmFilters(base.driver)

        time.sleep(3)


@allure.story("Extended")
@allure.feature('Фильтры')
@allure.description('ЛКЭ, Тестирование: фильтры в разделе "Отправления"')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_filter_departures_lke(base_fixture, domain, request):
    base, sidebar = base_fixture

    with allure.step("Переходим на вкладку 'Отправления'"):
        sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.dispatch_list_button)
        add = GmFilters(base.driver)

    with allure.step("Проверка фильтра 'Номер рейса'"):
        add.input_in_field(add.flight_number, "R-25-47-2447-1", wait='lst')
        time.sleep(2)
        add.verify_text_on_page(text="2448436500000")
        add.backspace_and_input(add.flight_number, "")

    with allure.step("Проверка фильтра 'По заданию №'"):
        add.input_in_field(add.according_task, "2448436490000", wait='lst')
        time.sleep(2)
        add.verify_text_on_page(text="R-25-46-2447-1")
        add.backspace_and_input(add.according_task, "")

    with allure.step("Проверка фильтров 'Адрес отправления/доставки'"):
        add.filter_departures_address_lke()

    with allure.step("Проверка фильтра 'Статус'"):
        add.filter_departure_status_lke()


@allure.story("Extended")
@allure.feature('Фильтры')
@allure.description('ЛКЭ, Тестирование: фильтры в разделе "Грузоместа"')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_filter_gm_lke(base_fixture, domain, request):
    base, sidebar = base_fixture

    with allure.step("Переходим на вкладку 'Грузоместа'"):
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


@allure.story("Extended")
@allure.feature('Фильтры')
@allure.description('ЛКЗ, Тестирование: фильтры в разделе "Контрагенты"')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_filter_contractor_lke(base_fixture, domain, request):
    base, sidebar = base_fixture

    with allure.step("Переходим на вкладку 'Заказчики'"):
        sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")
        add = ContractorList(base.driver)

    with allure.step("Проверка фильтра 'ИНН'"):
        add.input_in_field(add.contractor_inn, "979607")
        time.sleep(2)
        add.verify_text_on_page(text="0278979607", should_exist=True)
        add.verify_text_on_page(text="СПЕЦИАЛИЗИРОВАННЫЙ", should_exist=True)
        add.verify_text_on_page(text="НОВЭКС", should_exist=False)
        add.verify_text_on_page(text="9710109376", should_exist=False)
        add.verify_text_on_page(text="3123625054", should_exist=False)
        add.backspace_and_input(add.contractor_inn, "")

        add.input_in_field(add.contractor_inn, "7543")
        time.sleep(2)
        add.verify_text_on_page(text="7736207543", should_exist=False)
        add.verify_text_on_page(text="ЯНДЕКС", should_exist=False)
        add.backspace_and_input(add.contractor_inn, "")

        add.input_in_field(add.contractor_inn, "106209")
        time.sleep(2)
        add.verify_text_on_page(text="6883106209", should_exist=False)
        add.verify_text_on_page(text="6320002223", should_exist=False)
        add.backspace_and_input(add.contractor_inn, "")

    with allure.step("Проверка фильтра 'Наименование клиента'"):
        add.input_in_field(add.contractor_name, "ИНТЕГРАЛ")
        time.sleep(2)
        add.verify_text_on_page(text="9724206806", should_exist=True)
        add.verify_text_on_page(text="3123625054", should_exist=False)
        add.verify_text_on_page(text="Масляков", should_exist=False)
        add.backspace_and_input(add.contractor_name, "")

        add.input_in_field(add.contractor_name, "LKZ")
        time.sleep(2)
        add.verify_text_on_page(text="3123625054", should_exist=True)
        add.verify_text_on_page(text="9724206806", should_exist=False)
        add.verify_text_on_page(text="7751221408", should_exist=False)
        add.backspace_and_input(add.contractor_name, "")

    with allure.step("Переходим на вкладку 'Подрядчики'"):
        sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")
        add.move_to_element(add.contractor_role)
        time.sleep(2)
        add.click_on_the_cross(add.role_cross)
        time.sleep(2)

    with allure.step("Проверка фильтра 'ИНН'"):
        add.input_in_field(add.contractor_inn, "07543")
        time.sleep(2)
        add.verify_text_on_page(text="7736207543", should_exist=True)
        add.verify_text_on_page(text="ЯНДЕКС", should_exist=True)
        add.verify_text_on_page(text="3072686", should_exist=False)
        add.verify_text_on_page(text="6883106209", should_exist=False)
        add.verify_text_on_page(text="СТОЛИЦА ГРУПП", should_exist=False)
        add.backspace_and_input(add.contractor_inn, "")

        add.input_in_field(add.contractor_inn, "91506")
        time.sleep(2)
        add.verify_text_on_page(text="9710091506", should_exist=False)
        add.verify_text_on_page(text="КУЛЬТУРА", should_exist=False)
        add.backspace_and_input(add.contractor_inn, "")

        add.input_in_field(add.contractor_inn, "3625054")
        time.sleep(2)
        add.verify_text_on_page(text="782510049166", should_exist=False)
        add.verify_text_on_page(text="3123625054", should_exist=False)
        add.backspace_and_input(add.contractor_inn, "")

    with allure.step("Проверка фильтра 'Наименование подрядчика'"):
        add.input_in_field(add.contractor_name, "АВТОВАЗ")
        time.sleep(2)
        add.verify_text_on_page(text="НАО АВТОВАЗ", should_exist=True)
        add.verify_text_on_page(text="6320002223", should_exist=True)
        add.verify_text_on_page(text="7736207543", should_exist=False)
        add.verify_text_on_page(text="6883106209", should_exist=False)
        add.backspace_and_input(add.contractor_name, "")


@allure.story("Extended")
@allure.feature('Фильтры')
@allure.description('ЛКЭ, Тестирование: фильтры в разделе "Пользователи"')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_filter_users_lke(base_fixture, domain):
    base, sidebar = base_fixture

    with allure.step("Переход в таб 'Пользователи'"):
        sidebar.click_button(sidebar.profile_button, do_assert=True)
        tb = Profile(base.driver)
        tb.click_button(tb.users_tab)
        time.sleep(2)

    with allure.step("Включение всех фильтров"):
        add = UsersFilter(base.driver)
        add.click_button(add.reset_users_filter)
        time.sleep(1)
        add.click_button(add.additional_filters)
        time.sleep(1)
        add.click_button(add.default_filters)
        add.click_button(add.first_add_filter)
        add.click_button(add.second_add_filter)
        add.click_button(add.third_add_filter)
        add.click_button(add.groups_add_filter)
        add.click_button(add.apply_add_filter)
        time.sleep(1)

    with allure.step("Проверка фильтра 'ФИО'"):
        add.input_in_field(add.fio_filter, value="титов")
        time.sleep(2)
        add.verify_text_on_page(text="Борис Юрьевич", should_exist=True)
        add.verify_text_on_page(text="hkjh@mail.ru", should_exist=True)
        add.verify_text_on_page(text="e20251129212743", should_exist=False)
        add.verify_text_on_page(text="286-32-80", should_exist=False)
        add.backspace_and_input(add.fio_filter, "")

    with allure.step("Проверка фильтра 'Тип'"):
        add.dropdown_without_input(add.type_filter, option_text='Пользователь')
        add.input_in_field(add.phone_filter, value='429')
        time.sleep(2)
        add.verify_text_on_page(text="429-84-38", should_exist=True)
        add.click_button(add.reset_users_filter)
        time.sleep(1)
        add.dropdown_without_input(add.type_filter, option_text='Пользователь')
        add.input_in_field(add.email_filter, value='e20251129')
        time.sleep(2)
        add.verify_text_on_page(text="e20251129212511", should_exist=True)
        add.verify_text_on_page(text="286-32-80", should_exist=False)
        add.verify_text_on_page(text="861-51-97", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.dropdown_without_input(add.type_filter, option_text='API')
        time.sleep(2)
        add.verify_text_on_page(text="Ф-20240208095352", should_exist=True)
        add.verify_text_on_page(text="e20251127111248", should_exist=True)
        add.verify_text_on_page(text="429-84-38", should_exist=False)
        add.verify_text_on_page(text="184-28-54", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.dropdown_without_input(add.type_filter, option_text='Пользователь внутреннего контрагента')
        time.sleep(2)
        add.verify_text_on_page(text="099-18-18", should_exist=False)
        add.verify_text_on_page(text="085-47-15", should_exist=False)
        add.verify_text_on_page(text="709-93-41", should_exist=False)
        add.verify_text_on_page(text="975-19-01", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

    with allure.step("Проверка фильтра 'Роль'"):
        add.click_button(add.role_filter)
        add.click_button(add.manager_role)
        time.sleep(2)
        add.verify_text_on_page(text="278-29-40", should_exist=True)
        add.verify_text_on_page(text="000-19-10", should_exist=True)
        add.verify_text_on_page(text="951-17-71", should_exist=False)
        add.verify_text_on_page(text="263-08-91", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.click_button(add.role_filter)
        add.click_button(add.dispatcher_role)
        time.sleep(2)
        add.verify_text_on_page(text="dsdoopp@mail.ru", should_exist=True)
        add.verify_text_on_page(text="auto@lke.com", should_exist=True)
        add.verify_text_on_page(text="e20251129212511", should_exist=False)
        add.verify_text_on_page(text="e20251129105942", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.click_button(add.role_filter)
        add.click_button(add.administrator_role)
        add.input_in_field(add.phone_filter, value='4298438')
        time.sleep(2)
        add.verify_text_on_page(text="e20251129212743", should_exist=True)
        add.verify_text_on_page(text="951-17-71", should_exist=False)
        add.click_button(add.reset_users_filter)
        time.sleep(1)
        add.click_button(add.role_filter)
        add.click_button(add.administrator_role)
        add.input_in_field(add.email_filter, value='e202511292')
        time.sleep(2)
        add.verify_text_on_page(text="746-43-83", should_exist=True)
        add.verify_text_on_page(text="000-19-10", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.click_button(add.role_filter)
        add.click_button(add.logistician_role)
        time.sleep(2)
        add.verify_text_on_page(text="951-17-71", should_exist=True)
        add.verify_text_on_page(text="e20251129105942", should_exist=True)
        add.verify_text_on_page(text="099-18-18", should_exist=False)
        add.verify_text_on_page(text="125-65-00", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.click_button(add.role_filter)
        add.click_button(add.office_worker_role)
        time.sleep(2)
        add.verify_text_on_page(text="lkjhjkk@mail.ru", should_exist=True)
        add.verify_text_on_page(text="Фёдоров", should_exist=True)
        add.verify_text_on_page(text="429-84-38", should_exist=False)
        add.verify_text_on_page(text="e20251129110248", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

    with allure.step("Проверка фильтра 'Телефон'"):
        add.input_in_field(add.phone_filter, value='412263')
        time.sleep(1)
        add.verify_text_on_page(text="e20251128193852", should_exist=True)
        add.verify_text_on_page(text="Ф-20251128193832", should_exist=True)
        add.verify_text_on_page(text="Ф-20251129212451", should_exist=False)
        add.verify_text_on_page(text="286-32-80", should_exist=False)
        add.backspace_and_input(add.phone_filter, "")

        add.input_in_field(add.phone_filter, value='1235938834')
        time.sleep(2)
        add.verify_text_on_page(text="e20251128193620", should_exist=True)
        add.verify_text_on_page(text="20251128193600", should_exist=True)
        add.verify_text_on_page(text="20251129212723", should_exist=False)
        add.verify_text_on_page(text="20251129105955", should_exist=False)
        add.backspace_and_input(add.phone_filter, "")

    with allure.step("Проверка фильтра 'Email'"):
        add.input_in_field(add.email_filter, value='dsdoopp')
        time.sleep(1)
        add.verify_text_on_page(text="dsdoopp@mail.ru", should_exist=True)
        add.verify_text_on_page(text="Суворов", should_exist=True)
        add.verify_text_on_page(text="hkjh@mail.ru", should_exist=False)
        add.verify_text_on_page(text="e20240208095353", should_exist=False)
        add.backspace_and_input(add.email_filter, "")

        add.input_in_field(add.email_filter, value='lkjhjkk@mail.ru')
        time.sleep(1)
        add.verify_text_on_page(text="Фёдоров", should_exist=True)
        add.verify_text_on_page(text="890-87-57", should_exist=True)
        add.verify_text_on_page(text="429-84-38", should_exist=False)
        add.verify_text_on_page(text="108-99-92", should_exist=False)
        add.backspace_and_input(add.email_filter, "")

    with allure.step("Проверка фильтра 'Подразделение'"):
        add.click_button(add.subdivision_filter)
        add.click_button(add.subdivision_lke)
        time.sleep(2)
        add.verify_text_on_page(text="108-99-92", should_exist=True)
        add.verify_text_on_page(text="000-19-10", should_exist=True)
        add.verify_text_on_page(text="794-52-53", should_exist=False)
        add.verify_text_on_page(text="362-49-43", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

    with allure.step("Проверка фильтра 'Группы'"):
        add.click_button(add.groups_filter)
        add.click_button(add.x_group)
        time.sleep(2)
        add.verify_text_on_page(text="hkjh@mail.ru", should_exist=True)
        add.verify_text_on_page(text="e20251127111553", should_exist=True)
        add.verify_text_on_page(text="e20251129212511", should_exist=False)
        add.verify_text_on_page(text="e20251128193620", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)


@allure.story("Extended")
@allure.feature('Фильтры')
@allure.description('ЛКЭ, Тестирование: фильтры контрагентов в разделе прикрепления Пользователей')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_filter_user_responsible_lke(base_fixture, domain):
    base, sidebar = base_fixture

    with allure.step("Переход в профиль Пользователя"):
        sidebar.click_button(sidebar.profile_button, do_assert=True)
        tb = Profile(base.driver)
        tb.click_button(tb.users_tab)
        time.sleep(2)
        tb.click_button(tb.user_link, wait="form")
        time.sleep(1)

    with allure.step("Открытие таблицы с подрядчиками"):
        add = User(base.driver)
        add.click_button(add.add_responsible_button, wait="lst")
        add.click_button(add.producer_tab, wait="lst")
        time.sleep(2)

    with allure.step("Проверка фильтра 'ИНН"):
        cl = ContractorList(base.driver)
        cl.input_in_field(cl.contractor_inn, value='7733')
        time.sleep(1)
        cl.verify_text_on_page(text="7733769583", should_exist=True)
        cl.verify_text_on_page(text="АСТИС", should_exist=True)
        cl.verify_text_on_page(text="5024235160", should_exist=False)
        cl.verify_text_on_page(text="ДЮАС", should_exist=False)
        cl.backspace_and_input(cl.contractor_inn, "")
        time.sleep(1)

    with allure.step("Проверка фильтра 'Наименования исполнителя"):
        cl.input_in_field(cl.contractor_name, value='столица')
        time.sleep(2)
        cl.verify_text_on_page(text="СТОЛИЦА ГРУПП", should_exist=True)
        cl.verify_text_on_page(text="7731367582", should_exist=True)
        cl.verify_text_on_page(text="ЯНДЕКС", should_exist=False)
        cl.verify_text_on_page(text="6320002223", should_exist=False)
        cl.backspace_and_input(cl.contractor_name, "")
        time.sleep(1)
        cl.click_button(cl.cancel_button)

    with allure.step("Открытие таблицы с заказчиками"):
        add = User(base.driver)
        add.click_button(add.add_responsible_button, wait="lst")
        add.click_button(add.client_tab, wait="lst")
        time.sleep(2)

    with allure.step("Проверка фильтра 'ИНН"):
        cl = ContractorList(base.driver)
        cl.input_in_field(cl.contractor_inn, value='78')
        time.sleep(1)
        cl.verify_text_on_page(text="7814801242", should_exist=True)
        cl.verify_text_on_page(text="ЛИФТСТРОЙ", should_exist=True)
        cl.verify_text_on_page(text="7751221408", should_exist=False)
        cl.verify_text_on_page(text="ТЕХТРЕЙД", should_exist=False)
        cl.backspace_and_input(cl.contractor_inn, "")
        time.sleep(1)

    with allure.step("Проверка фильтра 'Наименования клиента"):
        cl.input_in_field(cl.contractor_name, value='бур')
        time.sleep(1)
        cl.verify_text_on_page(text="БУРСПЕЦСТРОЙ", should_exist=True)
        cl.verify_text_on_page(text="9710091506", should_exist=True)
        cl.verify_text_on_page(text="5506139969", should_exist=False)
        cl.verify_text_on_page(text="5001162998", should_exist=False)
        cl.backspace_and_input(cl.contractor_name, "")
        time.sleep(1)
        cl.click_button(cl.cancel_button)
















