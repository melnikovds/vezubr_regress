from base.base_class import Base


class NewFtlFilters(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    clear = {
        "xpath": "//button[contains(@class,'ant-btn semi-wide')]",
        "name": "clear"
    }
    execution_start_sate = {
        "xpath": "//div[@id='orders-maindate-select']//div[@class='ant-select-selection__rendered']",
        "name": "execution_start_sate"
    }
    transportation_type = {
        "xpath": "//div[@id='deliveryType']//div[@class='ant-select-selection__placeholder'][contains(text(),'Все')]",
        "name": "transportation_type"
    }
    delivery_type = {
        "xpath": "//div[@id='deliverySubType']//div[@class='ant-select-selection__rendered']//div[1]",
        "name": "delivery_type"
    }
    request_number = {
        "xpath": "//input[@placeholder='Номер заявки']",
        "name": "request_number"
    }
    request_status = {
        "xpath": "//div[@id='status']//div[@role='combobox']",
        "name": "request_status"
    }
    client_identifier = {
        "xpath": "//input[@placeholder='Идентификатор клиента']",
        "name": "client_identifier"
    }
    publication_date = {
        "xpath": "//span[@id='undefined-rangepicker']//input[@placeholder='С']",
        "name": "publication_date"
    }
    request_in_work = {
        "xpath": "//div[@id='implementerEmployee']//div[@role='combobox']",
        "name": "request_in_work"
    }
    first_point_city = {
        "xpath": "//input[@placeholder='Город Отправления']",
        "name": "first_point_city"
    }
    last_point_city = {
        "xpath": "//input[@placeholder='Город Доставки']",
        "name": "last_point_city"
    }

    additional_filters = {
        "xpath": "//p[@class='no-margin']",
        "name": "additional_filters"
    }
    default_filters = {
        "xpath": "//button[contains(text(),'По умолчанию')]",
        "name": "default_filters"
    }
    checkbox_producer = {
        "xpath": "//div[@role='document']//div[1]//div[1]//label[1]//span[2]",
        "name": "checkbox_producer"
    }
    checkbox_inn = {
        "xpath": "//body//div[@id='main']//div[contains(@role,'dialog')]//div[contains(@role,'dialog')]//div[2]//label[1]//span[2]",
        "name": "checkbox_inn"
    }
    checkbox_surname = {
        "xpath": "//div[contains(@class,'modal-body')]//div[3]//label[1]//span[2]",
        "name": "checkbox_surname"
    }
    checkbox_name = {
        "xpath": "//div[4]//label[1]//span[2]",
        "name": "checkbox_name"
    }
    checkbox_plate = {
        "xpath": "//div[5]//label[1]//span[2]",
        "name": "checkbox_plate"
    }
    checkbox_publication_type = {
        "xpath": "//div[6]//label[1]//span[2]",
        "name": "checkbox_publication_type"
    }
    checkbox_transport_type = {
        "xpath": "//div[7]//label[1]//span[2]",
        "name": "checkbox_transport_type"
    }
    checkbox_first_point_address = {
        "xpath": "//div[8]//label[1]//span[2]",
        "name": "checkbox_first_point_address"
    }
    apply_filters = {
        "xpath": "//button[contains(text(),'Применить')]",
        "name": "apply_filters"
    }

    producer_filter = {
        "xpath": "//input[@placeholder='Все подрядчики']",
        "name": "producer_filter"
    }
    inn_filter = {
        "xpath": "//input[@placeholder='ИНН подрядчика']",
        "name": "inn_filter"
    }
    surname_filter = {
        "xpath": "//input[@placeholder='Фамилия водителя']",
        "name": "surname_filter"
    }
    name_filter = {
        "xpath": "//input[@placeholder='Имя водителя']",
        "name": "name_filter"
    }
    plate_filter = {
        "xpath": "//input[@placeholder='Госномер ТС']",
        "name": "plate_filter"
    }
    publication_type_filter = {
        "xpath": "//div[@id='selectingStrategy']//div[@class='ant-select-selection__rendered']",
        "name": "publication_type_filter"
    }
    transport_type_filter = {
        "xpath": "//div[@id='vehicleTypeId']//div[@class='ant-select-selection__rendered']",
        "name": "transport_type_filter"
    }
    first_point_address_filter = {
        "xpath": "//input[contains(@placeholder,'Адрес подачи')]",
        "name": "first_point_address_filter"
    }

    request_type = {
        "xpath": "//div[@id='requestDirection']//div[@class='ant-select-selection__placeholder'][contains(text(),'Все')]",
        "name": "request_type"
    }


