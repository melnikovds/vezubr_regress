from base.base_class import Base


class Settings(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    personal_settings_tab = {
        "xpath": "//a[@class='vz-tabs-modern__item matched']",
        "name": "personal_settings_tab",
        "reference_xpath": ""
    }
    company_settings_tab = {
        "xpath": "//a[contains(text(),'Настройки компании')]",
        "name": "company_settings_tab",
        "reference_xpath": ""
    }
    contour_settings_tab = {
        "xpath": "//a[contains(text(),'Настройки контура')]",
        "name": "contour_settings_tab",
        "reference_xpath": ""
    }
    custom_fields_tab = {
        "xpath": "//a[text()='Пользовательские поля']",
        "name": "custom_field",
        "reference_xpath": "(//a[@class='vz-tabs-modern__item'])[3]"
    }
    notifications_field_tab = {
        "xpath": "//a[@href='/settings/notification']",
        "name": "notifications_field",
        "reference_xpath": "Настройки уведомлений"
    }


class PersonalSettingsParams(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    monitor = {
        "xpath": "//span[contains(text(),'Выводить в мониторе')]",
        "name": "monitor"
    }
    customizing_top_menu = {
        "xpath": "//div[@class='topNavControl__select ant-select ant-select-enabled']//div[@role='combobox']",
        "name": "customizing_top_menu"
    }
    customizing_start_page = {
        "xpath": "//span[contains(text(),'Настройка стартовой страницы')]",
        "name": "customizing_start_page"
    }


class CustomFieldsParam(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_field_button = {
        "xpath": "//button[@class='mid element-button theme-primary']",
        "name": "add_field_button",
        "reference_xpath": "// button[contains(., 'Добавить поле')]",
        "reference": "Добавить поле"
    }
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
    e_p_one = {
        "xpath": "//tbody/tr[1]/td[1]/div[1]/div[1]/img[1]",
        "name": "e_p_one"
    }
    e_p_two = {
        "xpath": "//tbody/tr[1]/td[1]/div[1]/div[1]/img[1]",
        "name": "e_p_two"
    }
    del_custom = {
        "xpath": "//tbody/tr[1]/td[1]/div[1]/div[2]/img[1]",
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




