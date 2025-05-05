import os
import time
import allure
import pytest
from pages.add_new_cdr_page import AddCdr

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Игнорировать INFO и WARNING сообщения


@allure.story("smoke")
@allure.feature('Создание заявки на доставку груза')
@allure.description('ЛКЗ, Тестирование: Создание ФТЛ заявки - город, грузоперевозка, новое ГМ, публикация на ЛКП')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_add_new_ftl_lkz_lkp(base_fixture, domain, request):
    base, sidebar = base_fixture
    time.sleep(2)

    with allure.step("Открытие формы создания новой заявки"):
        sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_delivery_request_button)
        add = AddCdr(base.driver)
        time.sleep(2)

    with allure.step("Выбор типа заявки: Доставку конкретным Типом ТС (FTL)"):
        add.dropdown_without_input(add.change_ftl, "Доставку конкретным Типом ТС (FTL)")

    with allure.step("Проставление даты и времени"):
        add.change_date_time()

    with allure.step("Генерация уникального ID для заявки"):
        unique_id = add.input_unique_id()
        assert unique_id is not None, "Уникальный ID не был сгенерирован."
        # Сохраняем уникальный ID в кэш
        request.config.cache.set("unique_id", unique_id)

    with allure.step("Выбор данных по транспортному средству"):
        add.click_button(add.type_of_road_transport)
        add.click_button(add.type_cargo)
        add.dropdown_without_input(add.type_transport, "1.5т / 9м3 / 4пал.")
        add.click_button(add.change_body_type)
        add.click_button(add.change_closed_body_type)

    with allure.step("Добавление адресов"):
        add.change_address()

    with allure.step("Выбор возможности изменять маршрут водителем"):
        add.random_point_change_type()

    with allure.step("Создание нового уникального ГМ"):
        add.new_cargo_place()

    with allure.step("Прокрутка до кнопки 'Сохранить и опубликовать'"):
        add.scroll_to_element(add.save_and_publish_button)

    with allure.step("Выбор полного списка документов"):
        add.required_documents()

    with allure.step("Публикация заявки на ЛКЭ и ЛКП"):
        add.save_and_publish_lkp()
        time.sleep(3)


@allure.story("smoke")
@allure.feature("Подтвержение и завершение рейса от ЛКЗ за ЛКП")
@allure.description("ЛКП, Тестирование: Подтверждаем заявку")
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_lkp_confirm_delivery(base_fixture, domain, request):
    base, sidebar = base_fixture
    time.sleep(2)

    with allure.step("Открытие раздела Заявки на доставку Груза"):
        sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.new_cdr_sidebar)
        add = AddCdr(base.driver)
        time.sleep(2)

    with allure.step("Нажимаем на кнопку сбросить"):
        add.click_button(add.click_reset)
        time.sleep(2)

    with allure.step("Выбираем заявку с уникальным id"):
        add.change_request_for_id(request)
        time.sleep(2)

    with allure.step("Жмем принять обязательства"):
        add.click_button(add.click_confirm_cdr)

    with allure.step("Назначаем ТС на рейс"):
        add.change_ts_and_driver()

    with allure.step("Стартуем рейс"):
        add.start_cdr()
        time.sleep(2)

    with allure.step("Заполняем время точек на рейсе"):
        add.change_time_to_address()

    with allure.step("Завершаем рейс через ЛК"):
        add.complete_cdr()


