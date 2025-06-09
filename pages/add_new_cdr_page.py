import random
import time
from datetime import datetime
from typing import NoReturn

from selenium.webdriver import ActionChains, Keys

from base.base_class import Base
from pages.generator.flight_generator import fake


class AddCdr(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    start_at_from_button = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(),'Дата и время начала от')]",
        "name": "start_at_from_button"
    }
    start_at_till_button = {
        "xpath": "(//input[@class='ant-calendar-picker-input ant-input'])[2]",
        "name": "start_at_til_button"
    }
    start_at_from_input = {
        "xpath": "//input[@class='ant-calendar-input ']",
        "name": "start_at_from_input"
    }
    calendar_ok_button = {
        "xpath": "//a[@class='ant-calendar-ok-btn']",
        "name": "calendar_ok_button"
    }
    today_button = {
        "xpath": "//a[@class='ant-calendar-today-btn ']",
        "name": "today_button"
    }
    today_till_button = {
        "xpath": "//span[@class='ant-calendar-footer-btn']//a[1]",
        "name": "today_till_button"
    }
    sidebar_new_request = {
        "xpath": "//div[@class='ant-menu-submenu-title']",
        "name": "sidebar_new_request"
    }
    sidebar_add_new_request = {
        "xpath": "(//li[contains(@class,'ant-menu-item sidebar__dropdown-item')])[5]",
        "name": "sidebar_add_new_request"
    }
    change_ftl = {
        "xpath": "//div[@role='combobox']",
        "name": "change_ftl"
    }
    change_start_time = {
        "xpath": "//input[@class='ant-calendar-picker-input ant-input']",
        "name": "change_start_time"
    }
    input_start_time = {
        "xpath": "(//input[@placeholder='Выберите дату и время'])[2]",
        "name": "input_start_time"
    }
    change_cdr_id = {
        "xpath": "//span[text()='Внешний идентификатор заявки']/following::input",
        "name": "change_cdr_id",
        "reference": "Внутренний идентификатор заявки"
    }
    input_start_time_ok = {
        "xpath": "//a[@class='ant-calendar-time-picker-btn']/following-sibling::a[1]",
        "name": "input_start_time_ok"
    }
    type_of_road_transport = {
        "xpath": "//span[@class='ant-select-selection ant-select-selection--single']",
        "name": "type_of_road_transport"
    }
    type_cargo = {
        "xpath": "//span[@class='ant-select-tree-title']",
        "name": "type_cargo"
    }
    type_transport = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[3]",
        "name": "type_transport"
    }
    change_body_type = {
        "xpath": "//span[@class='ant-select-search__field__placeholder']",
        "name": "change_body_type"
    }
    change_closed_body_type = {
        "xpath": "(//span[@class='ant-select-tree-title'])[4]",
        "name": "change_closed_body_type"
    }
    first_address_select = {
        "xpath": "(//a[@class='address-component-item__icon'])[2]",
        "name": "first_address_select"
    }
    second_address_select = {
        "xpath": "(//a[@class='address-component-item__icon'])[5]",
        "name": "second_address_select"
    }
    address_radio_button = {
        "xpath": "//span[@class='ant-radio']",
        "name": "address_radio_button"
    }
    address_filter = {
        "xpath": "(//input[@class='ant-input'])[3]",
        "name": "address_filter"
    }
    address_filter_ltl = {
        "xpath": "(//input[@class='ant-input'])[2]",
        "name": "address_filter_ltl"
    }
    confirm_address_button = {
        "xpath": "//button[contains(@class,'ant-btn margin-left-5')]",
        "name": "confirm_address_button"
    }
    point_change_type = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[4]",
        "name": "point_change_type"
    }
    add_cargo_place_button = {
        "xpath": "//button[contains(@class,'ant-btn order-assignments__add')]",
        "name": "add_cargo_place_button"
    }
    add_cargo_place_new_button = {
        "xpath": "//button[contains(@class,'ant-btn margin-left-5')]",
        "name": "add_cargo_place_new_button"
    }
    cost_cargo_place = {
        "xpath": "//input[@class='ant-input-number-input']",
        "name": "cost_cargo_place"
    }
    packaging_type = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[8]",
        "name": "packaging_type"
    }
    packaging_type_ltl = {
        "xpath": "//table[@class='ant-table-fixed']/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]",
        "name": "packaging_type_ltl"
    }
    weight_cargo_place = {
        "xpath": "(//input[@class='ant-input-number-input'])[2]",
        "name": "weight_cargo_place"
    }
    volume_cargo_place = {
        "xpath": "(//input[@class='ant-input-number-input'])[3]",
        "name": "volume_cargo_place"
    }
    name_cargo_place = {
        "xpath": "(//input[@class='ant-input'])[2]",
        "name": "name_cargo_place"
    }
    name_cargo_place_ltl = {
        "xpath": "(//div[@class='order-create-cargo__item ']//input)[4]",
        "name": "name_cargo_place_ltl"
    }
    price_cargo_place = {
        "xpath": "(//input[@class='ant-input-number-input'])[4]",
        "name": "price_cargo_place"
    }
    first_address_cargo_place = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[9]",
        "name": "first_address_cargo_place"
    }
    first_address_cargo_place_ltl = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[5]",
        "name": "first_address_cargo_place_ltl"
    }
    second_address_cargo_place = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[10]",
        "name": "second_address_cargo_place"
    }
    second_address_cargo_place_ltl = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[6]",
        "name": "second_address_cargo_place_ltl"
    }
    attach_cargo_place_button = {
        "xpath": "//button[contains(@class,'ant-btn margin-left-15')]",
        "name": "attach_cargo_place_button"
    }
    required_documents_list = {
        "xpath": "(//span[@class='ant-select-search__field__placeholder'])[2]",
        "name": "required_documents_list"
    }
    documents_for_city_button = {
        "xpath": "//span[@title='Город']",
        "name": "documents_for_city_button"
    }
    save_and_publish_button = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[2]",
        "name": "save_and_publish_button"
    }
    change_one_time_tariff = {
        "xpath": "//span[text()='Разовый тариф (ставка)']",
        "name": "change_one_time_tariff"
    }
    change_publication_rate = {
        "xpath": "//div[@class='ant-input-number-input-wrap']//input[1]",
        "name": "change_publication_rate"
    }
    change_publication_rate_asr = {
        "xpath": "(//div[@class='ant-input-number-input-wrap']//input)[5]",
        "name": "change_publication_rate_asr"
    }
    select_contractors = {
        "xpath": "(//div[@class='ant-select-selection__placeholder'])[5]",
        "name": "select_contractors"
    }
    select_contractors_asr_lkz_lkp = {
        "xpath": "(//div[@class='ant-select-selection__placeholder'])[4]",
        "name": "select_contractors_asr_lkz_lke"
    }
    select_contractors_asr_lkz_lke = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[7]",
        "name": "select_contractors_asr_lkz_lke"
    }
    select_contractors_ltl = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[4]",
        "name": "select_contractors_ltl"
    }
    publish_button = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[3]",
        "name": "publish_button"
    }
    publish_ok_button = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[4]",
        "name": "publish_ok_button"
    }
    additional_requirements_button = {
        "xpath": "//div[@class='ant-collapse-item']//div[1]",
        "name": "additional_requirements_button"
    }
    sanitization_flag_on = {
        "xpath": "//div[@class='vz-form-field-switch vz-form-field-switch__size-default']",
        "name": "sanitization_flag_on"
    }
    medical_book_flag_on = {
        "xpath": "//div[@id='order-advancedrequirements']/div[2]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]",
        "name": "medical_book_flag_on"
    }
    tail_lift_flag_on = {
        "xpath": "//div[@id='order-advancedrequirements']/div[2]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]",
        "name": "tail_lift_flag_on"
    }
    rokhla_flag_on = {
        "xpath": "//div[@id='order-advancedrequirements']/div[2]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]",
        "name": "rokhla_flag_on"
    }
    horsemen_flag_on = {
        "xpath": "//div[@id='order-advancedrequirements']/div[2]/div[1]/div[5]/label[1]/div[1]/div[1]/div[1]",
        "name": "horsemen_flag_on"
    }
    gps_flag_on = {
        "xpath": "//div[@id='order-advancedrequirements']/div[2]/div[1]/div[6]/label[1]/div[1]/div[1]/div[1]",
        "name": "gps_flag_on"
    }
    belts_flag_on = {
        "xpath": "//div[@id='order-advancedrequirements']/div[2]/div[1]/div[7]/label[1]/div[1]/div[1]/div[1]",
        "name": "belts_flag_on"
    }
    chain_flag_on = {
        "xpath": "//div[@id='order-advancedrequirements']/div[2]/div[1]/div[8]/label[1]/div[1]/div[1]/div[1]",
        "name": "chain_flag_on"
    }
    tarpaulin_flag_on = {
        "xpath": "//div[@id='order-advancedrequirements']/div[2]/div[1]/div[9]/label[1]/div[1]/div[1]/div[1]",
        "name": "tarpaulin_flag_on"
    }
    nets_flag_on = {
        "xpath": "//div[@id='order-advancedrequirements']/div[2]/div[1]/div[10]/label[1]/div[1]/div[1]/div[1]",
        "name": "nets_flag_on"
    }
    shoes_flag_on = {
        "xpath": "//div[@id='order-advancedrequirements']/div[2]/div[1]/div[11]/label[1]/div[1]/div[1]/div[1]",
        "name": "shoes_flag_on"
    }
    corner_posts_flag_on = {
        "xpath": "//div[@id='order-advancedrequirements']/div[2]/div[1]/div[12]/label[1]/div[1]/div[1]/div[1]",
        "name": "corner_posts_flag_on"
    }
    doppelstock_flag_on = {
        "xpath": "//div[@id='order-advancedrequirements']/div[2]/div[1]/div[13]/label[1]/div[1]/div[1]/div[1]",
        "name": "doppelstock_flag_on"
    }
    wooden_floor_flag_on = {
        "xpath": "//div[@id='order-advancedrequirements']/div[2]/div[1]/div[14]/label[1]/div[1]/div[1]/div[1]",
        "name": "wooden_floor_flag_on"
    }
    removal_packaging_flag_on = {
        "xpath": "//div[@id='order-advancedrequirements']/div[2]/div[1]/div[15]/label[1]/div[1]/div[1]/div[1]",
        "name": "removal_packaging_flag_on"
    }
    additional_service_button = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[6]",
        "name": "additional_service_button"
    }
    additional_service_time = {
        "xpath": "(//input[@class='ant-calendar-picker-input ant-input'])[4]",
        "name": "additional_service_time"
    }
    change_volume_prr = {
        "xpath": "//input[@class='ant-input-number-input']",
        "name": "change_volume_prr"
    }
    change_weight_prr = {
        "xpath": "(//input[@class='ant-input-number-input'])[2]",
        "name": "change_weight_prr"
    }
    first_address_select_prr = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[6]",
        "name": "first_address_select_prr"
    }

    change_specialization_prr = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[7]",
        "name": "change_specialization_prr"
    }
    change_quantity_specialization_prr = {
        "xpath": "(//input[@class='ant-input-number-input'])[3]",
        "name": "change_quantity_specialization_prr"
    }
    add_insurance = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[9]",
        "name": "add_insurance"
    }
    change_value_insurance = {
        "xpath": "(//input[@class='ant-input-number-input'])[4]",
        "name": "change_value_insurance"
    }
    change_category_insurance = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[9]",
        "name": "change_category_insurance"
    }
    input_id_cdr = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[9]",
        "name": "change_category_insurance"
    }
    click_reset = {
        "xpath": "//div[@class='filter-item filter-item--button']//button",
        "name": "click_reset"
    }
    click_first_element = {
        "xpath": "//a[@class='link-back']",
        "name": "click_first_element"
    }
    click_confirm_cdr = {
        "xpath": "//button[contains(@class,'ant-btn take-button')]",
        "name": "click_confirm_cdr"
    }
    click_options = {
        "xpath": "//img[@class='element-icon icon-small']",
        "name": "click_options"
    }
    click_change_transport = {
        "xpath": "//ul[contains(@class,'dropdown-list right')]//li[1]",
        "name": "click_change_transport"
    }
    input_ts_and_driver = {
        "xpath": "//input[@placeholder='Поиск по номеру ТС / фамилии водителя']",
        "name": "input_ts_and_driver"
    }
    appoint_ts_and_driver = {
        "xpath": "(//button[@type='button']//img)[4]",
        "name": "change_ts_and_driver"
    }
    filter_input_field_id = {
        "xpath": "//input[@placeholder='Идентификатор клиента']",
        "name": "filter_input_field_id"
    }
    click_execution_menu = {
        "xpath": "(//a[@class='vz-tabs-modern__item'])[4]",
        "name": "click_execution_menu"
    }
    start_execution = {
        "xpath": "(//button[@type='button'])[4]",
        "name": "start_execution"
    }
    start_execution_ok = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "start_execution"
    }
    time_address_1 = {
        "xpath": "//input[@class='ant-calendar-picker-input ant-input']",
        "name": "time_address_1"
    }
    time_address_2 = {
        "xpath": "(//input[@class='ant-calendar-picker-input ant-input'])[2]",
        "name": "time_address_2"
    }
    time_address_3 = {
        "xpath": "(//input[@class='ant-calendar-picker-input ant-input'])[3]",
        "name": "time_address_3"
    }
    time_address_4 = {
        "xpath": "(//input[@class='ant-calendar-picker-input ant-input'])[4]",
        "name": "time_address_4"
    }
    click_complete = {
        "xpath": "(//button[@type='button'])[4]",
        "name": "click_complete"
    }
    push_ok = {
        "xpath": "(// button[@ type='button'])[6]",
        "name": "push_ok"
    }
    processing_application_services = {
        "xpath": "(//li[contains(@class,'pointer ')])[8]",
        "name": "processing_application_services"
    }
    choose_main_service = {
        "xpath": "//input[@class='ant-checkbox-input']",
        "name": "choose_main_service"
    }
    hand_over_contractor = {
        "xpath": "(//button[@class='ant-btn'])[2]",
        "name": "hand_over_contractor"
    }
    create_and_publish_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']/following-sibling::button[1]",
        "name": "create_and_publish_button"
    }
    select_contractors_lkp = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[8]",
        "name": "select_contractors_lkp"
    }
    publish_button_lke = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[2]",
        "name": "publish_button"
    }
    change_body_type_close = {
        "xpath": "//ul[@class='ant-select-selection__rendered']",
        "name": "change_body_type_close"
    }

    def change_date_time(self) -> NoReturn:
        """
        Изменение даты и времени начала подачи.
        """
        # Генерация нового времени с заданным сдвигом (30 минут)
        new_time = self.naw_time_change(30)
        # Клик по кнопке выбора даты и времени начала подачи
        self.click_button(self.start_at_from_button)
        # Выбор сегодняшней даты из календаря
        self.click_button(self.today_button)
        # Повторный клик по кнопке выбора даты и времени для активации поля ввода
        self.click_button(self.start_at_from_button)
        # Ввод новой временной метки в поле ввода, предварительно очистив старое значение
        self.backspace_and_input(self.start_at_from_input, num=5, value=new_time)
        # Подтверждение выбора даты и времени нажатием кнопки "OK"
        self.click_button(self.calendar_ok_button)

    def input_unique_id(self) -> str:
        """
        Генерация и ввод уникального ID для записи.
        """
        # Создание уникального ID в формате FTL-DD.MM.YYYY-XXXX, где XXXX — случайное число
        unique_id = f"FTL-{datetime.now().strftime('%d.%m.%Y')}-{random.randint(1000, 9999)}"
        # Ввод сгенерированного уникального ID в соответствующее поле
        self.input_in_field(self.change_cdr_id, unique_id)
        return unique_id

    def change_address(self) -> NoReturn:
        """
        Изменение адресов отправления и назначения.
        """
        # Выбор первого адреса из списка доступных адресов
        self.click_button(self.first_address_select)
        time.sleep(2)
        # Фильтрация адресов по заданному значению и выбор первого подходящего адреса
        self.input_in_field(self.address_filter, "Свердловская обл, г Верхняя Пышма, Успенский пр-кт, д 103а")
        time.sleep(3)  # Ожидание завершения фильтрации
        self.click_button(self.address_radio_button)
        time.sleep(2)
        # Подтверждение выбора первого адреса
        self.click_button(self.confirm_address_button)
        time.sleep(3)  # Ожидание перед продолжением выполнения
        # Выбор второго адреса из списка доступных адресов
        self.click_button(self.second_address_select)
        # Фильтрация адресов по заданному значению и выбор второго подходящего адреса
        self.input_in_field(self.address_filter, "Свердловская обл, г Березовский, ул Театральная, д 13")
        time.sleep(3)  # Ожидание завершения фильтрации
        self.click_button(self.address_radio_button)
        # Подтверждение выбора второго адреса
        self.click_button(self.confirm_address_button)

    def random_point_change_type(self) -> NoReturn:
        """
        Случайный выбор типа изменения маршрута.
        """
        # Возможные варианты изменения маршрута
        options = [
            "Нельзя изменять очередность адресов в маршруте и/или пропускать их.",
            "Можно изменять очередность и/или пропускать любые адреса в маршруте, кроме адреса подачи.",
            "Можно изменять очередность и пропускать только промежуточные адреса в маршруте."
        ]
        # Выбор случайного варианта из списка
        selected_option = random.choice(options)
        # Применение выбранного варианта через выпадающий список
        self.dropdown_without_input(self.point_change_type, selected_option)

    def new_cargo_place(self) -> NoReturn:
        """
        Добавление нового ГМ с заполнением всех необходимых полей.
        """
        # Нажатие на кнопку добавления нового места груза
        self.click_button(self.add_cargo_place_button)
        self.click_button(self.add_cargo_place_new_button)
        # Заполнение полей для нового места груза
        self.input_in_field(self.cost_cargo_place, str(random.randint(1, 10)))  # Стоимость
        self.dropdown_without_input(self.packaging_type, "Палета")  # Тип упаковки
        self.input_in_field(self.weight_cargo_place, str(random.randint(500, 1500)))  # Вес
        self.input_in_field(self.volume_cargo_place, str(random.randint(1, 6)))  # Объем
        self.input_in_field(self.name_cargo_place, fake.word() + " с продуктами")  # Наименование
        self.input_in_field(self.price_cargo_place, str(random.randint(10000, 100000)))  # Цена
        # Выбор адресов для первого и второго пунктов доставки
        self.dropdown_without_input(self.first_address_cargo_place,
                                    "Свердловская обл, г Верхняя Пышма, Успенский пр-кт, д 103а")
        self.dropdown_without_input(self.second_address_cargo_place,
                                    "Свердловская обл, г Березовский, ул Театральная, д 13")
        # Подтверждение добавления места груза
        self.click_button(self.attach_cargo_place_button)

    def required_documents(self) -> NoReturn:
        """
        Выбор необходимых документов для перевозки.
        """
        # Открытие списка необходимых документов
        self.click_button(self.required_documents_list)
        # Выбор документов для города
        self.click_button(self.documents_for_city_button)

    def save_and_publish_lkp(self) -> NoReturn:
        """
        Сохранение и публикация заказа.
        """
        # Нажатие на кнопку сохранения и публикации
        self.click_button(self.save_and_publish_button)
        time.sleep(2)
        # Изменение тарифа за один раз
        self.click_button(self.change_one_time_tariff)
        time.sleep(2)
        # Установка случайной ставки публикации
        self.dropdown_with_input(self.change_publication_rate, str(random.randint(100000, 800000)))
        time.sleep(2)
        # Выбор подрядчиков через выпадающий список
        self.dropdown_without_input(self.select_contractors, "Auto LKP")
        ActionChains(self.driver).send_keys(Keys.TAB).perform()
        # Подтверждение публикации заказа
        self.click_button(self.publish_button)
        self.click_button(self.publish_ok_button)

    def save_and_publish_lke(self) -> NoReturn:
        """
        Сохранение и публикация заказа.
        """
        # Нажатие на кнопку сохранения и публикации
        self.click_button(self.save_and_publish_button)
        time.sleep(2)
        # Изменение тарифа за один раз
        self.click_button(self.change_one_time_tariff)
        time.sleep(2)
        # Установка случайной ставки публикации
        self.dropdown_with_input(self.change_publication_rate, str(random.randint(100000, 800000)))
        time.sleep(2)
        # Выбор подрядчиков через выпадающий список
        self.dropdown_without_input(self.select_contractors, "Auto LKE")
        ActionChains(self.driver).send_keys(Keys.TAB).perform()
        # Подтверждение публикации заказа
        self.click_button(self.publish_button)
        self.click_button(self.publish_ok_button)

    def save_and_publish_asr(self) -> NoReturn:
        """
        Сохранение и публикация заказа.
        """
        # Нажатие на кнопку сохранения и публикации
        self.click_button(self.save_and_publish_button)
        time.sleep(2)
        # Изменение тарифа за один раз
        self.click_button(self.change_one_time_tariff)
        time.sleep(2)
        # Установка случайной ставки публикации
        self.dropdown_with_input(self.change_publication_rate_asr, str(random.randint(100000, 800000)))
        time.sleep(2)
        # Выбор подрядчиков через выпадающий список
        self.dropdown_without_input(self.select_contractors_asr_lkz_lkp, "Auto LKP")
        ActionChains(self.driver).send_keys(Keys.TAB).perform()
        # Подтверждение публикации заказа
        self.click_button(self.publish_button)
        self.click_button(self.publish_ok_button)

    def save_and_publish_dop(self) -> NoReturn:
        """
        Сохранение и публикация заказа.
        """
        # Нажатие на кнопку сохранения и публикации
        self.click_button(self.save_and_publish_button)
        time.sleep(2)
        # Изменение тарифа за один раз
        self.click_button(self.change_one_time_tariff)
        time.sleep(2)
        # Установка случайной ставки публикации
        self.dropdown_with_input(self.change_publication_rate_asr, str(random.randint(100000, 800000)))
        time.sleep(2)
        # Выбор подрядчиков через выпадающий список
        self.dropdown_without_input(self.select_contractors_asr_lkz_lkp, "Auto LKP")
        ActionChains(self.driver).send_keys(Keys.TAB).perform()
        # Подтверждение публикации заказа
        self.click_button(self.publish_button)
        self.click_button(self.publish_ok_button)

    def change_date_second_time(self) -> NoReturn:
        """
        Изменение даты и времени второй раз с большим сдвигом (150 минут).
        """
        # Генерация нового времени с заданным сдвигом (150 минут)
        new_time = self.naw_time_change(150)
        # Клик по кнопке выбора даты и времени начала подачи
        self.click_button(self.start_at_till_button)
        # Выбор сегодняшней даты из календаря
        self.click_button(self.today_till_button)
        # Повторный клик по кнопке выбора даты и времени для активации поля ввода
        self.click_button(self.start_at_till_button)
        # Ввод новой временной метки в поле ввода, предварительно очистив старое значение
        self.backspace_and_input(self.start_at_from_input, num=5, value=new_time)
        # Подтверждение выбора даты и времени нажатием кнопки "OK"
        self.click_button(self.calendar_ok_button)

    def new_cargo_place_ltl(self) -> NoReturn:
        """
        Добавление нового ГМ для LTL-перевозок.
        """
        # Нажатие на кнопку добавления нового места груза
        self.click_button(self.add_cargo_place_button)
        self.click_button(self.add_cargo_place_new_button)
        # Заполнение полей для нового места груза
        self.input_in_field(self.cost_cargo_place, str(random.randint(1, 10)))  # Стоимость
        self.dropdown_without_input(self.packaging_type_ltl, "Палета")  # Тип упаковки
        self.input_in_field(self.weight_cargo_place, str(random.randint(500, 1500)))  # Вес
        self.input_in_field(self.volume_cargo_place, str(random.randint(1, 6)))  # Объем
        self.input_in_field(self.name_cargo_place_ltl, fake.word() + " с продуктами")  # Наименование
        self.input_in_field(self.price_cargo_place, str(random.randint(10000, 100000)))  # Цена
        # Выбор адресов для первого и второго пунктов доставки
        self.dropdown_without_input(self.first_address_cargo_place_ltl,
                                    "Свердловская обл, г Верхняя Пышма, Успенский пр-кт, д 103а")
        self.dropdown_without_input(self.second_address_cargo_place_ltl,
                                    "Свердловская обл, г Березовский, ул Театральная, д 13")
        # Подтверждение добавления места груза
        self.click_button(self.attach_cargo_place_button)

    def save_and_publish_ltl(self) -> NoReturn:
        """
        Сохранение и публикация заказа для LTL-перевозок.
        """
        # Нажатие на кнопку сохранения и публикации
        self.click_button(self.save_and_publish_button)
        time.sleep(2)
        # Выбор тарифа "Разовая ставка"
        self.click_button(self.change_one_time_tariff)
        time.sleep(2)
        # Установка случайной ставки публикации
        self.dropdown_with_input(self.change_publication_rate, str(random.randint(100000, 800000)))
        # Выбор подрядчиков через выпадающий список
        self.dropdown_without_input(self.select_contractors_ltl, "Auto LKP")
        ActionChains(self.driver).send_keys(Keys.TAB).perform()
        self.dropdown_without_input(self.select_contractors_ltl, "Auto LKE")
        ActionChains(self.driver).send_keys(Keys.TAB).perform()
        # Подтверждение публикации заказа
        self.click_button(self.publish_button)
        time.sleep(1)
        self.click_button(self.publish_ok_button)

    def add_additional_requirements(self) -> NoReturn:
        """
        Метод для добавления дополнительных требований к заказу.
        Последовательно кликает по кнопкам и флагам, активируя соответствующие опции.
        """
        # Клик по кнопке "Дополнительные требования" (открывает раздел с флагами)
        self.click_button(self.additional_requirements_button)
        # Активация флага "Санитарная обработка"
        self.click_button(self.sanitization_flag_on)
        # Активация флага "Медицинская книжка"
        self.click_button(self.medical_book_flag_on)
        # Активация флага "Гидроборт"
        self.click_button(self.tail_lift_flag_on)
        # Активация флага "Рохля" (грузовая тележка)
        self.click_button(self.rokhla_flag_on)
        # Активация флага "Конники" (крепления для груза)
        self.click_button(self.horsemen_flag_on)
        # Активация флага "GPS-трекер"
        self.click_button(self.gps_flag_on)
        # Активация флага "Ремни крепления"
        self.click_button(self.belts_flag_on)
        # Активация флага "Цепи крепления"
        self.click_button(self.chain_flag_on)
        # Активация флага "Тент"
        self.click_button(self.tarpaulin_flag_on)
        # Активация флага "Сетки крепления"
        self.click_button(self.nets_flag_on)
        # Активация флага "Башмаки"
        self.click_button(self.shoes_flag_on)
        # Активация флага "Угловые стойки"
        self.click_button(self.corner_posts_flag_on)
        # Активация флага "Двухъярусная загрузка"
        self.click_button(self.doppelstock_flag_on)
        # Активация флага "Деревянный пол"
        self.click_button(self.wooden_floor_flag_on)
        # Активация флага "Утилизация упаковки"
        self.click_button(self.removal_packaging_flag_on)

    def additional_service_add_prr(self) -> NoReturn:
        self.dropdown_without_input(self.additional_service_button, "ПРР")
        self.scroll_to_element(self.save_and_publish_button)
        new_time = self.naw_time_change(50)
        # Клик по кнопке выбора даты и времени начала подачи
        self.click_button(self.additional_service_time)
        # Выбор сегодняшней даты из календаря
        self.click_button(self.today_button)
        # Повторный клик по кнопке выбора даты и времени для активации поля ввода
        self.click_button(self.additional_service_time)
        # Ввод новой временной метки в поле ввода, предварительно очистив старое значение
        self.backspace_and_input(self.start_at_from_input, num=5, value=new_time)
        # Подтверждение выбора даты и времени нажатием кнопки "OK"
        self.click_button(self.calendar_ok_button)
        self.input_in_field(self.change_volume_prr, str(random.randint(1, 6)))
        self.input_in_field(self.change_weight_prr, str(random.randint(500, 1500)))
        # Выбор первого адреса из списка доступных адресов
        self.click_and_select_with_arrows(self.first_address_select_prr, 1)
        ActionChains(self.driver).send_keys(Keys.TAB).perform()
        self.dropdown_without_input(self.change_specialization_prr, "Грузчик")
        self.input_in_field(self.change_quantity_specialization_prr, "1")
        time.sleep(2)

    def additional_service_add_insurance(self) -> NoReturn:
        # Выбираем "Страхование" из выпадающего списка
        self.dropdown_without_input(self.add_insurance, "Страхование")
        # Генерируем случайную сумму страхования и вводим её в поле
        self.input_in_field(self.change_value_insurance, str(random.randint(10000, 100000)))
        # Выбираем категорию страхования "Алкогольные напитки"
        self.dropdown_without_input(self.change_category_insurance, "Алкогольные напитки")

    def change_ts_and_driver(self) -> NoReturn:
        # Нажимаем на кнопку "Опции"
        self.click_button(self.click_options)
        time.sleep(2)
        # Нажимаем на кнопку "Изменить транспортное средство"
        self.click_button(self.click_change_transport)
        time.sleep(2)
        # Вводим название ТС и водителя ("Робаут") в поле
        self.input_in_field(self.input_ts_and_driver, "Робаут")
        time.sleep(2)
        # Нажимаем на кнопку "Назначить ТС и водителя"
        self.click_button(self.appoint_ts_and_driver)
        time.sleep(2)

    def change_request_for_id(self, request) -> NoReturn:
        # Извлекаем уникальный ID из кэша
        unique_id = request.config.cache.get("unique_id", None)
        # Вводим уникальный ID в поле фильтра
        self.input_in_field(self.filter_input_field_id, unique_id)
        time.sleep(2)
        # Нажимаем на первый элемент в списке (или на элемент с уникальным ID)
        self.click_button(self.click_first_element)

    def start_cdr(self) -> NoReturn:
        # Нажимаем на меню "Исполнение"
        self.click_button(self.click_execution_menu)
        # Нажимаем на кнопку "Начать исполнение"
        self.click_button(self.start_execution)
        # Нажимаем "ОК" подтверждаем начало исполнения
        self.click_button(self.start_execution_ok)

    def change_time_to_address(self) -> NoReturn:
        self.click_button(self.time_address_1)
        self.click_button(self.today_button)
        time.sleep(1)
        self.click_button(self.time_address_2)
        self.click_button(self.today_button)
        time.sleep(1)
        self.click_button(self.time_address_3)
        self.click_button(self.today_button)
        time.sleep(1)
        self.click_button(self.time_address_4)
        self.click_button(self.today_button)
        time.sleep(1)

    def complete_cdr(self) -> NoReturn:
        # Нажимаем на кнопку "Завершить"
        self.click_button(self.click_complete)
        time.sleep(2)
        # Подтверждаем завершение, нажимая "OK"
        self.click_button(self.push_ok)

    def republish_cdr_lke_lkp(self) -> NoReturn:
        # Нажимаем на кнопку "Опции"
        self.click_button(self.click_options)
        self.click_button(self.processing_application_services)
        time.sleep(2)
        self.click_on_the_cross(self.choose_main_service)
        self.click_button(self.hand_over_contractor)
        time.sleep(2)
        self.change_date_time()
        self.scroll_to_element(self.create_and_publish_button)
        time.sleep(2)
        self.click_button(self.create_and_publish_button)
        # Выбор тарифа "Разовая ставка"
        self.click_button(self.change_one_time_tariff)
        time.sleep(2)
        # Установка случайной ставки публикации
        self.dropdown_with_input(self.change_publication_rate, str(random.randint(100000, 800000)))
        # Выбор подрядчиков через выпадающий список
        self.dropdown_without_input(self.select_contractors_lkp, "Auto LKP")
        ActionChains(self.driver).send_keys(Keys.TAB).perform()
        # Подтверждение публикации заказа
        self.click_button(self.publish_button_lke)
        time.sleep(1)
        self.click_button(self.publish_ok_button)

    # def clear_cache(self, request) -> NoReturn:
    #    """
    #    Очищает все данные из кэша.
    #    """
    #    # Удаляем все ключи из кэша
    #    request.config.cache.clear()
    #    print("Кэш успешно очищен.")

    def change_address_ltl(self) -> NoReturn:
        """
        Изменение адресов отправления и назначения.
        """
        # Выбор первого адреса из списка доступных адресов
        self.click_button(self.first_address_select)
        time.sleep(2)
        # Фильтрация адресов по заданному значению и выбор первого подходящего адреса
        self.input_in_field(self.address_filter_ltl, "Свердловская обл, г Верхняя Пышма, Успенский пр-кт, д 103а")
        time.sleep(3)  # Ожидание завершения фильтрации
        self.click_button(self.address_radio_button)
        time.sleep(2)
        # Подтверждение выбора первого адреса
        self.click_button(self.confirm_address_button)
        time.sleep(3)  # Ожидание перед продолжением выполнения
        # Выбор второго адреса из списка доступных адресов
        self.click_button(self.second_address_select)
        # Фильтрация адресов по заданному значению и выбор второго подходящего адреса
        self.input_in_field(self.address_filter_ltl, "Свердловская обл, г Березовский, ул Театральная, д 13")
        time.sleep(3)  # Ожидание завершения фильтрации
        self.click_button(self.address_radio_button)
        # Подтверждение выбора второго адреса
        self.click_button(self.confirm_address_button)
