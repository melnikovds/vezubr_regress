from base.base_class import Base


class Notification(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
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
    not_started = {
        "xpath": "//table[@class='ant-table-fixed']/tbody/tr[6]/td[2]",
        "name": "not_started"
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
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[4]/div[1]/div[1]/div[1]/div[2]",
        "name": "ts_not_assigned_sms"
    }
    driver_ts_replacement_sms = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[4]/div[1]/div[1]/div[1]",
        "name": "driver_ts_replacement_sms"
    }
    not_started_mail = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[6]/td[2]/div[1]/div[1]/div[1]",
        "name": "not_started_mail"
    }
    not_started_monitor = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[6]/td[3]/div[1]/div[1]/div[1]",
        "name": "not_started_monitor"
    }
    not_started_sms = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[6]/td[4]/div[1]/div[1]/div[1]",
        "name": "not_started_sms"
    }
    cancelled_contractor_mail = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[7]/td[2]/div[1]/div[1]/div[1]",
        "name": "cancelled_contractor_mail"
    }
    cancelled_contractor_monitor = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[7]/td[3]/div[1]/div[1]/div[1]",
        "name": "cancelled_contractor_monitor"
    }
    cancelled_contractor_sms = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[7]/td[4]/div[1]/div[1]/div[1]",
        "name": "cancelled_contractor_sms"
    }

    cancelled_owner_mail = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[8]/td[2]/div[1]/div[1]/div[1]",
        "name": "cancelled_owner_mail"
    }
    cancelled_owner_monitor = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[8]/td[3]/div[1]/div[1]/div[1]",
        "name": "cancelled_owner_monitor"
    }
    cancelled_owner_sms = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[8]/td[4]/div[1]/div[1]/div[1]",
        "name": "cancelled_owner_sms"
    }

    late_arrival_mail = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]",
        "name": "late_arrival_mail"
    }
    late_arrival_monitor = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]/div[1]/div[1]",
        "name": "late_arrival_monitor"
    }
    late_arrival_sms = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[1]/div[1]/div[1]",
        "name": "late_arrival_sms"
    }
    arrived_mail = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[1]",
        "name": "arrived_mail"
    }
    arrived_monitor = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/div[1]/div[1]/div[1]",
        "name": "arrived_monitor"
    }
    arrived_sms = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[4]/div[1]/div[1]/div[1]",
        "name": "arrived_sms"
    }

    loading_begun_mail = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/div[1]/div[1]/div[1]",
        "name": "loading_begun_mail"
    }
    loading_begun_monitor = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[3]/div[1]/div[1]/div[1]",
        "name": "loading_begun_monitor"
    }
    loading_begun_sms = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[4]/div[1]/div[1]/div[1]",
        "name": "loading_begun_sms"
    }

    loading_completed_mail = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[2]/div[1]/div[1]/div[1]",
        "name": "loading_completed_mail"
    }
    loading_completed_monitor = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[3]/div[1]/div[1]/div[1]",
        "name": "loading_completed_monitor"
    }
    loading_completed_sms = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[4]/div[1]/div[1]/div[1]",
        "name": "loading_completed_sms"
    }

    documents_received_mail = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[2]/div[1]/div[1]/div[1]",
        "name": "documents_received_mail"
    }
    documents_received_monitor = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[3]/div[1]/div[1]/div[1]",
        "name": "documents_received_monitor"
    }
    documents_received_sms = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[4]/div[1]/div[1]/div[1]",
        "name": "documents_received_sms"
    }

    flight_over_mail = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[6]/td[2]/div[1]/div[1]/div[1]",
        "name": "flight_over_mail"
    }
    flight_over_monitor = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[6]/td[3]/div[1]/div[1]/div[1]",
        "name": "flight_over_monitor"
    }
    flight_over_sms = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[6]/td[4]/div[1]/div[1]/div[1]",
        "name": "flight_over_sms"
    }

    flight_confirmation_mail = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]",
        "name": "flight_confirmation_mail"
    }
    flight_confirmation_monitor = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]/div[1]/div[1]",
        "name": "flight_confirmation_monitor"
    }
    flight_confirmation_sms = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[1]/div[1]/div[1]",
        "name": "flight_confirmation_sms"
    }

    register_confirmation_mail = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[1]",
        "name": "register_confirmation_mail"
    }
    register_confirmation_monitor = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/div[1]/div[1]/div[1]",
        "name": "register_confirmation_monitor"
    }
    register_confirmation_sms = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[4]/div[1]/div[1]/div[1]",
        "name": "register_confirmation_sms"
    }

    registry_not_confirmed_mail = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/div[1]/div[1]/div[1]",
        "name": "registry_not_confirmed_mail"
    }
    registry_not_confirmed_monitor = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[3]/div[1]/div[1]/div[1]",
        "name": "registry_not_confirmed_monitor"
    }
    registry_not_confirmed_sms = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[4]/div[1]/div[1]/div[1]",
        "name": "registry_not_confirmed_sms"
    }

    critical_charge_mail = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]",
        "name": "critical_charge_mail"
    }
    critical_charge_monitor = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]/div[1]/div[1]",
        "name": "critical_charge_monitor"
    }
    critical_charge_sms = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[1]/div[1]/div[1]",
        "name": "critical_charge_sms"
    }

    no_connection_mail = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[1]",
        "name": "no_connection_mail"
    }
    no_connection_monitor = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/div[1]/div[1]/div[1]",
        "name": "no_connection_monitor"
    }
    no_connection_sms = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[4]/div[1]/div[1]/div[1]",
        "name": "no_connection_sms"
    }

    cargo_not_accepted_mail = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]",
        "name": "cargo_not_accepted_mail"
    }
    cargo_not_accepted_monitor = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]/div[1]/div[1]",
        "name": "cargo_not_accepted_monitor"
    }
    cargo_not_accepted_sms = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[1]/div[1]/div[1]",
        "name": "cargo_not_accepted_sms"
    }

    address_missing_mail = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[1]",
        "name": "address_missing_mail"
    }
    address_missing_monitor = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/div[1]/div[1]/div[1]",
        "name": "address_missing_monitor"
    }
    address_missing_sms = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[4]/div[1]/div[1]/div[1]",
        "name": "address_missing_sms"
    }

    safe_notifications = {
        "xpath": "//div[contains(@class,'vz-form-actions vz-form-actions--right')]//button[1]",
        "name": "safe_notifications"
    }


class NotificationLKE(Base):
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


class ResetNotifications(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    fields_2 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_2"
    }
    fields_3 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_3"
    }
    fields_4 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_4"
    }
    fields_5 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_5"
    }
    fields_6 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[6]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_6"
    }
    fields_7 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[7]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_7"
    }
    fields_8 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[8]/td[4]/div[1]/div[1]/div[1]/div[2]",
        "name": "fields_8"
    }

    fields_9 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_9"
    }
    fields_10 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_10"
    }
    fields_11 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_11"
    }
    fields_12 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_12"
    }
    fields_13 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_13"
    }
    fields_14 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[6]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_14"
    }
    fields_15 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_15"
    }
    fields_16 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_16"
    }
    fields_17 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_17"
    }
    fields_18 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_18"
    }
    fields_19 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_19"
    }
    fields_20 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_20"
    }
    fields_21 = {
        "xpath": "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/form[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[4]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]",
        "name": "fields_21"
    }