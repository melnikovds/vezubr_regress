import time
import allure
import pytest
import re
import random
from selenium.webdriver.common.by import By
from tests.base_test import base_test_with_login
from pages.cargo_place_add_page import CargoPlaceAdd
from pages.cargo_place_list_page import CargoPlaceList
from pages.request_delivery_add_page import DeliveryAdd
from pages.cdr_ftl_page import AddCdr
from pages.filters_new_ftl_page import NewFtlFilters


@allure.story("Smoke test")
@allure.feature('Создание FTL заявок')
@allure.description('ЛКЗ. Тест создания FTL заявки: тип - Город, подача - Сейчас +30мин, гм - Создаем в тесте, '
                    'ТС - Груз 2т / 14м3 / 7пал., кузов - Закрытый, адреса - Конкретные, публикация - Позже')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
@pytest.mark.smoke
def test_ftl_request_no_publish_add_lkz(base_fixture, domain):
    # Инициализация базовых объектов и авторизация под ролью 'lkz'
    base, sidebar = base_fixture

    # Переход к списку грузомест
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    cp_list = CargoPlaceList(base.driver)
    # Клик по кнопке добавления грузоместа
    # cp_list.click_button(cp_list.add_cargo_place_button, wait="form")
    cp_list.click_button(cp_list.add_cargo_place_button)
    time.sleep(3)

    add_cp = CargoPlaceAdd(base.driver)
    # Добавление базового грузоместа
    cp_stamp = add_cp.add_base_cargo_place_lkz()

    # Переход к созданию новой FTL заявки
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_delivery_request_button,
                           do_assert=True, wait="form")

    ftl = DeliveryAdd(base.driver)
    # Выбор типа заявки - Доставка ГМ (FTL)
    # ftl.dropdown_with_input(ftl.request_type_select, "Доставку конкретным Типом ТС (FTL)")
    add = AddCdr(base.driver)
    add.dropdown_without_input(add.change_ftl, "Доставку конкретным Типом ТС (FTL)")
    # Заполнение базовой информации для FTL заявки
    ftl.add_base_ftl_lkz()
    # Прокрутка страницы вниз для прикрепления грузоместа
    ftl.scroll_to_element(ftl.attach_cargo_place_button)
    time.sleep(1)
    ftl.click_button(ftl.attach_cargo_place_button)
    # ftl.click_button(ftl.existing_cargo_place_button, wait="lst")
    ftl.click_button(ftl.existing_cargo_place_button)
    time.sleep(3)

    cpl = CargoPlaceList(base.driver)
    # Поиск и выбор созданного грузоместа по штрихкоду
    cpl.input_in_field(cpl.barcode_filter_input, cp_stamp, wait="lst")
    cpl.click_button(cpl.auto_attachment_button)
    time.sleep(1)
    cpl.scroll_to_element(cpl.save_gm_button)
    cpl.click_button(cpl.save_gm_button)
    time.sleep(1)
    ftl.click_button(ftl.close_button)
    # Клик по кнопке создания заявки
    ftl.scroll_to_element(ftl.publish_later_button)
    time.sleep(1)
    # Публикация заявки позже
    ftl.click_button(ftl.publish_later_button, do_assert=True)
    time.sleep(1)
    ftl.click_button(ftl.create_button)
    time.sleep(1)
    # Завершение теста
    sidebar.test_finish()
