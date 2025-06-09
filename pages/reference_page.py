from base.base_class import Base


class Filter(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    creation_date = {
        "xpath": "//div[@class='ant-select-selection__rendered']",
        "name": "creation_date"
    }
    confirm_address = {
        "xpath": "(//input[@class='ant-input'])[3]",
        "name": "confirm_address"
    }
    name_address = {
        "xpath": "(//input[@class='ant-input'])[5]",
        "name": "name_address"
    }
    sender_recipient = {
        "xpath": "//input[@placeholder='Отправитель/Получатель']",
        "name": "sender_recipient"
    }
    status = {
        "xpath": "//div[@class='ant-select-selection__placeholder']",
        "name": "status"
    }
    region = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[3]",
        "name": "region"
    }
    refresh = {
        "xpath": "//button[contains(@class,'ant-btn semi-wide')]",
        "name": "refresh"
    }
    id_address = {
        "xpath": "(//span[@class ='ant-table-column-title'])[7]",
        "name": "active_dop"
    }
    confirmed = {
        "xpath": "(//input[@class='ant-input'])[9]",
        "name": "confirmed"
    }
    created = {
        "xpath": "//input[@placeholder='Создал']",
        "name": "created"
    }
    partner_id = {
        "xpath": "//input[@placeholder='ID Адреса Партнёра']",
        "name": "partner_id"
    }
    address_owner = {
        "xpath": "//input[@placeholder='Владелец Адреса']",
        "name": "address_owner"
    }
    save_button = {
        "xpath": "(//button[contains(@class,'ant-btn semi-wide')])[2]",
        "name": "save_button"
    }
    filter_name = {
        "xpath": "(//input[@data-__field='[object Object]'])[10]",
        "name": "filter_name"
    }
    save_filter = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "save_filter"
    }
    filter_saved = {
        "xpath": "//button[contains(@class,'ant-btn filters-apply__button')]",
        "name": "filer_saved"
    }
    edit_filter = {
        "xpath": "(//img[@class='element-icon pointer'])[2]",
        "name": "edit_filter"
    }
    edit_filter_name = {
        "xpath": "(//input[contains(@class,'ant-input ant-input-sm')])[2]",
        "name": "edit_filter_name"
    }
    save_filter_name = {
        "xpath": "//button[contains(@class,'ant-btn filters-apply__save-button')]",
        "name": "save_filter_name"
    }
    default_filter = {
        "xpath": "//input[@type='radio']",
        "name": "default_filter"
    }
    save_default_filter = {
        "xpath": "(//button[contains(@class,'ant-btn semi-wide')])[3]",
        "name": "save_default_filter"
    }
    close_default_filter = {
        "xpath": "(//button[@type='button']//span)[6]",
        "name": "close_default_filter"
    }
    delete_filter = {
        "xpath": "(//img[@class='element-icon pointer'])[3]",
        "name": "delete_filter"
    }
    tariff_name = {
        "xpath": "//input[@class='ant-input']",
        "name": "tariff_name"
    }
    tariff_status = {
        "xpath": "//div[@data-__field='[object Object]']//div",
        "name": "tariff_not_active"
    }
    soname_driver = {
        "xpath": "//input[@class='ant-input']",
        "name": "soname_driver"
    }
    status_driver = {
        "xpath": "//div[@class='ant-select-selection__placeholder']",
        "name": "status_driver"
    }
    name_driver = {
        "xpath": "(//input[@class='ant-input'])[3]",
        "name": "name_driver"
    }
    flight_status = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[2]",
        "name": "flight_status"
    }
    surname = {
        "xpath": "(//input[@class='ant-input'])[5]",
        "name": "surname"
    }
    phone_driver = {
        "xpath": "(//input[@class='ant-input'])[7]",
        "name": "phone_driver"
    }
    contractor = {
        "xpath": "(//input[@class='ant-input'])[9]",
        "name": "contractor"
    }
    number_of_tractor = {
        "xpath": "//label[text()='Госномер Тягача']/following::input",
        "name": "number_of_tractor"
    }
    status_tractor = {
        "xpath": "//div[@data-__field='[object Object]']//div",
        "name": "status_tractor"
    }
    flight_status_tractor = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[2]",
        "name": "flight_status_tractor"
    }
    contractor_tractor = {
        "xpath": "(//input[@class='ant-input'])[3]",
        "name": "contractor_tractor"
    }
    number_of_trailer = {
        "xpath": "//label[text()='Госномер Полуприцепа']/following::input",
        "name": "number_of_trailer"
    }
    status_trailer = {
        "xpath": "//div[@data-__field='[object Object]']//div",
        "name": "status_trailer"
    }
    type_of_road_trailer = {
        "xpath": "//span[@class='ant-select-selection__rendered']",
        "name": "type_of_road_trailer"
    }
    type_of_road_trailer_change = {
        "css": "span.ant-select-tree-node-content-wrapper.ant-select-tree-node-content-wrapper-normal",
        "name": "type_of_road_trailer_change"
    }
    flight_status_trailer = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[2]",
        "name": "flight_status_trailer"
    }
    contractor_trailer = {
        "xpath": "(//input[@class='ant-input'])[3]",
        "name": "contractor_trailer"
    }
    specialist_type = {
        "xpath": "//ul[@class='ant-select-selection__rendered']/following-sibling::span[1]",
        "name": "specialist_type"
    }
    specialist_type_check = {
        "xpath": "(//span[@class='ant-select-tree-checkbox-inner'])[1]",
        "name": "specialist_type_check"
    }
    specialist_click_check = {
        "xpath": "//span[@class='ant-select-selection ant-select-selection--multiple']//ul[1]",
        "name": "specialist_type_check"
    }
    # specialist_type_uncheck = {
    #    "xpath": "//span[@class='ant-select-tree-checkbox ant-select-tree-checkbox-checked']//span[1]",
    #    "name": "specialist_type_check"
    # }
    surname_specialist = {
        "xpath": "(//input[@class='ant-input'])[1]",
        "name": "surname_specialist"
    }
    name_specialist = {
        "xpath": "(//input[@class='ant-input'])[3]",
        "name": "name_specialist"
    }
    soname_specialist = {
        "xpath": "(//input[@class='ant-input'])[5]",
        "name": "soname_specialist"
    }
    phone_specialist = {
        "xpath": "(//input[@class='ant-input'])[7]",
        "name": "phone_specialist"
    }
    contractor_specialist = {
        "xpath": "(//input[@class='ant-input'])[9]",
        "name": "contactor_specialist"
    }
    speshl_click_driver = {
        "xpath": "//div[@class='ant-table-column-sorters']",
        "name": "speshl_click_driver"
    }
    spisok = {
        "xpath": "//span[@class='ant-select-tree-switcher ant-select-tree-switcher_close']",
        "name": "spisok"
    }
    x_button = {
        "css": "i.anticon.anticon-close-circle.ant-input-clear-icon",
        "name": "x_button"
    }
    x_button1 = {
        "css": "i.anticon.anticon-close-circle.ant-input-clear-icon",
        "name": "x_button1"
    }
    x_button2 = {
        "css": ".ant-select-selection--single",
        "name": "x_button2"
    }
    x1_button = {
        "css": ".ant-select-focused .ant-select-selection__placeholder",
        "name": "x1_button"
    }
    x2_button = {
        "css": ".ant-select-switcher-icon path",
        "name": "x2_button"
    }
    x3_button = {
        "css": ".ant-select-tree-child-tree > .ant-select-tree-treenode-switcher-close:nth-child(1) "
               ".ant-select-tree-title",
        "name": "x3_button"
    }
    x4_button = {
        "css": ".filter-item:nth-child(2) .ant-select-selection__clear:nth-child(2) path:nth-child(1)",
        "name": "x4_button"
    }
    number_vehicles = {
        "xpath": "//input[@class='ant-input']",
        "name": "number_vehicles"
    }
    name_driver_vehicle = {
        "xpath": "(//input[@class='ant-input'])[5]",
        "name": "name_driver_vehicle"
    }
    surname_driver_vehicle = {
        "xpath": "//input[@placeholder='Фамилия водителя']",
        "name": "surname_driver_vehicle"
    }
    patronymic_driver_vehicle = {
        "xpath": "(//input[@class='ant-input'])[7]",
        "name": "patronymic_driver_vehicle"
    }
    contractor_vehicle = {
        "xpath": "(//input[@class='ant-input'])[9]",
        "name": "contractor_vehicle"
    }