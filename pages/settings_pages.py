from base.base_class import Base


class Settings(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
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
        "xpath": "(//table[@class='ant-table-fixed']/following::table)[3]",
        "name": "delete_field"
    }
    delete_ok = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "delete_ok"
    }
    notification_field = {
        "xpath": "//a[@href='/settings/notification']",
        "name": "notification_field"
    }
    settings_subdivision = {
        "xpath": "//a[@class='vz-tabs-modern__item']",
        "name": "settings_subdivision"
    }
    profile_field = {
        "xpath": "(//li[contains(@class,'ant-menu-item sidebar__list-item')])[2]",
        "name": "profile_field"
    }
    profile_field_lkz = {
        "xpath": "(//li[contains(@class,'ant-menu-item sidebar__list-item')])[2]",
        "name": "profile_field_lkz"
    }
