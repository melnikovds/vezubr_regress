import time
from typing import NoReturn
from base.base_class import Base


class GmFilters(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    order_number = {
        "xpath": "//input[@placeholder='Номер заказа']",
        "name": "order_number"
    }
    sender = {
        "xpath": "//input[@placeholder='Отправитель']",
        "name": "sender"
    }
    recipient = {
        "xpath": "//input[@placeholder='Получатель']",
        "name": "recipient"
    }
    to_aplication = {
        "xpath": "//div[text()='Кому передать Заявку']",
        "name": "to_aplication"
    }
    to_aplication_2 = {
        "xpath": "//div[@title='Маршрутизация Везубр']",
        "name": "to_aplication"
    }
    to_aplication_3 = {
        "xpath": "//div[text()='FM']",
        "name": "to_aplication_3"
    }
    del_aplication = {
        "xpath": "(//i[contains(@class,'anticon anticon-down')])[3]",
        "name": "to_aplication_2"
    }
    # region_dispatch = {
    #     "xpath": "(//div[@class='ant-select-selection__rendered'])[4]",
    #     "name": "region_dispatch"
    # }
    region_dispatch = {
        "xpath": "//div[@id='departureRegionId']//div[@class='ant-select-selection__rendered']//div[1]",
        "name": "region_dispatch"
    }
    region_dispatch_lkz = {
        "xpath": "//div[@id='departurePointRegion']//div[@class='ant-select-selection__rendered']//div[1]",
        "name": "region_dispatch_lkz"
    }
    del_region_dispatch = {
        "xpath": "(//i[contains(@class,'anticon anticon-down')])[4]",
        "name": "del_region_dispatch"
    }
    del_region_dispatch_gm = {
        "xpath": "//i[@aria-label='icon: close-circle']//*[name()='svg']",
        "name": "del_region_dispatch_gm"
    }
    city_dispatch = {
        "xpath": "//div[text()='Город отправки']",
        "name": "city_dispatch"
    }
    del_city_dispatch = {
        "xpath": "(//i[contains(@class,'anticon anticon-down')])[5]",
        "name": "del_city_dispatch"
    }
    # region_delivery = {
    #     "xpath": "//div[@id='arrivalPointRegion']//div[@role='combobox']",
    #     "name": "region_delivery"
    # }
    region_delivery = {
        "xpath": "//div[@id='deliveryRegionId']//div[@class='ant-select-selection__rendered']//div[1]",
        "name": "region_delivery"
    }
    region_delivery_lkz = {
        "xpath": "//div[@id='arrivalPointRegion']//div[@class='ant-select-selection__rendered']//div[1]",
        "name": "region_delivery_lkz"
    }
    del_region_delivery = {
        "xpath": "(//i[contains(@class,'anticon anticon-down')])[6]",
        "name": "del_region_delivery"
    }
    city_delivery = {
        "xpath": "//div[text()='Город доставки']",
        "name": "city_delivery"
    }
    del_city_delivery = {
        "xpath": "(//i[contains(@class,'anticon anticon-down')])[7]",
        "name": "del_city_delivery"
    }
    flight_number = {
        "xpath": "//input[@placeholder='Номер рейса']",
        "name": "flight_number"
    }
    according_task = {
        "xpath": "(//input[@class='ant-input'])[5]",
        "name": "according_task"
    }
    departure_address = {
        "xpath": "(//input[@class='ant-input'])[7]",
        "name": "departure_address"
    }
    delivery_address = {
        "xpath": "(//input[@class='ant-input'])[9]",
        "name": "delivery_address"
    }
    status = {
        "xpath": "//span[text()='Статус']",
        "name": "status"
    }
    waiting_shipment = {
        "xpath": "//span[@class='ant-select-tree-checkbox-inner']",
        "name": "waiting_shipment"
    }
    reset_filters = {
        "xpath": "//button[contains(@class,'ant-btn semi-wide')]",
        "name": "reset_filters"
    }
    creation_date = {
        "xpath": "//div[@class='ant-select-selection__rendered']",
        "name": "creation_date"
    }
    partner_gm_id = {
        "xpath": "(//input[@class='ant-input'])[5]",
        "name": "partner_gm_id"
    }
    type_gm = {
        "xpath": "//div[@class='ant-select-selection__placeholder']",
        "name": "type_gm"
    }
    type_gmv2 = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[2]",
        "name": "type_gmv2"
    }
    name_gm = {
        "xpath": "(//input[@class='ant-input'])[7]",
        "name": "type_gm"
    }
    departure_address_gm = {
        "xpath": "(//input[@class='ant-input'])[9]",
        "name": "departure_address_gm"
    }
    click_cross_type_gm = {
        "xpath": "(//i[contains(@class,'anticon anticon-down')])[2]",
        "name": "departure_address_gm"
    }
    delivery_address_gm = {
        "xpath": "//input[@placeholder='Адрес доставки']",
        "name": "delivery_address_gm"
    }
    invoice_number = {
        "xpath": "//input[@placeholder='Номер накладной']",
        "name": "invoice_number"
    }
    wms_number = {
        "xpath": "//input[@placeholder='Номер WMS']",
        "name": "wms_number"
    }
    bar_code = {
        "xpath": "//input[@placeholder='Bar code']",
        "name": "bar_code"
    }
    required_shipping_date = {
        "xpath": "//input[@placeholder='Bar code']",
        "name": "required_shipping_date"
    }
    required_delivery_date = {
        "xpath": "//input[@placeholder='Bar code']",
        "name": "required_delivery_date"
    }
    required_search_by_date = {
        "xpath": "//div[@id='tasks-maindate-select']//div[@role='combobox']",
        "name": "required_search_by_date"
    }

    cross_status_dispatch = {
        "xpath": "//i[@aria-label='icon: close-circle']//*[name()='svg']",
        "name": "cross_status_dispatch"
    }
    status_modified = {
        "xpath": "//ul[@role='menubar']",
        "name": "status_modified"
    }


    task_status = {
        "xpath": "//div[@id='status']//div[@class='ant-select-selection__rendered']//div[1]",
        "name": "task_status"
    }
    task_status_created = {
        "xpath": "//li[@title='Создано']",
        "name": "task_status_created"
    }
    task_status_pick_pending = {
        "xpath": "//li[@title='Ожидание сборки']",
        "name": "task_status_pick_pending"
    }
    task_status_in_progress = {
        "xpath": "//li[@title='В работе']",
        "name": "task_status_in_progress"
    }
    task_status_completed = {
        "xpath": "//li[@title='Исполнено']",
        "name": "task_status_completed"
    }
    task_cross = {
        "xpath": "//i[@aria-label='icon: close-circle']//*[name()='svg']//*[name()='path' and contains(@d,'M512 64C26')]",
        "name": "task_cross"
    }


    def to_whom_aplication(self) -> NoReturn:
        self.dropdown_without_input(self.to_aplication, "Маршрутизация Везубр")
        time.sleep(2)
        self.verify_text_on_page(text="Авто тест 1")
        self.dropdown_without_input(self.to_aplication_2, "FM")
        time.sleep(2)
        self.verify_text_on_page(text="Очень важное")
        self.dropdown_without_input(self.to_aplication_3, "Почта РФ")
        time.sleep(2)
        self.verify_text_on_page(text="11.06.2025 - 100")
        self.click_on_the_cross(self.del_aplication)
        time.sleep(2)

    def filters_region(self) -> NoReturn:
        self.dropdown_without_input(self.region_dispatch_lkz, "Удмуртская республика")
        time.sleep(2)
        self.verify_text_on_page(text="11.06.2025 - 100")
        self.click_on_the_cross(self.del_region_dispatch)
        self.dropdown_without_input(self.city_dispatch, "Ижевск")
        time.sleep(2)
        self.verify_text_on_page(text="11.06.2025 - 100")
        self.click_on_the_cross(self.del_city_dispatch)
        self.refresh_page()
        time.sleep(2)
        self.click_on_the_cross(self.del_city_dispatch)
        self.dropdown_without_input(self.region_delivery_lkz, "Мурманская область")
        time.sleep(2)
        self.verify_text_on_page(text="khgjhf")
        self.click_on_the_cross(self.del_region_delivery)
        self.dropdown_without_input(self.city_delivery, "Ижевск")
        time.sleep(2)
        self.verify_text_on_page(text="11.06.2025 - 100")
        self.click_on_the_cross(self.del_city_delivery)
        time.sleep(2)

    def filters_region_gm(self) -> NoReturn:
        self.dropdown_without_input(self.region_dispatch, "Удмуртская республика")
        time.sleep(2)
        self.verify_text_on_page(text="2448445650000")
        self.click_on_the_cross(self.del_region_dispatch_gm)
        self.refresh_page()
        time.sleep(2)
        self.click_on_the_cross(self.del_region_dispatch_gm)
        self.dropdown_without_input(self.region_delivery, 'Тверская область')
        time.sleep(2)
        self.verify_text_on_page(text="2448000046449")
        self.click_on_the_cross(self.del_region_delivery)
        time.sleep(2)

    def filter_departures_address(self) -> NoReturn:
        self.input_in_field(self.departure_address, "Владимир")
        time.sleep(2)
        self.verify_text_on_page(text="2448436160000")
        self.backspace_and_input(self.departure_address, "")
        self.input_in_field(self.delivery_address, "Санкт")
        time.sleep(2)
        self.verify_text_on_page(text="2448436050000")
        self.backspace_and_input(self.delivery_address, "")

    def filter_departures_address_lke(self) -> NoReturn:
        self.input_in_field(self.departure_address, "Ижевск")
        time.sleep(2)
        self.verify_text_on_page(text="2448432780000")
        self.backspace_and_input(self.departure_address, "")
        self.input_in_field(self.delivery_address, "Ижевск")
        time.sleep(2)
        self.verify_text_on_page(text="2448432780000")
        self.backspace_and_input(self.delivery_address, "")

    def filter_departure_status(self) -> NoReturn:
        self.click_button(self.status)
        time.sleep(2)
        self.click_button(self.waiting_shipment)
        time.sleep(2)
        self.verify_text_on_page(text="R-25-173-2448-1")

    def filter_departure_status_lke(self) -> NoReturn:
        self.click_button(self.status)
        time.sleep(2)
        self.click_button(self.waiting_shipment)
        time.sleep(2)
        self.verify_text_on_page(text="R-25-47-2447-1")

    def filter_type_gm(self) -> NoReturn:
        self.input_in_field(self.departure_address_gm, "Ижевск", wait='lst')
        self.dropdown_without_input(self.type_gm, "Короб")
        self.verify_text_on_page(text="2448436400000")
        self.dropdown_without_input(self.type_gmv2, "Палета")
        self.verify_text_on_page(text="2448445650000")
        self.dropdown_without_input(self.type_gmv2, "Мешок")
        self.verify_text_on_page(text="2448445440000")
        self.backspace_and_input(self.departure_address_gm, "")
        self.click_on_the_cross(self.click_cross_type_gm)

    # def filter_required_date(self) -> NoReturn:
    #     self
