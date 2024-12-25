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





    safe_notifications = {
        "xpath": "//div[contains(@class,'vz-form-actions vz-form-actions--right')]//button[1]",
        "name": "safe_notifications"
    }

