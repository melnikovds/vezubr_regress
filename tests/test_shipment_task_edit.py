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
@allure.description('ЛКЗ. Тест обновления Задания с включенной комплектацией грузоместами')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_shipment_task_with_gm_edit_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку заданий
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.tasks_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)
    lst = GmFilters(base.driver)

    # Выбор нужного Задания
    lst.dropdown_without_input(lst.required_search_by_date, "За все время")
    time.sleep(2)
    lst.input_in_field(lst.order_number, "дэвять", wait='lst')
    time.sleep(3)
    lst.click_button(lst.first_task_click)
    time.sleep(2)

    # Редактируем Задание
    add = ShipmentTaskAdd(base.driver)
    add.click_button(add.task_edit_button)
    time.sleep(1)
    a = ["Телефоны", "Ноутбуки", "Наушники", "Клавиатуры", "Принтеры", "Мониторы"]
    b = random.choice(a)
    add.backspace_and_input(add.product_name, value=b)
    c = ["FM", "Маршрутизация Везубр", "Почта РФ"]
    d = random.choice(c)
    add.dropdown_without_input(add.whom_task_edit_button, option_text=d)
    add.click_button(add.save_edit_button)
    time.sleep(1)

    add.reload_page()
    time.sleep(5)

    add.verify_text_on_page(text=b)
    add.verify_text_on_page(text=d)