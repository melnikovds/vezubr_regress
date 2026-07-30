import allure
import pytest
import time
from pages.filters_old_ftl_page import OldFTL
from api_pages.create_entities import CreateEntities



@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description('ЛКЗ. Тест фильтров в разделе Активные old FTL-заявки ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_filter_old_ftl_lkz(base_fixture, domain):
    base, sidebar = base_fixture

    creator = CreateEntities(role='lkz')
    departure_point_id = 17098
    arrival_point_id = 16935

    order_data = creator.create_old_ftl_order_for_filters(
        departure_point_id=departure_point_id,
        arrival_point_id=arrival_point_id,
        producer_id=2447
    )

    test_data = order_data['test_data']
    order_nr = test_data['order_nr']
    client_number = test_data['client_number']
    order_number = test_data['order_number']
    publication_from = test_data['publication_date_from']
    publication_to = test_data['publication_date_to']

    print(f"\n=== СОЗДАН ЗАКАЗ ===")
    print(f"Номер заявки: {order_nr}")
    print(f"Идентификатор: {client_number}")
    print(f"Номер рейса: {order_number}")
    print(f"===================\n")

    time.sleep(5)

    # Переход в раздел
    base.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_active_list_button,
                        do_assert=True, wait='lst')

    add = OldFTL(base.driver)

    # ========== ПРОВЕРКА ФИЛЬТРА "НОМЕР ЗАЯВКИ" ==========
    # Сброс перед проверкой
    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    add.click_button(add.start_date)
    time.sleep(1)
    add.click_button(add.all_time)
    time.sleep(2)

    add.input_in_field(add.request_number, value=order_nr, click_first=True)
    time.sleep(3)
    add.verify_text_on_page(text=order_nr, should_exist=True)
    # НЕ очищаем поле! Просто переходим к следующей проверке

    # ========== ПРОВЕРКА ФИЛЬТРА "СТАТУС ЗАЯВКИ" ==========
    # Меняем статус, номер заявки уже введен
    add.dropdown_without_input(add.request_status, option_text='Заявка опубликована')
    time.sleep(2)
    add.verify_text_on_page(text=order_nr, should_exist=True)

    add.dropdown_without_input(add.request_status, option_text='Заявка принята')
    time.sleep(2)
    add.find_text_on_page(text=order_nr, occurrences=2)

    # ========== ПРОВЕРКА ФИЛЬТРА "ИДЕНТИФИКАТОР ЗАЯВКИ" ==========
    # Сброс всех фильтров перед новой проверкой
    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    add.click_button(add.start_date)
    time.sleep(1)
    add.click_button(add.all_time)
    time.sleep(2)

    add.input_in_field(add.request_identifier, value=client_number, click_first=True)
    time.sleep(2)
    add.verify_text_on_page(text=client_number, should_exist=True)

    # ========== ПРОВЕРКА ФИЛЬТРА "ДАТА ПУБЛИКАЦИИ" ==========
    # Сброс перед проверкой
    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    add.click_button(add.start_date)
    time.sleep(1)
    add.click_button(add.all_time)
    time.sleep(2)

    add.click_button(add.publication_date)
    time.sleep(1)
    add.input_in_field(add.publication_from, value=publication_from, click_first=True)
    time.sleep(2)
    add.input_in_field(add.publication_before, value=publication_to, click_first=True)
    time.sleep(3)
    add.verify_text_on_page(text=order_nr, should_exist=True)

    # # ========== ПРОВЕРКА ФИЛЬТРА "НОМЕР РЕЙСА" ==========
    # # Сброс перед проверкой
    # add.click_button(element_dict=add.reset_filters)
    # time.sleep(1)
    # add.click_button(add.start_date)
    # time.sleep(1)
    # add.click_button(add.all_time)
    # time.sleep(2)
    #
    # add.input_in_field(add.order_number, value=order_nr, click_first=True)
    # time.sleep(2)
    # add.verify_text_on_page(text=order_number, should_exist=True)

    creator.client.session.close()
    print(f"\n✅ Тест успешно завершен для заказа {order_nr}")


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description('ЛКЕ. Тест фильтров в разделе Активные old FTL-заявки ')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_filter_old_ftl_lke(base_fixture, domain):
    base, sidebar = base_fixture

    creator = CreateEntities(role='lke')

    # Создаем заказ по рабочему curl
    order_data = creator.create_old_ftl_order_for_lke(
        client_id=2447,  # как в curl
        producer_id=2449  # ЛКП
    )

    test_data = order_data['test_data']
    order_nr = test_data['order_nr']
    client_number = test_data['client_number']

    print(f"\n=== СОЗДАН ЗАКАЗ (ЛКЕ) ===")
    print(f"Номер заявки: {order_nr}")
    print(f"Client number: {client_number}")
    print(f"==========================\n")

    time.sleep(5)

    base.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_active_list_button,
                        do_assert=True, wait='lst')

    add = OldFTL(base.driver)

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    add.click_button(add.start_date)
    time.sleep(1)
    add.click_button(add.all_time)
    time.sleep(2)

    add.input_in_field(add.request_number, value=order_nr, click_first=True)
    time.sleep(3)
    add.verify_text_on_page(text=order_nr, should_exist=True)
   # баг на фронте за ЛКЕ
   # add.dropdown_without_input(add.request_status, option_text='Заявка опубликована')
   # time.sleep(2)
   # add.verify_text_on_page(text=order_nr, should_exist=True)

   # add.dropdown_without_input(add.request_status, option_text='Заявка принята')
   # time.sleep(2)
   # add.verify_text_on_page(text=order_nr, should_exist=False)

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    add.click_button(add.start_date)
    time.sleep(1)
    add.click_button(add.all_time)
    time.sleep(2)

    add.input_in_field(add.request_identifier, value=client_number, click_first=True)
    time.sleep(2)
    add.verify_text_on_page(text=client_number, should_exist=True)

    creator.client.session.close()

    print(f"\n✅ Тест ЛКЕ успешно завершен для заказа {order_nr}")


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description('ЛКП. Тест фильтров в разделе Активные old FTL-заявки ')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_filter_old_ftl_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход в раздел Активные FTL-заявки
    base.move_and_click(move_to=sidebar.orders_old_hover_lkp, click_to=sidebar.ftl_active_list_button,
                        do_assert=True, wait='lst')

    add = OldFTL(base.driver)
    # сброс фильтров
    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    add.click_button(add.start_date)
    time.sleep(1)
    add.click_button(add.all_time)
    time.sleep(1)

    # проверка фильтра "номер заявки"
    add.input_in_field(add.request_number, value='25-112201-2449', click_first=True)
    time.sleep(3)
    add.find_text_on_page(text='25-112201-2449', occurrences=3)
    add.verify_text_on_page(text='25-112564-2449', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.request_number, value='')

    # проверка фильтра "статус заявки"
    add.dropdown_without_input(add.request_status, option_text='Заявка опубликована')
    time.sleep(3)
    add.verify_text_on_page(text='25-114898-2449', should_exist=True)
    add.verify_text_on_page(text='25-114880-2449', should_exist=False)
    time.sleep(1)
    add.dropdown_without_input(add.request_status, option_text='Заявка принята')
    time.sleep(3)
    add.verify_text_on_page(text='25-114878-2449', should_exist=True)
    add.verify_text_on_page(text='25-114877-2449', should_exist=False)
    time.sleep(1)

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    add.click_button(add.start_date)
    time.sleep(1)
    add.click_button(add.all_time)
    time.sleep(1)

    # проверка фильтра "Идентификатор заявки"
    add.input_in_field(add.request_identifier, value='78', click_first=True)
    time.sleep(2)
    add.verify_text_on_page(text='rog-17-78', should_exist=True)
    add.verify_text_on_page(text='rog-17-77', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.request_identifier, value='')

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    add.click_button(add.start_date)
    time.sleep(1)
    add.click_button(add.all_time)
    time.sleep(1)

    # проверка фильтра "номер рейса"
    add.input_in_field(add.order_number, value='880-2449', click_first=True)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-114880-2449-1', should_exist=True)
    add.verify_text_on_page(text='R-25-114879-2449-1', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.order_number, value='')


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description('ЛКЗ. Тест фильтров в разделе Все FTl-рейсы ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_filter_order_ftl_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход в раздел Все FTL-рейсы
    base.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_list_button,
                        do_assert=True, wait='lst')

    add = OldFTL(base.driver)
    # сброс фильтров
    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    add.click_button(add.order_start_date)
    time.sleep(1)
    add.click_button(add.order_all_time)
    time.sleep(1)

    # проверка фильтра "номер рейса"
    add.input_in_field(add.order_number_two, value='60-2448', click_first=True)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-60-2448-1', should_exist=True)
    add.verify_text_on_page(text='R-25-59-2448-1', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.order_number_two, value='')

    # проверка фильтра "номер заявки"
    add.input_in_field(add.request_number_two, value='25-49-2448', click_first=True)
    time.sleep(3)
    add.find_text_on_page(text='25-49-2448', occurrences=5)
    add.verify_text_on_page(text='25-48-2448', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.request_number_two, value='')

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    add.click_button(add.order_start_date)
    time.sleep(1)
    add.click_button(add.order_all_time)
    time.sleep(1)

    # проверка фильтра "стадии заявки"
    add.dropdown_with_input(add.order_stage, option_text='подбор')
    add.click_button(add.checkbox_one)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-311-2448-1', should_exist=True)
    add.verify_text_on_page(text='R-25-258-2448-1', should_exist=False)

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    add.click_button(add.order_start_date)
    time.sleep(1)
    add.click_button(add.order_all_time)
    time.sleep(1)

    add.dropdown_with_input(add.order_stage, option_text='исполнение')
    add.click_button(add.checkbox_two)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-312-2448-1', should_exist=True)
    add.verify_text_on_page(text='R-25-68-2448-1', should_exist=False)

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    add.click_button(add.order_start_date)
    time.sleep(1)
    add.click_button(add.order_all_time)
    time.sleep(1)

    add.dropdown_with_input(add.order_stage, option_text='расч')
    add.click_button(add.checkbox_three)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-48-2448-1', should_exist=True)
    add.verify_text_on_page(text='R-25-4-2448-1', should_exist=False)

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    add.click_button(add.order_start_date)
    time.sleep(1)
    add.click_button(add.order_all_time)
    time.sleep(1)

    add.dropdown_with_input(add.order_stage, option_text='отме')
    add.click_button(add.checkbox_four)
    time.sleep(1)
    add.input_in_field(add.order_number_two, value='25-16', click_first=True)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-16-2448-1', should_exist=True)
    add.verify_text_on_page(text='R-25-49-2448-1', should_exist=False)

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    add.click_button(add.order_start_date)
    time.sleep(1)
    add.click_button(add.order_all_time)
    time.sleep(1)

    # проверка фильтра "ответственный пользователь"
    add.click_and_select_with_arrows(add.responsible_user, arrow_presses=0)
    time.sleep(1)
    add.verify_text_on_page(text='1555 1555', should_exist=True)
    add.verify_text_on_page(text='R-25-69-2448-1', should_exist=True)
    add.verify_text_on_page(text='R-25-59-2448-1', should_exist=False)


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description('ЛКЕ. Тест фильтров в разделе Все FTl-рейсы ')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_filter_order_ftl_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход в раздел Все FTL-рейсы
    base.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_list_button,
                        do_assert=True, wait='lst')

    add = OldFTL(base.driver)
    # сброс фильтров
    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)

    # проверка фильтра "номер рейса"
    add.input_in_field(add.order_number_two, value='36-2447', click_first=True)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-36-2447-1', should_exist=True)
    add.verify_text_on_page(text='R-25-35-2447-1', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.order_number_two, value='')

    # проверка фильтра "номер заявки"
    add.input_in_field(add.request_number_two, value='25-27-2447', click_first=True)
    time.sleep(3)
    add.find_text_on_page(text='25-27-2447', occurrences=5)
    add.verify_text_on_page(text='25-26-2447', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.request_number_two, value='')

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)

    # проверка фильтра "стадии заявки"
    add.dropdown_with_input(add.order_stage, option_text='подбор')
    add.click_button(add.checkbox_one)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-36-2447-1', should_exist=True)
    add.verify_text_on_page(text='R-25-27-2447-1', should_exist=False)

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)

    add.dropdown_with_input(add.order_stage, option_text='исполнение')
    add.click_button(add.checkbox_two)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-46-2447-1', should_exist=True)
    add.verify_text_on_page(text='R-25-35-2447-1', should_exist=False)

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)

    add.dropdown_with_input(add.order_stage, option_text='расч')
    add.click_button(add.checkbox_three)
    time.sleep(3)
    add.verify_text_on_page(text='R-24-75-2447-1', should_exist=True)
    add.verify_text_on_page(text='R-25-33-2447-1', should_exist=False)

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)

    add.dropdown_with_input(add.order_stage, option_text='отме')
    add.click_button(add.checkbox_four)
    time.sleep(3)
    add.verify_text_on_page(text='25-17-2447', should_exist=True)
    add.verify_text_on_page(text='R-25-32-2447-1', should_exist=False)

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)

    # проверка фильтра "ответственный пользователь"
    add.click_and_select_with_arrows(add.responsible_user, arrow_presses=0)
    time.sleep(1)
    add.verify_text_on_page(text='1555 1555', should_exist=True)
    add.verify_text_on_page(text='R-25-36-2447-1', should_exist=True)
    add.verify_text_on_page(text='R-25-47-2447-1', should_exist=False)


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description('ЛКП. Тест фильтров в разделе Все FTl-рейсы ')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_filter_order_ftl_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход в раздел Все FTL-рейсы
    base.move_and_click(move_to=sidebar.orders_old_hover_lkp, click_to=sidebar.ftl_list_button,
                        do_assert=True, wait='lst')

    add = OldFTL(base.driver)
    # сброс фильтров
    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)

    # проверка фильтра "номер рейса"
    add.input_in_field(add.order_number_two, value='54-2449', click_first=True)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-54-2449-1', should_exist=True)
    add.verify_text_on_page(text='R-25-53-2449-1', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.order_number_two, value='')

    # проверка фильтра "номер заявки"
    add.input_in_field(add.request_number_two, value='25-38-2449', click_first=True)
    time.sleep(3)
    add.find_text_on_page(text='25-38-2449', occurrences=5)
    add.verify_text_on_page(text='25-37-2449', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.request_number_two, value='')

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)

    # проверка фильтра "стадии заявки"
    add.dropdown_with_input(add.order_stage, option_text='подбор')
    add.click_button(add.checkbox_one)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-54-2449-1', should_exist=True)
    add.verify_text_on_page(text='R-25-38-2449-1', should_exist=False)

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)

    add.dropdown_with_input(add.order_stage, option_text='исполнение')
    add.click_button(add.checkbox_two)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-16-2449-1', should_exist=True)
    add.verify_text_on_page(text='R-25-37-2449-1', should_exist=False)

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)

    add.dropdown_with_input(add.order_stage, option_text='расч')
    add.click_button(add.checkbox_three)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-36-2449-1', should_exist=True)
    add.verify_text_on_page(text='R-25-54-2449-1', should_exist=False)

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)

    add.dropdown_with_input(add.order_stage, option_text='отме')
    add.click_button(add.checkbox_four)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-12-2449-1', should_exist=True)
    add.verify_text_on_page(text='R-25-37-2449-1', should_exist=False)

    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)

    # проверка фильтра "ответственный пользователь"
    add.click_and_select_with_arrows(add.responsible_user, arrow_presses=4)
    time.sleep(3)
    add.verify_text_on_page(text='120544', should_exist=True)
    add.verify_text_on_page(text='R-25-54-2449-1', should_exist=True)
    add.verify_text_on_page(text='R-25-53-2449-1', should_exist=False)


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description('ЛКЗ. Тест фильтров в разделе Отложенные Рейсы ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_filter_delayed_order_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход в раздел Все FTL-рейсы
    base.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.deferred_list_button,
                        do_assert=True, wait='lst')

    add = OldFTL(base.driver)
    # сброс фильтров
    add.move_to_element(add.menu_calendar)
    time.sleep(2)
    add.click_on_the_cross(add.cross)
    time.sleep(2)

    # проверка фильтра "номер рейса"
    add.input_in_field(add.order_number_three, value='428', click_first=True)
    time.sleep(3)
    add.find_text_on_page(text='R-22-428-1598-1', occurrences=4)
    add.verify_text_on_page(text='R-22-277-1598-1', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.request_number_two, value='')

    # проверка фильтра "номер заявки"
    add.input_in_field(add.request_number_two, value='24-177-2448', click_first=True)
    time.sleep(3)
    add.find_text_on_page(text='24-177-2448', occurrences=4)
    add.verify_text_on_page(text='24-172-2448', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.request_number_two, value='')

    # проверка фильтра "Идентификатор рейса"
    add.input_in_field(add.order_identifier, value='vb-81', click_first=True)
    time.sleep(2)
    add.verify_text_on_page(text='25-67-2448', should_exist=True)
    add.verify_text_on_page(text='24-8-2448', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.order_identifier, value='')


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description('ЛКЭ. Тест фильтров в разделе Отложенные Рейсы ')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_filter_delayed_order_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход в раздел Все FTL-рейсы
    base.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.deferred_list_button,
                        do_assert=True, wait='lst')

    add = OldFTL(base.driver)
    # сброс фильтров
    add.move_to_element(add.menu_calendar)
    time.sleep(2)
    add.click_on_the_cross(add.cross)
    time.sleep(2)

    # # проверка фильтра "номер рейса"
    # add.input_in_field(add.order_number_three, value='428', click_first=True)
    # time.sleep(3)
    # add.find_text_on_page(text='R-22-428-1598-1', occurrences=4)
    # add.verify_text_on_page(text='R-22-277-1598-1', should_exist=False)
    # time.sleep(1)
    # add.backspace_and_input(add.request_number_two, value='')

    # проверка фильтра "номер заявки"
    add.input_in_field(add.request_number_two, value='24-1-2447', click_first=True)
    time.sleep(3)
    add.find_text_on_page(text='24-1-2447', occurrences=4)
    add.verify_text_on_page(text='24-195-2448', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.request_number_two, value='')

    # проверка фильтра "Идентификатор рейса"
    add.input_in_field(add.order_identifier, value='vb-81', click_first=True)
    time.sleep(2)
    add.verify_text_on_page(text='25-67-2448', should_exist=True)
    add.verify_text_on_page(text='24-8-2448', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.order_identifier, value='')


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description('ЛКЗ. Тест фильтров в разделе Регулярные Рейсы ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_filter_regular_order_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход в раздел Все FTL-рейсы
    base.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.regular_list_button,
                        do_assert=True, wait='lst')

    add = OldFTL(base.driver)

    add.move_to_element(add.order_type)
    time.sleep(1)
    add.click_on_the_cross(add.cross_two)

    # проверка фильтра "название шаблона"
    add.input_in_field(add.template_name, value='34-1190564', click_first=True)
    time.sleep(3)
    add.find_text_on_page(text='проект 34-11905643', occurrences=2)
    add.verify_text_on_page(text='25-172973', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.template_name, value='')

    # проверка фильтра "статус"
    add.dropdown_with_input(add.template_status, option_text='Активный')
    time.sleep(1)
    add.verify_text_on_page(text='25-172973', should_exist=True)
    add.verify_text_on_page(text='1-22', should_exist=False)

    # проверка фильтра "тип рейса"
    add.click_and_select_with_arrows(add.order_type, arrow_presses=0)
    time.sleep(1)
    add.verify_text_on_page(text='шаблон 1-11', should_exist=True)
    add.verify_text_on_page(text='25-172973', should_exist=False)

    add.click_and_select_with_arrows(add.order_type, arrow_presses=1)
    time.sleep(1)
    add.verify_text_on_page(text='25-172973', should_exist=True)
    add.verify_text_on_page(text='шаблон 1-11', should_exist=False)

    add.refresh_page()
    time.sleep(3)

    add.move_to_element(add.order_type)
    time.sleep(1)
    add.click_on_the_cross(add.cross_two)

    # проверка фильтра "адрес подачи"
    add.input_in_field(add.filing_address, value='санкт', click_first=True)
    time.sleep(3)
    add.verify_text_on_page(text='11-289754', should_exist=True)
    add.verify_text_on_page(text='34-11905643', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.filing_address, value='')

    # проверка фильтра "адрес доставки"
    add.input_in_field(add.delivery_address, value='Сыктывкар', click_first=True)
    time.sleep(3)
    add.verify_text_on_page(text='Юхнина', should_exist=True)
    add.verify_text_on_page(text='11-289754', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.delivery_address, value='')


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description('ЛКЭ. Тест фильтров в разделе Регулярные Рейсы ')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_filter_regular_order_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход в раздел Все FTL-рейсы
    base.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.regular_list_button,
                        do_assert=True, wait='lst')

    add = OldFTL(base.driver)

    add.move_to_element(add.order_type)
    time.sleep(1)
    add.click_on_the_cross(add.cross_two)

    # проверка фильтра "название шаблона"
    add.input_in_field(add.template_name, value='карт', click_first=True)
    time.sleep(3)
    add.find_text_on_page(text='картограф', occurrences=2)
    add.verify_text_on_page(text='межгородддд', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.template_name, value='')

    # проверка фильтра "тип рейса"
    add.click_and_select_with_arrows(add.order_type, arrow_presses=0)
    time.sleep(1)
    add.verify_text_on_page(text='городдддд 677', should_exist=True)
    add.verify_text_on_page(text='межгородддд', should_exist=False)

    add.click_and_select_with_arrows(add.order_type, arrow_presses=1)
    time.sleep(1)
    add.verify_text_on_page(text='межгородддд', should_exist=True)
    add.verify_text_on_page(text='городдддд 677', should_exist=False)

    add.refresh_page()
    time.sleep(3)

    add.move_to_element(add.order_type)
    time.sleep(1)
    add.click_on_the_cross(add.cross_two)

    # проверка фильтра "адрес подачи"
    add.input_in_field(add.filing_address, value='оруж', click_first=True)
    time.sleep(3)
    add.verify_text_on_page(text='Тамбов', should_exist=True)
    add.verify_text_on_page(text='Екатеринбург', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.filing_address, value='')

    # проверка фильтра "адрес доставки"
    add.input_in_field(add.delivery_address, value='Екатеринбург', click_first=True)
    time.sleep(3)
    add.verify_text_on_page(text='городдддд 677', should_exist=True)
    add.verify_text_on_page(text='Ижевск', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.delivery_address, value='')


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description('ЛКЗ. Тест фильтров в разделе Застрахованные Рейсы ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_filter_insured_order_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход в раздел "Страховые компании"
    base.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.insurers_list_button,
                        do_assert=True, wait='lst')

    add = OldFTL(base.driver)

    add.click_button(add.vsk)
    add.click_button(add.insured_orders)

    add.move_to_element(add.menu_calendar)
    time.sleep(1)
    add.click_on_the_cross(add.cross_four)

    # проверка фильтра "стадии рейса"
    add.dropdown_with_input(add.order_stage, option_text='подбор')
    add.click_button(add.checkbox_one)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-217', should_exist=True)
    add.verify_text_on_page(text='R-25-79-2448-1', should_exist=False)

    add.move_to_element(add.order_stage)
    time.sleep(1)
    add.click_on_the_cross(add.cross_three)

    add.dropdown_with_input(add.order_stage, option_text='исполнение')
    add.click_button(add.checkbox_two)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-218', should_exist=True)
    add.verify_text_on_page(text='R-25-79-2448-1', should_exist=False)

    add.move_to_element(add.order_stage)
    time.sleep(1)
    add.click_on_the_cross(add.cross_three)

    add.dropdown_with_input(add.order_stage, option_text='расч')
    add.click_button(add.checkbox_three)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-219', should_exist=True)
    add.verify_text_on_page(text='R-25-77-2448-1', should_exist=False)

    add.move_to_element(add.order_stage)
    time.sleep(1)
    add.click_on_the_cross(add.cross_three)

    add.dropdown_with_input(add.order_stage, option_text='отме')
    add.click_button(add.checkbox_four)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-220', should_exist=True)
    add.verify_text_on_page(text='R-25-79-2448-1', should_exist=False)

    add.move_to_element(add.order_stage)
    time.sleep(1)
    add.click_on_the_cross(add.cross_three)

    add.refresh_page()
    time.sleep(3)

    # проверка фильтра "номер рейса"
    add.input_in_field(add.order_number_three, value='79-')
    time.sleep(3)
    add.verify_text_on_page(text='R-25-79-2448-1', should_exist=True)
    add.verify_text_on_page(text='R-25-77-2448-1', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.order_number_three, value='')

    # проверка фильтра "номер договора"
    add.input_in_field(add.contract_number, value='111')
    time.sleep(3)
    add.verify_text_on_page(text='1-111', should_exist=True)
    time.sleep(1)
    add.backspace_and_input(add.contract_number, value='')


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description('ЛКЭ. Тест фильтров в разделе Застрахованные Рейсы ')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_filter_insured_order_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход в раздел "Страховые компании"
    base.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.insurers_list_button,
                        do_assert=True, wait='lst')

    add = OldFTL(base.driver)

    add.click_button(add.vsk)
    add.click_button(add.insured_orders)

    add.move_to_element(add.menu_calendar)
    time.sleep(1)
    add.click_on_the_cross(add.cross_four)

    # проверка фильтра "стадии рейса"
    add.dropdown_with_input(add.order_stage, option_text='подбор')
    add.click_button(add.checkbox_one)
    time.sleep(3)
    add.verify_text_on_page(text='158-2447', should_exist=True)
    add.verify_text_on_page(text='159-2447', should_exist=False)

    add.move_to_element(add.order_stage)
    time.sleep(1)
    add.click_on_the_cross(add.cross_three)

    add.dropdown_with_input(add.order_stage, option_text='исполнение')
    add.click_button(add.checkbox_two)
    time.sleep(3)
    add.verify_text_on_page(text='159-2447', should_exist=True)
    add.verify_text_on_page(text='158-2447', should_exist=False)

    add.move_to_element(add.order_stage)
    time.sleep(1)
    add.click_on_the_cross(add.cross_three)

    add.dropdown_with_input(add.order_stage, option_text='расч')
    add.click_button(add.checkbox_three)
    time.sleep(3)
    add.verify_text_on_page(text='160-2447', should_exist=True)
    add.verify_text_on_page(text='161-2447', should_exist=False)

    add.move_to_element(add.order_stage)
    time.sleep(1)
    add.click_on_the_cross(add.cross_three)

    add.dropdown_with_input(add.order_stage, option_text='отме')
    add.click_button(add.checkbox_four)
    time.sleep(3)
    add.verify_text_on_page(text='161-2447', should_exist=True)
    add.verify_text_on_page(text='160-2447', should_exist=False)

    add.move_to_element(add.order_stage)
    time.sleep(1)
    add.click_on_the_cross(add.cross_three)

    add.refresh_page()
    time.sleep(3)

    # проверка фильтра "номер рейса"
    add.input_in_field(add.order_number_three, value='25-161')
    time.sleep(3)
    add.verify_text_on_page(text='R-25-161-2447-1', should_exist=True)
    add.verify_text_on_page(text='R-25-160-2447-1', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.order_number_three, value='')

    # проверка фильтра "номер договора"
    add.input_in_field(add.contract_number, value='001')
    time.sleep(3)
    add.verify_text_on_page(text='R-25-163', should_exist=True)
    add.verify_text_on_page(text='R-25-162', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.contract_number, value='')


