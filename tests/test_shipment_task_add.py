import time
import allure
import pytest
import random
from faker import Faker
from pages.shipment_task_page import ShipmentTaskAdd
from pages.address_list_page import AddressesList
from pages.filters_gm_lkz_lke_page import GmFilters
from pages.cargo_place_list_page import CargoPlaceList


@allure.story("Smoke test")
@allure.feature('Создание и удаление заданий')
@allure.description('ЛКЗ. Тест содания Задания с выключенной комплектацией грузоместами')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_shipment_task_without_gm_add_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку заданий
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.tasks_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)
    add = ShipmentTaskAdd(base.driver)

    # Клик по кнопке создания задания
    add.click_button(add.task_create_button)
    time.sleep(1)
    # Заполняем параметры Задания
    a = str(base.random_value_int(2000, 3000))
    add. input_in_field(add.task_number, value=a)
    b = base.random_value_float_str(50, 100, 2)
    add.input_in_field(add.task_weight, value=b)
    c = base.random_value_float_str(1, 10, 2)
    add.input_in_field(add.task_volume, value=c)
    d = base.random_value_float_str(1000, 100000, 2)
    add.input_in_field(add.task_cost, value=d)
    e = str(base.random_value_int(10, 100))
    add.input_in_field(add.number_place, value=e)
    fake = Faker('en_US')
    h = fake.word()
    add.input_in_field(add.product_name, value=h)
    time.sleep(2)
    add.click_button(add.departure_address)
    al = AddressesList(base.driver)
    al.input_in_field(al.factual_address, value='Фрунзе, д 15')
    time.sleep(2)
    al.click_button(al.first_radio_button_19225, wait_type='located')
    al.click_button(al.save_selected_address)
    time.sleep(1)
    add.click_button(add.delivery_address)
    al.input_in_field(al.factual_address, value='Ковалевской')
    time.sleep(2)
    al.click_button(al.first_radio_button_18466, wait_type='located')
    al.click_button(al.save_selected_address)
    time.sleep(1)
    add.dropdown_without_input(add.type_package, option_text='Короб')
    add.dropdown_without_input(add.whom_task, option_text='Маршрутизация Везубр')
    time.sleep(1)
    add.click_button(add.creation_complete)
    time.sleep(1)
    add.click_button(add.successfully_created)
    time.sleep(1)

    add.reload_page()
    time.sleep(5)

    def normalize_float_str(value: str) -> str:
        return str(float(value))

    add.verify_text_on_page(text=a)
    add.verify_text_on_page(text=normalize_float_str(b))
    add.verify_text_on_page(text=normalize_float_str(c))
    add.verify_text_on_page(text=d)
    add.verify_text_on_page(text=e)
    add.verify_text_on_page(text=h)


@allure.story("Smoke test")
@allure.feature('Создание и удаление заданий')
@allure.description('ЛКЗ. Тест содания Задания с включённой комплектацией грузоместами')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_shipment_task_with_gm_add_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку заданий
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.tasks_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)
    add = ShipmentTaskAdd(base.driver)

    # Клик по кнопке создания задания
    add.click_button(add.task_create_button)
    time.sleep(1)
    # Заполняем параметры Задания
    a = str(base.random_value_int(2000, 3000))
    add. input_in_field(add.task_number, value=a)
    fake = Faker('en_US')
    h = fake.word()
    add.input_in_field(add.product_name, value=h)
    add.click_button(add.switch_complete_gm)
    time.sleep(2)
    add.click_button(add.departure_address)
    al = AddressesList(base.driver)
    al.input_in_field(al.factual_address, value='Академика Павлова, д 3')
    time.sleep(2)
    al.click_button(al.first_radio_button_19194, wait_type='located')
    al.click_button(al.save_selected_address)
    time.sleep(1)
    add.click_button(add.delivery_address)
    al.input_in_field(al.factual_address, value='Винатовского, д 28')
    time.sleep(2)
    al.click_button(al.first_radio_button_16831, wait_type='located')
    al.click_button(al.save_selected_address)
    time.sleep(1)
    add.dropdown_without_input(add.whom_task, option_text='Почта РФ')
    time.sleep(1)
    add.click_button(add.creation_complete)
    time.sleep(1)
    add.click_button(add.successfully_created)
    time.sleep(1)

    add.reload_page()
    time.sleep(5)

    add.verify_text_on_page(text=a)
    add.verify_text_on_page(text=h)

















































