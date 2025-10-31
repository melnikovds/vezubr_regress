import allure
import pytest
import time
from pages.clients_list_page import ClientsList
from pages.contractor_page import Contractor
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@allure.story("Smoke test")
@allure.feature('Прикрепление и открепление договоров страхования')
@allure.description('ЛКЭ. Тест прикрепления и открепления договора страхования к ГВ')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_insurance_contract_attach_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку клиентов
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")
    
    client_list = ClientsList(base.driver)
    # Клик по клиенту с ИНН "client_lkz_inn"
    client_list.click_button(client_list.client_lkz_inn, wait="form")
    
    contractor = Contractor(base.driver)
    # Переход на вкладку настроек контрагента
    contractor.click_button(contractor.settings_tab)
    # Разворачивание списка договоров страхования
    contractor.click_button(contractor.insurance_expandable_list)


    # Очистка поля договора страхования
    # contractor.move_and_click(move_to=contractor.insurance_contract_select, click_to=contractor.clear_button)
    contractor.move_to_element(contractor.insurance_contract_select)
    time.sleep(2)
    try:
        element = base.driver.find_element(By.XPATH, "//i[@aria-label='icon: close-circle']")

        # проверка есть ли у элемента размер и видим ли он
        if element.is_displayed() and element .size['height'] > 0 and element.size['width'] > 0:
            contractor.click_on_the_cross(contractor.clear_button)
        else:
            print("элемент найден, но он невидим или нулевого размера - пропускаем клик")

    except NoSuchElementException:
        print("элемент не найден - пропускаем клик")


    # Выбор страховой компании "Энергогарант"
    contractor.dropdown_without_input(contractor.insurance_company_select, "Энергогарант")
    # Выбор конкретного договора страхования
    contractor.dropdown_without_input(contractor.insurance_contract_select,
                                          "Договор №№-20251015171206 «Н-20251015171207» от 15.10.2025")
    # Подтверждение привязки договора
    contractor.click_button(contractor.confirm_button, do_assert=True)
    # Подтверждение успешного выполнения действия
    contractor.click_button(contractor.ok_button)
    # Очистка выбора договора страхования для дальнейшего открепления
    contractor.move_and_click(move_to=contractor.insurance_contract_select, click_to=contractor.clear_button)
    # Клик по кнопке открепления договора
    contractor.click_button(contractor.delete_button, do_assert=True)
    # Подтверждение открепления договора
    contractor.click_button(contractor.ok_button)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Прикрепление и открепление договоров страхования')
@allure.description('ЛКП. Тест прикрепления и открепления договора страхования к ГВ')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_insurance_contract_attach_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку клиентов
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")
    
    client_list = ClientsList(base.driver)
    # Клик по клиенту с ИНН "client_lkz_inn"
    client_list.click_button(client_list.client_lkz_inn, wait="form")
    
    contractor = Contractor(base.driver)
    # Переход на вкладку настроек контрагента
    contractor.click_button(contractor.settings_tab)
    # Разворачивание списка договоров страхования
    contractor.click_button(contractor.insurance_expandable_list)

    # Очистка поля договора страхования
    contractor.move_to_element(contractor.insurance_contract_select)
    time.sleep(2)
    try:
        element = base.driver.find_element(By.XPATH, "//i[@aria-label='icon: close-circle']")

        # проверка есть ли у элемента размер и видим ли он
        if element.is_displayed() and element .size['height'] > 0 and element.size['width'] > 0:
            contractor.click_on_the_cross(contractor.clear_button)
        else:
            print("элемент найден, но он невидим или нулевого размера - пропускаем клик")

    except NoSuchElementException:
        print("элемент не найден - пропускаем клик")


    # Выбор страховой компании "Энергогарант"
    contractor.dropdown_without_input(contractor.insurance_company_select, "Энергогарант")
    # Выбор конкретного договора страхования
    contractor.click_and_select_with_arrows(contractor.insurance_contract_select, arrow_presses=4)
    # Подтверждение привязки договора
    contractor.click_button(contractor.confirm_button, do_assert=True)
    # Подтверждение успешного выполнения действия
    contractor.click_button(contractor.ok_button)
    time.sleep(2)
    # # Проверка наличия одного из договоров на странице
    # contractor.verify_text_on_page(text='123241', should_exist=True)
    # Очистка выбора договора страхования для дальнейшего открепления
    contractor.move_and_click(move_to=contractor.insurance_contract_select, click_to=contractor.clear_button)
    # Клик по кнопке открепления договора
    contractor.click_button(contractor.delete_button, do_assert=True)
    # Подтверждение открепления договора
    contractor.click_button(contractor.ok_button)
    # Конец теста
    