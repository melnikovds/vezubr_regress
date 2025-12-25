import time
import allure
import pytest
from pages.filters_gm_lkz_lke_page import GmFilters
from pages.contractor_list_page import ContractorList
from pages.profile_page import *


@allure.story("Extended")
@allure.feature('Фильтры')
@allure.description('ЛКП, Тестирование: фильтры в разделе "Отправления"')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_filter_departures_lkp(base_fixture, domain, request):
    base, sidebar = base_fixture

    with allure.step("Переходим на вкладку 'Отправления'"):
        sidebar.click_button(sidebar.dispatch_list_button, do_assert=True, wait="lst")
        add = GmFilters(base.driver)

    with allure.step("Проверка фильтра 'Номер рейса'"):
        add.input_in_field(add.flight_number, "R-25-43546-2449-1", wait='lst')
        time.sleep(2)
        add.verify_text_on_page(text="2448445360000")
        add.verify_text_on_page(text="2448445370000", should_exist=False)
        add.backspace_and_input(add.flight_number, "")

    with allure.step("Проверка фильтра 'По заданию №'"):
        add.input_in_field(add.according_task, "2448445350000", wait='lst')
        time.sleep(2)
        add.verify_text_on_page(text="R-25-40816-2449-1")
        add.verify_text_on_page(text="R-25-40815-2449-1", should_exist=False)
        add.backspace_and_input(add.according_task, "")

    with allure.step("Проверка фильтров 'Адрес отправления/доставки'"):
        add.input_in_field(add.departure_address, "оружейная")
        time.sleep(2)
        add.verify_text_on_page(text="2448436050000")
        add.verify_text_on_page(text="2448000045450", should_exist=False)
        add.backspace_and_input(add.departure_address, "")
        add.input_in_field(add.delivery_address, "сыктывкар")
        time.sleep(2)
        add.verify_text_on_page(text="2448000045450")
        add.verify_text_on_page(text="2448445340000", should_exist=False)
        add.backspace_and_input(add.delivery_address, "")

    with allure.step("Проверка фильтра 'Статус'"):
        add.click_button(add.status)
        time.sleep(2)
        add.click_button(add.waiting_shipment)
        time.sleep(2)
        add.verify_text_on_page(text="2448445640000")
        add.verify_text_on_page(text="2448436320000", should_exist=False)

        add.refresh_page()
        time.sleep(2)

        add.move_to_element(add.status_modified)
        time.sleep(2)
        add.click_on_the_cross(add.cross_status_dispatch)


@allure.story("Extended")
@allure.feature('Фильтры')
@allure.description('ЛКЗ, Тестирование: фильтры в разделе "Контрагенты"')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_filter_contractor_lkp(base_fixture, domain, request):
    base, sidebar = base_fixture

    with allure.step("Переходим на вкладку 'Заказчики'"):
        sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")
        add = ContractorList(base.driver)

    with allure.step("Проверка фильтра 'ИНН'"):
        add.input_in_field(add.contractor_inn, "312362")
        time.sleep(2)
        add.verify_text_on_page(text="3123625054", should_exist=True)
        add.verify_text_on_page(text="Auto LKZ", should_exist=True)
        add.verify_text_on_page(text="5178860124", should_exist=False)
        add.verify_text_on_page(text="Auto LKE", should_exist=False)
        add.backspace_and_input(add.contractor_inn, "")

        add.input_in_field(add.contractor_inn, "60124")
        time.sleep(2)
        add.verify_text_on_page(text="5178860124", should_exist=True)
        add.verify_text_on_page(text="Auto LKE", should_exist=True)
        add.verify_text_on_page(text="3123625054", should_exist=False)
        add.verify_text_on_page(text="Auto LKZ", should_exist=False)
        add.backspace_and_input(add.contractor_inn, "")

    with allure.step("Проверка фильтра 'Наименование клиента'"):
        add.input_in_field(add.contractor_name, "Auto LKZ")
        time.sleep(2)
        add.verify_text_on_page(text="3123625054", should_exist=True)
        add.verify_text_on_page(text="Auto LKE", should_exist=False)
        add.verify_text_on_page(text="5178860124", should_exist=False)
        add.backspace_and_input(add.contractor_name, "")

        add.input_in_field(add.contractor_name, "Auto LKE")
        time.sleep(2)
        add.verify_text_on_page(text="5178860124", should_exist=True)
        add.verify_text_on_page(text="Auto LKZ", should_exist=False)
        add.verify_text_on_page(text="3123625054", should_exist=False)
        add.backspace_and_input(add.contractor_name, "")


