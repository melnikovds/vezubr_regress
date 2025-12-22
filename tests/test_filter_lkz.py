import time
import allure
import pytest
from setuptools.command.setopt import option_base
from pages.filters_gm_lkz_lke_page import GmFilters
from pages.contractor_list_page import ContractorList
from pages.profile_page import *
from pages.user_add_page import *


@allure.story("Extended")
@allure.feature('Фильтры')
@allure.description('ЛКЗ, Тестирование: фильтры в разделе "Задания"')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_filter_assignment_lkz(base_fixture, domain, request):
    base, sidebar = base_fixture

    with allure.step("Переходим на вкладку 'Задания'"):
        sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.tasks_list_button)
        add = GmFilters(base.driver)

    with allure.step("Устанавливаем дату создания 'За все время'"):
        add.dropdown_without_input(add.required_search_by_date, "За все время")

    with allure.step("Проверка фильтра 'Номер заказа'"):
        add.input_in_field(add.order_number, "очень", wait='lst')
        time.sleep(2)
        add.verify_text_on_page(text="важное")
        add.backspace_and_input(add.order_number, "")

    with allure.step("Проверка фильтра 'Отправитель'"):
        add.input_in_field(add.sender, "ВОРОНЕЖСКАЯ", wait='lst')
        time.sleep(2)
        add.verify_text_on_page(text="11.06.2025 - 100")
        add.backspace_and_input(add.sender, "")

    with allure.step("Проверка фильтра 'Получатель'"):
        add.input_in_field(add.recipient, "ТОРГОВАЯ", wait='lst')
        time.sleep(2)
        add.verify_text_on_page(text="Авто тест 1")
        add.backspace_and_input(add.recipient, "")

    with allure.step("Проверка фильтра 'Кому передать Заявку'"):
        add.to_whom_aplication()

    with allure.step("Проверка фильтров 'Регионы/города'"):
        add.filters_region()


@allure.story("Extended")
@allure.feature('Фильтры')
@allure.description('ЛКЗ, Тестирование: фильтры в разделе "Отправления"')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_filter_departures_lkz(base_fixture, domain, request):
    base, sidebar = base_fixture

    with allure.step("Переходим на вкладку 'отправления'"):
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
@allure.description('ЛКЗ, Тестирование: фильтры в разделе "Грузоместа"')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_filter_gm_lkz(base_fixture, domain, request):
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


@allure.story("Extended")
@allure.feature('Фильтры')
@allure.description('ЛКЗ, Тестирование: фильтры в разделе "Контрагенты"')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_filter_contractor_lkz(base_fixture, domain, request):
    base, sidebar = base_fixture

    with allure.step("Переходим на вкладку 'Подрядчики'"):
        sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                               do_assert=True, wait="lst")
        add = ContractorList(base.driver)
        add.move_to_element(add.contractor_role)
        time.sleep(2)
        add.click_on_the_cross(add.role_cross)
        time.sleep(2)

    with allure.step("Проверка фильтра 'ИНН'"):
        add.input_in_field(add.contractor_inn, "68831")
        time.sleep(2)
        add.verify_text_on_page(text="6883106209", should_exist=True)
        add.verify_text_on_page(text="Auto LKP", should_exist=True)
        add.verify_text_on_page(text="5178860124", should_exist=False)
        add.verify_text_on_page(text="Auto LKE", should_exist=False)
        add.backspace_and_input(add.contractor_inn, "")

    with allure.step("Проверка фильтра 'Наименование подрядчика'"):
        add.input_in_field(add.contractor_name, "Перевозчик")
        time.sleep(2)
        add.verify_text_on_page(text="ООО", should_exist=True)
        add.verify_text_on_page(text="5009112893", should_exist=True)
        add.verify_text_on_page(text="Auto LKP", should_exist=False)
        add.verify_text_on_page(text="Auto LKE", should_exist=False)
        add.backspace_and_input(add.contractor_name, "")

    with allure.step("Проверка фильтра 'Роль'"):
        # add.dropdown_with_input(add.contractor_role, option_text='Подрядчик', index=1, wait_type='located')
        add.click_button(add.contractor_role)
        time.sleep(1)
        add.click_button(add.first_role)
        time.sleep(2)
        add.verify_text_on_page(text="106209", should_exist=True)
        add.verify_text_on_page(text="112893", should_exist=True)
        add.verify_text_on_page(text="860124", should_exist=False)

        add.move_to_element(add.contractor_role_modified)
        time.sleep(2)
        add.click_on_the_cross(add.role_cross)
        time.sleep(2)

        # add.dropdown_with_input(add.contractor_role, option_text='Экспедитор')
        add.click_button(add.contractor_role)
        time.sleep(1)
        add.click_button(add.second_role)
        time.sleep(2)
        add.verify_text_on_page(text="860124", should_exist=True)
        add.verify_text_on_page(text="106209", should_exist=False)
        add.verify_text_on_page(text="112893", should_exist=False)

        add.move_to_element(add.contractor_role_modified)
        time.sleep(2)
        add.click_on_the_cross(add.role_cross)
        time.sleep(2)