@allure.story("smoke")
@allure.feature('Создание заявки на доставку груза')
@allure.description('ЛКЗ, Тестирование: Создание ФТЛ заявки - город, грузоперевозка, новое ГМ, публикация на ЛКЭ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_add_new_ftl_lkz_lke(base_fixture, domain, request):
    base, sidebar = base_fixture
    time.sleep(2)

    with allure.step("Открытие формы создания новой заявки"):
        sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_delivery_request_button)
        add = AddCdr(base.driver)
        time.sleep(2)

    with allure.step("Выбор типа заявки: Доставку конкретным Типом ТС (FTL)"):
        add.dropdown_without_input(add.change_ftl, "Доставку конкретным Типом ТС (FTL)")

    with allure.step("Проставление даты и времени"):
        add.change_date_time()

    with allure.step("Генерация уникального ID для заявки"):
        unique_id = add.input_unique_id()
        assert unique_id is not None, "Уникальный ID не был сгенерирован."
        # Сохраняем уникальный ID в кэш
        request.config.cache.set("unique_id", unique_id)

    with allure.step("Выбор данных по транспортному средству"):
        add.click_button(add.type_of_road_transport)
        add.click_button(add.type_cargo)
        add.dropdown_without_input(add.type_transport, "1.5т / 9м3 / 4пал.")
        add.click_button(add.change_body_type)
        add.click_button(add.change_closed_body_type)

    with allure.step("Добавление адресов"):
        add.change_address()

    with allure.step("Выбор возможности изменять маршрут водителем"):
        add.random_point_change_type()

    with allure.step("Создание нового уникального ГМ"):
        add.new_cargo_place()

    with allure.step("Прокрутка до кнопки 'Сохранить и опубликовать'"):
        add.scroll_to_element(add.save_and_publish_button)

    with allure.step("Выбор полного списка документов"):
        add.required_documents()

    with allure.step("Публикация заявки на ЛКЭ"):
        add.save_and_publish_lke()
        time.sleep(3)


@allure.story("smoke")
@allure.feature('Подтвержение и перепубликация рейса от ЛКЗ к ЛКЭ, ЛКЭ к ЛКП')
@allure.description('ЛКЗ, Тестирование: Принятие ФТЛ заявки за ЛКЭ и перепубликация на ЛКП')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_republishing_new_ftl_lke_lkp(base_fixture, domain, request):
    base, sidebar = base_fixture
    time.sleep(2)

    with allure.step("Открытие формы создания новой заявки"):
        sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.new_cdr_sidebar)
        add = AddCdr(base.driver)
        time.sleep(2)

    with allure.step("Нажимаем на кнопку сбросить"):
        add.click_button(add.click_reset)
        time.sleep(2)

    with allure.step("Выбираем заявку с уникальным id"):
        add.change_request_for_id(request)
        time.sleep(2)

    # with allure.step("Жмем принять обязательства"):
    # add.click_button(add.click_confirm_cdr)
    # time.sleep(2)

    with allure.step("Перепубликуем заявку от ЛКЭ на ЛКП"):
        add.republish_cdr_lke_lkp()


@allure.story("smoke")
@allure.feature('Подтвержение и завершение рейса от ЛКЗ к ЛКЭ, ЛКЭ к ЛКП')
@allure.description('ЛКЗ, Тестирование: Принятие ФТЛ заявки за ЛКП и pfdthitybt')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_republishing_new_ftl_lke_lkp(base_fixture, domain, request):
    base, sidebar = base_fixture
    time.sleep(2)

    with allure.step("Открытие раздела Заявки на доставку Груза"):
        sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.new_cdr_sidebar)
        add = AddCdr(base.driver)
        time.sleep(2)

    with allure.step("Нажимаем на кнопку сбросить"):
        add.click_button(add.click_reset)
        time.sleep(2)

    with allure.step("Выбираем заявку с уникальным id"):
        add.change_request_for_id(request)
        time.sleep(2)


@allure.story("smoke")
@allure.feature('Создание заявки на доставку груза')
@allure.description('ЛКЗ, Тестирование: Создание ЛТЛ заявки - новое ГМ, адреса, публикация')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_add_new_ltl_lkz(base_fixture, domain):
    base, sidebar = base_fixture
    time.sleep(2)

    with allure.step("Открытие формы создания новой заявки"):
        sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_delivery_request_button)
        add = AddCdr(base.driver)
        time.sleep(2)

    with allure.step("Выбор типа заявки: Доставку ГМ (LTL)"):
        add.dropdown_without_input(add.change_ftl, "Доставку ГМ (LTL)")

    with allure.step("Проставление даты и времени"):
        add.change_date_time()
        time.sleep(2)
        add.change_date_second_time()

    with allure.step("Добавление адресов"):
        add.change_address()

    with allure.step("Создание нового ГМ для ЛТЛ"):
        add.new_cargo_place_ltl()

    with allure.step("Публикация заявки"):
        add.save_and_publish_ltl()


