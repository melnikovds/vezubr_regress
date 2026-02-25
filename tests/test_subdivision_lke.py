import time
import allure
import pytest
from pages.settings_company_page import Company
from pages.setting_page import Settings


@allure.story("Extended path test")
@allure.feature('Тестирование подразделений')
@allure.description('ЛКЭ, Создание подразделения')
@pytest.mark.order(1)
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_create_subdivision_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    sidebar.click_button(sidebar.settings_button, do_assert=True)
    # Переход к настройкам
    settings = Settings(base.driver)
    settings.click_button(settings.settings_subdivision)
    # Открываем подразделения и создаем
    add = Company(base.driver)
    add.scroll_to_element(add.muve)
    time.sleep(2)
    add.click_button(add.subdivision)
    time.sleep(2)
    add.click_button(add.add_subdivision)
    add.input_in_field(add.name_subdivision, "подразделение DNS")
    add.input_in_field(add.id_subdivision, "006")
    add.click_button(add.save_subdivision)
    time.sleep(2)
    add.click_button(add.ok_button, do_assert=True)


@allure.story("Extended path test")
@allure.feature('Тестирование подразделений')
@allure.description('ЛКЭ, Назначение пользователя в подразделение')
@pytest.mark.order(2)
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_accept_user_to_division_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    sidebar.click_button(sidebar.settings_button, do_assert=True)
    # Открываем настройки профиля
    settings = Settings(base.driver)
    settings.click_button(settings.profile_field)
    # добавляем пользователя
    add = Company(base.driver)
    add.click_button(add.click_users)
    add.click_button(add.edit_user, wait="form")
    add.dropdown_without_input(add.change_user_to_subdivision, "подразделение DNS")
    add.click_button(add.click_save)
    time.sleep(2)
    add.click_button(add.click_ok, do_assert=True)


@allure.story("Extended path test")
@allure.feature('Тестирование подразделений')
@allure.description('ЛКЭ, Редактирование и удаление подразделения')
@pytest.mark.order(3)
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_edit_subdivision_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    sidebar.click_button(sidebar.settings_button, do_assert=True)
    # Переход к настройкам
    settings = Settings(base.driver)
    settings.click_button(settings.settings_subdivision)
    # Изменение и удаление подразделения
    add = Company(base.driver)
    add.move_to_element(add.muve)
    add.click_button(add.subdivision)
    add.click_button(add.click_edit_subdivision)
    add.backspace_and_input(add.name_subdivision, "Управление перевозками")
    add.backspace_and_input(add.id_subdivision, "0044")
    add.click_button(add.save_subdivision)

    add.refresh_page()
    time.sleep(5)
    add.move_to_element(add.muve)
    add.click_button(add.subdivision)
    time.sleep(2)
    add.verify_text_on_page(text='Управление')

    add.click_button(add.del_subdivision)
    add.click_button(add.del_confirm)
    time.sleep(1)
    add.verify_text_on_page(text='Подразделение удалено')
    add.click_button(add.ok_button)
