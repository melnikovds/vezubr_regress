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
    add.dropdown_without_input(add.day_to_allowed, option_text="Только по рабочим дням")
    add.dropdown_without_input(add.send_notification, option_text="По всем Рейсам")
    time.sleep(2)

    # add.dropdown_without_input(add.driver_search_mail, option_text="15 мин")
    # add.dropdown_without_input(add.min_cost_mail, option_text="уведомлять")
    # add.dropdown_without_input(add.executor_add_mail, option_text="уведомлять", index=2)
    # add.dropdown_without_input(add.ts_not_assigned, option_text="Каждый час")
    # add.dropdown_without_input(add.driver_ts_replacement, option_text="уведомлять", index=3)
    # time.sleep(1)

    # add.dropdown_without_input(add.driver_search_monitor, option_text="15 мин", index=2)
    # add.dropdown_without_input(add.driver_search_sms, option_text="15 мин", index=3)
    # add.dropdown_without_input(add.min_cost_monitor, option_text="уведомлять", index=2)
    # add.dropdown_without_input(add.executor_add_monitor, option_text="уведомлять", index=4)
    # add.dropdown_without_input(add.ts_not_assigned_monitor, option_text="Каждые 2 часа", index=2)
    # add.dropdown_without_input(add.driver_ts_replacement_monitor, option_text="уведомлять", index=6)
    # add.dropdown_without_input(add.min_cost_sms, option_text="уведомлять", index=3)
    # add.dropdown_without_input(add.executor_add_sms, option_text="уведомлять", index=6)
    # time.sleep(1)
    #
    # add.click_and_select_with_arrows(add.ts_not_assigned_sms, arrow_presses=4)
    # time.sleep(1)
    # add.click_and_select_with_arrows(add.driver_ts_replacement_sms, arrow_presses=1)
    # time.sleep(1)
    # add.click_and_select_with_arrows(add.not_started_mail, arrow_presses=4)
    # time.sleep(1)
    # add.click_and_select_with_arrows(add.not_started_monitor, arrow_presses=7)
    # time.sleep(1)
    # add.click_and_select_with_arrows(add.not_started_sms, arrow_presses=8)
    # time.sleep(1)
    #
    # add.click_and_select_with_arrows(add.cancelled_contractor_mail, arrow_presses=1)
    # add.click_and_select_with_arrows(add.cancelled_contractor_monitor, arrow_presses=1)
    # add.click_and_select_with_arrows(add.cancelled_contractor_sms, arrow_presses=1)
    #
    # add.click_and_select_with_arrows(add.cancelled_owner_mail, arrow_presses=1)
    # add.click_and_select_with_arrows(add.cancelled_owner_monitor, arrow_presses=1)
    # add.click_and_select_with_arrows(add.cancelled_owner_sms, arrow_presses=1)


    element = base.find_element(By.XPATH_SELECTOR, "late_arrival_mail")
    base.execute_script("arguments[0].scrollIntoView(true);", element)


    add.click_and_select_with_arrows(add.late_arrival_mail, arrow_presses=12)
    add.click_and_select_with_arrows(add.late_arrival_monitor, arrow_presses=13)
    add.click_and_select_with_arrows(add.late_arrival_sms, arrow_presses=7)




    add.click_button(add.safe_notifications, wait='form')