import time
import allure
import pytest
from pages.cargo_place_add_page import CargoPlaceAdd
from pages.cargo_place_list_page import CargoPlaceList
from pages.request_delivery_add_page import DeliveryAdd
from pages.cdr_ftl_page import AddCdr
from tests.base_test import base_test_with_login


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
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")

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
    ftl.add_base_ftl()
    # Прокрутка страницы вниз для прикрепления грузоместа
    ftl.scroll_to_element(ftl.attach_cargo_place_button)
    time.sleep(1)
    ftl.click_button(ftl.attach_cargo_place_button)
    ftl.click_button(ftl.existing_cargo_place_button, wait="lst")

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
@allure.description('ЛКЭ. Тест перепубликации FTL заявки: тип - Город, подача - Сейчас +30мин, гм - Создаем в тесте, '
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
    ftl.click_button(ftl.existing_cargo_place_button, wait="lst")

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

    