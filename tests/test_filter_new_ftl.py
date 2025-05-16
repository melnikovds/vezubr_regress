import allure
import pytest
from pages.filters_new_ftl_page import NewFtlFilters


@allure.story("Extended path test")
@allure.feature('Фильтры новых доставок груза')
@allure.description('ЛКЗ, Тестирование фильтров новые доставки груза')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_filters_new_ftl_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.cdr_active_list_button,
                           do_assert=True, wait="lst")

    add = NewFtlFilters(base.driver)

    add.click_button(add.clear)