#
#
# @allure.story("Smoke test")
# @allure.feature('Создание FTL заявок')
# @allure.description('ЛКЭ. Тест создания FTL заявки: тип - Город, подача - Сейчас +30мин, гм - Создаем в тесте, '
#                     'ТС - Груз 0.5т, кузов - Закрытый, адреса - Конкретные, публикация - Позже')
# def test_ftl_request_no_publish_add_lke(domain):
#     # Инициализация базовых объектов и авторизация под ролью 'lke'
#     base, sidebar = base_test_with_login(domain=domain, role='lke')
#
#     # Переход к списку грузомест
#     sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
#                            do_assert=True, wait="lst")
#     time.sleep(1)
#
#     cp_list = CargoPlaceList(base.driver)
#     # Клик по кнопке добавления грузоместа
#     cp_list.click_button(cp_list.add_cargo_place_button, wait="form")
#
#     add_cp = CargoPlaceAdd(base.driver)
#     # Выбор владельца грузоместа "Auto LKZ"
#     add_cp.dropdown_click_input_click(add_cp.cargo_place_owner_select, "Auto LKZ")
#     # Добавление базового грузоместа
#     cp_stamp = add_cp.add_base_cargo_place_lke()
#
#     # Переход к созданию новой FTL заявки
#     sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_delivery_request_button,
#                            do_assert=True, wait="form")
#
#     ftl = DeliveryAdd(base.driver)
#     # Выбор типа заявки - Доставка ГМ (FTL)
#     ftl.dropdown_click_input_click(ftl.request_type_select, "Доставку конкретным Типом ТС (FTL)")
#     # Выбор владельца заявки
#     ftl.dropdown_click_input_click(ftl.request_owner_select, "Auto LKZ")
#     # Заполнение базовой информации для FTL заявки
#     ftl.add_base_ftl()
#     # Прокрутка страницы вниз для прикрепления грузоместа
#     ftl.scroll_to_bottom()
#     ftl.click_button(ftl.attach_cargo_place_button)
#     ftl.click_button(ftl.existing_cargo_place_button, wait="lst")
#
#     cpl = CargoPlaceList(base.driver)
#     # Поиск и выбор созданного грузоместа по штрихкоду
#     cpl.input_in_field(cpl.barcode_filter_input, cp_stamp, wait="lst")
#     cpl.click_button(cpl.auto_attachment_button)
#     cpl.click_button(cpl.close_button)
#
#     # Клик по кнопке создания заявки
#     ftl.click_button(ftl.create_button)
#     time.sleep(1)
#     # Публикация заявки позже
#     ftl.click_button(ftl.publish_later_button, do_assert=True)
#
#     # Завершение теста
#     sidebar.test_finish()


@allure.story("Smoke test")
@allure.feature('Создание FTL заявок')
@allure.description('ЛКЭ. Тест перепубликации FTL заявки: тип - Межгород, подача - Сейчас +30мин, гм - Создаем в тесте, '
                    'ТС - Груз 2т / 14м3 / 7пал., кузов - Закрытый, адреса - Конкретные, публикация - от внутреннего ГВ на внутреннего ПВ')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
