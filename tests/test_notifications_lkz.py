import allure
import pytest
import time
from pages.notifications_page import Notification
from pages.settings_page import Settings


@allure.story("Extended path test")
@allure.feature('Уведомления')
@allure.description('ЛКЗ. Установка уведомлений')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_notification_field_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    sidebar.click_button(sidebar.settings_button, do_assert=True)

    notification = Settings(base.driver)
    notification.click_button(notification.notifications_field_tab)

    add = Notification(base.driver)
    add.click_button(add.click_sms)
    add.dropdown_without_input(add.day_to_allowed, option_text="Никогда")
    add.dropdown_without_input(add.send_notification, option_text="По всем Рейсам")
    time.sleep(2)
    add.dropdown_without_input(add.driver_search_mail, option_text="15 мин")
    add.dropdown_without_input(add.min_cost_mail, option_text="уведомлять")
    time.sleep(1)
    add.dropdown_without_input(add.executor_add_mail, option_text="уведомлять", index=2)
    time.sleep(1)
    add.dropdown_without_input(add.ts_not_assigned, option_text="Каждый час")
    add.dropdown_without_input(add.driver_ts_replacement, option_text="уведомлять", index=3)
    time.sleep(2)
    add.dropdown_without_input(add.driver_search_monitor, option_text="15 мин", index=2)
    add.dropdown_without_input(add.driver_search_sms, option_text="15 мин", index=3)
    add.dropdown_without_input(add.min_cost_monitor, option_text="уведомлять", index=2)
    add.dropdown_without_input(add.executor_add_monitor, option_text="уведомлять", index=4)
    add.dropdown_without_input(add.ts_not_assigned_monitor, option_text="Каждые 2 часа", index=2)
    add.dropdown_without_input(add.driver_ts_replacement_monitor, option_text="уведомлять", index=6)
    add.dropdown_without_input(add.min_cost_sms, option_text="уведомлять", index=3)
    add.dropdown_without_input(add.executor_add_sms, option_text="уведомлять", index=6)

    add.dropdown_without_input(add.ts_not_assigned_sms, option_text="Каждые 4 часа", index=4)
    # add.dropdown_without_input(add.driver_ts_replacement_sms, option_text="уведомлять", index=1)

