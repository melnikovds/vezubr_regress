import time

import allure
import pytest

from pages.contractor_page import Contractor
from pages.filter_page import Contractors
from pages.producers_list_page import ProducersList
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
    profile.input_in_field(profile.surname_filter, value='Ф-20250526230920')
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
    profile.input_in_field(profile.surname_filter, value='Ф-20250526230920')
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
    profile.input_in_field(profile.surname_filter, value='Ф-20250526230920')
    time.sleep(1)
    profile.click_button(profile.user_link, wait="form")
    time.sleep(3)
    profile.find_text_on_page(text="группа Икс", occurrences=0)
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
    profile.input_in_field(profile.surname_filter, value='Ф-20250526230920')
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
    profile.input_in_field(profile.surname_filter, value='Ф-20250526230920')
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
    profile.input_in_field(profile.surname_filter, value='Ф-20250526230920')
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
    profile.input_in_field(profile.surname_filter, value='Ф-20250526230920')
    time.sleep(1)

    # Переход к профилю первого пользователя в списке
    profile.click_button(profile.user_link, wait="form")
    time.sleep(1)

    user = User(base.driver)
    # Клик по кнопке добавления ответственности
    user.click_button(user.add_responsible_button)
    # Переход на вкладку "Перевозчики"
    user.click_button(user.producer_tab, wait="lst")
    time.sleep(2)
    user.input_in_field(user.filter_company, value='яндекс')
    time.sleep(2)
    # Назначение ответственности за первого в списке перевозчика
    user.click_button(user.first_producer_on_checkbox, wait_type='located')
    time.sleep(2)
    # Подтверждение назначения ответственности
    user.click_button(user.confirm_responsible_button, wait="lst")
    time.sleep(2)

    # Делегирование внутреннему ПВ
    user.dropdown_without_input(user.contractor_role_select, option_text='Подрядчик')
    user.click_button(user.choice_contractor, wait_type='located')
    user.click_button(user.delegate_responsibility_button)

    profile.input_in_field(profile.surname_filter, value='Ф-20250526230920')
    time.sleep(2)
    user.click_button(user.user_checkbox)
    time.sleep(1)
    user.click_button(user.confirm_responsible_button)
    time.sleep(1)

    # Переход к списку перевозчиков
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")

    ctr = Contractors(base.driver)
    ctr.input_in_field(ctr.contractor_name, value='яндекс')
    time.sleep(1)

    producer_list = ProducersList(base.driver)
    # Клик по первому в списке подрядчику
    producer_list.click_button(producer_list.first_producer, wait="lst")

    contractor = Contractor(base.driver)
    # Переход на вкладку настроек
    contractor.click_button(contractor.settings_tab)
    time.sleep(2)
    # Фильтрация пользователей по фамилии
    ctr.input_in_field(ctr.users_for_delegation, value='Ф-20250526230920')
    time.sleep(3)

    # Делегирование пользователю права управления ЛК
    contractor.click_button(contractor.user_checkbox_empty, 2)
    contractor.click_button(contractor.save_delegation_button, do_assert=True)
    contractor.click_button(contractor.ok_button)

    ctr.reload_page()
    time.sleep(3)
    ctr.move_to_element(ctr.users_for_delegation)
    time.sleep(1)
    ctr.click_button(ctr.cross_users_for_delegation)
    time.sleep(1)

    # Фильтрация пользователей по фамилии
    ctr.input_in_field(ctr.users_for_delegation, value='Ф-20250526230920')
    time.sleep(3)

    # Отмена делегирования пользователю
    contractor.click_button(contractor.user_checkbox_filled, 2)
    contractor.click_button(contractor.save_delegation_button, do_assert=True)
    contractor.click_button(contractor.ok_button)

    ctr.reload_page()
    time.sleep(3)

    # Переход к профилю
    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    # Переход на вкладку пользователей
    profile.click_button(profile.users_tab, do_assert=True)

    # Фильтрация пользователей по фамилии
    profile.input_in_field(profile.surname_filter, value='Ф-20250526230920')
    time.sleep(1)

    # Переход к профилю первого пользователя в списке
    profile.click_button(profile.user_link, wait="form")
    time.sleep(1)

    # отвязываем пользователя от ПВ
    user.dropdown_without_input(user.contractor_role_select, option_text='Подрядчик')
    time.sleep(1)
    user.click_button(user.choice_contractor, wait_type='located')
    user.click_button(user.off_responsibility_button)
    user.click_button(user.confirm_off_responsible_button)

    user.reload_page()
    time.sleep(3)

    user.verify_text_on_page(text='Яндекс', should_exist=False)
