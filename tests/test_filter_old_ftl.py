import allure
import pytest

from pages.filters_old_order_page import OldFilters


@allure.story("Extended path test")
@allure.feature('Фильтры старых рейсов')
@allure.description('ЛКЭ, Тестирование фильтров активных ФТЛ')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_filters_old_ftl_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру

    base, sidebar = base_fixture
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_active_list_button,
                           do_assert=True, wait="lst")

    add = OldFilters(base.driver)
    # фильтр номер заявки
    add.click_button(add.clear)
    add.input_in_field(add.application_number, "13")
    add.verify_text_on_page("25-13-2447")
    add.input_in_field(add.application_number, "")

    # фильтр по статусу заявки
