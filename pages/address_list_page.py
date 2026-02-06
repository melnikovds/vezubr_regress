from base.base_class import Base


class AddressesList(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_address_button = {
        "xpath": "//button[@class='filter-button rounded box-shadow primary default']",
        "name": "add_address_button"
    }
    name_filter = {
        "xpath": "//input[@placeholder='Название адреса']",
        "name": "name_filter"
    }
    reset_button = {
        "xpath": "//button[contains(., 'Сбросить')]",
        "name": "reset_button"
    }
    first_address_link = {
        "xpath": "//a[@class='link-back']",
        "name": "first_address_link"
    }

    """Address list"""
    factual_address = {
        "xpath": "//input[@placeholder='Фактический адрес']",
        "name": "factual_address"
    }
    identifier_address = {
        "xpath": "//input[@placeholder='Идентификатор адреса']",
        "name": "identifier_address"
    }
    first_radio_button_19225 = {
        "xpath": "//input[@value='19225']",
        "name": "first_radio_button_19225"
    }
    first_radio_button_18466 = {
        "xpath": "//input[@value='18466']",
        "name": "first_radio_button_18466"
    }
    save_selected_address = {
        "xpath": "//div[@class='ant-modal-root']//button[2]",
        "name": "save_selected_address"
    }
