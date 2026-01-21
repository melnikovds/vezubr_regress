import time
import allure
import pytest
from pages.shipment_task_page import ShipmentTaskAdd
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










