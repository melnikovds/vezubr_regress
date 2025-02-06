import time

import allure
import pytest

from pages.notifications_page import Notification
from pages.settings_page import Settings


@allure.story("Extended path test")
@allure.feature('Маршрутизация грузомест')
@allure.description('ЛКЭ. Тест маршрутизации ГМ ГВ: создаем - ГМ ГВ, маршрутизируем - ТС 20т/90м3/ 33пал')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_notification_field_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    sidebar.click_button(sidebar.settings_button, do_assert=True)

    notification = Settings(base.driver)
    notification.click_button(notification.notification_field)

    add = Notification(base.driver)
    add.click_button(add.click_sms)
    add.dropdown_without_input(add.day_to_allowed, "Никогда")
    add.dropdown_without_input(add.send_notification, "По всем Рейсам")

    # Заполняем поля "подбор"
    add.dropdown_without_input(add.driver_search_mail, "15 мин")
    add.dropdown_without_input(add.min_cost_mail, "уведомлять")
    add.dropdown_without_input(add.executor_add_mail, "уведомлять", index=2)
    add.dropdown_without_input(add.ts_not_assigned, "Каждый час")
    add.dropdown_without_input(add.driver_ts_replacement, "уведомлять", index=3)
    add.dropdown_without_input(add.driver_search_monitor, "15 мин", index=2)
    add.dropdown_without_input(add.driver_search_sms, "15 мин", index=3)
    add.dropdown_without_input(add.min_cost_monitor, "уведомлять", index=2)
    add.dropdown_without_input(add.executor_add_monitor, "уведомлять", index=4)
    add.dropdown_without_input(add.ts_not_assigned_monitor, "Каждые 2 часа", index=2)
    add.dropdown_without_input(add.driver_ts_replacement_monitor, "уведомлять", index=6)
    add.dropdown_without_input(add.min_cost_sms, "уведомлять", index=3)
    add.dropdown_without_input(add.executor_add_sms, "уведомлять", index=6)
    add.click_and_select_with_arrows(add.ts_not_assigned_sms, 1)
    add.click_and_select_with_arrows(add.driver_ts_replacement_sms, 1)
    add.scroll_to_element(add.move_to_element1)
    add.click_and_select_with_arrows(add.not_started_mail, 3)
    add.click_and_select_with_arrows(add.not_started_phone, 3)
    add.click_and_select_with_arrows(add.not_started_sms, 3)
    add.click_and_select_with_arrows(add.cancel_by_contractor_mail, 1)
    add.click_and_select_with_arrows(add.cancel_by_contractor_phone, 1)
    add.click_and_select_with_arrows(add.cancel_by_contractor_sms, 1)
    add.click_and_select_with_arrows(add.cancel_by_customer_mail, 1)
    add.click_and_select_with_arrows(add.cancel_by_customer_phone, 1)
    add.click_and_select_with_arrows(add.cancel_by_customer_sms, 1)

    # Заполняем поля "исполнение"
    add.click_and_select_with_arrows(add.late_arrival_mail, 3)
    add.click_and_select_with_arrows(add.late_arrival_phone, 3)
    add.click_and_select_with_arrows(add.late_arrival_sms, 3)
    add.click_and_select_with_arrows(add.arrived_mail, 3)
    add.click_and_select_with_arrows(add.arrived_phone, 3)
    add.click_and_select_with_arrows(add.arrived_sms, 3)
    add.click_and_select_with_arrows(add.started_and_not_completed_mail, 3)
    add.click_and_select_with_arrows(add.started_and_not_completed_phone, 3)
    add.click_and_select_with_arrows(add.started_and_not_completed_sms, 3)
    add.click_and_select_with_arrows(add.waiting_for_documents_mail, 3)
    add.click_and_select_with_arrows(add.waiting_for_documents_phone, 3)
    add.click_and_select_with_arrows(add.waiting_for_documents_sms, 3)
    add.click_and_select_with_arrows(add.documents_received_mail, 3)
    add.click_and_select_with_arrows(add.documents_received_phone, 3)
    add.click_and_select_with_arrows(add.documents_received_sms, 3)
    add.click_and_select_with_arrows(add.delivery_completed_mail, 3)
    add.click_and_select_with_arrows(add.delivery_completed_phone, 3)
    add.click_and_select_with_arrows(add.delivery_completed_sms, 3)
    add.scroll_to_element(add.skroll2)

    # Заполняем поля "проверка"
    add.click_and_select_with_arrows(add.being_confirmed_mail, 3)
    add.click_and_select_with_arrows(add.being_confirmed_phone, 3)
    add.click_and_select_with_arrows(add.being_confirmed_sms, 3)
    add.click_and_select_with_arrows(add.registry_confirm_mail, 3)
    add.click_and_select_with_arrows(add.registry_confirm_phone, 3)
    add.click_and_select_with_arrows(add.registry_confirm_sms, 3)
    add.click_and_select_with_arrows(add.register_not_confirm_mail, 3)
    add.click_and_select_with_arrows(add.register_not_confirm_phone, 3)
    add.click_and_select_with_arrows(add.register_not_confirm_sms, 3)

    # Заполняем поля "Мобильное приложение"
    add.click_and_select_with_arrows(add.critical_charge_mail, 1)
    add.click_and_select_with_arrows(add.critical_charge_phone, 1)
    add.click_and_select_with_arrows(add.critical_charge_sms, 1)
    add.click_and_select_with_arrows(add.mp_disconnect_mail, 1)
    add.click_and_select_with_arrows(add.mp_disconnect_phone,1)
    add.click_and_select_with_arrows(add.mp_disconnect_sms, 1)

    # Заполняем поля "ГМ адрес пропущен"
    add.click_and_select_with_arrows(add.gm_not_accepted_mail, 1)
    add.click_and_select_with_arrows(add.gm_not_accepted_phone, 1)
    add.click_and_select_with_arrows(add.gm_not_accepted_sms, 1)
    add.click_and_select_with_arrows(add.gm_address_missing_mail, 1)
    add.click_and_select_with_arrows(add.gm_address_missing_phone, 1)
    add.click_and_select_with_arrows(add.gm_address_missing_sms, 1)

    # Сохраняем изменения
    add.click_button(add.click_save)
    time.sleep(2)

