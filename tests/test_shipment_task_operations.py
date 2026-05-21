import time
import allure
import pytest
from pages.shipment_task_page import ShipmentTaskAdd
from pages.filters_gm_lkz_lke_page import GmFilters
from api_pages.create_entities import CreateEntities


@allure.story("Smoke test")
@allure.feature('Создание и удаление заданий')
@allure.description('LKZ Тест удаления Задания ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_shipment_task_with_gm_delete_lkz(base_fixture, domain, task_number_lkz):
    # Инициализация базовых объектов через фикстуру UI
    base, sidebar = base_fixture

    # Переход к списку заданий
    sidebar.move_and_click(
        move_to=sidebar.assignments_hover,
        click_to=sidebar.tasks_list_button,
        do_assert=True,
        wait="lst"
    )

    lst = GmFilters(base.driver)
    add = ShipmentTaskAdd(base.driver)

    # Выбор нужного Задания по номеру из API
    lst.dropdown_without_input(lst.required_search_by_date, "За все время")
    time.sleep(2)
    lst.input_in_field(lst.order_number, task_number_lkz, wait='lst')
    time.sleep(3)
    lst.click_button(lst.first_task_click)
    time.sleep(2)
    add.click_button(add.task_delete_button)
    add.click_button(add.task_delete_button_confirm)
    time.sleep(1)
    add.click_button(add.task_delete_window_confirm)

    with allure.step("Ожидание загрузки страницы со списком заданий"):
        try:
            base.get_element(base.loading_list, wait_type="visible")
            print("Спиннер загрузки появился")
        except:
            print("Спиннер загрузки не появился")

        try:
            base.get_element(base.loading_list, wait_type="invisibility")
            print("Спиннер загрузки исчез")
        except:
            print("Спиннер загрузки не исчез")

        time.sleep(2)

    with allure.step(f"Проверка что задание {task_number_lkz} удалено"):
        lst.backspace_and_input(lst.order_number, "")
        time.sleep(1)
        base.refresh_page()
        time.sleep(2)

        try:
            base.get_element(base.loading_list, wait_type="invisibility")
        except:
            pass

        base.verify_text_on_page(task_number_lkz, should_exist=False)

    print(f"\n✅ ТЕСТ ПРОЙДЕН: Задание {task_number_lkz} успешно удалено")


@allure.story("Integration test")
@allure.feature('Передача задания от LKZ к LKE')
@allure.description('LKZ создает задание и заявку, LKE находит задание в списке')
def test_transfer_task_from_lkz_to_lke(domain):
    """
    Тест передачи задания от LKZ к LKE через заявку
    """
    # ========== API часть ==========
    with allure.step("Создание задания через API (роль LKZ)"):
        lkz_creator = CreateEntities(role='lkz')

        departure_point_id = 28754
        arrival_point_id = 28756

        task = lkz_creator.create_task(
            departure_point_id=departure_point_id,
            arrival_point_id=arrival_point_id,
            title_prefix="Передача_LKZ_LKE",
            use_dates=True
        )

        task_number = task.get('task_number') or task.get('number')
        task_id = task.get('id')
        print(f"✅ Создано задание: {task_number}")

    with allure.step("Создание и публикация заявки LKZ с привязкой задания"):
        delivery_request = lkz_creator.create_and_publish_delivery_request_with_task(
            task_id=task_id,
            departure_point_id=departure_point_id,
            arrival_point_id=arrival_point_id
        )

        request_number = delivery_request.get('requestNr')
        print(f"✅ Создана заявка: {request_number}")

    # ========== UI часть ==========
    with allure.step("Вход в систему как LKE"):
        from tests.base_test import base_test_with_login
        base, sidebar = base_test_with_login(domain, 'lke')
        add = ShipmentTaskAdd(base.driver)

    try:
        with allure.step("Переход к списку активных заявок"):
            sidebar.move_and_click(
                move_to=sidebar.requests_hover,
                click_to=sidebar.cdr_active_list_button,
                do_assert=True,
                wait="lst"
            )

        with allure.step(f"Поиск заявки {request_number}"):
            add.dropdown_without_input(add.required_search_by_date_lke, "Сегодня и завтра")
            time.sleep(2)
            add.input_in_field(add.order_number, request_number, wait='lst')
            time.sleep(2)
            add.click_button(add.first_request_click)
            time.sleep(2)

        with allure.step("Подтверждение заявки экспедитором"):
            add.click_button(add.confirm_request_button)
            time.sleep(2)

        with allure.step("Переход к списку заданий"):
            sidebar.move_and_click(
                move_to=sidebar.assignments_hover,
                click_to=sidebar.tasks_list_button,
                do_assert=True,
                wait="lst"
            )

        with allure.step(f"Поиск задания {task_number}"):
            add.dropdown_without_input(add.required_search_by_date, "Сегодня и завтра")
            time.sleep(2)
            add.input_in_field(add.task_sdr_input, task_number, wait='lst')
            time.sleep(2)
            add.click_button(add.first_task_click)
            time.sleep(2)

        with allure.step(f"Проверка что открыто задание {task_number}"):
            base.verify_text_on_page(task_number, should_exist=True)
            print(f"✅ Задание {task_number} найдено в интерфейсе LKE")

    finally:
        base.driver.quit()

    print(f"\n✅ ТЕСТ ПРОЙДЕН: Задание {task_number} успешно передано от LKZ к LKE")
