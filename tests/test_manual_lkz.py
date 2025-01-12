import allure
import pytest
import time
from pages.manual_page import Manual

@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description("ЛКЗ Тест фильтра 'Адреса' в разделе справочники")
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True) # Параметризация роли
def test_address_directory_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку адресов
    base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                        do_assert=True, wait='lst')

    add = Manual(base.driver)
    # сброс фильтров
    add.click_button(element_dict=add.reset)

    # проверка фильтра "дата создания"
    add.dropdown_without_input(add.filter_date_create, option_text='За год')
    time.sleep(3)

    # проверка №1 фильтра "Подтвержденный адрес"
    add.input_in_field(add.verified_address, value='Ленина', click_first=True)
    time.sleep(1)
    add.verify_text_on_page(text='г Екатеринбург, пр-кт Ленина, д 68')
    add.verify_text_on_page(text='Зиминская', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.verified_address, value='')

    # проверка №2 фильтра "Подтвержденный адрес"
    add.backspace_and_input(add.verified_address, value='Великие Луки', click_first=True)
    time.sleep(1)
    add.verify_text_on_page(text='Винатовского')
    add.verify_text_on_page(text='Екатеринбург', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.verified_address, value='')

    # проверка №3 фильтра "Подтвержденный адрес"
    add.backspace_and_input(add.verified_address, value='Мурманск', click_first=True)
    time.sleep(1)
    add.verify_text_on_page(text='Плато')
    add.verify_text_on_page(text='Луки', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.verified_address, value='')

    # проверка №4 фильтра "Подтвержденный адрес"
    add.backspace_and_input(add.verified_address, value='Винатовского', click_first=True)
    time.sleep(1)
    add.verify_text_on_page(text='Великие Луки')
    add.verify_text_on_page(text='Мурманск', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.verified_address, value='')

    # проверка №5 фильтра "Подтвержденный адрес"
    add.backspace_and_input(add.verified_address, value='Плато', click_first=True)
    time.sleep(1)
    add.verify_text_on_page(text='Мурманск')
    add.verify_text_on_page(text='Ленина', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.verified_address, value='')

    # проверка №1 фильтра "Название адреса"
    add.input_in_field(add.name_address, value='тгл', wait='lst')
    add.verify_text_on_page(text='Нижний Тагил')
    add.verify_text_on_page(text='Магнитогорск', should_exist=False)
    add.backspace_and_input(add.name_address, value='')
    time.sleep(1)

    # проверка №2 фильтра "Название адреса"
    add.input_in_field(add.name_address, value='мрмск', wait='lst')
    add.verify_text_on_page(text='Мурманск')
    add.verify_text_on_page(text='Тагил', should_exist=False)
    add.backspace_and_input(add.name_address, value='')
    time.sleep(1)

    # проверка фильтра "Отправитель/Получатель"
    add.input_in_field(add.sender_recipient, value='Авангард', wait='lst')
    add.verify_text_on_page('Лиговский')
    add.verify_text_on_page(text='Монолит', should_exist=False)
    add.backspace_and_input(add.sender_recipient, value='')

    # проверка №1 фильтра  "Статус"
    add.dropdown_without_input(add.status, option_text='Активный')
    time.sleep(3)
    add.verify_text_on_page('Россия, Псковская обл, г Великие Луки, ул Винатовского, д 28')
    time.sleep(1)
    add.verify_text_on_page(text='Ясный', should_exist=False)
    time.sleep(1)

    # проверка №2 фильтра  "Статус"
    add.dropdown_without_input(add.status, option_text='Неактивный')
    time.sleep(3)
    add.verify_text_on_page('86')
    time.sleep(1)
    add.verify_text_on_page(text='Пышма', should_exist=False)
    time.sleep(1)

    # сброс фильтров
    add.click_button(element_dict=add.reset)

    # проверка фильтра регион
    add.dropdown_without_input(add.region, option_text='Псковская область')
    time.sleep(1)
    add.verify_text_on_page('Россия, Псковская обл, г Великие Луки, ул Винатовского, д 28')
    add.verify_text_on_page(text='Екатеринбург', should_exist=False)

    # сброс фильтров
    add.click_button(element_dict=add.reset)

    # проверка фильтра "Подтвердил"
    add.input_in_field(add.approved, value='auto@LKZ.com', wait='lst')
    add.verify_text_on_page('Винатовского')
    add.backspace_and_input(add.approved, value='')
    time.sleep(1)

    # проверка фильтра "Создал"
    add.input_in_field(add.created, value='auto@LKZ.com', wait='lst')
    add.verify_text_on_page('Плато')
    add.backspace_and_input(add.created, value='')
    time.sleep(1)

    # проверка фильтра "ID Адреса Партнёра"
    add.input_in_field(add.id_address, value='20241207174426')
    time.sleep(1)
    add.verify_text_on_page('Адрес-20241207174426')
    add.verify_text_on_page(text='5720', should_exist=False)
    add.backspace_and_input(add.id_address, value='')

    # сброс фильтров
    add.click_button(element_dict=add.reset)

    # создание фильтра с несколькими значениями
    add.input_in_field(add.approved, value='auto@LKZ.com', wait='lst')
    add.input_in_field(add.created, value='auto@LKZ.com', wait='lst')
    add.dropdown_without_input(add.region, option_text='Оренбургская область')
    add.dropdown_without_input(add.status, option_text='Неактивный')

    # сохранение фильтра с несколькими значениями
    add.click_button(element_dict=add.save_filter)
    time.sleep(1)
    add.input_in_field(add.name_filter, value='Фильтр Filter_11')
    time.sleep(1)
    add.click_button(element_dict=add.second_save_filter)
    time.sleep(1)

    # проверка работы Сохранённого фильтра №1
    add.click_button(element_dict=add.saved_filters)
    time.sleep(3)
    add.click_button(element_dict=add.radio_input_one, wait_type='located')
    time.sleep(1)
    add.click_button(element_dict=add.apply_filter)
    time.sleep(1)
    add.verify_text_on_page(text='орс', should_exist=False)
    add.verify_text_on_page(text='мрмск', should_exist=False)
    add.verify_text_on_page(text='Екатеринбург', should_exist=True)
    add.verify_text_on_page(text='Пышма', should_exist=True)

    # обновление страницы
    add.refresh_page()

    # проверка работы Сохранённого фильтра №2
    add.click_button(element_dict=add.saved_filters)
    time.sleep(3)
    add.click_button(element_dict=add.radio_input_two, wait_type='located')
    time.sleep(1)
    add.click_button(element_dict=add.apply_filter)
    time.sleep(1)
    add.verify_text_on_page(text='орс', should_exist=True)
    add.verify_text_on_page(text='орен', should_exist=True)
    add.verify_text_on_page(text='мрмск', should_exist=False)
    add.verify_text_on_page(text='Великие Луки', should_exist=False)
    add.verify_text_on_page(text='Екатеринбург', should_exist=False)
    add.verify_text_on_page(text='мгнрск', should_exist=False)

    # переименование сохранённого фильтра
    add.click_button(element_dict=add.saved_filters)
    time.sleep(1)
    add.click_button(element_dict=add.edit_filter)
    time.sleep(1)
    add.backspace_and_input(element_dict=add.rename_filter, click_first=True, value='57657')
    time.sleep(1)
    add.click_button(element_dict=add.third_save_filter)
    time.sleep(2)
    add.click_button(element_dict=add.cross)
    time.sleep(1)

    # обновление страницы
    add.refresh_page()

    # удаление сохранённого фильтра
    add.click_button(element_dict=add.saved_filters)
    time.sleep(1)
    add.click_button(element_dict=add.remove_filter)
    add.verify_text_on_page(text='57657', should_exist=False)
    time.sleep(1)
    add.click_button(element_dict=add.cross)
    time.sleep(1)

    # сброс фильтров
    add.click_button(element_dict=add.reset)
    time.sleep(1)
    # Конец теста


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description("ЛКЗ Тест фильтра 'Тарифы' в разделе справочники")
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True) # Параметризация роли
def test_tariff_directory_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # переход к списку тарифов
    base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                        do_assert=True, wait='lst')

    add = Manual(base.driver)
    # проверка фильтра "Название тарифа"
    add.input_in_field(add.tariff_name, value='202412092122', click_first=True)
    time.sleep(2)
    add.verify_text_on_page(text='LTL-20241209212214', should_exist=True)
    add.verify_text_on_page(text='20241210031127', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.tariff_name, value='')
    time.sleep(2)

    # проверка №1 фильтра "Статус"
    add.dropdown_without_input(add.tariff_status, option_text='Не активный')
    time.sleep(2)
    add.verify_text_on_page(text='ПРР-20241209180612', should_exist=True)
    add.verify_text_on_page(text='ТТ-20240910124407', should_exist=False)
    time.sleep(2)

    # проверка №2 фильтра "Статус"
    add.dropdown_without_input(add.tariff_status, option_text='Активный')
    time.sleep(2)
    add.verify_text_on_page(text='ПРР-20240818230735', should_exist=True)
    add.verify_text_on_page(text='ПРР-20241206111102', should_exist=False)
    time.sleep(2)

    # проверка №1 фильтра с несколькими значениями
    add.input_in_field(add.tariff_name, value='ПРР-20241209212319', click_first=True)
    add.dropdown_without_input(add.tariff_status, option_text='Не активный')
    time.sleep(2)
    add.find_text_on_page(text='319', occurrences=3)
    add.verify_text_on_page(text='10.12.2024 05:58', should_exist=True)
    add.verify_text_on_page(text='ПРР-20241206111102', should_exist=False)
    add.verify_text_on_page(text='93428', should_exist=False)
    time.sleep(2)

    # очистка поля "Название тарифа"
    add.backspace_and_input(add.tariff_name, value='')

    # проверка №2 фильтра с несколькими значениями
    add.input_in_field(add.tariff_name, value='ГГ-20241006200435', click_first=True)
    add.dropdown_without_input(add.tariff_status, option_text='Активный')
    time.sleep(2)
    add.find_text_on_page(text='435', occurrences=3)
    add.verify_text_on_page(text='10.12.2024 05:58', should_exist=False)
    add.verify_text_on_page(text='ПРР-20241206111102', should_exist=False)
    add.verify_text_on_page(text='93428', should_exist=False)
    time.sleep(2)

    # очистка поля "Название тарифа"
    add.backspace_and_input(add.tariff_name, value='')

    # Конец теста























