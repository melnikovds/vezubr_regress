import allure
import pytest

from pages.insurer_page import Insurer
from pages.insurers_list_page import InsurersList
from pages.profile_page import Profile


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списков заявок по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_sorting_requests_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку активных FTL заявок
    base.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_active_list_button,
                        do_assert=True, wait="lst")
    # Клик по кнопке сброса фильтров
    base.click_button(base.reset_button, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=13, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКП. Тест сортировок списков заявок по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_sorting_requests_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку активных FTL заявок
    base.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_active_list_button,
                        do_assert=True, wait="lst")
    # Клик по кнопке сброса фильтров
    base.click_button(base.reset_button, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=12, num_clicks=3, wait="lst")

    # Переход к списку заявок на доставку груза
    base.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.cdr_active_list_button,
                        do_assert=True, wait="lst")
    # Клик по кнопке сброса фильтров
    base.click_button(base.reset_button, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=9, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЗ. Тест сортировок списков заявок по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_sorting_requests_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку активных FTL заявок
    base.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_active_list_button,
                        do_assert=True, wait="lst")
    # Клик по кнопке сброса фильтров
    base.click_button(base.reset_button, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=12, num_clicks=3, wait="lst")


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списков рейсов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_sorting_orders_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку FTL рейсов
    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.ftl_list_button,
                           do_assert=True, wait="lst")
    # Клик по кнопке сброса фильтров
    base.click_button(base.reset_button, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=24, num_clicks=3, wait="lst")

    # Переход к списку отложенных рейсов
    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.deferred_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=7, num_clicks=3, wait="lst")

    # Переход к списку регулярных рейсов
    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.regular_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=11, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКП. Тест сортировок списков рейсов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_sorting_orders_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку FTL рейсов
    sidebar.move_and_click(move_to=sidebar.order_hover_lkp, click_to=sidebar.ftl_list_button_lkp,
                           do_assert=True, wait="lst")
    # Клик по кнопке сброса фильтров
    base.click_button(base.reset_button, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=20, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЗ. Тест сортировок списков рейсов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_sorting_orders_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку FTL рейсов
    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.ftl_list_button,
                           do_assert=True, wait="lst")
    # Клик по кнопке сброса фильтров
    base.click_button(base.reset_button, wait="lst")

    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=20, num_clicks=3, wait="lst")

    # Переход к списку отложенных рейсов
    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.deferred_list_button,
                           do_assert=True, wait="lst")

    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=7, num_clicks=3, wait="lst")

    # Переход к списку регулярных рейсов
    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.regular_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=11, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списка грузомест по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_sorting_cargo_place_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку грузомест
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    # Клик по кнопке сброса фильтров
    base.click_button(base.reset_button, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=19, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЗ. Тест сортировок списка грузомест по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_sorting_cargo_place_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку грузомест
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    # Клик по кнопке сброса фильтров
    base.click_button(base.reset_button, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=19, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списков контрагентов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_sorting_contractor_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку заказчиков
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=7, num_clicks=3, wait="lst")

    # Переход к списку подрядчиков
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=7, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКП. Тест сортировок списка заказчиков по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_sorting_contractor_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку заказчиков
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")

    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=7, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЗ. Тест сортировок списка подрядчиков по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_sorting_contractor_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку подрядчиков
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")

    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=7, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списков реестров по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_sorting_registries_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку формирования реестров для ГВ
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.reg_client_create_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=16, num_clicks=3, wait="lst")

    # Переход к списку формирования реестров от ПВ
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.reg_producer_create_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=16, num_clicks=3, wait="lst")

    # Переход к списку реестров для ГВ
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.registries_client_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=8, num_clicks=3, wait="lst")

    # Переход к списку реестров от ПВ
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.registries_producer_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=7, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКП. Тест сортировок списков реестров по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_sorting_registries_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку формирования реестров для ГВ
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.reg_client_create_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=16, num_clicks=3, wait="lst")

    # Переход к списку реестров для ГВ
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.registries_list_button_lkp,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=8, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЗ. Тест сортировок списка реестров по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_sorting_registries_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку реестров от ПВ
    sidebar.click_button(sidebar.registries_list_button_lkz, do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=7, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списков документов и застрахованных рейсов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_sorting_documents_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку перевозочных документов
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.transport_doc_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=4, num_clicks=3, wait="lst")

    # Переход к списку проверка докуметнов
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.verification_doc_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=19, num_clicks=3, wait="lst")

    # Переход к списку страховых компаний
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.insurers_list_button_lke,
                           do_assert=True, wait="lst")

    insurers_list = InsurersList(base.driver)
    # Клик по страховщику с ИНН "insurer_energy_inn"
    insurers_list.click_button(insurers_list.insurer_energy_inn)

    insurer = Insurer(base.driver)
    # Переход к списку застрахаованные рейсы
    insurer.click_button(insurer.insured_orders_list, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    insurer.click_multiple_buttons(base.sorting_button, num_buttons=11, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКП. Тест сортировок списков документов и застрахованных рейсов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_sorting_documents_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку перевозочных документов
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.transport_doc_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=4, num_clicks=3, wait="lst")

    # Переход к списку проверка докуметнов
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.verification_doc_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=19, num_clicks=3, wait="lst")

    # Переход к списку страховых компаний
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.insurers_list_button,
                           do_assert=True, wait="lst")

    insurers_list = InsurersList(base.driver)
    # Клик по страховщику с ИНН "insurer_energy_inn"
    insurers_list.click_button(insurers_list.insurer_energy_inn)

    insurer = Insurer(base.driver)
    # Переход к списку застрахаованные рейсы
    insurer.click_button(insurer.insured_orders_list, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    insurer.click_multiple_buttons(base.sorting_button, num_buttons=11, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЗ. Тест сортировок списков документов и застрахованных рейсов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_sorting_documents_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку перевозочных документов
    sidebar.click_button(sidebar.transport_doc_list_button, do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=4, num_clicks=3, wait="lst")

    # Переход к списку страховых компаний
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.insurers_list_button,
                           do_assert=True, wait="lst")

    insurers_list = InsurersList(base.driver)
    # Клик по страховщику с ИНН "insurer_energy_inn"
    insurers_list.click_button(insurers_list.insurer_energy_inn)

    insurer = Insurer(base.driver)
    # Переход к списку застрахаованные рейсы
    insurer.click_button(insurer.insured_orders_list, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    insurer.click_multiple_buttons(base.sorting_button, num_buttons=11, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списков адресов и тарифов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_sorting_tariff_point_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку адресов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=16, num_clicks=3, wait="lst")

    # Переход к списку тарифов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=5, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКП. Тест сортировок списка тарифов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_sorting_tariff_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку тарифов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=5, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЗ. Тест сортировок списков адресов и тарифов по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_sorting_tariff_point_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку адресов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=15, num_clicks=3, wait="lst")

    # Переход к списку тарифов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=5, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списков водителей, специалистов и пользователей по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_sorting_employee_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку водтелей
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=12, num_clicks=3, wait="lst")
    
    # Переход к списку специалистов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.loaders_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=9, num_clicks=3, wait="lst")
    
    profile = Profile(base.driver)
    # Переход в профиль
    profile.click_button(sidebar.profile_button, do_assert=True)
    # Переход на вкладку пользователей
    profile.click_button(profile.users_tab, do_assert=True)
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    profile.click_multiple_buttons(base.sorting_button, num_buttons=7, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКП. Тест сортировок списков водителей, специалистов и пользователей по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_sorting_employee_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку водтелей
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=11, num_clicks=3, wait="lst")
    


    
    profile = Profile(base.driver)
    # Переход в профиль
    profile.click_button(sidebar.profile_button, do_assert=True)
    # Переход на вкладку пользователей
    profile.click_button(profile.users_tab, do_assert=True)
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    profile.click_multiple_buttons(base.sorting_button, num_buttons=7, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЗ. Тест сортировок списка пользователей по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_sorting_employee_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    profile = Profile(base.driver)
    # Переход в профиль
    profile.click_button(sidebar.profile_button, do_assert=True)
    # Переход на вкладку пользователей
    profile.click_button(profile.users_tab, do_assert=True)
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    profile.click_multiple_buttons(base.sorting_button, num_buttons=7, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списков транспортных сведств по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_sorting_transport_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку монорамных ТС
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=17, num_clicks=3, wait="lst")

    # Переход к списку тягачей
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tractors_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=6, num_clicks=3, wait="lst")

    # Переход к списку полуприцепов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.trailers_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=16, num_clicks=3, wait="lst")
    # Конец теста


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКП. Тест сортировок списков транспортных сведств по всем столбцам')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_sorting_transport_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку монорамных ТС
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=16, num_clicks=3, wait="lst")

    # Переход к списку тягачей
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tractors_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=5, num_clicks=3, wait="lst")

    # Переход к списку полуприцепов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.trailers_list_button,
                           do_assert=True, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=15, num_clicks=3, wait="lst")
    # Конец теста
