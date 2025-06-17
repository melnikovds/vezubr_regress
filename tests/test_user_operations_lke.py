import time
import allure
import pytest
from pages.profile_page import Profile
from pages.user_add_page import User


@allure.story("Extended test")
@allure.feature('Назначение пользователя')
@allure.description('ЛКЭ. Тест назначения пользователя в Группу')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_user_group_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к профилю
    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    # Переход на вкладку пользователей
    profile.click_button(profile.users_tab, do_assert=True)

    # Фильтрация пользователей по фамилии
    profile.input_in_field(profile.surname_filter,value='Ф-20250526230920')
    time.sleep(1)

    # Переход к профилю первого пользователя в списке
    profile.click_button(profile.user_link, wait="form")
    time.sleep(1)

    user = User(base.driver)
    # Редактирование данных пользователя
    user.click_button(user.user_edit_button, wait="form")
    time.sleep(1)

    # Выбор группы пользователя
    user.dropdown_without_input(user.user_group_select, "группа Икс")
    time.sleep(1)
    user.click_button(user.phone_input)
    # Сохранение изменений
    user.click_button(user.save_edit_user_button, do_assert=True)
    time.sleep(1)
    # Подтверждение изменений
    user.click_button(user.confirm_add_button)
    time.sleep(1)

    profile.reload_page()
    time.sleep(5)

    # Проверка наличия изменений
    profile.input_in_field(profile.surname_filter,value='Ф-20250526230920')
    time.sleep(1)
    profile.click_button(profile.user_link, wait="form")
    time.sleep(3)
    profile.find_text_on_page(text="группа Икс", occurrences=2)

    # Удаляем группу
    user.click_button(user.user_edit_button, wait="form")
    time.sleep(1)
    user.click_button(user.cross)
    time.sleep(1)
    user.click_button(user.phone_input)
    # Сохранение изменений
    user.click_button(user.save_edit_user_button, do_assert=True)
    time.sleep(1)
    # Подтверждение изменений
    user.click_button(user.confirm_add_button)
    time.sleep(1)


    # Проверка наличия изменений
    profile.input_in_field(profile.surname_filter,value='Ф-20250526230920')
    time.sleep(1)
    profile.click_button(profile.user_link, wait="form")
    time.sleep(3)
    profile.find_text_on_page(text="группа Икс",occurrences=0)
    time.sleep(1)


@allure.story("Extended test")
@allure.feature('Назначение пользователя')
@allure.description('ЛКЭ. Тест назначения пользователя в Подразделение')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_user_subdivision_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к профилю
    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    # Переход на вкладку пользователей
    profile.click_button(profile.users_tab, do_assert=True)

    # Фильтрация пользователей по фамилии
    profile.input_in_field(profile.surname_filter,value='Ф-20250526230920')
    time.sleep(1)

    # Переход к профилю первого пользователя в списке
    profile.click_button(profile.user_link, wait="form")
    time.sleep(1)

    user = User(base.driver)
    # Редактирование данных пользователя
    user.click_button(user.user_edit_button, wait="form")
    time.sleep(1)

    # Выбор подразделения пользователя
    user.dropdown_without_input(user.user_subdivision_select, "подразделение Лямбда")

    # Сохранение изменений
    user.click_button(user.save_edit_user_button, do_assert=True)
    time.sleep(1)
    # Подтверждение изменений
    user.click_button(user.confirm_add_button)
    time.sleep(1)

    profile.reload_page()
    time.sleep(5)

    # Проверка наличия изменений
    profile.input_in_field(profile.surname_filter,value='Ф-20250526230920')
    time.sleep(1)
    profile.click_button(profile.user_link, wait="form")
    time.sleep(3)
    profile.find_text_on_page(text="подразделение Лямбда", occurrences=2)

    # Смена подразделения
    user.click_button(user.user_edit_button, wait="form")
    time.sleep(1)
    user.click_and_select_with_arrows(user.user_subdivision_select, arrow_presses=2)
    time.sleep(1)
    # Сохранение изменений
    user.click_button(user.save_edit_user_button, do_assert=True)
    time.sleep(1)
    # Подтверждение изменений
    user.click_button(user.confirm_add_button)
    time.sleep(1)

    # Проверка наличия изменений
    profile.input_in_field(profile.surname_filter,value='Ф-20250526230920')
    time.sleep(1)
    profile.click_button(profile.user_link, wait="form")
    time.sleep(3)
    profile.find_text_on_page(text="подразделение Лямбда", occurrences=0)
    time.sleep(1)


@allure.story("Extended test")
@allure.feature('Назначение пользователя')
@allure.description('ЛКЭ. Тест назначения пользователя к внутр. ПВ')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_user_contractor_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к профилю
    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    # Переход на вкладку пользователей
    profile.click_button(profile.users_tab, do_assert=True)

    # Фильтрация пользователей по фамилии
    profile.input_in_field(profile.surname_filter,value='Ф-20250526230920')
    time.sleep(1)

    # Переход к профилю первого пользователя в списке
    profile.click_button(profile.user_link, wait="form")
    time.sleep(1)

    user = User(base.driver)
    # Клик по кнопке добавления ответственности
    user.click_button(user.add_responsible_button, wait="lst")
    # Переход на вкладку "Перевозчики"
    user.click_button(user.producer_tab, wait="lst")
    time.sleep(2)
    # Назначение ответственности за первого в списке перевозчика
    user.click_button(user.first_producer_on_checkbox)
    # Подтверждение назначения ответственности
    user.click_button(user.confirm_responsible_button, wait="lst")





































