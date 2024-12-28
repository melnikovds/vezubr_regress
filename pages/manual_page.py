from base.base_class import Base


class Manual(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    filter_date_create = {
        "xpath": "//div[@class='ant-select-selection__rendered']",
        "name": "filter_date_create"
    }
    verified_address = {
        "xpath": "(//input[@class='ant-input'])[3]",
        "name": "verified_address"
    }
    name_address = {
        "xpath": "//input[@placeholder='Название адреса']",
        "name": "name_address"
    }
    sender_recipient = {
        "xpath": "//input[@placeholder='Отправитель/Получатель']",
        "name": "sender_recipient"
    }
    status = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[2]",
        "name": "status"
    }
    region = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[3]",
        "name": "region"
    }
    approved = {
        "xpath": "//input[@placeholder='Подтвердил']",
        "name": "approved"
    }
    created = {
        "xpath": "//input[@placeholder='Создал']",
        "name": "created"
    }
    reset = {
        "xpath": "//button[contains(@class,'ant-btn semi-wide')]",
        "name": "reset"
    }








    # filter_date_create = {
    #     "xpath": "//div[@class='ant-select-selection__rendered']",
    #     "name": "filter_date_create",
    #     "reference_xpath": "//div[text()='За год']",
    #     "reference": "За год"
    # }

