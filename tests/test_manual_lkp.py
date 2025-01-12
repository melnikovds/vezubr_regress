import allure
import pytest
import time
from pages.manual_page import Manual

@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description("ЛКЗ Тест фильтра 'Тарифы' в разделе справочники")
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True) # Параметризация роли
def test_tariff_directory_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # переход к списку тарифов
    base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                        do_assert=True, wait='lst')

    add = Manual(base.driver)
    # проверка фильтра "Название тарифа"
    add.input_in_field(add.tariff_name, value='20241204172', click_first=True)
    time.sleep(2)
    add.verify_text_on_page(text='LTL-20241204172745', should_exist=True)
    add.verify_text_on_page(text='ГГ-20241210025702', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.tariff_name, value='')
    time.sleep(2)

    # проверка №1 фильтра "Статус"
    add.dropdown_without_input(add.tariff_status, option_text='Не активный')
    time.sleep(2)
    add.verify_text_on_page(text='ПРР-20241209212258', should_exist=True)
    add.verify_text_on_page(text='ПБ-20241205233932', should_exist=False)
    time.sleep(2)

    # проверка №2 фильтра "Статус"
    add.dropdown_without_input(add.tariff_status, option_text='Активный')
    time.sleep(2)
    add.verify_text_on_page(text='ПЧ-20241209211124', should_exist=True)
    add.verify_text_on_page(text='ПРР-20241205194647', should_exist=False)
    time.sleep(2)

    # проверка №1 фильтра с несколькими значениями
    add.input_in_field(add.tariff_name, value='ПРР-20241209183834', click_first=True)
    add.dropdown_without_input(add.tariff_status, option_text='Не активный')
    time.sleep(2)
    add.find_text_on_page(text='83834', occurrences=3)
    add.verify_text_on_page(text='10.12.2024 00:11', should_exist=True)
    add.verify_text_on_page(text='ПРР-20241209145054', should_exist=False)
    add.verify_text_on_page(text='212151', should_exist=False)
    time.sleep(2)

    # очистка поля "Название тарифа"
    add.backspace_and_input(add.tariff_name, value='')

    # проверка №2 фильтра с несколькими значениями
    add.input_in_field(add.tariff_name, value='ПЧ-20240716214624', click_first=True)
    add.dropdown_without_input(add.tariff_status, option_text='Активный')
    time.sleep(2)
    add.find_text_on_page(text='624', occurrences=3)
    add.verify_text_on_page(text='10.12.2024 00:11', should_exist=False)
    add.verify_text_on_page(text='ПРР-20241209145054', should_exist=False)
    add.verify_text_on_page(text='212151', should_exist=False)
    time.sleep(2)

    # очистка поля "Название тарифа"
    add.backspace_and_input(add.tariff_name, value='')

    # Конец теста
