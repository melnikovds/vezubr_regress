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
    ftl.click_button(ftl.first_address_select, wait="lst")
    ftl.input_in_field(ftl.address_filter, "Бассейная", wait="lst")
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    time.sleep(3)
    # Выбор второго адреса из списка
    ftl.click_button(ftl.second_address_select, wait="lst")
    ftl.input_in_field(ftl.address_filter, "Софийская", wait="lst")
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    time.sleep(3)
    # Выбор третьего адреса из списка
    ftl.click_button(ftl.third_address_select, wait="lst")
    ftl.input_in_field(ftl.address_filter, "Турку", wait="lst")
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    time.sleep(3)
    # Выбор четвёртого адреса из списка
    ftl.click_button(ftl.fourth_address_select, wait="lst")
    ftl.input_in_field(ftl.address_filter, "Белы Куна", wait="lst")
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)

    # Ожидание завершения расчета стоимости
    base.get_element(ftl.calculate_finish)
    # Публикация заявки с использованием тарифа
    ftl.click_button(ftl.tariff_button)
    ftl.click_button(ftl.producer_select)
    ftl.click_button(ftl.select_all_producer)
    time.sleep(1)
    ftl.click_button(ftl.producer_select_text)
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

    ftl.click_button(ftl.continue_button, do_assert=True)
    ftl.click_button(ftl.confirm_add_button, wait="lst")



