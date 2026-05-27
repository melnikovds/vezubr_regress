import time
import allure
import pytest
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.request_old_ftl_add_page import FTLAdd
from pages.login_page import Login
from pages.filters_old_ftl_page import OldFTL
from pages.registries_old_page import RegistriesOld


@allure.story("Smoke test")
@allure.feature('Создание FTL заявок')
@allure.description('Первый тестовый сценарий')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_scenario_one_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к созданию новой FTL заявки
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.new_ftl_city_button,
                           do_assert=True)

    ftl = FTLAdd(base.driver)
    # Сброс ранее введенных и сохраненных данных
    ftl.click_button(ftl.cancel_button)

    # Переход к созданию новой FTL заявки
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.new_ftl_city_button,
                           do_assert=True)

    # Установка даты подачи заявки на сегодня
    ftl.click_button(ftl.start_date_field)
    ftl.click_button(ftl.today_button)
    # Установка времени подачи заявки через 3 часа от текущего времени
    ftl.click_button(ftl.start_time_field)
    new_time = ftl.naw_time_change(180)
    ftl.input_in_field(ftl.start_time_input, new_time)
    time.sleep(1)
    # Выбор категории заявки
    ftl.click_button(ftl.request_category_select)
    ftl.click_button(ftl.select_freight)
    # Выбор типа ТС
    ftl.click_button(ftl.vehicle_type_select)
    ftl.dropdown_with_input(ftl.vehicle_type_select, "1.5т / 9м3 / 4пал.")
    # Выбор типа кузова
    ftl.click_button(ftl.vehicle_body_select)
    ftl.click_button(ftl.body_type_closed_checkbox)

    time.sleep(1)

    # Выбор первого адреса из списка
    ftl.click_button(ftl.first_address_select)
    time.sleep(3)
    ftl.input_in_field(ftl.address_filter, "Бассейная")
    time.sleep(3)
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    time.sleep(3)
    # Выбор второго адреса из списка
    ftl.click_button(ftl.second_address_select)
    time.sleep(3)
    ftl.input_in_field(ftl.address_filter, "Софийская")
    time.sleep(3)
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    time.sleep(3)
    # Выбор третьего адреса из списка
    ftl.click_button(ftl.third_address_select)
    time.sleep(3)
    ftl.input_in_field(ftl.address_filter, "Турку")
    time.sleep(3)
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    time.sleep(3)
    # Выбор четвёртого адреса из списка
    ftl.click_button(ftl.fourth_address_select)
    time.sleep(3)
    ftl.input_in_field(ftl.address_filter, "Белы Куна")
    time.sleep(3)
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    time.sleep(1)
    ftl.scroll_to_element(element_info=ftl.publication_button)
    time.sleep(1)

    # Добавление дополнительных данных
    ftl.click_button(ftl.additional_requirements)
    ide_code = FTLAdd.generate_ide_code()  # вызов метода
    ftl.input_in_field(ftl.order_identifier, value=ide_code)
    time.sleep(1)

    # Ожидание завершения расчета стоимости
    base.get_element(ftl.calculate_finish)
    # Публикация заявки с использованием ставки
    ftl.click_button(ftl.publication_button)
    time.sleep(1)
    ftl.click_button(ftl.rate_button, wait_type='located')
    time.sleep(1)
    ftl.input_in_field(ftl.rate_amount, value='10000')
    ftl.click_button(ftl.producer_select)
    # ftl.click_button(ftl.select_all_producer)
    time.sleep(1)
    # ftl.click_on_the_cross(cross_info=ftl.perevozchik_cross)
    # ftl.click_on_the_cross(cross_info=ftl.lkp_cross)
    ftl.click_button(ftl.lke_select_checkbox)
    # ftl.click_button(ftl.producer_select_text)
    ftl.click_outside()
    time.sleep(1)
    ftl.click_button(ftl.publish_button)
    ftl.click_button(ftl.continue_button, do_assert=True)

    wait = WebDriverWait(base.driver, 10)

    element = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'ant-modal-confirm-content')]")
        )
    )

    # ждём появления номера
    wait.until(lambda driver: "№" in element.text or "#" in element.text)

    text = element.text.strip()
    print(f"TEXT FROM MODAL: {repr(text)}")

    match = re.search(r'[№#N°]\s*([A-Za-z0-9\-]+)', text)

    if match:
        application_number = match.group(1)
        print(f"Номер заявки: {application_number}")
    else:
        raise ValueError(f"Не удалось найти номер заявки в тексте: {text}")


    ftl.click_button(ftl.confirm_add_button, wait="lst")

    # # Находим элемент с сообщением
    # element = base.driver.find_element(By.XPATH, "//div[@class='ant-modal-confirm-content']")
    # text = element.text.strip()
    #
    # # Извлекаем всё после "№" — только допустимые символы
    # # match = re.search(r'№([A-Za-z0-9\-]+)', text)
    # match = re.search(r'№\s*([\w/-]+)', text)
    #
    # if match:
    #     application_number = match.group(1)  # например: '25-VZ-494'
    #     print(f"Номер заявки: {application_number}")
    # else:
    #     raise ValueError(f"Не удалось найти номер заявки в тексте: {text}")
    #
    # print(match)

    # ftl.click_button(ftl.continue_button, do_assert=True)
    # ftl.click_button(ftl.confirm_add_button, wait="lst")

    # Выход из ЛКЗ
    sidebar.click_button(sidebar.exit_button)
    time.sleep(3)

    # Вход за ЛКЭ
    login = Login(base.driver, domain)
    login.authorization("lke")
    time.sleep(10)

    sidebar.click_button(sidebar.sidebar_button)

    # Переход в раздел Активные FTL-заявки
    base.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_active_list_button,
                        do_assert=True, wait='lst')

    add = OldFTL(base.driver)
    # Сброс фильтров
    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    # add.input_in_field(add.request_number, value=application_number, click_first=True)
    add.input_in_field(add.request_identifier, value=ide_code, click_first=True)
    time.sleep(2)
    # Перепубликция заявки
    ftl.click_button(ftl.click_on_request)
    time.sleep(2)
    ftl.click_button(ftl.accept_obligations)
    time.sleep(2)
    # ftl.click_button(ftl.order_accept)
    # time.sleep(2)
    ftl.click_button(ftl.republication_button)
    time.sleep(2)
    ftl.scroll_to_element(ftl.publication_button)

    # Публикация заявки с использованием ставки
    ftl.click_button(ftl.publication_button)
    time.sleep(1)
    ftl.click_button(ftl.rate_button, wait_type='located')
    time.sleep(1)
    ftl.click_button(ftl.producer_select)
    time.sleep(1)
    ftl.click_button(ftl.lkp_select_checkbox)
    ftl.click_outside()
    time.sleep(1)
    ftl.click_button(ftl.publish_button)
    ftl.click_button(ftl.continue_share_button, do_assert=True)
    ftl.click_button(ftl.share_ok)

    # Выход из ЛКЭ
    sidebar.click_button(sidebar.exit_button)
    time.sleep(3)

    # Вход за ЛКП
    login = Login(base.driver, domain)
    login.authorization("lkp")
    time.sleep(10)

    sidebar.click_button(sidebar.sidebar_button)

    # Переход в раздел Активные FTL-заявки
    base.move_and_click(move_to=sidebar.orders_old_hover_lkp, click_to=sidebar.ftl_active_list_button,
                        do_assert=True, wait='lst')

    # Сброс фильтров
    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    add.input_in_field(add.request_identifier, value=ide_code, click_first=True)
    time.sleep(2)
    # Принятие заявки
    ftl.click_button(ftl.click_on_request)
    time.sleep(2)
    ftl.click_button(ftl.accept_obligations)
    time.sleep(2)
    ftl.click_button(ftl.order_accept)
    time.sleep(2)
    # Назначение водителя
    ftl.input_in_field(ftl.search_driver, value='Фронтов')
    time.sleep(1)
    ftl.click_button(ftl.attach_driver, wait='form')
    ftl.click_button(ftl.order_accepted)
    time.sleep(10)

    ftl.reload_page()

    # Начало исполнения рейса
    ftl.click_button(ftl.burger_menu)
    ftl.click_button(ftl.start_execution)
    time.sleep(3)

    time_1, time_2, time_3, time_4, time_5, time_6, time_7, time_8 = FTLAdd.get_time_intervals_many()

    # Простановка времени работы на 1 точке
    ftl.click_button(ftl.point_1_start)
    time.sleep(1)
    ftl.input_in_field(ftl.input_point, value=time_1)
    time.sleep(1)
    ftl.click_button(ftl.point_1_finish)
    time.sleep(1)
    ftl.input_in_field(ftl.input_point, value=time_2)
    time.sleep(1)

    ftl.click_button(ftl.save_changes)
    time.sleep(1)
    ftl.click_button(ftl.approve_changes)
    time.sleep(5)
    ftl.click_button(ftl.ok_time)
    time.sleep(3)

    # Простановка времени работы на 2 точке
    ftl.click_button(ftl.point_2_start)
    time.sleep(1)
    ftl.input_in_field(ftl.input_point, value=time_3)
    time.sleep(1)
    ftl.click_button(ftl.point_2_finish)
    time.sleep(1)
    ftl.input_in_field(ftl.input_point, value=time_4)
    time.sleep(1)

    ftl.click_button(ftl.save_changes)
    time.sleep(1)
    ftl.click_button(ftl.approve_changes)
    time.sleep(5)
    ftl.click_button(ftl.ok_time)
    time.sleep(3)

    # Простановка времени работы на 3 точке
    ftl.click_button(ftl.point_3_start)
    time.sleep(1)
    ftl.input_in_field(ftl.input_point, value=time_5)
    time.sleep(1)
    ftl.click_button(ftl.point_3_finish)
    time.sleep(1)
    ftl.input_in_field(ftl.input_point, value=time_6)
    time.sleep(1)

    ftl.click_button(ftl.save_changes)
    time.sleep(1)
    ftl.click_button(ftl.approve_changes)
    time.sleep(5)
    ftl.click_button(ftl.ok_time)
    time.sleep(3)

    # Простановка времени работы на 4 точке
    ftl.click_button(ftl.point_4_start)
    time.sleep(1)
    ftl.input_in_field(ftl.input_point, value=time_7)
    time.sleep(1)
    ftl.click_button(ftl.point_4_finish)
    time.sleep(1)
    ftl.input_in_field(ftl.input_point, value=time_8)
    time.sleep(1)

    ftl.click_button(ftl.save_changes)
    time.sleep(1)
    ftl.click_button(ftl.approve_changes)
    time.sleep(5)

    # Отправка документов и расчёта Подрядчиком
    ftl.click_button(ftl.send_calculation_and_documents, do_assert=True)
    time.sleep(5)
    ftl.click_button(ftl.sent_ok)
    time.sleep(5)
    ftl.click_button(ftl.tab_documents)
    time.sleep(1)
    ftl.click_button(ftl.send_documents, do_assert=True)
    time.sleep(5)
    ftl.click_button(ftl.sent_ok)
    time.sleep(1)

    # Выход из ЛКП
    sidebar.click_button(sidebar.exit_button)
    time.sleep(3)

    # Вход за ЛКЭ
    login = Login(base.driver, domain)
    login.authorization("lke")
    time.sleep(10)

    sidebar.click_button(sidebar.sidebar_button)

    # Переход в раздел 'Все Рейсы'
    base.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_list_button,
                        do_assert=True, wait='lst')

    # Переход в Рейс
    add.click_button(element_dict=add.reset_filters)
    time.sleep(1)
    add.click_button(add.add_filter)
    time.sleep(1)
    add.click_button(add.checkbox_client_request_number)
    time.sleep(1)
    add.scroll_to_element(add.apply_filters)
    time.sleep(1)
    add.click_button(add.apply_filters)
    time.sleep(1)
    add.input_in_field(add.client_request_number, value=application_number)
    time.sleep(3)
    ftl.click_button(ftl.click_on_request)
    time.sleep(2)

    # Работа с расчётом Экспедитором
    ftl.click_button(ftl.tab_calculation_producer)
    time.sleep(1)
    ftl.click_button(ftl.exp_accept_calculation)
    ftl.click_button(ftl.exp_documents_allright)
    ftl.click_button(ftl.exp_approve_calculation, do_assert=True)
    time.sleep(5)
    ftl.click_button(ftl.approved_ok)
    time.sleep(5)
    ftl.click_button(ftl.tab_calculation_client)
    time.sleep(1)
    ftl.scroll_to_element(ftl.exp_send_calculation_and_documents)
    time.sleep(1)
    ftl.click_button(ftl.exp_send_calculation_and_documents, do_assert=True)
    time.sleep(5)
    ftl.click_button(ftl.sent_ok)
    time.sleep(5)
    ftl.click_button(ftl.tab_documents)
    time.sleep(1)
    ftl.click_button(ftl.send_documents, do_assert=True)
    time.sleep(5)
    ftl.click_button(ftl.sent_ok)
    time.sleep(1)

    # Выход из ЛКЭ
    sidebar.click_button(sidebar.exit_button)
    time.sleep(3)

    # Вход за ЛКЗ
    login = Login(base.driver, domain)
    login.authorization("lkz")
    time.sleep(10)

    sidebar.click_button(sidebar.sidebar_button)

    # Переход в Рейс
    base.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_list_button,
                        do_assert=True, wait='lst')

    add.input_in_field(add.request_number_two, value=application_number, click_first=True)
    time.sleep(3)
    ftl.click_button(ftl.click_on_request)
    time.sleep(2)

    # Работа с расчётом Заказчиком
    ftl.click_button(ftl.tab_calculation_producer_lkz)
    time.sleep(1)
    ftl.click_button(ftl.exp_accept_calculation)
    ftl.click_button(ftl.exp_documents_allright)
    ftl.click_button(ftl.exp_approve_calculation, do_assert=True)
    time.sleep(5)
    ftl.click_button(ftl.approved_ok)
    time.sleep(5)
    ftl.click_button(ftl.tab_documents)
    time.sleep(1)
    ftl.click_button(ftl.documents_approve)
    ftl.click_button(ftl.documents_approve_approve, do_assert=True)
    time.sleep(5)
    ftl.click_button(ftl.sent_ok)
    time.sleep(1)

    ftl.refresh_page()
    time.sleep(5)
    ftl.verify_text_on_page(text='Взаиморасчеты', should_exist=True)

    # Выход из ЛКЗ
    sidebar.click_button(sidebar.exit_button)
    time.sleep(3)

    # Вход за ЛКЭ
    login = Login(base.driver, domain)
    login.authorization("lke")
    time.sleep(10)

    # Переход на вкладку 'Формирование реестров для ГВ'
    sidebar.click_button(sidebar.sidebar_button)
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.reg_client_create_old_list_button,
                           do_assert=True, wait="lst")

    add.input_in_field(add.client_order_number, value=application_number)
    time.sleep(3)
    reg = RegistriesOld(base.driver)
    reg.click_button(reg.checkbox_one, wait_type='located')
    reg.click_button(reg.form_new_registry, do_assert=True)

    wait = WebDriverWait(base.driver, 10)

    element = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'ant-modal-confirm-content')]")
        )
    )

    # ждём появления номера
    wait.until(lambda driver: "№" in element.text or "#" in element.text)

    text = element.text.strip()
    print(f"TEXT FROM MODAL: {repr(text)}")

    match = re.search(r'[№#N°]\s*([A-Za-z0-9\-]+)', text)

    if match:
        registry_number = match.group(1)
        print(f"Номер реестра: {registry_number}")
    else:
        raise ValueError(f"Не удалось найти номер реестра в тексте: {text}")

    reg.click_button(reg.registry_ok)

    # Выход из ЛКЭ
    sidebar.click_button(sidebar.exit_button)
    time.sleep(3)

    # Вход за ЛКЗ
    login = Login(base.driver, domain)
    login.authorization("lkz")
    time.sleep(10)

    # Переход на вкладку 'Список реестров'
    sidebar.click_button(sidebar.sidebar_button)
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.registries_old_list_button,
                           do_assert=True, wait="lst")

    add.input_in_field(add.registry_number, value=registry_number)

    # locator = (
    #     By.XPATH,
    #     f"//a[@id='registries-number-{registry_number}']"
    # )
    #
    # element = wait.until(EC.element_to_be_clickable(locator))

    # Переход в реестр
    locator = (By.ID, f"registries-number-{registry_number}")
    element = wait.until(EC.presence_of_element_located(locator))
    base.driver.execute_script("arguments[0].click();", element)

    time.sleep(3)

    ftl.verify_text_on_page(text='Взаиморасчеты')
    ftl.verify_text_on_page(text='Фронтов')
    ftl.verify_text_on_page(text=application_number)














    




























































