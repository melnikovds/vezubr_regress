import allure
import pytest
import time
from pages.manual_page import Manual

@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description('ЛКЗ Тест фильтра Адреса в разделе справочники')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True) # Параметризация роли
def test_address_directory_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture


    base.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                        do_assert=True, wait='lst')

    add = Manual(base.driver)

    add.click_button(element_dict=add.reset)

    add.dropdown_without_input(add.filter_date_create, option_text='За год')
    time.sleep(2)
    add.input_in_field(add.verified_address, value='Ленина', click_first=True)
    time.sleep(2)
    add.verify_text_on_page(text='г Екатеринбург, пр-кт Ленина, д 68')
    time.sleep(1)

    add.backspace_and_input(add.verified_address, value='Великие Луки', click_first=True)
    time.sleep(1)
    add.verify_text_on_page(text='Винатовского')
    time.sleep(1)
    add.backspace_and_input(add.verified_address, value='')

    add.backspace_and_input(add.verified_address, value='Мурманск', click_first=True)
    time.sleep(2)
    add.verify_text_on_page(text='Плато')
    time.sleep(1)
    add.backspace_and_input(add.verified_address, value='')

    add.backspace_and_input(add.verified_address, value='Винатовского', click_first=True)
    time.sleep(2)
    add.verify_text_on_page(text='Великие Луки')
    time.sleep(1)
    add.backspace_and_input(add.verified_address, value='')

    add.backspace_and_input(add.verified_address, value='Плато', click_first=True)
    time.sleep(2)
    add.verify_text_on_page(text='Мурманск')
    time.sleep(1)
    add.backspace_and_input(add.verified_address, value='')

    add.input_in_field(add.name_address, value='тгл', wait='lst')
    add.verify_text_on_page(text='Нижний Тагил')
    add.backspace_and_input(add.name_address, value='')
    time.sleep(1)

    add.input_in_field(add.name_address, value='мрмск', wait='lst')
    add.verify_text_on_page(text='Мурманск')
    add.backspace_and_input(add.name_address, value='')
    time.sleep(1)

    add.input_in_field(add.sender_recipient, value='Авангард', wait='lst')
    add.verify_text_on_page('Лиговский')
    add.backspace_and_input(add.sender_recipient, value='')


    add.dropdown_without_input(add.status, option_text='Активный')
    time.sleep(3)
    add.verify_text_on_page('Россия, Псковская обл, г Великие Луки, ул Винатовского, д 28')
    time.sleep(1)
    add.verify_text_on_page(text='Ясный', should_exist=False)
    time.sleep(1)

    add.dropdown_without_input(add.status, option_text='Неактивный')
    time.sleep(3)
    add.verify_text_on_page('86')
    add.verify_text_on_page(text='Пышма', should_exist=False)
    time.sleep(1)

    add.click_button(element_dict=add.reset)

    add.dropdown_without_input(add.region, option_text='Псковская область')
    add.verify_text_on_page('Россия, Псковская обл, г Великие Луки, ул Винатовского, д 28')
    time.sleep(3)
    add.verify_text_on_page(text='Екатеринбург', should_exist=False)
    time.sleep(1)

    add.click_button(element_dict=add.reset)

    add.input_in_field(add.approved, value='auto@LKZ.com', wait='lst')
    add.verify_text_on_page('Винатовского')
    add.backspace_and_input(add.sender_recipient, value='')

    add.input_in_field(add.created, value='auto@LKZ.com', wait='lst')
    add.verify_text_on_page('Плато')
    add.backspace_and_input(add.sender_recipient, value='')
    time.sleep(1)

    add.input_in_field(add.id_address, value='20241207174426')
    add.verify_text_on_page('Адрес-20241207174426')
    time.sleep(2)
    add.backspace_and_input(add.id_address, value='')

    add.click_button(element_dict=add.reset)


    add.input_in_field(add.approved, value='auto@LKZ.com', wait='lst')
    add.input_in_field(add.created, value='auto@LKZ.com', wait='lst')
    add.dropdown_without_input(add.region, option_text='Оренбургская область')
    add.dropdown_without_input(add.status, option_text='Неактивный')

    add.click_button(element_dict=add.save_filter)
    time.sleep(1)
    add.input_in_field(add.name_filter, value='Фильтр Filter_11')
    time.sleep(1)
    add.click_button(element_dict=add.second_save_filter)
    time.sleep(1)


    add.click_button(element_dict=add.saved_filters)
    time.sleep(3)
    add.click_button(element_dict=add.radio_input_one, wait_type='located')
    time.sleep(3)
    add.click_button(element_dict=add.apply_filter)
    time.sleep(3)
    add.verify_text_on_page(text='орс', should_exist=False)
    add.verify_text_on_page(text='мрмск', should_exist=False)
    add.verify_text_on_page(text='Екатеринбург', should_exist=True)
    add.verify_text_on_page(text='Пышма', should_exist=True)

    add.refresh_page()

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

    add.refresh_page()

    time.sleep(1)
    add.click_button(element_dict=add.saved_filters)
    time.sleep(1)
    add.click_button(element_dict=add.remove_filter)
    add.verify_text_on_page(text='57657', should_exist=False)
    time.sleep(1)
    add.click_button(element_dict=add.cross)
    time.sleep(1)

    add.click_button(element_dict=add.reset)
    time.sleep(2)


