@allure.story("Extended")
@allure.feature('Фильтры')
@allure.description('ЛКЗ, Тестирование: фильтры в разделе "Пользователи"')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_filter_users_lkz(base_fixture, domain):
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
        add.click_button(add.apply_add_filter)
        time.sleep(1)

    with allure.step("Проверка фильтра 'ФИО'"):
        add.input_in_field(add.fio_filter, value="1918")
        time.sleep(2)
        add.verify_text_on_page(text="Ф-20251125081918", should_exist=True)
        add.verify_text_on_page(text="718-07-62", should_exist=True)
        add.verify_text_on_page(text="Ф-20251127111930", should_exist=False)
        add.verify_text_on_page(text="940-02-50", should_exist=False)
        add.backspace_and_input(add.fio_filter, "")

    with allure.step("Проверка фильтра 'Тип'"):
        add.dropdown_without_input(add.type_filter, option_text='Пользователь')
        time.sleep(2)
        add.verify_text_on_page(text="649-06-66", should_exist=True)
        add.verify_text_on_page(text="0807144826", should_exist=True)
        add.verify_text_on_page(text="177-71-36", should_exist=False)
        add.verify_text_on_page(text="1129110625", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.dropdown_without_input(add.type_filter, option_text='API')
        time.sleep(2)
        add.verify_text_on_page(text="177-71-36", should_exist=True)
        add.verify_text_on_page(text="1129110625", should_exist=True)
        add.verify_text_on_page(text="0807144826", should_exist=False)
        add.verify_text_on_page(text="649-06-66", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.dropdown_without_input(add.type_filter, option_text='Пользователь внутреннего контрагента')
        time.sleep(2)
        add.verify_text_on_page(text="177-71-36", should_exist=False)
        add.verify_text_on_page(text="1129110625", should_exist=False)
        add.verify_text_on_page(text="0807144826", should_exist=False)
        add.verify_text_on_page(text="649-06-66", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

    with allure.step("Проверка фильтра 'Роль'"):
        # add.dropdown_without_input(add.role_filter, option_text='Диспетчер', dd_index=1)
        add.click_button(add.role_filter)
        add.click_button(add.dispatcher_role)
        time.sleep(2)
        add.verify_text_on_page(text="560-68-80", should_exist=True)
        add.verify_text_on_page(text="125-65-01", should_exist=True)
        add.verify_text_on_page(text="177-71-36", should_exist=False)
        add.verify_text_on_page(text="047-45-91", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.click_button(add.role_filter)
        add.click_button(add.manager_role)
        time.sleep(2)
        add.verify_text_on_page(text="278-29-40", should_exist=True)
        add.verify_text_on_page(text="1555 1555", should_exist=True)
        add.verify_text_on_page(text="560-68-80", should_exist=False)
        add.verify_text_on_page(text="auto@lke.com", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.click_button(add.role_filter)
        add.click_button(add.administrator_role)
        time.sleep(2)
        add.verify_text_on_page(text="174-18-05", should_exist=True)
        add.verify_text_on_page(text="802-49-36", should_exist=True)
        add.verify_text_on_page(text="278-29-40", should_exist=False)
        add.verify_text_on_page(text="480-32-19", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.click_button(add.role_filter)
        add.click_button(add.logistician_role)
        time.sleep(2)
        add.verify_text_on_page(text="177-71-36", should_exist=True)
        add.verify_text_on_page(text="940-02-50", should_exist=True)
        add.verify_text_on_page(text="174-18-05", should_exist=False)
        add.verify_text_on_page(text="560-68-80", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.click_button(add.role_filter)
        add.click_button(add.office_worker_role)
        time.sleep(2)
        add.verify_text_on_page(text="432-77-88", should_exist=True)
        add.verify_text_on_page(text="099-45-00", should_exist=True)
        add.verify_text_on_page(text="177-71-36", should_exist=False)
        add.verify_text_on_page(text="649-06-66", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

    with allure.step("Проверка фильтра 'Телефон'"):
        add.input_in_field(add.phone_filter, value='1300')
        time.sleep(1)
        add.verify_text_on_page(text="086-13-00", should_exist=True)
        add.verify_text_on_page(text="e20251126193432", should_exist=True)
        add.verify_text_on_page(text="560-68-80", should_exist=False)
        add.verify_text_on_page(text="Разинов", should_exist=False)
        add.backspace_and_input(add.phone_filter, "")

        add.input_in_field(add.phone_filter, value='921560')
        time.sleep(2)
        add.verify_text_on_page(text="560-68-80", should_exist=True)
        add.verify_text_on_page(text="Середенко", should_exist=True)
        add.verify_text_on_page(text="432-77-88", should_exist=False)
        add.verify_text_on_page(text="613-89-76", should_exist=False)
        add.backspace_and_input(add.phone_filter, "")

    with allure.step("Проверка фильтра 'Email'"):
        add.input_in_field(add.email_filter, value='razinov')
        time.sleep(1)
        add.verify_text_on_page(text="razinov@mail.ru", should_exist=True)
        add.verify_text_on_page(text="Разинов", should_exist=True)
        add.verify_text_on_page(text="gfdsaddd@mail.ru", should_exist=False)
        add.verify_text_on_page(text="e20251129213121", should_exist=False)
        add.backspace_and_input(add.email_filter, "")

        add.input_in_field(add.email_filter, value='auto@lkz.com')
        time.sleep(1)
        add.verify_text_on_page(text="auto@LKZ.com auto@LKZ.com", should_exist=True)
        add.verify_text_on_page(text="125-65-01", should_exist=True)
        add.verify_text_on_page(text="auto@LKE.com auto@LKE.com", should_exist=False)
        add.verify_text_on_page(text="razinov@mail.ru", should_exist=False)
        add.backspace_and_input(add.email_filter, "")

    with allure.step("Проверка фильтра 'Подразделение'"):
        add.click_button(add.subdivision_filter)
        add.click_button(add.subdivision_one)
        time.sleep(2)
        add.verify_text_on_page(text="432-77-88", should_exist=True)
        add.verify_text_on_page(text="265-33-98", should_exist=True)
        add.verify_text_on_page(text="747-69-69", should_exist=False)
        add.verify_text_on_page(text="802-49-36", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.click_button(add.subdivision_filter)
        add.click_button(add.subdivision_two)
        time.sleep(2)
        add.verify_text_on_page(text="747-69-69", should_exist=True)
        add.verify_text_on_page(text="427-74-70", should_exist=True)
        add.verify_text_on_page(text="432-77-88", should_exist=False)
        add.verify_text_on_page(text="174-18-05", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)


@allure.story("Extended")
@allure.feature('Фильтры')
@allure.description('ЛКЗ, Тестирование: фильтры контрагентов в разделе прикрепления Пользователей')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_filter_user_responsible_lkz(base_fixture, domain):
    base, sidebar = base_fixture

    with allure.step("Переход в профиль Пользователя"):
        sidebar.click_button(sidebar.profile_button, do_assert=True)
        tb = Profile(base.driver)
        tb.click_button(tb.users_tab)
        time.sleep(2)
        tb.click_button(tb.user_link, wait="form")
        time.sleep(1)

    with allure.step("Открытие таблицы с контрагентами"):
        add = User(base.driver)
        add.click_button(add.add_responsible_button, wait="lst")
        add.click_button(add.producer_tab, wait="lst")
        time.sleep(2)

    with allure.step("Проверка фильтра 'ИНН"):
        cl = ContractorList(base.driver)
        cl.input_in_field(cl.contractor_inn, value='68')
        time.sleep(1)
        cl.verify_text_on_page(text="6883106209", should_exist=True)
        cl.verify_text_on_page(text="Auto LKP", should_exist=True)
        cl.verify_text_on_page(text="5178860124", should_exist=False)
        cl.verify_text_on_page(text="Перевозчик", should_exist=False)
        cl.backspace_and_input(cl.contractor_inn, "")
        time.sleep(1)

    with allure.step("Проверка фильтра 'Наименования исполнителя"):
        cl.input_in_field(cl.contractor_name, value='перевоз')
        time.sleep(1)
        cl.verify_text_on_page(text="Перевозчик", should_exist=True)
        cl.verify_text_on_page(text="2893", should_exist=True)
        cl.verify_text_on_page(text="60124", should_exist=False)
        cl.verify_text_on_page(text="06209", should_exist=False)
        cl.backspace_and_input(cl.contractor_name, "")
        time.sleep(1)
        cl.click_button(cl.cancel_button)
