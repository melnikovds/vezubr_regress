from base.base_class import Base


class Company(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    subdivision = {
        "xpath": "//div[@class='ant-collapse-header']",
        "name": "subdivision"
    }
    muve = {
        "xpath": "//div[text()='Причины отмены Заявок/Рейсов ']",
        "name": "muve"
    }
    add_subdivision = {
        "xpath": "//button[contains(@class,'filter-button rounded')]//span[1]",
        "name": "add_subdivision"
    }
    name_subdivision = {
        "xpath": "(//label[text()='Название подразделения']/following::input)[3]",
        "name": "name_subdivision"
    }
    id_subdivision = {
        "xpath": "(//span[text()='Идентификатор в системе'])[2]/following::input",
        "name": "id_subdivision"
    }
    save_subdivision = {
        "xpath": "//button[contains(@class,'ant-btn margin-top-35')]",
        "name": "save_subdivision"
    }
    click_edit_subdivision = {
        "xpath": "//img[@alt='editBlack']",
        "name": "click_edit_subdivision"
    }
    del_subdivision = {
        "xpath": "//img[@alt='trashBinBlack']",
        "name": "del_subdivision"
    }
    del_confirm = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[2]",
        "name": "del_confirm"
    }
    ok_button = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[2]",
        "name": "ok_button"
    }
    click_users = {
        "xpath": "(//a[@class='vz-tabs-modern__item'])[3]",
        "name": "click_users"
    }
    edit_user = {
        "xpath": "//*[@id='main']/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]"
                 "/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/img[1]",
        "name": "edit_user"
    }
    change_user_to_subdivision = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[4]",
        "name": "change_user_to_subdivision"
    }
    click_save = {
        "xpath": "//button[contains(@class,'ant-btn semi-wide')]",
        "name": "click_save"
    }
    click_ok = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "click_ok"
    }
    click_users_lkz_lkp = {
        "xpath": "(//a[@class='vz-tabs-modern__item'])[2]",
        "name": "click_user_lkz_lkp"
    }
