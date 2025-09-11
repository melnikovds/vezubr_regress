import allure
import pytest
import time
from pages.notifications_page import *
from pages.settings_page import Settings


@allure.story("Extended path test")
@allure.feature('Уведомления')
@allure.description('ЛКП. Установка уведомлений')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_notification_field_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # переход в раздел 'Настройки'
    sidebar.click_button(sidebar.settings_button, do_assert=True)

    notification = Settings(base.driver)
    # переход в таб 'Настройки уведомлений'
    notification.click_button(notification.notifications_field_tab)
    add = Notification(base.driver)

    # настройка уведомлений по смс
    add.click_button(add.click_sms)
    add.dropdown_without_input(add.day_to_allowed, option_text="Только по рабочим дням")

    # настройка уведомлений по рейсам
    add.dropdown_without_input(add.send_notification, option_text="По всем Рейсам")
    time.sleep(1)

    # установка уведомлений в блоке 'Подбор'
    add.dropdown_without_input(add.driver_search_mail, option_text="15 мин")
    add.dropdown_without_input(add.min_cost_mail, option_text="уведомлять")
    add.dropdown_without_input(add.executor_add_mail, option_text="уведомлять", index=2)
    add.dropdown_without_input(add.ts_not_assigned, option_text="Каждый час")
    add.dropdown_without_input(add.driver_ts_replacement, option_text="уведомлять", index=3)
    time.sleep(1)

    add.dropdown_without_input(add.driver_search_monitor, option_text="15 мин", index=2)
    add.dropdown_without_input(add.driver_search_sms, option_text="15 мин", index=3)
    add.dropdown_without_input(add.min_cost_monitor, option_text="уведомлять", index=2)
    add.dropdown_without_input(add.executor_add_monitor, option_text="уведомлять", index=4)
    add.dropdown_without_input(add.ts_not_assigned_monitor, option_text="Каждые 2 часа", index=2)
    add.dropdown_without_input(add.driver_ts_replacement_monitor, option_text="уведомлять", index=6)
    add.dropdown_without_input(add.min_cost_sms, option_text="уведомлять", index=3)
    add.dropdown_without_input(add.executor_add_sms, option_text="уведомлять", index=6)
    time.sleep(1)

    add.click_and_select_with_arrows(add.ts_not_assigned_sms, arrow_presses=4)
    add.click_and_select_with_arrows(add.driver_ts_replacement_sms, arrow_presses=1)
    add.click_and_select_with_arrows(add.not_started_mail, arrow_presses=4)
    add.click_and_select_with_arrows(add.not_started_monitor, arrow_presses=7)
    add.click_and_select_with_arrows(add.not_started_sms, arrow_presses=8)

    add.click_and_select_with_arrows(add.cancelled_contractor_mail, arrow_presses=1)
    add.click_and_select_with_arrows(add.cancelled_contractor_monitor, arrow_presses=1)
    add.click_and_select_with_arrows(add.cancelled_contractor_sms, arrow_presses=1)

    add.click_and_select_with_arrows(add.cancelled_owner_mail, arrow_presses=1)
    add.click_and_select_with_arrows(add.cancelled_owner_monitor, arrow_presses=1)
    add.click_and_select_with_arrows(add.cancelled_owner_sms, arrow_presses=1)

    # прокрутка страницы вниз
    add.scroll_to_element(add.late_arrival_mail)

    # установка уведомлений в блоке 'Исполнение'
    add.click_and_select_with_arrows(add.late_arrival_mail, arrow_presses=12)
    add.click_and_select_with_arrows(add.late_arrival_monitor, arrow_presses=13)
    add.click_and_select_with_arrows(add.late_arrival_sms, arrow_presses=7)

    add.click_and_select_with_arrows(add.arrived_mail, arrow_presses=9)
    add.click_and_select_with_arrows(add.arrived_monitor, arrow_presses=10)
    add.click_and_select_with_arrows(add.arrived_sms, arrow_presses=4)

    add.click_and_select_with_arrows(add.loading_begun_mail, arrow_presses=5)
    add.click_and_select_with_arrows(add.loading_begun_monitor, arrow_presses=6)
    add.click_and_select_with_arrows(add.loading_begun_sms, arrow_presses=8)

    # прокрутка страницы вниз
    add.scroll_to_element(add.loading_completed_mail)

    add.click_and_select_with_arrows(add.loading_completed_mail, arrow_presses=1)
    add.click_and_select_with_arrows(add.loading_completed_monitor, arrow_presses=2)
    add.click_and_select_with_arrows(add.loading_completed_sms, arrow_presses=3)

    add.click_and_select_with_arrows(add.documents_received_mail, arrow_presses=16)
    add.click_and_select_with_arrows(add.documents_received_monitor, arrow_presses=17)
    add.click_and_select_with_arrows(add.documents_received_sms, arrow_presses=18)

    # прокрутка страницы вниз
    add.scroll_to_element(add.flight_over_mail)

    add.click_and_select_with_arrows(add.flight_over_mail, arrow_presses=5)
    add.click_and_select_with_arrows(add.flight_over_monitor, arrow_presses=10)
    add.click_and_select_with_arrows(add.flight_over_sms, arrow_presses=15)

    # прокрутка страницы вниз
    add.scroll_to_element(add.flight_confirmation_mail)

    # установка уведомлений в блоке 'Проверка'
    add.click_and_select_with_arrows(add.flight_confirmation_mail, arrow_presses=2)
    add.click_and_select_with_arrows(add.flight_confirmation_monitor, arrow_presses=3)
    add.click_and_select_with_arrows(add.flight_confirmation_sms, arrow_presses=8)

    add.click_and_select_with_arrows(add.register_confirmation_mail, arrow_presses=1)
    add.click_and_select_with_arrows(add.register_confirmation_monitor, arrow_presses=4)
    add.click_and_select_with_arrows(add.register_confirmation_sms, arrow_presses=14)

    add.click_and_select_with_arrows(add.registry_not_confirmed_mail, arrow_presses=1)
    add.click_and_select_with_arrows(add.registry_not_confirmed_monitor, arrow_presses=4)
    add.click_and_select_with_arrows(add.registry_not_confirmed_sms, arrow_presses=14)

    # прокрутка страницы вниз
    add.scroll_to_element(add.critical_charge_mail)

    # установка уведомлений в блоке 'Мобильное приложение'
    add.click_and_select_with_arrows(add.critical_charge_mail, arrow_presses=1)
    add.click_and_select_with_arrows(add.critical_charge_monitor, arrow_presses=1)
    add.click_and_select_with_arrows(add.critical_charge_sms, arrow_presses=1)

    add.click_and_select_with_arrows(add.no_connection_mail, arrow_presses=1)
    add.click_and_select_with_arrows(add.no_connection_monitor, arrow_presses=1)
    add.click_and_select_with_arrows(add.no_connection_sms, arrow_presses=1)

    # установка уведомлений в блоке 'Грузоместа'
    add.click_and_select_with_arrows(add.cargo_not_accepted_mail, arrow_presses=1)
    add.click_and_select_with_arrows(add.cargo_not_accepted_monitor, arrow_presses=1)
    add.click_and_select_with_arrows(add.cargo_not_accepted_sms, arrow_presses=1)

    add.click_and_select_with_arrows(add.address_missing_mail, arrow_presses=1)
    add.click_and_select_with_arrows(add.address_missing_monitor, arrow_presses=1)
    add.click_and_select_with_arrows(add.address_missing_sms, arrow_presses=1)

    # сохранение настроек
    add.click_button(add.safe_notifications, wait='form')

    # сброс уведомлений по смс
    res = ResetNotifications(base.driver)

    add.dropdown_without_input(add.driver_search_sms, option_text="не уведомлять", index=1)

    add.click_button(add.min_cost_sms)
    time.sleep(1)
    res.click_button(res.fields_2)

    add.click_button(add.executor_add_sms)
    time.sleep(1)
    res.click_button(res.fields_3)

    add.click_button(add.ts_not_assigned_sms)
    time.sleep(1)
    res.click_button(res.fields_4)

    add.click_button(add.driver_ts_replacement_sms)
    time.sleep(1)
    res.click_button(res.fields_5)

    add.click_button(add.not_started_sms)
    time.sleep(1)
    res.click_button(res.fields_6)

    add.click_button(add.cancelled_contractor_sms)
    time.sleep(1)
    res.click_button(res.fields_7)

    add.click_button(add.cancelled_owner_sms)
    time.sleep(1)
    res.click_button(res.fields_8)

    # прокрутка страницы вниз
    add.scroll_to_element(add.late_arrival_sms)

    add.click_button(add.late_arrival_sms)
    time.sleep(1)
    res.click_button(res.fields_9)

    add.click_button(add.arrived_sms)
    time.sleep(1)
    res.click_button(res.fields_10)

    add.click_button(add.loading_begun_sms)
    time.sleep(1)
    res.click_button(res.fields_11)

    # прокрутка страницы вниз
    add.scroll_to_element(add.loading_completed_mail)

    add.click_button(add.loading_completed_sms)
    time.sleep(1)
    res.click_button(res.fields_12)

    add.click_button(add.documents_received_sms)
    time.sleep(1)
    res.click_button(res.fields_13)

    add.click_button(add.flight_over_sms)
    time.sleep(1)
    res.click_button(res.fields_14)

    # прокрутка страницы вниз
    add.scroll_to_element(add.flight_confirmation_mail)

    add.click_button(add.flight_confirmation_sms)
    time.sleep(1)
    res.click_button(res.fields_15)

    add.click_button(add.register_confirmation_sms)
    time.sleep(1)
    res.click_button(res.fields_16)

    add.click_button(add.registry_not_confirmed_sms)
    time.sleep(1)
    res.click_button(res.fields_17)

    # прокрутка страницы вниз
    add.scroll_to_element(add.critical_charge_mail)

    add.click_button(add.critical_charge_sms)
    time.sleep(1)
    res.click_button(res.fields_18)

    add.click_button(add.no_connection_sms)
    time.sleep(1)
    res.click_button(res.fields_19)

    add.click_button(add.cargo_not_accepted_sms)
    time.sleep(1)
    res.click_button(res.fields_20)

    add.click_button(add.address_missing_sms)
    time.sleep(1)
    res.click_button(res.fields_21)

    # Конец теста

