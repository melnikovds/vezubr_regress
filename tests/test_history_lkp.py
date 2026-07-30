import allure
import pytest
import time
import re
from pages.contractor_list_page import *
from pages.clients_list_page import *
from pages.history_journal_page import *
from pages.agreement_page import *
from pages.contractor_page import *
from pages.filters_new_ftl_page import NewFtlFilters
from pages.cdr_ftl_page import AddCdr


@allure.story("Extended test")
@allure.feature('Журналирование')
@allure.description('ЛКП. Проверка журналирования Контрагента')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_journal_contractor_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    ctr = ContractorList(base.driver)
    cl = ClientsList(base.driver)
    jrn = Journal(base.driver)

    # Выбор нужного контрагента
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")
    time.sleep(2)
    ctr.input_in_field(ctr.contractor_name, value='климат')
    time.sleep(2)
    cl.click_button(cl.contractor_inn)
    time.sleep(1)
    jrn.click_button(jrn.tab_history_contractor)
    time.sleep(1)
    jrn.dropdown_without_input(jrn.time_event, option_text='За все время')
    time.sleep(10)
    jrn.verify_text_on_page(text='Лиговский пр-кт, д 140')
    jrn.verify_text_on_page(text='ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "РУС')
    jrn.verify_text_on_page(text='7810579798')
    jrn.verify_text_on_page(text='781601001')


@allure.story("Extended test")
@allure.feature('Журналирование')
@allure.description('ЛКП. Проверка журналирования Договора')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_journal_agreement_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    ctr = ContractorList(base.driver)
    cl = ClientsList(base.driver)
    ct = Contractor(base.driver)
    jrn = Journal(base.driver)

    # Выбор нужного контрагента
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")
    time.sleep(2)
    ctr.input_in_field(ctr.contractor_name, value='климат')
    time.sleep(2)
    cl.click_button(cl.contractor_inn)
    time.sleep(1)
    ct.click_button(ct.agreement_link_two)
    jrn.click_button(jrn.tab_history_agreement)
    time.sleep(1)
    jrn.dropdown_without_input(jrn.time_event, option_text='За все время')
    time.sleep(10)
    jrn.verify_text_on_page(text='872334')
    jrn.verify_text_on_page(text='правила перевозок')
    jrn.verify_text_on_page(text='auto@LKP.com')


@allure.story("Critical test")
@allure.feature('Журналирование')
@allure.description('ЛКП. Проверка журналирования FTL Заявки')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_journal_cdr_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    add = NewFtlFilters(base.driver)
    cdr = AddCdr(base.driver)
    jrn = Journal(base.driver)

    # Выбор нужной Заявки
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.cdr_active_list_button,
                           do_assert=True, wait="lst")

    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(1)
    add.input_in_field(add.request_number, value='26-VZ-198')
    time.sleep(3)
    cdr.click_button(cdr.click_first_element)
    time.sleep(1)
    jrn.click_button(jrn.tab_history_ftl_request)
    time.sleep(1)
    jrn.dropdown_without_input(jrn.time_event, option_text='За все время')
    time.sleep(10)
    jrn.verify_text_on_page(text='Водитель')
    jrn.verify_text_on_page(text='Госномер ТС')
    jrn.verify_text_on_page(text='5537')
    jrn.verify_text_on_page(text='ТС-20240425204228')



