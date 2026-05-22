from base.base_class import Base
import time
import allure


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
    switch_complete_gm = {
        "xpath": "//div[@class='vz-form-field-switch vz-form-field-switch__size-default']",
        "name": "switch_complete_gm"
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


    tab_characteristics = {
        "xpath": "//div[contains(text(),'Характеристики')]",
        "name": "tab_characteristics"
    }
    tab_gm = {
        "xpath": "//div[contains(text(),'Грузоместа')]",
        "name": "tab_gm"
    }
    tab_history = {
        "xpath": "//div[contains(text(),'История')]",
        "name": "tab_history"
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

    # Блок удаления заданий

    task_delete_button = {
        "xpath": "//button[@class='ant-btn ant-btn-danger']",
        "name": "task_delete_button"
    }
    task_delete_button_confirm = {
        "xpath": "//div[@class='ant-modal-root']//button[2]",
        "name": "task_delete_button_confirm"
    }
    task_delete_window_confirm = {
        "xpath": "//div[@class='ant-modal-confirm-btns']//button[@type='button']",
        "name": "task_delete_window_confirm"
    }

    # Блок передачи задания от ЛКЗ к ЛКЭ

    task_sdr_input = {
        "xpath": "//input[@placeholder='Номер заказа']",
        "name": "task_sdr_input"
    }
    first_request_click = {
        "xpath": "//a[@class='link-back'][normalize-space()='1']",
        "name": "first_request_click"
    }
    required_search_by_date_lke = {
        "xpath": "//div[@id='orders-maindate-select']//div[@role='combobox']",
        "name": "required_search_by_date"
    }
    confirm_request_button = {
        "xpath": "//button[@id='order-take']",
        "name": "confirm_request_button"
    }
    order_number = {
        "xpath": "//input[@placeholder='Номер заявки']",
        "name": "order_number"
    }
    required_search_by_date = {
        "xpath": "//div[@id='tasks-maindate-select']//div[@role='combobox']",
        "name": "required_search_by_date"
    }
    first_task_click = {
        "xpath": "//a[@class='link-back'][normalize-space()='1']",
        "name": "first_task_click"
    }

    # ========== Методы для работы с заявками ==========

    @allure.step("Поиск заявки по номеру в статусе 'Сегодня и завтра'")
    def find_request_by_number(self, request_number: str) -> None:
        """Поиск заявки по номеру в списке активных заявок"""
        self.dropdown_without_input(self.required_search_by_date_lke, "Сегодня и завтра")
        time.sleep(1)
        self.input_in_field(self.order_number, request_number, wait='lst')
        time.sleep(2)
        self.click_button(self.first_request_click)
        time.sleep(2)

    @allure.step("Подтверждение заявки (принятие)")
    def accept_request(self) -> None:
        """Подтверждение/принятие заявки экспедитором"""
        self.click_button(self.confirm_request_button)
        time.sleep(2)
        # Если есть диалог подтверждения
        # self.click_button(self.confirm_dialog_button)
        # time.sleep(2)

    @allure.step("Поиск задания по номеру в списке заданий")
    def find_task_by_number(self, task_number: str) -> None:
        """Поиск и открытие задания по номеру"""
        self.dropdown_without_input(self.required_search_by_date, "Сегодня и завтра")
        time.sleep(1)
        self.input_in_field(self.order_number, task_number, wait='lst')
        time.sleep(2)
        self.click_button(self.first_task_click)
        time.sleep(2)

    @allure.step("Проверка что открыто задание с номером {task_number}")
    def verify_task_opened(self, task_number: str) -> None:
        """Проверка что открыто правильное задание"""
        self.verify_text_on_page(task_number, should_exist=True)
