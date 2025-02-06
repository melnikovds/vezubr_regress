from base.base_class import Base


class CustomFieldParam(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    add_ru = {
        "xpath": "//input[@class='ant-input']",
        "name": "add_ru",
    }
    add_en = {
        "xpath": "(//input[@class='ant-input'])[2]",
        "name": "add_en",
        "reference_xpath": "//span[text()='Наименование поля на латинице']/following::input"
    }
    add_role = {
        "xpath": "//div[@class='ant-select-selection__rendered']",
        "name": "add_role"
    }
    add_type = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[2]",
        "name": "add_type"
    }
    click_save = {
        "xpath": "//button[@class='ant-btn margin-right-16']/following-sibling::button[1]",
        "name": "click_save",
        #"reference_xpath": "//button[@class='ant-btn margin-right-16']/following-sibling::button[1]"
    }
    click_ok = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[2]",
        "name": "click_ok",
        #"reference_xpath": "//button[@class='ant-btn margin-right-16']/following-sibling::button[1]"
    }
    click_meaning = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "click_meaning"
    }
    unic_n = {
        "xpath": "(//input[@class='ant-input'])[3]",
        "name": "unic_n"
    }
    named_n = {
        "xpath": "//input[@placeholder='Наименование значения']",
        "name": "named_n"
    }
    confirm_add = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[3]",
        "name": "confirm_add",
        "reference_xpath": "//button[span[text()='Сохранить']]"
    }