@allure.story("Extended test")
@allure.feature('Фильтры')
@allure.description('ЛКП. Тест фильтров в разделе Застрахованные Рейсы ')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_filter_insured_order_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход в раздел "Страховые компании"
    base.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.insurers_list_button,
                        do_assert=True, wait='lst')

    add = OldFTL(base.driver)

    add.click_button(add.vsk)
    add.click_button(add.insured_orders)

    add.move_to_element(add.menu_calendar)
    time.sleep(1)
    add.click_on_the_cross(add.cross_four)

    # проверка фильтра "стадии рейса"
    add.dropdown_with_input(add.order_stage, option_text='подбор')
    add.click_button(add.checkbox_one)
    time.sleep(3)
    add.verify_text_on_page(text='37099', should_exist=True)
    add.verify_text_on_page(text='R-25-63-2449-1', should_exist=False)

    add.move_to_element(add.order_stage)
    time.sleep(1)
    add.click_on_the_cross(add.cross_three)

    add.dropdown_with_input(add.order_stage, option_text='исполнение')
    add.click_button(add.checkbox_two)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-60-2449-1', should_exist=True)
    add.verify_text_on_page(text='R-25-61-2449-1', should_exist=False)

    add.move_to_element(add.order_stage)
    time.sleep(1)
    add.click_on_the_cross(add.cross_three)

    add.dropdown_with_input(add.order_stage, option_text='расч')
    add.click_button(add.checkbox_three)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-63-2449-1', should_exist=True)
    add.verify_text_on_page(text='R-25-58-2449-1', should_exist=False)

    add.move_to_element(add.order_stage)
    time.sleep(1)
    add.click_on_the_cross(add.cross_three)

    add.dropdown_with_input(add.order_stage, option_text='отме')
    add.click_button(add.checkbox_four)
    time.sleep(3)
    add.verify_text_on_page(text='R-25-61-2449-1', should_exist=True)
    add.verify_text_on_page(text='R-25-60-2449-1', should_exist=False)

    add.move_to_element(add.order_stage)
    time.sleep(1)
    add.click_on_the_cross(add.cross_three)

    add.refresh_page()
    time.sleep(3)

    add.move_to_element(add.menu_calendar)
    time.sleep(1)
    add.click_on_the_cross(add.cross_four)

    # проверка фильтра "номер рейса"
    add.input_in_field(add.order_number_three, value='59-')
    time.sleep(3)
    add.verify_text_on_page(text='R-25-59-2449-1', should_exist=True)
    add.verify_text_on_page(text='R-25-58-2449-1', should_exist=False)
    time.sleep(1)
    add.backspace_and_input(add.order_number_three, value='')

    # проверка фильтра "номер договора"
    add.input_in_field(add.contract_number, value='111')
    time.sleep(3)
    add.verify_text_on_page(text='1-111', should_exist=True)
    time.sleep(1)
    add.backspace_and_input(add.contract_number, value='')