@allure.story("Extended")
@allure.feature('Фильтры')
@allure.description('ЛКП, Тестирование: фильтры в разделе "Пользователи"')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_filter_users_lkp(base_fixture, domain):
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
        add.input_in_field(add.fio_filter, value="савенков")
        time.sleep(2)
        add.verify_text_on_page(text="Мануил", should_exist=True)
        add.verify_text_on_page(text="888-01-01", should_exist=True)
        add.verify_text_on_page(text="838-54-84", should_exist=False)
        add.verify_text_on_page(text="222-08-09", should_exist=False)
        add.backspace_and_input(add.fio_filter, "")

    with allure.step("Проверка фильтра 'Тип'"):
        add.dropdown_without_input(add.type_filter, option_text='Пользователь')
        time.sleep(2)
        add.verify_text_on_page(text="Ф-20250819192856", should_exist=True)
        add.verify_text_on_page(text="879-50-37", should_exist=True)
        add.verify_text_on_page(text="838-54-84", should_exist=False)
        add.verify_text_on_page(text="20251128194140", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.dropdown_without_input(add.type_filter, option_text='API')
        time.sleep(2)
        add.verify_text_on_page(text="20251127111842", should_exist=True)
        add.verify_text_on_page(text="175-61-89", should_exist=True)
        add.verify_text_on_page(text="888-01-01", should_exist=False)
        add.verify_text_on_page(text="215-67-65", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.dropdown_without_input(add.type_filter, option_text='Пользователь внутреннего контрагента')
        time.sleep(2)
        add.verify_text_on_page(text="222-08-09", should_exist=False)
        add.verify_text_on_page(text="215-67-65", should_exist=False)
        add.verify_text_on_page(text="376-02-56", should_exist=False)
        add.verify_text_on_page(text="593-24-50", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

    with allure.step("Проверка фильтра 'Роль'"):
        add.click_button(add.role_filter)
        add.click_button(add.dispatcher_role)
        time.sleep(2)
        add.verify_text_on_page(text="savenkovmn", should_exist=True)
        add.verify_text_on_page(text="125-65-02", should_exist=True)
        add.verify_text_on_page(text="377-93-90", should_exist=False)
        add.verify_text_on_page(text="175-61-89", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.click_button(add.role_filter)
        add.click_button(add.driver_dispatcher_role)
        time.sleep(2)
        add.verify_text_on_page(text="377-93-90", should_exist=True)
        add.verify_text_on_page(text="vodilov@mail.ru", should_exist=True)
        add.verify_text_on_page(text="savenkovmn@mail.ru", should_exist=False)
        add.verify_text_on_page(text="107-69-96", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.click_button(add.role_filter)
        add.click_button(add.manager_role)
        time.sleep(2)
        add.verify_text_on_page(text="slavik@mail.ru", should_exist=True)
        add.verify_text_on_page(text="e20240208094824@mail.ru", should_exist=True)
        add.verify_text_on_page(text="e20251129213033@mail.ru", should_exist=False)
        add.verify_text_on_page(text="vodilov@mail.ru", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.click_button(add.role_filter)
        add.click_button(add.administrator_role)
        time.sleep(2)
        add.verify_text_on_page(text="649-86-30", should_exist=True)
        add.verify_text_on_page(text="879-50-37", should_exist=True)
        add.verify_text_on_page(text="888-01-01", should_exist=False)
        add.verify_text_on_page(text="838-54-84", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.click_button(add.role_filter)
        add.click_button(add.logistician_role)
        time.sleep(2)
        add.verify_text_on_page(text="792-17-14", should_exist=True)
        add.verify_text_on_page(text="235-84-71", should_exist=True)
        add.verify_text_on_page(text="e20250807144810@mail.ru", should_exist=False)
        add.verify_text_on_page(text="e20240208094824@mail.ru", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

        add.click_button(add.role_filter)
        add.click_button(add.office_worker_role)
        time.sleep(2)
        add.verify_text_on_page(text="222-08-09", should_exist=True)
        add.verify_text_on_page(text="gulyaevll@mail.ru", should_exist=True)
        add.verify_text_on_page(text="Ф-20251129110537", should_exist=False)
        add.verify_text_on_page(text="Ф-20250819192856", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

    with allure.step("Проверка фильтра 'Телефон'"):
        add.input_in_field(add.phone_filter, value='91188')
        time.sleep(1)
        add.verify_text_on_page(text="zotov@mail.ru", should_exist=True)
        add.verify_text_on_page(text="Зотов", should_exist=True)
        add.verify_text_on_page(text="gulyaevll@mail.ru", should_exist=False)
        add.verify_text_on_page(text="e20251129110537@mail.ru", should_exist=False)
        add.backspace_and_input(add.phone_filter, "")

        add.input_in_field(add.phone_filter, value='9827921714')
        time.sleep(2)
        add.verify_text_on_page(text="e20251129110537@mail.ru", should_exist=True)
        add.verify_text_on_page(text="Ф-20251129110537", should_exist=True)
        add.verify_text_on_page(text="e20251129213033@mail.ru", should_exist=False)
        add.verify_text_on_page(text="e20251128194141@mail.ru", should_exist=False)
        add.backspace_and_input(add.phone_filter, "")

    with allure.step("Проверка фильтра 'Email'"):
        add.input_in_field(add.email_filter, value='gulyaev')
        time.sleep(1)
        add.verify_text_on_page(text="gulyaevll@mail.ru", should_exist=True)
        add.verify_text_on_page(text="Гуляев", should_exist=True)
        add.verify_text_on_page(text="savenkovmn@mail.ru", should_exist=False)
        add.verify_text_on_page(text="e20251129213033@mail.ru", should_exist=False)
        add.backspace_and_input(add.email_filter, "")

        add.input_in_field(add.email_filter, value='auto@lkp.com')
        time.sleep(1)
        add.verify_text_on_page(text="auto@LKP.com auto@LKP.com", should_exist=True)
        add.verify_text_on_page(text="125-65-02", should_exist=True)
        add.verify_text_on_page(text="auto@LKE.com auto@LKE.com", should_exist=False)
        add.verify_text_on_page(text="el1234567890@mai.ru", should_exist=False)
        add.backspace_and_input(add.email_filter, "")

    with allure.step("Проверка фильтра 'Подразделение'"):
        add.click_button(add.subdivision_filter)
        add.click_button(add.subdivision_lkp)
        time.sleep(2)
        add.verify_text_on_page(text="savenkovmn@mail.ru", should_exist=True)
        add.verify_text_on_page(text="slavik@mail.ru", should_exist=True)
        add.verify_text_on_page(text="e20251129213033@mail.ru", should_exist=False)
        add.verify_text_on_page(text="e20240208094624@mail.ru", should_exist=False)

        add.click_button(add.reset_users_filter)
        time.sleep(1)

























