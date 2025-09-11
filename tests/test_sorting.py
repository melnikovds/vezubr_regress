import allure
import pytest

from pages.insurer_page import Insurer
from pages.insurers_list_page import InsurersList
from pages.profile_page import Profile


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЗ. Тест сортировок списков заявок по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_sorting_requests_lkz(base_fixture, domain):
    base, sidebar = base_fixture

    base.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_active_list_button,
                        do_assert=True, wait="lst")
    base.click_button(base.reset_button, wait="lst")

    # Кликаем по ВСЕМ найденным кнопкам сортировки, по 3 раза
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списков заявок по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_sorting_requests_lke(base_fixture, domain):
    base, sidebar = base_fixture

    base.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_active_list_button,
                        do_assert=True, wait="lst")
    base.click_button(base.reset_button, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКП. Тест сортировок списков заявок по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_sorting_requests_lkp(base_fixture, domain):
    base, sidebar = base_fixture

    base.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_active_list_button,
                        do_assert=True, wait="lst")
    base.click_button(base.reset_button, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    base.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.cdr_active_list_button,
                        do_assert=True, wait="lst")
    base.click_button(base.reset_button, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЗ. Тест сортировок списков рейсов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_sorting_orders_lkz(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.ftl_list_button,
                           do_assert=True, wait="lst")
    base.click_button(base.reset_button, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.deferred_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.regular_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списков рейсов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_sorting_orders_lke(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.ftl_list_button,
                           do_assert=True, wait="lst")
    base.click_button(base.reset_button, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.deferred_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.regular_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКП. Тест сортировок списков рейсов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_sorting_orders_lkp(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.order_hover_lkp, click_to=sidebar.ftl_list_button_lkp,
                           do_assert=True, wait="lst")
    base.click_button(base.reset_button, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЗ. Тест сортировок списка грузомест по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_sorting_cargo_place_lkz(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    base.click_button(base.reset_button, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списка грузомест по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_sorting_cargo_place_lke(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button_lke,
                           do_assert=True, wait="lst")
    base.click_button(base.reset_button, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЗ. Тест сортировок списка подрядчиков по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_sorting_contractor_lkz(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списков контрагентов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_sorting_contractor_lke(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКП. Тест сортировок списка заказчиков по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_sorting_contractor_lkp(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЗ. Тест сортировок списка реестров по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_sorting_registries_lkz(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.click_button(sidebar.registries_list_button_lkz, do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списков реестров по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_sorting_registries_lke(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.reg_client_create_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.reg_producer_create_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.registries_client_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.registries_producer_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКП. Тест сортировок списков реестров по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_sorting_registries_lkp(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.reg_client_create_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.registries_list_button_lkp,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЗ. Тест сортировок списков документов и застрахованных рейсов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_sorting_documents_lkz(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.transport_doc_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.insurers_list_button,
                           do_assert=True, wait="lst")

    insurers_list = InsurersList(base.driver)
    insurers_list.click_button(insurers_list.insurer_energy_inn)

    insurer = Insurer(base.driver)
    insurer.click_button(insurer.insured_orders_list, wait="lst")
    insurer.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списков документов и застрахованных рейсов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_sorting_documents_lke(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.transport_doc_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.verification_doc_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.insurers_list_button_lke,
                           do_assert=True, wait="lst")

    insurers_list = InsurersList(base.driver)
    insurers_list.click_button(insurers_list.insurer_energy_inn)

    insurer = Insurer(base.driver)
    insurer.click_button(insurer.insured_orders_list, wait="lst")
    insurer.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКП. Тест сортировок списков документов и застрахованных рейсов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_sorting_documents_lkp(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.transport_doc_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.verification_doc_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.insurers_list_button,
                           do_assert=True, wait="lst")

    insurers_list = InsurersList(base.driver)
    insurers_list.click_button(insurers_list.insurer_energy_inn)

    insurer = Insurer(base.driver)
    insurer.click_button(insurer.insured_orders_list, wait="lst")
    insurer.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЗ. Тест сортировок списков адресов и тарифов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_sorting_tariff_point_lkz(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списков адресов и тарифов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_sorting_tariff_point_lke(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКП. Тест сортировок списка тарифов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_sorting_tariff_lkp(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЗ. Тест сортировок списка пользователей по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_sorting_employee_lkz(base_fixture, domain):
    base, sidebar = base_fixture

    profile = Profile(base.driver)
    profile.click_button(sidebar.profile_button, do_assert=True)
    profile.click_button(profile.users_tab, do_assert=True)
    profile.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списков водителей, специалистов и пользователей по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_sorting_employee_lke(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.loaders_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    profile = Profile(base.driver)
    profile.click_button(sidebar.profile_button, do_assert=True)
    profile.click_button(profile.users_tab, do_assert=True)
    profile.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКП. Тест сортировок списков водителей, специалистов и пользователей по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_sorting_employee_lkp(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    profile = Profile(base.driver)
    profile.click_button(sidebar.profile_button, do_assert=True)
    profile.click_button(profile.users_tab, do_assert=True)
    profile.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списков транспортных средств по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_sorting_transport_lke(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tractors_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.trailers_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКП. Тест сортировок списков транспортных средств по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_sorting_transport_lkp(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tractors_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")

    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.trailers_list_button,
                           do_assert=True, wait="lst")
    base.click_multiple_buttons(base.sorting_button, num_clicks=3, wait="lst")
