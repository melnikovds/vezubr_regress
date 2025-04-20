from base.base_class import Base


class Notification(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    click_sms = {
        "xpath": "//button[contains(@class,'ant-btn form-field-range-time__action')]",
        "name": "click_sms"
    }
    day_to_allowed = {
        "xpath": "//div[@class='ant-select-selection__rendered']",
        "name": "day_to_allowed"
    }
    send_notification = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[2]",
        "name": "send_notification"
    }
    driver_search_mail = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[3]",
        "name": "driver_search_mail"
    }
    driver_search_monitor = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[1]/td[3]",
        "name": "driver_search_monitor"
    }
    driver_search_sms = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[1]/td[4]",
        "name": "driver"
    }
    min_cost_mail = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]"
                 "/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[1]",
        "name": "min_cost_mail"
    }
    executor_add_mail = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[3]/td[2]",
        "name": "executor_add_mail"
    }
    ts_not_assigned = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[4]/td[2]",
        "name": "ts_not_assigned"
    }
    driver_ts_replacement = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[5]/td[2]",
        "name": "driver_ts_replacement"
    }
    not_started_mail = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[6]/td[2]",
        "name": "not_started_mail"
    }
    min_cost_monitor = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[2]/td[3]",
        "name": "executor_add_mail"
    }
    executor_add_monitor = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[3]/td[3]",
        "name": "executor_add_monitor"
    }
    ts_not_assigned_monitor = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[4]/td[3]",
        "name": "ts_not_assigned_monitor"
    }
    driver_ts_replacement_monitor = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[5]/td[3]",
        "name": "driver_ts_replacement_monitor"
    }
    min_cost_sms = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[2]/td[4]",
        "name": "min_cost_sms"
    }
    executor_add_sms = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[3]/td[4]",
        "name": "executor_add_sms"
    }
    ts_not_assigned_sms = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[4]/td[4]",
        "name": "ts_not_assigned_sms"
    }
    driver_ts_replacement_sms = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[5]/td[4]",
        "name": "driver_ts_replacement_sms",
    }
    move_to_element1 = {
        "xpath": "(//h2[@class='settings-form__group__title'])[2]",
        "name": "move_to_element1"
    }
    skroll = {
        "xpath": "//form[contains(@class,'ant-form ant-form-vertical')]",
        "name": "skroll"
    }
    not_started_phone = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[6]/td[3]",
        "name": "not_started_mail"
    }
    not_started_sms = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[6]/td[4]",
        "name": "not_started_mail"
    }
    cancel_by_contractor_mail = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[7]/td[2]",
        "name": "cancel_by_contractor_mail"
    }
    cancel_by_contractor_phone = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[7]/td[3]",
        "name": "cancel_by_contractor_phone"
    }
    cancel_by_contractor_sms = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[7]/td[4]",
        "name": "cancel_by_contractor_sms"
    }
    cancel_by_customer_mail = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[8]/td[2]",
        "name": "cancel_by_customer_mail"
    }
    cancel_by_customer_phone = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[8]/td[3]",
        "name": "cancel_by_customer_phone"
    }
    cancel_by_customer_sms = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[8]/td[4]",
        "name": "cancel_by_customer_sms"
    }
    late_arrival_mail = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[1]/tbody/tr[1]/td[2]",
        "name": "late_arrival_mail"
    }
    late_arrival_phone = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[1]/tbody/tr[1]/td[3]",
        "name": "late_arrival_phone"
    }
    late_arrival_sms = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[1]/tbody/tr[1]/td[4]",
        "name": "late_arrival_sms"
    }
    arrived_mail = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[1]/tbody/tr[2]/td[2]",
        "name": "arrived_mail"
    }
    arrived_phone = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[1]/tbody/tr[2]/td[3]",
        "name": "arrived_phone"
    }
    arrived_sms = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[1]/tbody/tr[2]/td[4]",
        "name": "arrived_sms"
    }
    started_and_not_completed_mail = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[1]/tbody/tr[3]/td[2]",
        "name": "started_and_not_completed_phone"
    }
    started_and_not_completed_phone = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[1]/tbody/tr[3]/td[3]",
        "name": "started_and_not_completed_phone"
    }
    started_and_not_completed_sms = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[1]/tbody/tr[3]/td[4]",
        "name": "started_and_not_completed_phone"
    }
    waiting_for_documents_mail = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[1]/tbody/tr[4]/td[2]",
        "name": "waiting_for_documents_mail"
    }
    waiting_for_documents_phone = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[1]/tbody/tr[4]/td[3]",
        "name": "waiting_for_documents_phone"
    }
    waiting_for_documents_sms = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[1]/tbody/tr[4]/td[4]",
        "name": "waiting_for_documents_sms"
    }
    documents_received_mail = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[1]/tbody/tr[5]/td[2]",
        "name": "Documents_received_mail"
    }
    documents_received_phone = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[1]/tbody/tr[5]/td[3]",
        "name": "Documents_received_phone"
    }
    documents_received_sms = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[1]/tbody/tr[5]/td[4]",
        "name": "Documents_received_sms"
    }
    delivery_completed_mail = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[1]/tbody/tr[6]/td[2]",
        "name": "delivery_completed_mail"
    }
    delivery_completed_phone = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[1]/tbody/tr[6]/td[3]",
        "name": "delivery_completed_phone"
    }
    delivery_completed_sms = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[1]/tbody/tr[6]/td[4]",
        "name": "delivery_completed_sms"
    }
    skroll2 = {
        "xpath": "//tr[@data-row-key='420']//td[1]",
        "name": "skroll2"
    }
    being_confirmed_mail = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[2]/tbody/tr[1]/td[2]",
        "name": "delivery_completed_mail"
    }
    being_confirmed_phone = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[2]/tbody/tr[1]/td[3]",
        "name": "delivery_completed_phone"
    }
    being_confirmed_sms = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[2]/tbody/tr[1]/td[4]",
        "name": "delivery_completed_sms"
    }
    registry_confirm_mail = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[2]/tbody/tr[2]/td[2]",
        "name": "registry_confirm_mail"
    }
    registry_confirm_phone = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[2]/tbody/tr[2]/td[3]",
        "name": "registry_confirm_phone"
    }
    registry_confirm_sms = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[2]/tbody/tr[2]/td[4]",
        "name": "registry_confirm_sms"
    }
    register_not_confirm_mail = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[2]/tbody/tr[3]/td[2]",
        "name": "register_not_confirm_mail"
    }
    register_not_confirm_phone = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[2]/tbody/tr[3]/td[3]",
        "name": "register_not_confirm_phone"
    }
    register_not_confirm_sms = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[2]/tbody/tr[3]/td[4]",
        "name": "register_not_confirm_sms"
    }
    critical_charge_mail = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[3]/tbody/tr[1]/td[2]",
        "name": "battery_is_critical_mail"
    }
    critical_charge_phone = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[3]/tbody/tr[1]/td[3]",
        "name": "battery_is_critical_phone"
    }
    critical_charge_sms = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[3]/tbody/tr[1]/td[4]",
        "name": "battery_is_critical_sms"
    }
    mp_disconnect_mail = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[3]/tbody/tr[2]/td[2]",
        "name": "mp_disconnect_mail"
    }
    mp_disconnect_phone = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[3]/tbody/tr[2]/td[3]",
        "name": "mp_disconnect_phone"
    }
    mp_disconnect_sms = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[3]/tbody/tr[2]/td[4]",
        "name": "mp_disconnect_sms"
    }
    gm_not_accepted_mail = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[4]/tbody/tr[1]/td[2]",
        "name": "gm_not_accepted_mail"
    }
    gm_not_accepted_phone = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[4]/tbody/tr[1]/td[3]",
        "name": "gm_not_accepted_phone"
    }
    gm_not_accepted_sms = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[4]/tbody/tr[1]/td[4]",
        "name": "gm_not_accepted_sms"
    }
    gm_address_missing_mail = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[4]/tbody/tr[2]/td[2]",
        "name": "gm_address_missing_mail"
    }
    gm_address_missing_phone = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[4]/tbody/tr[2]/td[3]",
        "name": "gm_address_missing_phone"
    }
    gm_address_missing_sms = {
        "xpath": "//table[@class='ant-table-fixed']/following::table[4]/tbody/tr[2]/td[4]",
        "name": "gm_address_missing_sms"
    }
    click_save = {
        "xpath": "//button[contains(@class,'ant-btn semi-wide')]",
        "name": "click_save"
    }
