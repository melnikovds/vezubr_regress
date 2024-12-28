import allure
import pytest
from pages.manual_page import Manual

@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description('ЛКЗ Тест фильтра Адреса в разделе справочники')
@pytest.mark.paramtrize('base_fixture', ['lkz'], indirect=True) # Параметризация роли
def test_address_directory_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture


    base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                        do_assert=True, wait='lst')

    manual = Manual(base.driver)

    manual.click_button(manual.filter_date_create, do_assert=True)


