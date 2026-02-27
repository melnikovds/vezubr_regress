import allure
import pytest
import time
import random
from pages.address_add_page import AddressAdd
from pages.address_list_page import AddressesList
from pages.filter_directory_page import Manual
from pages.setting_page import Settings


@allure.story("Critical path test")
@allure.feature('Редактирование настроек маршрутизации в Адресе')
@allure.description('ЛКЗ. Тест изменения полей маршрутизации, изменяем поля в табе "Настройки маршрутизации" ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_address_routing_one_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку адресов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                           do_assert=True, wait="lst")

    # Поиск нужного адреса
    fltr = Manual(base.driver)
    fltr.click_button(element_dict=fltr.reset)
    fltr.dropdown_without_input(fltr.filter_date_create, option_text='За все время')
    time.sleep(1)
    fltr.input_in_field(fltr.verified_address, value='Торцева, д 75', click_first=True)
    time.sleep(1)

    # Редактирование настроек маршрутизации у выбранного адреса
    lst = AddressesList(base.driver)
    lst.click_button(lst.first_address_link, wait="form")
    add = AddressAdd(base.driver)
    add.click_button(add.settings_tab)
    add.click_button(add.redact_routing)
    time.sleep(1)
    add.click_on_the_cross(add.cross_algorithm)
    time.sleep(1)
    add.click_and_select_with_arrows(add.time_calculation_algorithm, arrow_presses=2)
    time.sleep(1)
    a = str(base.random_value_int(5, 100))
    add.backspace_and_input(add.average_arrival_time, value=a, num=10)
    time.sleep(1)
    b = str(base.random_value_int(5, 100))
    add.backspace_and_input(add.average_departure_time, value=b, num=10)
    time.sleep(1)
    add.dropdown_without_input(add.routing_group, option_text='Утро')
    time.sleep(1)
    add.click_button(add.save_routing)
    time.sleep(1)

    # Обновление страницы
    add.refresh_page()
    time.sleep(5)

    add.verify_text_on_page(text=a)
    add.verify_text_on_page(text=b)
    add.verify_text_on_page(text='окна работы')

    add.click_button(add.redact_routing)
    time.sleep(1)
    add.click_on_the_cross(add.cross_algorithm)
    time.sleep(1)
    add.click_and_select_with_arrows(add.time_calculation_algorithm, arrow_presses=0)
    time.sleep(1)
    c = str(base.random_value_int(5, 100))
    add.backspace_and_input(add.average_arrival_time, value=c, num=10)
    time.sleep(1)
    d = str(base.random_value_int(5, 100))
    add.backspace_and_input(add.average_departure_time, value=d, num=10)
    time.sleep(1)
    add.dropdown_without_input(add.routing_group, option_text='Вечер')
    time.sleep(1)
    add.click_button(add.save_routing)
    time.sleep(1)

    # Обновление страницы
    add.refresh_page()
    time.sleep(5)

    add.verify_text_on_page(text=c)
    add.verify_text_on_page(text=d)
    add.verify_text_on_page(text='По нормативу')


@allure.story("Critical path test")
@allure.feature('Редактирование настроек маршрутизации в Адресе')
@allure.description('ЛКЗ. Тест изменения полей маршрутизации, изменяем поля в табе "График Приёма/Работы" ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_address_routing_two_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку адресов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                           do_assert=True, wait="lst")

    # Поиск нужного адреса
    fltr = Manual(base.driver)
    fltr.click_button(element_dict=fltr.reset)
    fltr.dropdown_without_input(fltr.filter_date_create, option_text='За все время')
    time.sleep(1)
    fltr.input_in_field(fltr.name_address, value='график', click_first=True)
    time.sleep(1)

    # Редактирование графика у выбранного адреса
    lst = AddressesList(base.driver)
    lst.click_button(lst.first_address_link, wait="form")
    add = AddressAdd(base.driver)
    add.click_button(add.schedule_tab)
    time.sleep(1)
    add.click_button(add.schedule_edit)
    time.sleep(1)
    add.click_button(add.monday_add)
    time.sleep(1)
    add.input_in_field(add.fill_monday, value='11351245',click_first=True)
    time.sleep(1)
    add.click_button(add.tuesday_add_one)
    add.input_in_field(add.fill_tuesday_one, value='06280755',click_first=True)
    time.sleep(1)
    add.click_button(add.tuesday_add_two)
    add.input_in_field(add.fill_tuesday_two, value='20372152',click_first=True)
    time.sleep(1)
    add.click_button(add.save_schedule_edit)
    time.sleep(1)
    add.click_button(add.settings_tab)

    add.refresh_page()
    time.sleep(3)

    # Проверяем наличие созданного графика работы
    add.click_button(add.schedule_tab)
    add.verify_text_on_page(text='11:35 - 12:45')
    add.verify_text_on_page(text='06:28 - 07:55')
    add.verify_text_on_page(text='20:37 - 21:52')

    # Удаляем созданный график работы
    add.click_button(add.schedule_edit)
    time.sleep(1)
    add.move_to_element(add.fill_monday)
    add.click_on_the_cross(add.cross_one)
    time.sleep(1)
    add.move_to_element(add.tuesday_add_one)
    add.click_on_the_cross(add.cross_two)
    time.sleep(1)
    add.move_to_element(add.tuesday_add_two)
    add.click_on_the_cross(add.cross_three)
    time.sleep(1)
    add.click_button(add.save_schedule_edit)
    time.sleep(1)
    add.click_button(add.settings_tab)

    add.refresh_page()
    time.sleep(3)

    # Проверяем отсутствие созданного графика работы
    add.click_button(add.schedule_tab)
    add.verify_text_on_page(text='11:35 - 12:45', should_exist=False)
    add.verify_text_on_page(text='06:28 - 07:55', should_exist=False)
    add.verify_text_on_page(text='20:37 - 21:52', should_exist=False)


@allure.story("Critical path test")
@allure.feature('Создание группы Адресов')
@allure.description('ЛКЗ. Создание и редактирование группы адресов ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_address_group_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    sidebar.click_button(sidebar.settings_button, do_assert=True)
    # Переход к настройкам
    settings = Settings(base.driver)
    settings.click_button(settings.settings_subdivision)
    time.sleep(2)
    # settings.move_to_element(settings.addresses_subsection)
    settings.scroll_to_element(settings.addresses_subsection)
    # settings.click_button(settings.addresses_subsection)
    time.sleep(1)
    settings.click_button(settings.addresses_subsection)
    time.sleep(1)

    # Создание группы
    settings.click_button(settings.create_group)
    time.sleep(1)
    settings.input_in_field(settings.name_group_rus, value='День')
    settings.input_in_field(settings.name_group_eng, value='Day')
    settings.click_button(settings.save_group)
    time.sleep(1)
    settings.click_button(settings.add_confirm)

    settings.reload_page()
    time.sleep(3)

    settings.scroll_to_element(settings.addresses_subsection)
    settings.click_button(settings.addresses_subsection)
    time.sleep(1)
    settings.verify_text_on_page(text='День')
    settings.verify_text_on_page(text='Day')

    # Редактирование группы
    settings.click_button(settings.edit_group)
    time.sleep(1)
    settings.backspace_and_input(settings.name_group_rus, value='Ночь', num=10)
    settings.backspace_and_input(settings.name_group_eng, value='Night', num=10)
    settings.click_button(settings.save_group)
    time.sleep(1)

    settings.reload_page()
    time.sleep(3)

    settings.scroll_to_element(settings.addresses_subsection)
    settings.click_button(settings.addresses_subsection)
    time.sleep(1)
    settings.verify_text_on_page(text='Ночь')
    settings.verify_text_on_page(text='Night')

    # Удаление группы
    settings.click_button(settings.delete_group)
    time.sleep(1)
    settings.click_button(settings.reject_delete)
    time.sleep(1)
    settings.click_button(settings.delete_group)
    time.sleep(1)
    settings.click_button(settings.accept_delete)
    time.sleep(1)
    settings.click_button(settings.add_del)
    time.sleep(1)

    settings.reload_page()
    time.sleep(3)

    settings.scroll_to_element(settings.addresses_subsection)
    settings.click_button(settings.addresses_subsection)
    time.sleep(1)
    settings.verify_text_on_page(text='Ночь', should_exist=False)
    settings.verify_text_on_page(text='Night', should_exist=False)


@allure.story("Critical path test")
@allure.feature('Редактирование настроек маршрутизации в Адресе')
@allure.description('ЛКЗ. Тест изменения полей маршрутизации, изменяем поле "Приоритет адреса" ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_address_routing_three_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку адресов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                           do_assert=True, wait="lst")

    # Поиск нужного адреса
    fltr = Manual(base.driver)
    fltr.click_button(element_dict=fltr.reset)
    fltr.dropdown_without_input(fltr.filter_date_create, option_text='За все время')
    time.sleep(1)
    fltr.input_in_field(fltr.verified_address, value='Судостроительная, д 12', click_first=True)
    time.sleep(1)

    # Редактирование приоритета у выбранного адреса
    lst = AddressesList(base.driver)
    lst.click_button(lst.first_address_link, wait="form")
    add = AddressAdd(base.driver)
    add.click_button(add.settings_tab)
    add.click_button(add.redact_routing)
    time.sleep(2)
    a = random.randint(20, 50)
    add.backspace_and_input_int(add.address_priority, value=a, num=10)
    add.click_button(add.save_routing)
    time.sleep(1)

    # Проверяем что изменения применились
    add.refresh_page()
    time.sleep(5)
    p = str(a)
    add.verify_text_on_page(text=p)
































    






