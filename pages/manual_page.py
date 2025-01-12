from base.base_class import Base


class Manual(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
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
    id_address = {
        "xpath": "//input[@placeholder='ID Адреса Партнёра']",
        "name": "id_address"
    }

    reset = {
        "xpath": "//button[contains(@class,'ant-btn semi-wide')]",
        "name": "reset"
    }
    save_filter = {
        "xpath": "(//button[contains(@class,'ant-btn semi-wide')])[2]",
        "name": "save_filter"
    }
    name_filter = {
        "xpath": "//span[text()='НАЗВАНИЕ ФИЛЬТРА']/following::input",
        "name": "name_filter"
    }
    second_save_filter = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "second_save_filter"
    }
    saved_filters = {
        "xpath": "//button[contains(@class,'ant-btn filters-apply__button')]",
        "name": "saved_filters"
    }
    radio_input_two = {
        "xpath": "(//input[@type='radio'])[2]",
        "name": "radio_input_two"
    }
    apply_filter = {
        "xpath": "(//button[contains(@class,'ant-btn semi-wide')])[3]",
        "name": "apply_filter"
    }
    edit_filter = {
        "xpath": "(//img[@alt='editBlack'])[2]",
        "name": "edit_filter"
    }
    rename_filter = {
        "xpath": "//input[contains(@class,'ant-input ant-input-sm')]",
        "name": "rename_filter"
    }
    third_save_filter = {
        "xpath": "//button[contains(@class,'ant-btn filters-apply__save-button')]",
        "name": "third_save_filter"
    }
    radio_input_one = {
        "xpath": "//input[@class='ant-radio-input']",
        "name": "radio_input_one"
    }
    remove_filter = {
        "xpath": "(//img[@alt='trashBinOrange'])[2]",
        "name": "remove_filter"
    }
    cross = {
        "xpath": "//button[@class='ant-modal-close']//span[1]",
        "name": "cross"
    }

    tariff_name = {
        "xpath": "//label[text()='Название тарифа']/following::input",
        "name": "tariff_name"
    }
    tariff_status = {
        "xpath": "//div[@data-__field='[object Object]']//div",
        "name": "tariff_status"
    }








