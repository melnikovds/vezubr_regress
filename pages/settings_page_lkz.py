from base.base_class import Base


class Settings(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
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
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "save_custom"
    }

    done_pop_up = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[2]",
        "name": "done_pop_up"
    }



class EditFieldsParam(Base):
    def __init__(self, driver):
        super().__init__(driver)

    e_p = {
        "xpath": "(// img[@ alt='editBlack'])[2]",
        "name": "e_p"
    }

