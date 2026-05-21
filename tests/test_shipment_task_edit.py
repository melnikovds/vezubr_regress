import time
import allure
import pytest
import random
from faker import Faker

from api_pages.create_entities import CreateEntities
from pages.shipment_task_page import ShipmentTaskAdd
from pages.address_list_page import AddressesList
from pages.filters_gm_lkz_lke_page import GmFilters
from pages.cargo_place_list_page import CargoPlaceList
from pages.cargo_place_add_page import CargoPlaceAdd


@allure.story("Smoke test")
@allure.feature('Создание и удаление заданий')
@allure.description('ЛКЗ. Тест обновления Задания с включенной комплектацией грузоместами')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_shipment_task_with_gm_edit1_lkz(base_fixture, domain):
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


@allure.story("Smoke test")
@allure.feature('Создание и удаление заданий')
@allure.description('ЛКЗ. Тест добавления фактических ГМ в Задание')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_shipment_task_with_gm_edit2_lkz(base_fixture, domain):
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
    al.input_in_field(al.factual_address, value='Великие Луки, ул С.Ковалевской')
    time.sleep(2)
    al.click_button(al.first_radio_button_18466, wait_type='located')
    al.click_button(al.save_selected_address)
    time.sleep(1)
    add.click_button(add.delivery_address)
    al.input_in_field(al.factual_address, value='Череповец, ул Менделеева')
    time.sleep(2)
    al.click_button(al.first_radio_button_16934, wait_type='located')
    al.click_button(al.save_selected_address)
    time.sleep(1)
    add.dropdown_without_input(add.whom_task, option_text='FM')
    time.sleep(1)
    add.click_button(add.creation_complete)
    time.sleep(1)
    add.click_button(add.successfully_created)
    time.sleep(1)

    add.reload_page()
    time.sleep(5)

    add.verify_text_on_page(text=a)
    add.verify_text_on_page(text=h)

    # сохраняем id созданного Задания
    current_url = base.driver.current_url
    task_id = current_url.split('/')[-1]
    print(f"task_id {task_id}")

    # Переход к списку грузомест
    sidebar.click_button(sidebar.sidebar_button)
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    time.sleep(2)
    cp_list = CargoPlaceList(base.driver)
    # Клик по кнопке добавления грузоместа
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")

    add_cp = CargoPlaceAdd(base.driver)
    # Добавление полного грузоместа
    cp_stamp = add_cp.add_full_cargo_place_lkz()

    # Сброс фильтров
    cp_list.click_button(cp_list.reset_button, wait="lst")
    # Ввод штрихкода грузоместа в поле фильтрации
    cp_list.input_in_field(cp_list.barcode_filter, value=cp_stamp, wait="lst")
    # Клик по ссылке первого грузоместа в списке
    cp_list.click_button(cp_list.first_cp_link, wait="form")

    # сохраняем id первого Грузоместа
    current_url = base.driver.current_url
    cargo_place_id_one = current_url.split('/')[-1]
    print(f"cargo_place_id_one {cargo_place_id_one}")

    # Переход к списку грузомест
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    time.sleep(2)
    cp_list = CargoPlaceList(base.driver)
    # Клик по кнопке добавления грузоместа
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")

    add_cp = CargoPlaceAdd(base.driver)
    # Добавление полного грузоместа
    cp_stamp = add_cp.add_full_cargo_place_lkz()

    # Сброс фильтров
    cp_list.click_button(cp_list.reset_button, wait="lst")
    # Ввод штрихкода грузоместа в поле фильтрации
    cp_list.input_in_field(cp_list.barcode_filter, value=cp_stamp, wait="lst")
    # Клик по ссылке первого грузоместа в списке
    cp_list.click_button(cp_list.first_cp_link, wait="form")

    # сохраняем id второго Грузоместа
    current_url = base.driver.current_url
    cargo_place_id_two = current_url.split('/')[-1]
    print(f"cargo_place_id_two {cargo_place_id_two}")

    # with allure.step("Обновление Задания через API"):
    #     lkz_creator = CreateEntities(role='lkz')
    #
    #     updated_data = lkz_creator.build_update_task_data









