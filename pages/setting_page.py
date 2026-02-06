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
    """Address Group"""
    addresses_subsection = {
        "xpath": "//div[contains(text(),'Показать/скрыть настройки групп')]",
        "name": "addresses_subsection"
    }
    create_group = {
        "xpath": "//p[@class='no-margin']",
        "name": "create_group"
    }
    name_group_rus = {
        "xpath": "//label[@class='vz-form-item vz-form-item--required']//input[@type='text']",
        "name": "name_group_rus"
    }
    name_group_eng = {
        "xpath": "//div[@class='ant-col ant-col-12 vz-form-col']//label[@class='vz-form-item']//input[@type='text']",
        "name": "name_group_eng"
    }
    save_group = {
        "xpath": "//button[@class='ant-btn margin-top-35 margin-left-auto ant-btn-primary']",
        "name": "save_group"
    }
    add_confirm = {
        "xpath": "//div[@class='ant-modal-confirm-btns']//button[@type='button']",
        "name": "add_confirm"
    }
    edit_group = {
        "xpath": "//tbody/tr[3]/td[4]/div[1]/div[1]/img[1]",
        "name": "edit_group"
    }
    delete_group = {
        "xpath": "//tbody/tr[3]/td[4]/div[1]/div[2]/img[1]",
        "name": "delete_group"
    }
    reject_delete = {
        "xpath": "//button[@class='ant-btn']",
        "name": "reject_delete"
    }
    accept_delete = {
        "xpath": "//body//div//button[2]",
        "name": "accept_delete"
    }
    add_del = {
        "xpath": "//div[@class='ant-modal-confirm-btns']//button[@type='button']",
        "name": "add_del"
    }


