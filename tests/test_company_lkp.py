import time

import allure
import pytest

from pages.settings_company_page import Company
from pages.setting_page import Settings


@allure.story("Extended path test")
@allure.feature('Тестирование подразделений')
@allure.description('ЛКП, Создание подразделения')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_create_subdivision_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    sidebar.click_button(sidebar.settings_button, do_assert=True)
    # Переход к настройкам
    settings = Settings(base.driver)
    settings.click_button(settings.settings_subdivision)
    time.sleep(2)
    # Открываем подразделения и создаем
    add = Company(base.driver)
    add.move_to_element(add.muve)
    time.sleep(2)
    add.click_button(add.subdivision)
    time.sleep(2)
    add.click_button(add.add_subdivision)
    add.input_in_field(add.name_subdivision, "подразделение ОРКИ")
    add.input_in_field(add.id_subdivision, "007")
    add.click_button(add.save_subdivision)
    time.sleep(2)
    add.click_button(add.ok_button)


@allure.story("Extended path test")
@allure.feature('Тестирование подразделений')
@allure.description('ЛКП, Назначение пользователя в подразделение')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_accept_user_to_division_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    # Открываем настройки профиля
    sidebar.click_button(sidebar.profile_button, do_assert=True)
    time.sleep(2)
    # добавляем пользователя
    add = Company(base.driver)
    add.click_button(add.click_users_lkz_lkp)
    add.click_button(add.edit_user, wait="form")
    add.dropdown_without_input(add.change_user_to_subdivision, "подразделение ОРКИ")
    add.click_button(add.click_save)
    time.sleep(2)
    add.click_button(add.click_ok)


@allure.story("Extended path test")
@allure.feature('Тестирование подразделений')
@allure.description('ЛКП, Редактирование и удаление подразделения')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_edit_subdivision_lkz(base_fixture, domain):
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
    add.backspace_and_input(add.name_subdivision, "Звездный десант")
    add.backspace_and_input(add.id_subdivision, "0055")
    add.click_button(add.save_subdivision)
    add.click_button(add.del_subdivision)
    add.click_button(add.del_confirm)
    time.sleep(2)
    add.click_button(add.ok_button)
