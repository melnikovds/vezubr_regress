from base.base_class import Base


class ContractorList(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    contractor_inn = {
        "xpath": "//input[@placeholder='ИНН']",
        "name": "contractor_inn"
    }
    contractor_name = {
        "xpath": "//div[@class='table-filters-main-zone']//div[2]//div[1]//div[2]//div[1]//span[1]//span[1]//input[1]",
        "name": "contractor_name"
    }
    contractor_role = {
        "xpath": "//div[@class='ant-select-selection__placeholder']",
        "name": "contractor_role"
    }
    role_cross = {
        "xpath": "//i[@aria-label='icon: close-circle']//*[name()='svg']",
        "name": "role_cross"
    }
    first_role = {
        "xpath": "//li[@title='Подрядчик']",
        "name": "first_role"
    }
    second_role = {
        "xpath": "//li[@title='Экспедитор']",
        "name": "second_role"
    }
    contractor_role_modified = {
        "xpath": "//div[@class='ant-select-selection__rendered']",
        "name": "contractor_role_modified"
    }
    cancel_button = {
        "xpath": "//div[@class='ant-modal-body']//button[1]",
        "name": "cancel_button"
    }



