from base.base_class import Base
import time


class ShipmentTaskAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    task_create_button = {
        "xpath": "//p[@class='no-margin']",
        "name": "task_create_button"
    }
    task_number = {
        "xpath": "//label[@class='vz-form-item vz-form-item--required']//input[@type='text']",
        "name": "task_number"
    }
    task_weight = {
        "xpath": "//div[@class='vzubr-white-box vzubr-white-box-wide']//div//div[2]//div[1]//div[1]//label[1]//div[1]//div[1]//div[1]//div[2]//input[1]",
        "name": "task_weight"
    }
    task_volume = {
        "xpath": "//div[@class='vz-form-row']//div[2]//label[1]//div[1]//div[1]//div[1]//div[2]//input[1]",
        "name": "task_volume"
    }
    task_cost = {
        "xpath": "//div[@class='vz-form-row']//div[3]//label[1]//div[1]//div[1]//div[1]//div[2]//input[1]",
        "name": "task_cost"
    }
    number_place = {
        "xpath": "//div[@class='dashboard-content margin-top-60']//div[3]//div[1]//div[1]//label[1]//div[1]//div[1]//div[1]//div[2]//input[1]",
        "name": "number_place"
    }
    type_package = {
        "xpath": "//body/div[@id='main']/div[@class='dashboard']/div[@class='dashboard-content margin-top-60']/div[@class='shipment-tasks page-shipment-tasks-create page-shipment-tasks-create path-shipment-tasks-create container']/div[@class='vzubr-white-box vzubr-white-box-wide']/div/div/div/div[@class='vz-form-group']/div[3]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[1]",
        "name": "type_package"
    }
    product_name = {
        "xpath": "//label[@class='vz-form-item']//span[@class='ant-input-affix-wrapper']//input[@type='text']",
        "name": "product_name"
    }
    whom_task = {
        "xpath": "//body/div[@id='main']/div[@class='dashboard']/div[@class='dashboard-content margin-top-60']/div[@class='shipment-tasks page-shipment-tasks-create page-shipment-tasks-create path-shipment-tasks-create container']/div[@class='vzubr-white-box vzubr-white-box-wide']/div/div/div/div[@class='vz-form-group']/div[3]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]/div[1]",
        "name": "whom_task"
    }
    departure_address = {
        "xpath": "//body/div[@id='main']/div[@class='dashboard']/div[@class='dashboard-content margin-top-60']/div[@class='shipment-tasks page-shipment-tasks-create page-shipment-tasks-create path-shipment-tasks-create container']/div[@class='vzubr-white-box vzubr-white-box-wide']/div/div/div/div[@class='vz-form-group']/div[@class='vz-form-row']/div[@class='ant-row-flex vz-form-row__native']/div[1]/button[1]",
        "name": "departure_address"
    }
    delivery_address = {
        "xpath": "//div[@class='vz-form-row']//div[2]//button[1]",
        "name": "delivery_address"
    }
    creation_complete = {
        "xpath": "//button[@class='ant-btn margin-left-10 ant-btn-primary']",
        "name": "creation_complete"
    }
    successfully_created = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "successfully_created"
    }


    task_edit_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "task_edit_button"
    }
    save_edit_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "save_edit_button"
    }
    whom_task_edit_button = {
        "xpath": "//div[@class='ant-select ant-select-enabled ant-select-allow-clear']//div[@class='ant-select-selection__rendered']",
        "name": "whom_task_edit_button"
    }