@allure.story("smoke")
@allure.feature('Создание заявки на доставку груза')
@allure.description('ЛКЗ, Тестирование: Создание ФТЛ заявки - город, грузоперевозка, новое ГМ, публикация, все допы.')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_add_new_ftl_lkz_dop(base_fixture, domain):
    base, sidebar = base_fixture
    time.sleep(2)

    with allure.step("Открытие формы создания новой заявки"):
        sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_delivery_request_button)
        add = AddCdr(base.driver)
        time.sleep(2)

    with allure.step("Выбор типа заявки: Доставку конкретным Типом ТС (FTL)"):
        add.dropdown_without_input(add.change_ftl, "Доставку конкретным Типом ТС (FTL)")

    with allure.step("Проставление даты и времени"):
        add.change_date_time()

    with allure.step("Генерация уникального ID для заявки"):
        add.input_unique_id()

    with allure.step("Выбор данных по транспортному средству"):
        add.click_button(add.type_of_road_transport)
        add.click_button(add.type_cargo)
        add.dropdown_without_input(add.type_transport, "1.5т / 9м3 / 4пал.")
        add.click_button(add.change_body_type)
        add.click_button(add.change_closed_body_type)

    with allure.step("Добавление доп. услуг"):
        add.add_additional_requirements()

    with allure.step("Прокрутка до кнопки 'Сохранить и опубликовать'"):
        add.scroll_to_element(add.save_and_publish_button)

    with allure.step("Добавление адресов"):
        add.change_address()

    with allure.step("Выбор возможности изменять маршрут водителем"):
        add.random_point_change_type()

    with allure.step("Создание нового уникального ГМ"):
        add.new_cargo_place()

    with allure.step("Выбор полного списка документов"):
        add.required_documents()

    with allure.step("Публикация заявки на ЛКЭ и ЛКП"):
        add.save_and_publish_dop()
        time.sleep(3)


@allure.story("smoke")
@allure.feature('Создание заявки на доставку груза')
@allure.description(
    'ЛКЗ, Тестирование: Создание ФТЛ заявки - город, грузоперевозка, новое ГМ, публикация, ПРР+Страховка.')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_add_new_ftl_lkz_asr(base_fixture, domain):
    base, sidebar = base_fixture
    time.sleep(2)

    with allure.step("Открытие формы создания новой заявки"):
        sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_delivery_request_button)
        add = AddCdr(base.driver)
        time.sleep(2)

    with allure.step("Выбор типа заявки: Доставку конкретным Типом ТС (FTL)"):
        add.dropdown_without_input(add.change_ftl, "Доставку конкретным Типом ТС (FTL)")

    with allure.step("Проставление даты и времени"):
        add.change_date_time()

    with allure.step("Генерация уникального ID для заявки"):
        add.input_unique_id()

    with allure.step("Выбор данных по транспортному средству"):
        add.click_button(add.type_of_road_transport)
        add.click_button(add.type_cargo)
        add.dropdown_without_input(add.type_transport, "1.5т / 9м3 / 4пал.")
        add.click_button(add.change_body_type)
        add.click_button(add.change_closed_body_type)

    with allure.step("Добавление доп. услуг"):
        add.add_additional_requirements()

    with allure.step("Добавление адресов"):
        add.change_address()

    with allure.step("Прокрутка до кнопки 'Сохранить и опубликовать'"):
        add.scroll_to_element(add.save_and_publish_button)

    with allure.step("Выбор возможности изменять маршрут водителем"):
        add.random_point_change_type()

    with allure.step("Создание нового уникального ГМ"):
        add.new_cargo_place()

    with allure.step("Выбор полного списка документов"):
        add.required_documents()

    with allure.step("Добавление услуги ПРР"):
        add.additional_service_add_prr()

    with allure.step("Добавление страховки"):
        add.additional_service_add_insurance()

    with allure.step("Публикация заявки на ЛКЭ и ЛКП"):
        add.save_and_publish_asr()
        time.sleep(3)
