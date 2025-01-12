from base.base_class import Base


class Settings(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    notifications_field_tab = {
        "xpath": "//a[@href='/settings/notification']",
        "name": "notifications_field",
        "reference_xpath": "Настройки уведомлений"
    }
    custom_fields_tab = {
        "xpath": "//a[text()='Пользовательские поля']",
        "name": "custom_field",
        "reference_xpath": "(//a[@class='vz-tabs-modern__item'])[3]"
    }
    add_field_button = {
        "xpath": "//button[@class='mid element-button theme-primary']",
        "name": "add_field_button",
        "reference_xpath": "// button[contains(., 'Добавить поле')]",
        "reference": "Добавить поле"
    }


class CustomFieldsParam(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_ru = {
        "xpath": "//input[@class='ant-input']",
        "name": "add_ru",
        "reference_xpath": "//span[text()='Наименование поля на кириллице']/following::input",
        "reference": "Наименование поля на кириллице"
    }
    add_en = {
        "xpath": "(//input[@class='ant-input'])[2]",
        "name": "add_en",
        "reference_xpath": "//span[text()='Наименование поля на латинице']/following::input",
        "reference": "Наименование поля на латинице"
    }
    add_role = {
        "xpath": "//div[@class='ant-select-selection__rendered']",
        "name": "add_role"
    }
    add_type = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[2]",
        "name": "add_role"
    }
    save_custom = {
        "xpath": "//button[@class='ant-btn margin-right-16']/following-sibling::button[1]",
        "name": "save_custom"
    }
    done_pop_up = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[2]",
        "name": "done_pop_up"
    }
    done_pop_up_second = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[3]",
        "name": "done_pop_up_second"
    }


class EditFieldsParam(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    e_p = {
        "xpath": "(// img[@ alt='editBlack'])[2]",
        "name": "e_p"
    }
    del_custom = {
        "xpath": "(//img[@alt='trashBinBlack'])[2]",
        "name": "del_custom"
    }
    acc_del = {
        "xpath": "//button[@class='ant-btn']/following-sibling::button[1]",
        "name": "acc_del"
    }
    rej_del = {
        "xpath": "//div[@class='ant-modal-confirm-btns']//button[1]",
        "name": "rej_del"
    }
    add_val = {
        "xpath": "(//div[contains(@class,'flexbox justify-right')]//button)[2]",
        "name": "add_val"
    }
    unique_number_value = {
        "xpath": "(//input[@class='ant-input'])[3]",
        "name": "unique_number_value"
    }
    name_value = {
        "xpath": "//input[@placeholder='Наименование значения']",
        "name": "name_value"
    }
    save_unique_value = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[3]",
        "name": "name_value"
    }
    edit_value = {
        "xpath": "(//button[contains(@class,'ant-btn margin-right-8')])[2]",
        "name": "edit_value"
    }
    delete_value = {
        "xpath": "(//button[@class='ant-btn ant-btn-sm'])[2]",
        "name": "delete_value"
    }




