import allure
import pytest
from pages.custom_page import Settings, CustomFieldParam


@allure.story("Extended path test")
@allure.feature('Маршрутизация грузомест')
@allure.description('ЛКП. ')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_create_custom_field_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    sidebar.click_button(sidebar.settings_button, do_assert=True)
    settings = Settings(base.driver)
    settings.click_button(settings.custom_field)
    settings.click_button(settings.add_field)
    add_param = CustomFieldParam(base.driver)
    add_param.input_in_field(add_param.add_ru, "Новое поле")
    add_param.input_in_field(add_param.add_en, "new field")
    add_param.dropdown_without_input(add_param.add_role, "Договор")
    add_param.dropdown_without_input(add_param.add_type, "Числовое значение")
    add_param.click_button(add_param.click_save)
    add_param.click_button(add_param.click_ok)


@allure.story("Extended path test")
@allure.feature('Маршрутизация грузомест')
@allure.description('ЛКП. ')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_edit_custom_field_lkp(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.click_button(sidebar.settings_button, do_assert=True)
    settings = Settings(base.driver)
    settings.click_button(settings.custom_field)
    settings.click_button(settings.edit_field)
    add_param = CustomFieldParam(base.driver)
    add_param.backspace_and_input(add_param.add_ru, "Новое поле2")
    add_param.backspace_and_input(add_param.add_en, "new field2")
    add_param.dropdown_without_input(add_param.add_role, "Заявка")
    add_param.dropdown_without_input(add_param.add_type, "Ввод нескольких значений")
    add_param.click_button(add_param.click_save)
    add_param.click_button(add_param.click_ok)


@allure.story("Extended path test")
@allure.feature('Маршрутизация грузомест')
@allure.description('ЛКП. ')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_delete_custom_field_lkp(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.click_button(sidebar.settings_button, do_assert=True)
    settings = Settings(base.driver)
    settings.click_button(settings.custom_field)
    settings.click_button(settings.delete_field)
    settings.click_button(settings.delete_ok)


@allure.story("Extended path test")
@allure.feature('Маршрутизация грузомест')
@allure.description('ЛКП. ')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_create_custom_field2_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    sidebar.click_button(sidebar.settings_button, do_assert=True)
    settings = Settings(base.driver)
    settings.click_button(settings.custom_field)
    settings.click_button(settings.add_field)
    add_param = CustomFieldParam(base.driver)
    add_param.input_in_field(add_param.add_ru, "Новое поле")
    add_param.input_in_field(add_param.add_en, "new field")
    add_param.dropdown_without_input(add_param.add_role, "Контрагент")
    add_param.dropdown_without_input(add_param.add_type, "Текстовое значение")
    add_param.click_button(add_param.click_save)
    add_param.click_button(add_param.click_ok)


@allure.story("Extended path test")
@allure.feature('Маршрутизация грузомест')
@allure.description('ЛКП. ')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_edit_custom_field2_lkp(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.click_button(sidebar.settings_button, do_assert=True)
    settings = Settings(base.driver)
    settings.click_button(settings.custom_field)
    settings.click_button(settings.edit_field)
    add_param = CustomFieldParam(base.driver)
    add_param.backspace_and_input(add_param.add_ru, "Новое поле2")
    add_param.backspace_and_input(add_param.add_en, "new field2")
    add_param.dropdown_without_input(add_param.add_role, "Рейс")
    add_param.dropdown_without_input(add_param.add_type, "Выбор из нескольких значений")
    add_param.click_button(add_param.click_meaning)
    add_param.input_in_field(add_param.unic_n, "1499")
    add_param.input_in_field(add_param.named_n, "1488")
    add_param.click_button(add_param.confirm_add)
    add_param.click_button(add_param.click_save)
    add_param.click_button(add_param.click_ok)


@allure.story("Extended path test")
@allure.feature('Маршрутизация грузомест')
@allure.description('ЛКП. ')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_delete_custom_field2_lkp(base_fixture, domain):
    base, sidebar = base_fixture

    sidebar.click_button(sidebar.settings_button, do_assert=True)
    settings = Settings(base.driver)
    settings.click_button(settings.custom_field)
    settings.click_button(settings.delete_field)
    settings.click_button(settings.delete_ok)

