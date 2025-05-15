import allure
import pytest
import time
from pages.agreement_page import Agreement
from pages.contractor_page import Contractor
from pages.extra_agreement_add_page import ExtraAgreementAdd
from pages.producers_list_page import ProducersList


@allure.story("Critical path test")
@allure.feature('Прикрепление тарифов')
@allure.description('ЛКЗ. Тест прикрепления тарифа к ДУ c ПВ: создаем базовый ДУ и сразу прикрепляем существующий '
                    'тариф - Первый в списке')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_tariff_attach_producer_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку перевозчиков
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")

    producer_list = ProducersList(base.driver)
    # Выбор перевозчика по ИНН
    producer_list.click_button(producer_list.producer_logo_inn, wait="lst")

    contractor = Contractor(base.driver)
    # Переход к договорам
    contractor.click_button(contractor.agreements_link, wait="form")
    time.sleep(1)


    agreement = Agreement(base.driver)
    # Переход на вкладку дополнительных соглашений
    agreement.click_button(agreement.extra_agreement_tab)
    time.sleep(1)
    # Клик по кнопке добавления дополнительного соглашения
    agreement.click_button(agreement.add_extra_agr_button)
    time.sleep(1)

    add_extra = ExtraAgreementAdd(base.driver)
    # Создание базового дополнительного соглашения
    add_extra.add_base_extra_agreements()
    time.sleep(1)
    # Выбор тарифа
    add_extra.click_button(add_extra.radio_button, wait_type="located")
    # Подтверждение выбора тарифа
    add_extra.click_button(add_extra.confirm_tariff_button, do_assert=True)
    # Подтверждение добавления дополнительного соглашения
    add_extra.click_button(add_extra.confirm_add_button, wait="form")
    # Конец теста
