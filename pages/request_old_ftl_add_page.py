from base.base_class import Base
import random
from datetime import datetime, timedelta
from typing import Tuple


class FTLAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    """Request owner drop-down list"""
    request_owner_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(),'Грузовладелец')]",
        "name": "request_owner_select"
    }
    select_own_request = {
        "xpath": "//ul[@role='listbox']/li[text()='Собственный Заказ']",
        "name": "select_own_request"
    }
    start_date_field = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(),'Дата подачи')]",
        "name": "start_date_field"
    }
    start_time_field = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(),'Время подачи')]",
        "name": "start_time_field"
    }
    start_time_input = {
        "xpath": "//input[@class='ant-time-picker-panel-input']",
        "name": "start_time_input"
    }
    today_button = {
        "xpath": "//a[@class='ant-calendar-today-btn ']",
        "name": "today_button"
    }
    """Request category drop-down list"""
    request_category_select = {
        "xpath": "//span[@class='ant-select-selection__rendered']",
        "name": "request_category_select"
    }
    select_freight = {
        "xpath": "//span[contains(text(), 'Грузовая')]",
        "name": "select_freight"
    }
    """TS type drop-down list"""
    vehicle_type_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(), 'Тип ТС')]",
        "name": "vehicle_type_select"
    }
    """TS body drop-down list"""
    vehicle_body_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(),'Тип кузова')]",
        "name": "vehicle_body_select"
    }
    body_type_closed_checkbox = {
        "xpath": "//span[@class='ant-select-tree-title' and contains(text(), 'Закрытый')]",
        "name": "body_type_closed_checkbox"
    }
    """First address drop-down list"""
    first_address_select = {
        "xpath": "//*[@id='order-address-0']",
        "name": "first_address_select"
    }
    select_first_radio = {
        "xpath": "//span[@class='ant-radio']",
        "name": "select_first_radio"
    }
    """Second address drop-down list"""
    second_address_select = {
        "xpath": "//*[@id='order-address-1']",
        "name": "second_address_select"
    }
    select_second_radio = {
        "xpath": "(//span[@class='ant-radio'])[2]",
        "name": "select_first_radio"
    }

    third_address_select = {
        "xpath": "//a[@id='order-address-1']//span[@class='vz-address-modern-favorite__icon']",
        "name": "third_address_select"
    }
    fourth_address_select = {
        "xpath": "//a[@id='order-address-2']//span[@class='vz-address-modern-favorite__icon']",
        "name": "fourth_address_select"
    }


    address_filter = {
        "xpath": "//input[@placeholder='Введите Адрес']",
        "name": "address_filter"
    }
    confirm_address_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary' and span[contains(text(), 'Применить выбранный')]]",
        "name": "confirm_address_button"
    }
    calculate_loading = {
        "xpath": "//i[@aria-label='icon: loading']",
        "name": "calculate_loading"
    }
    calculate_finish = {
        "xpath": "//span[@class='cost cost-min']",
        "name": "calculate_finish"
    }
    publication_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary' and span[contains(text(), 'По тарифу')]]",
        "name": "publication_button"
    }
    tariff_button = {
        "xpath": "//button[@data-tariffpublishing='true']",
        "name": "tariff_button"
    }
    rate_button = {
        "xpath": "//input[@value='rate']",
        "name": "rate_button"
    }
    rate_amount = {
        "xpath": "//input[@id='order-clientrate']",
        "name": "rate_amount"
    }
    bargain_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary' and span[contains(text(), 'В торги')]]",
        "name": "bargain_button"
    }
    perevozchik_cross = {
        "xpath": "//li[@title='ООО 'Перевозчик'']//i[@aria-label='icon: close']",
        "name": "perevozchik_cross"
    }
    lkp_cross = {
        "xpath": "//li[@title='Auto LKP']//i[@aria-label='icon: close']//*[name()='svg']",
        "name": "lkp_cross"
    }
    lke_select_checkbox = {
        "xpath": "//span[contains(text(),'Auto LKE')]",
        "name": "lke_select_checkbox"
    }



    """Producer drop-down list"""
    producer_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(), 'Подрядчики')]",
        "name": "producer_select"
    }
    select_all_producer = {
        "xpath": "//span[@class='ant-select-tree-title' and contains(text(), 'Все подрядчики')]",
        "name": "select_all_producer"
    }
    producer_select_text = {
        "xpath": "//h4[@class='vz-form-group__title' and contains(text(), 'Выбор подрядчиков')]",
        "name": "producer_select_text"
    }
    publish_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary' and span[contains(text(), 'Опубликовать')]]",
        "name": "publish_button"
    }
    # continue_button = {
    #     "xpath": "//button[@class='ant-btn ant-btn-primary' and span[contains(text(), 'Продолжить')]]",
    #     "name": "continue_button",
    #     "reference_xpath": "//div[@class='ant-modal-confirm-content' and contains(text(), 'Рейс был успешно создан')]",
    #     "reference": r'Рейс был успешно создан, .*'
    # }
    continue_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary' and span[contains(text(), 'Продолжить')]]",
        "name": "continue_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and contains(text(), 'Рейс был успешно создан')]",
        "reference": "Рейс был успешно создан",
        "match_type": "contains"
    }
    confirm_add_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary' and span[contains(text(), 'OK')]]",
        "name": "confirm_add_button"
    }
    cancel_button = {
        "xpath": "//button[@class='ant-btn ant-btn-ghost' and span[contains(text(), 'Отмена')]]",
        "name": "cancel_button"
    }
    producer_check_box = {
        "xpath": "//span[contains(@class, 'ant-select-tree-title') and contains(text(), 'Контур')]",
        "name": "producer_check_box"
    }


    """Перепубликация"""
    republication_button = {
        "xpath": "//button[@id='order-republish']",
        "name": "republication_button"
    }
    lkp_select_checkbox = {
        "xpath": "//span[contains(text(),'Auto LKP')]",
        "name": "lkp_select_checkbox"
    }
    continue_share_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary' and span[contains(text(), 'Продолжить')]]",
        "name": "continue_share_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content']",
        "reference": "Рейс был расшарен для всех указанных подрядчиков"
    }
    share_ok = {
        "xpath": "//div[@class='ant-modal-confirm-btns']//button[@type='button']",
        "name": "share_ok",
    }

    # Methods
    @staticmethod
    def generate_ide_code() -> str:
        """
        Генерирует идентификатор заявки
        """
        ide_code = f"ide-{random.randint(100000, 999999)}"

        return ide_code

    # @staticmethod
    # def get_time_intervals():
    #     # Получаем текущее время
    #     now = datetime.now()
    #
    #     # Вычисляем временные промежутки
    #     time_one = now - timedelta(hours=4)  # Четыре часа назад
    #     time_two = now - timedelta(hours=3)  # Три часа назад
    #     time_three = now - timedelta(hours=2)  # Два часа назад
    #     time_four = now - timedelta(hours=1)  # Один час назад
    #
    #     # Форматируем время в нужном формате (дд.мм.гггг чч:мм)
    #     time_one_formatted = time_one.strftime('%d.%m.%Y %H:%M')
    #     time_two_formatted = time_two.strftime('%d.%m.%Y %H:%M')
    #     time_three_formatted = time_three.strftime('%d.%m.%Y %H:%M')
    #     time_four_formatted = time_four.strftime('%d.%m.%Y %H:%M')
    #
    #     return time_one_formatted, time_two_formatted, time_three_formatted, time_four_formatted

    @staticmethod
    def get_time_intervals() -> Tuple[str, str, str, str]:
        now = datetime.now()

        time_one = now - timedelta(hours=4)
        time_two = now - timedelta(hours=3)
        time_three = now - timedelta(hours=2)
        time_four = now - timedelta(hours=1)

        # Формат: "ддммгггг ччмм"
        fmt = '%d%m%Y %H%M'

        return (
            time_one.strftime(fmt),
            time_two.strftime(fmt),
            time_three.strftime(fmt),
            time_four.strftime(fmt),
        )

    @staticmethod
    def get_time_intervals_many() -> Tuple[str, str, str, str, str, str, str, str]:
        now = datetime.now()

        time_1 = now - timedelta(hours=8)
        time_2 = now - timedelta(hours=7)
        time_3 = now - timedelta(hours=6)
        time_4 = now - timedelta(hours=5)
        time_5 = now - timedelta(hours=4)
        time_6 = now - timedelta(hours=3)
        time_7 = now - timedelta(hours=2)
        time_8 = now - timedelta(hours=1)

        # Формат: "ддммгггг ччмм"
        fmt = '%d%m%Y %H%M'

        return (
            time_1.strftime(fmt),
            time_2.strftime(fmt),
            time_3.strftime(fmt),
            time_4.strftime(fmt),
            time_5.strftime(fmt),
            time_6.strftime(fmt),
            time_7.strftime(fmt),
            time_8.strftime(fmt),
        )

    # Locators
    attach_cargoplaces = {
        "xpath": "//button[contains(@class,'ant-btn order-cargo-places__add')]",
        "name": "attach_cargoplaces"
    }
    new_cargoplace = {
        "xpath": "//button[contains(@class,'ant-btn margin-left-5')]",
        "name": "new_cargoplace"
    }
    number_of_pieces = {
        "xpath": "//input[@class='ant-input-number-input']",
        "name": "number_of_pieces"
    }
    type_of_packaging = {
        "xpath": "//table[@class='ant-table-fixed']/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]",
        "name": "type_of_packaging"
    }
    weight = {
        "xpath": "(//input[@class='ant-input-number-input'])[2]",
        "name": "weight"
    }
    volume = {
        "xpath": "(//input[@class='ant-input-number-input'])[3]",
        "name": "volume"
    }
    name_of_cargo = {
        "xpath": "//input[@class='ant-input']",
        "name": "name_of_cargo"
    }
    cost = {
        "xpath": "//table[@class='ant-table-fixed']/tbody[1]/tr[1]/td[6]/div[1]/div[1]/div[2]/input[1]",
        "name": "cost"
    }
    loading = {
        "xpath": "//table[@class='ant-table-fixed']/tbody[1]/tr[1]/td[7]/div[1]/div[1]/div[1]",
        "name": "loading"
    }
    unloading = {
        "xpath": "//table[@class='ant-table-fixed']/tbody[1]/tr[1]/td[8]/div[1]/div[1]/div[1]",
        "name": "unloading"
    }
    attach = {
        "xpath": "//button[contains(@class,'ant-btn margin-left-15')]",
        "name": "attach"
    }
    additional_requirements = {
        "xpath": "//div[@class='ant-collapse-header']",
        "name": "additional_requirements"
    }
    order_identifier = {
        "xpath": "//span[text()='Идентификатор рейса']/following::input",
        "name": "order_identifier"
    }
    # custom_fields = {
    #     "xpath": "//div[@id='1-Z25-0039']/div[1]",
    #     "name": "custom_fields"
    # }
    custom_fields = {
        "xpath": "//div[@id='1-oldj']//div[@class='ant-select-selection__rendered']",
        "name": "custom_fields"
    }
    order_insurance = {
        "xpath": "//button[@id='order-insurance']",
        "name": "order_insurance"
    }
    cargo_category = {
        "xpath": "//div[@id='order-cargocategoryids']//div",
        "name": "cargo_category"
    }
    estimated_value = {
        "xpath": "//div[@class='ant-input-number-input-wrap']//input[1]",
        "name": "estimated_value"
    }
    responsible_employee = {
        "xpath": "(//div[@class='ant-collapse-header'])[2]",
        "name": "responsible_employee"
    }
    select_employee = {
        "xpath": "//label[@class='vz-form-item responsible-employees__select']",
        "name": "select_employee"
    }
    publish_order = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[2]",
        "name": "publish_order"
    }
    radio_button_rate = {
        "xpath": "(//div[@class='ant-radio-group ant-radio-group-outline']//div)[2]",
        "name": "radio_button_rate"
    }
    rate_for_publication = {
        "xpath": "//input[@id='order-clientrate']",
        "name": "rate_for_publication"
    }
    # selection_of_contractors = {
    #     "xpath": "//span[text()='Подрядчики (для публикации доступно: 3 из 3)']",
    #     "name": "selection_of_contractors"
    # }
    selection_of_contractors_lkz = {
        "xpath": "//span[text()='Подрядчики (для публикации доступно: 4 из 4)']",
        "name": "selection_of_contractors_lkz"
    }
    selection_of_contractors_lke = {
        "xpath": "//span[text()='Подрядчики (для публикации доступно: 3 из 21)']",
        "name": "selection_of_contractors_lke"
    }
    contractor_checkbox = {
        "xpath": "(//span[@class='ant-select-tree-checkbox']//span)[2]",
        "name": "contractor_checkbox"
    }
    publish = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[3]",
        "name": "publish"
    }
    ok = {
        "xpath": "//div[@class='ant-modal-confirm-btns']//button[1]",
        "name": "ok"
    }


    click_on_request = {
        "xpath": "//td[@class='ant-table-row-cell-break-word']//a[1]",
        "name": "click_on_request"
    }
    accept_obligations = {
        "xpath": "//button[contains(@class,'ant-btn take-button')]",
        "name": "accept_obligations"
    }
    order_accept = {
        "xpath": "//button[contains(@class,'ant-btn rounded')]",
        "name": "order_accept"
    }
    search_driver = {
        "xpath": "//input[@placeholder='Поиск по номеру ТС / фамилии водителя']",
        "name": "search_driver"
    }
    attach_driver = {
        "xpath": "//button[contains(@class,'ant-btn square')]//img",
        "name": "attach_driver"
    }
    order_accepted = {
        "xpath": "//div[@class='ant-modal-confirm-btns']//button[1]",
        "name": "order_accepted"
    }
    burger_menu = {
        "xpath": "//img[@class='element-icon icon-small']",
        "name": "burger_menu"
    }
    start_execution = {
        "xpath": "//img[@alt='playOrange']",
        "name": "start_execution"
    }
    # tab_execution = {
    #     "xpath": "//a[contains(@class,'vz-tabs-modern__item active')]/following-sibling::a[1]",
    #     "name": "tab_execution"
    # }
    tab_execution = {
        "xpath": "order-calculation",
        "name": "tab_execution",
        "reference": "Расчет заказчика"
    }
    input_start = {
        "xpath": "//input[contains(@class,'ant-calendar-input')]",
        "name": "input_loading_start"
    }
    input_finish = {
        "xpath": "//input[contains(@class,'ant-calendar-input')]",
        "name": "input_loading_finish"
    }
    point_loading_start = {
        "xpath": "//input[@class='ant-calendar-picker-input ant-input']",
        "name": "point_loading_start"
    }
    point_loading_finish = {
        "xpath": "(//input[@class='ant-calendar-picker-input ant-input'])[2]",
        "name": "point_loading_finish"
    }
    point_unloading_start = {
        "xpath": "//span[@class='  ant-calendar-picker']//input",
        "name": "point_unloading_start"
    }
    point_unloading_finish = {
        "xpath": "//span[@id='order-worktime-last']//input[1]",
        "name": "point_unloading_finish"
    }
    save_changes = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "save_changes"
    }
    approve_changes = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[2]",
        "name": "approve_changes"
    }
    ok_time = {
        "xpath": "//div[@class='ant-modal-confirm-btns']//button[@type='button']",
        "name": "ok_time"
    }
    complete_order = {
        "xpath": "//button[@ant-click-animating-without-extra-node='false']",
        "name": "complete_order"
    }
    approve_and_complete_order = {
        "xpath": "//button[@class='ant-btn']/following-sibling::button[1]",
        "name": "approve_and_complete_order"
    }


    point_1_start = {
        "xpath": "//input[@class='ant-calendar-picker-input ant-input']",
        "name": "point_1_start"
    }
    point_1_finish = {
        "xpath": "(//input[@class='ant-calendar-picker-input ant-input'])[2]",
        "name": "point_1_finish"
    }
    point_2_start = {
        "xpath": "//div[contains(@class,'white-box-modern order-view-tab-calculation-client order-view__tab')]//div[2]//div[3]//div[1]//span[1]//div[1]//input[1]",
        "name": "point_2_start"
    }
    point_2_finish = {
        "xpath": "//div[contains(@class,'white-box-modern order-view-tab-calculation-client order-view__tab')]//div[2]//div[3]//div[2]//span[1]//div[1]//input[1]",
        "name": "point_2_finish"
    }
    point_3_start = {
        "xpath": "//div[contains(@class,'order-work-time')]//div[3]//div[3]//div[1]//span[1]//div[1]//input[1]",
        "name": "point_3_start"
    }
    point_3_finish = {
        "xpath": "//div[contains(@class,'order-work-time')]//div[3]//div[3]//div[2]//span[1]//div[1]//input[1]",
        "name": "point_3_finish"
    }
    point_4_start = {
        "xpath": "//div[4]//div[3]//div[1]//span[1]//div[1]//input[1]",
        "name": "point_4_start"
    }
    point_4_finish = {
        "xpath": "//span[@id='order-worktime-last']//input[contains(@placeholder,'дд.мм.гггг чч:мм')]",
        "name": "point_4_finish"
    }
    input_point = {
        "xpath": "//input[contains(@class,'ant-calendar-input')]",
        "name": "input_point"
    }

    """Стадия расчёта"""
    tab_documents = {
        "xpath": "//a[@id='order-documents-order']",
        "name": "tab_documents"
    }
    send_calculation_and_documents = {
        "xpath": "//button[@type='submit']",
        "name": "send_calculation_and_documents",
        "reference_xpath": "//div[@class='ant-modal-confirm-content']",
        "reference": "Расчёт успешно отправлен"
    }
    sent_ok = {
        "xpath": "//div[@class='ant-modal-confirm-btns']//button[@type='button']",
        "name": "sent_ok"
    }
    send_documents = {
        "xpath": "//button[@type='submit']",
        "name": "send_documents",
        "reference_xpath": "//div[@class='ant-modal-confirm-content']",
        "reference": "Документы отправлены"
    }

    tab_calculation_producer = {
        "xpath": "//a[@id='order-documents-producer']",
        "name": "tab_calculation_producer"
    }
    exp_accept_calculation = {
        "xpath": "//span[contains(text(),'Принять')]",
        "name": "exp_accept_calculation"
    }
    exp_documents_allright = {
        "xpath": "//span[contains(text(),'Документы в порядке')]",
        "name": "exp_documents_allright"
    }
    exp_approve_calculation = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "exp_approve_calculation",
        "reference_xpath": "//div[@class='ant-modal-confirm-content']",
        "reference": "Расчет утвержден"
    }
    approved_ok = {
        "xpath": "//div[@class='ant-modal-confirm-btns']//button[@type='button']",
        "name": "approved_ok"
    }

    tab_calculation_client = {
        "xpath": "//a[@id='order-documents-client']",
        "name": "tab_calculation_client"
    }
    exp_send_calculation_and_documents = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "exp_send_calculation_and_documents",
        "reference_xpath": "//div[@class='ant-modal-confirm-content']",
        "reference": "Расчёт успешно отправлен"
    }

    tab_calculation_producer_lkz = {
        "xpath": "//a[@id='order-calculation']",
        "name": "tab_calculation_producer_lkz"
    }
    documents_approve = {
        "xpath": "//span[contains(text(),'Документы в порядке')]",
        "name": "documents_approve"
    }
    documents_approve_approve = {
        "xpath": "//button[@type='submit']",
        "name": "documents_approve_approve",
        "reference_xpath": "//div[@class='ant-modal-confirm-content']",
        "reference": "Документы утверждены"
    }



