@pytest.mark.smoke
def test_ftl_request_republish_lke(base_fixture, domain):
    # Инициализация базовых объектов
    base, sidebar = base_fixture

    # Переход к списку грузомест
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    cp_list = CargoPlaceList(base.driver)
    # Клик по кнопке добавления грузоместа
    cp_list.click_button(cp_list.add_cargo_place_button)
    time.sleep(3)

    add_cp = CargoPlaceAdd(base.driver)
    # Добавление базового грузоместа
    add_cp.dropdown_without_input(add_cp.cargo_place_owner_select, "ООО ТЕХТРЕЙД")
    cp_stamp = add_cp.add_full_cargo_place_inner_lke()

    # Переход к созданию новой FTL заявки
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_delivery_request_button,
                           do_assert=True, wait="form")

    ftl = DeliveryAdd(base.driver)
    # Выбор типа заявки - Доставка ГМ (FTL)
    # ftl.dropdown_with_input(ftl.request_type_select, "Доставку конкретным Типом ТС (FTL)")
    add = AddCdr(base.driver)
    add.dropdown_without_input(add.change_ftl, "Доставку конкретным Типом ТС (FTL)")
    # Заполнение базовой информации для FTL заявки
    ftl.dropdown_with_input(ftl.request_owner_select, "ООО ТЕХТРЕЙД")
    ftl.add_base_ftl_inner()
    # Прокрутка страницы вниз для прикрепления грузоместа
    ftl.scroll_to_element(ftl.attach_cargo_place_button)
    time.sleep(1)
    ftl.click_button(ftl.attach_cargo_place_button)
    ftl.click_button(ftl.existing_cargo_place_button)
    time.sleep(3)

    cpl = CargoPlaceList(base.driver)
    # Поиск и выбор созданного грузоместа по штрихкоду
    cpl.input_in_field(cpl.barcode_filter_input, cp_stamp)
    time.sleep(3)
    cpl.click_button(cpl.auto_attachment_button)
    time.sleep(1)
    cpl.scroll_to_element(cpl.save_gm_button)
    cpl.click_button(cpl.save_gm_button)
    time.sleep(1)
    ftl.click_button(ftl.close_button)
    # Клик по кнопке создания заявки
    ftl.scroll_to_element(ftl.publish_now_button)
    ftl.click_button(ftl.publish_now_button)
    time.sleep(3)
    # Публикация Заявки
    ftl.click_button(ftl.rate_radio, wait_type='located')
    ftl.input_in_field(ftl.rate_input, value='17700')
    ftl.click_button(ftl.producer_lke_button, wait_type='located')
    ftl.click_button(ftl.publish_button)
    time.sleep(3)

    # Находим элемент с сообщением
    element = base.driver.find_element(By.XPATH, "//div[@class='ant-modal-confirm-content']")
    text = element.text.strip()

    # Извлекаем всё после "№" — только допустимые символы
    match = re.search(r'№([A-Za-z0-9\-]+)', text)

    if match:
        application_number = match.group(1)  # например: '25-VZ-494'
        print(f"Номер заявки: {application_number}")
    else:
        raise ValueError(f"Не удалось найти номер заявки в тексте: {text}")

    ftl.click_button(ftl.ok_button)
    time.sleep(3)

    # Принятие Заявки Экспедитором
    add = NewFtlFilters(base.driver)
    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    add.input_in_field(add.request_number, value=application_number)
    time.sleep(3)
    addd = AddCdr(base.driver)
    addd.click_button(addd.click_first_element)
    time.sleep(3)
    addd.click_button(addd.click_confirm_cdr)

    time.sleep(3)
    # Передача Заявки Подрядчику
    addd.click_button(addd.click_options)
    addd.click_button(addd.processing_application_services)
    time.sleep(2)
    addd.click_on_the_cross(addd.choose_main_service)
    addd.click_button(addd.hand_over_contractor)
    time.sleep(2)
    addd.scroll_to_element(addd.create_and_publish_button)
    time.sleep(2)
    addd.click_button(addd.create_and_publish_button)
    addd.click_button(addd.change_one_time_tariff)
    time.sleep(2)
    addd.input_in_field(addd.change_publication_rate, str(random.randint(100000, 800000)))
    # Выбор подрядчиков через выпадающий список
    addd.input_in_field(addd.select_contractors_lkp, "Автоваз")
    time.sleep(2)
    addd.click_button(addd.select_all_contractors, wait_type='located')
    time.sleep(1)
    # Подтверждение публикации заказа
    addd.click_button(addd.publish_button_lke)
    time.sleep(3)

    # Находим элемент с сообщением
    element = base.driver.find_element(By.XPATH, "//div[@class='ant-modal-confirm-content']")
    text = element.text.strip()

    # Извлекаем всё после "№" — только допустимые символы
    match = re.search(r'№([A-Za-z0-9\-]+)', text)

    if match:
        application_number2 = match.group(1)  # например: '25-VZ-494'
        print(f"Номер заявки: {application_number2}")
    else:
        raise ValueError(f"Не удалось найти номер заявки в тексте: {text}")

    addd.click_button(addd.publish_ok_button_lke)

    # Проверка данных Заявки
    add.reload_page()
    time.sleep(5)
    addd.verify_text_on_page(text='Подтверждён')
    addd.verify_text_on_page(text=application_number2)
    addd.verify_text_on_page(text='Ставка')






    