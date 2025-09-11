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
    type_road_transport_two = {
        "xpath": "//span[@class='ant-select-selection ant-select-selection--multiple']",
        "name": "type_road_transport_two"
    }
    cross_six = {
        "xpath": "/html/body/div[2]/div/div[3]/div[2]/div/form/div[2]/div[1]/div/div[2]/div/span/span/span/span[1]",
        "name": "cross_six"
    }
    cargo_passenger_transportation = {
        "xpath": "(//span[@class='ant-select-tree-checkbox-inner'])[2]",
        "name": "cargo_passenger_transportation"
    }
    transport_number = {
        "xpath": "//input[@class='ant-input']",
        "name": "transport_number"
    }
    cross_seven = {
        "xpath": "/html/body/div[2]/div/div[3]/div[2]/div/form/div[2]/div[2]/div/div[2]/div/span/span/span/span[1]/span/i[1]",
        "name": "cross_seven"
    }
    cross_eight = {
        "xpath": "/html/body/div[2]/div/div[3]/div[2]/div/form/div[2]/div[4]/div/div[2]/div/span/div/div/span",
        "name": "cross_eight"
    }
    surname_driver_two = {
        "xpath": "(//input[@class='ant-input'])[3]",
        "name": "surname_driver_two"
    }
    name_driver_two = {
        "xpath": "//label[text()='Имя водителя']/following::input",
        "name": "name_driver_two"
    }
    patronymic_driver_two = {
        "xpath": "//label[text()='Отчество водителя']/following::input",
        "name": "patronymic_driver_two"
    }

    special_transportation = {
        "xpath": "//span[@class='ant-select-tree-switcher ant-select-tree-switcher_close']",
        "name": "special_transportation"
    }
    cross_four = {
        "xpath": "(//i[contains(@class,'anticon anticon-down')])[3]",
        "name": "cross_four"
    }
    manipulator_truck = {
        "xpath": "//span[@title='Манипулятор']",
        "name": "manipulator_truck"
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
    # status = {
    #     "xpath": "//div[@class='ant-select-selection__placeholder']",
    #     "name": "status"
    # }
    status = {
        "xpath": "//div[@id='status']//div[@class='ant-select-selection__rendered']//div[1]",
        "name": "status"
    }
    active_status = {
        "xpath": "//li[@title='Активный']",
        "name": "active_status"
    }
    inactive_status = {
        "xpath": "//li[@title='Неактивный']",
        "name": "inactive_status"
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


    surname_driver = {
        "xpath": "//input[@class='ant-input']",
        "name": "surname_driver"
    }
    status_driver = {
        "xpath": "//div[@class='ant-select-selection__placeholder']",
        "name": "status_driver"
    }
    name_driver = {
        "xpath": "(//input[@class='ant-input'])[3]",
        "name": "name_driver"
    }
    driver_status = {
        "xpath": "//div[@id='status']//div[@class='ant-select-selection__rendered']",
        "name": "driver_status"
    }
    flight_status = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[2]",
        "name": "flight_status"
    }
    patronymic_driver = {
        "xpath": "(//input[@class='ant-input'])[5]",
        "name": "patronymic_driver"
    }
    phone_driver = {
        "xpath": "(//input[@class='ant-input'])[7]",
        "name": "phone_driver"
    }
    contractor = {
        "xpath": "(//input[@class='ant-input'])[9]",
        "name": "contractor"
    }
    cross_status_in_the_system = {
        "xpath": "//div[@id='status']//i[@aria-label='icon: close-circle']//*[name()='svg']//*[name()='path' and contains(@d,'M512 64C26')]",
        "name": "cross_status_in_the_system"
    }
    cross_status_in_flight = {
        "xpath": "//div[@id='uiState']//i[@aria-label='icon: close-circle']//*[name()='svg']",
        "name": "cross_status_in_flight"
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
    # cross_status_in_the_system_tractor = {
    #     "xpath": "//i[@aria-label='icon: close-circle']//*[name()='svg']//*[name()='path' and contains(@d,'M512 64C26')]",
    #     "name": "cross_status_in_the_system_tractor"
    # }
    cross_status_in_the_system_tractor = {
        "xpath": "//i[@aria-label='icon: close-circle']//*[name()='svg']",
        "name": "cross_status_in_the_system_tractor"
    }
    cross_status_in_flight_tractor = {
        "xpath": "//div[@id='uiState']//i[@aria-label='icon: close-circle']//*[name()='svg']",
        "name": "cross_status_in_flight_tractor"
    }
    tractor_status = {
        "xpath": "//div[@id='status']//div[@class='ant-select-selection__rendered']",
        "name": "tractor_status"
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
    cross_status_in_the_system_trailer = {
        "xpath": "//div[@id='status']//i[@aria-label='icon: close-circle']//*[name()='svg']",
        "name": "cross_status_in_the_system_trailer"
    }
    cross_status_in_flight_trailer = {
        "xpath": "//div[@id='uiState']//i[@aria-label='icon: close-circle']//*[name()='svg']//*[name()='path' and contains(@d,'M512 64C26')]",
        "name": "cross_status_in_flight_trailer"
    }
    cross_type_of_road_trailer = {
        "xpath": "//*[name()='path' and contains(@d,'M512 64C26')]",
        "name": "cross_type_of_road_trailer"
    }
    trailer_status = {
        "xpath": "//div[@id='status']//div[@class='ant-select-selection__rendered']",
        "name": "trailer_status"
    }
    trailer_cargo_transportation = {
        "xpath": "//span[@title='Грузовая']",
        "name": "trailer_cargo_transportation"
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
