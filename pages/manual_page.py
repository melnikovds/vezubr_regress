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


    surname_driver = {
    "xpath": "//input[@class='ant-input']",
    "name": "surname_driver"
    }
    status_in_system = {
    "xpath": "//div[@class='ant-select-selection__rendered']",
    "name": "status_in_system"
    }
    status_on_flight = {
    "xpath": "(//div[@class='ant-select-selection__rendered'])[2]",
    "name": "status_on_flight"
    }
    name_driver = {
    "xpath": "(//input[@class='ant-input'])[3]",
    "name": "name_driver"
    }
    patronymic_driver = {
    "xpath": "//input[@placeholder='Отчество']",
    "name": "patronymic_driver"
    }
    telephone_driver = {
    "xpath": "//label[text()='Телефон']/following::input",
    "name": "telephone_driver"
    }

    cross_two = {
    "xpath": "(//span[@unselectable='on']//i)[2]",
    "name": "cross_two"
    }
    cross_three = {
    "xpath": "(//span[@class='ant-select-arrow']//i)[2]",
    "name": "cross_three"
    }

    tractor_number = {
    "xpath": "//input[@class='ant-input']",
    "name": "tractor_number"
    }
    status_in_system_two = {
    "xpath": "//div[@class='ant-select-selection__rendered']",
    "name": "status_in_system_two"
    }
    status_on_flight_two = {
    "xpath": "(//div[@class='ant-select-selection__rendered'])[2]",
    "name": "status_on_flight_two"
    }


    trailer_number = {
    "xpath": "//input[@class='ant-input']",
    "name": "trailer_number"
    }
    type_road_transport = {
    "xpath": "//span[@class='ant-select-selection__rendered']",
    "name": "type_road_transport"
    }
    status_in_system_three = {
    "xpath": "//div[@class='ant-select-selection__rendered']",
    "name": "status_in_system_three"
    }
    status_on_flight_three = {
    "xpath": "(//div[@class='ant-select-selection__rendered'])[2]",
    "name": "status_on_flight_three"
    }
    cargo_transportation = {
    "xpath": "//span[@title='Грузовая']",
    "name": "cargo_transportation"
    }
    special_transportation = {
    "xpath": "//span[@class='ant-select-tree-switcher ant-select-tree-switcher_close']",
    "name": "special_transportation"
    }
    cross_four = {
    "xpath": "(//i[contains(@class,'anticon anticon-down')])[3]",
    "name": "cross_four"
    }
    mainline_trawl = {
    "xpath": "//span[@class='ant-select-tree-node-content-wrapper ant-select-tree-node-content-wrapper-normal']",
    "name": "mainline_trawl"
    }
    cistern_car = {
    "xpath": "//span[@title='Цистерна']",
    "name": "cistern_car"
    }
    dump_truck = {
    "xpath": "//span[@title='Самосвал']",
    "name": "dump_truck"
    }
    car_transporter = {
    "css": "div#rc-tree-select-list_1>ul>li:nth-of-type(2)>ul>li:nth-of-type(4)>span:nth-of-type(2)",
    "name": "car_transporter"
    }
    container_truck = {
    "xpath": "//span[@title='Контейнеровоз']",
    "name": "container_truck"
    }
    cross_five = {
    "xpath": "//i[contains(@class,'anticon anticon-down')]",
    "name": "cross_five"
    }


















    specialist_type = {
        "xpath": "//ul[@class='ant-select-selection__rendered']/following-sibling::span[1]",
        "name": "specialist_type"
    }
    specialist_type_field = {
        "xpath": "//span[@class='ant-select-selection ant-select-selection--multiple']",
        "name": "specialist_type_field"
    }
    specialist_checkbox_one = {
        "xpath": "(//span[@class='ant-select-tree-checkbox-inner'])[1]",
        "name": "specialist_checkbox_one"
    }
    specialist_checkbox_two = {
        "xpath": "(//span[@class='ant-select-tree-checkbox-inner'])[2]",
        "name": "specialist_checkbox_two"
    }
    specialist_checkbox_three = {
        "xpath": "(//span[@class='ant-select-tree-checkbox-inner'])[3]",
        "name": "specialist_checkbox_three"
    }
    specialist_checkbox_four = {
        "css": "div#rc-tree-select-list_1>ul>li:nth-of-type(4)>span:nth-of-type(2)>span",
        "name": "specialist_checkbox_four"
    }
    specialist_checkbox_five = {
        "css": "div#rc-tree-select-list_1>ul>li:nth-of-type(5)>span:nth-of-type(2)>span",
        "name": "specialist_checkbox_five"
    }
    specialist_checkbox_six = {
        "css": "div#rc-tree-select-list_1>ul>li:nth-of-type(6)>span:nth-of-type(2)>span",
        "name": "specialist_checkbox_six"
    }
    specialist_checkbox_seven = {
        "css": "div#rc-tree-select-list_1>ul>li:nth-of-type(7)>span:nth-of-type(2)>span",
        "name": "specialist_checkbox_seven"
    }
    specialist_checkbox_eight = {
        "css": "div#rc-tree-select-list_1>ul>li:nth-of-type(8)>span:nth-of-type(2)>span",
        "name": "specialist_checkbox_eight"
    }
    specialist_type_cross = {
        "xpath": "//span[@class='ant-select-selection ant-select-selection--multiple']",
        "name": "specialist_type_cross"
    }

    specialist_surname = {
    "xpath": "//input[@placeholder='Фамилия']",
    "name": "specialist_surname"
    }
    specialist_name = {
    "xpath": "//input[@placeholder='Имя']",
    "name": "specialist_name"
    }
    specialist_patronymic = {
    "xpath": "//input[@placeholder='Отчество']",
    "name": "specialist_patronymic"
    }
    specialist_telephone = {
    "xpath": "//label[text()='Телефон']/following::input",
    "name": "specialist_telephone"
    }

    loader = {
    "xpath": "//span[@class='ant-select-tree-checkbox-inner']",
    "name": "loader"
    }














