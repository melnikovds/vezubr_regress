from base.base_class import Base


class Settings(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    custom_field = {
        "xpath": "//a[text()='Пользовательские поля']",
        "name": "custom_field",
        "reference_xpath": "(//a[@class='vz-tabs-modern__item'])[3]"
    }
    add_field = {
        "xpath": "//button[contains(@class,'mid element-button')]",
        "name": "add_field",
        "reference_xpath": "//a[text()='Добавить поле']"
    }
    edit_field = {
        "xpath": "(//img[@alt='editBlack'])[2]",
        "name": "edit_field"
    }
    delete_field = {
        "xpath": "(//img[@alt='trashBinBlack'])[2]",
        "name": "delete_field"
    }
    delete_ok = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "delete_ok"
    }


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
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[2]",
        "name": "click_save"
    }
    click_save_two = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "click_save_two"
    }
    click_ok = {
        "xpath": "//div[@class='ant-modal-confirm-btns']//button[1]",
        "name": "click_ok"
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
    click_require_field = {
        "xpath": "//button[@class='ant-switch ant-switch-checked']",
        "name": "require_field"
    }

