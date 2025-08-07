from base.base_class import Base
import requests
import time
from tests.conftest import api_login


class ProducersList(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    producer_lkp_inn = {
        "xpath": "//a[@class='link-back' and contains(text(), '6883106209')]",
        "name": "producer_lkp_inn"
    }
    producer_logo_inn = {
        "xpath": "//a[@class='link-back' and contains(text(), '5009112893')]",
        "name": "producer_logo_inn"
    }
    producer_vaz_inn = {
        "xpath": "//a[@class='link-back' and contains(text(), '6320002223')]",
        "name": "producer_vaz_inn"
    }
    producer_lke_inn = {
        "xpath": "//a[@class='link-back' and contains(text(), '5178860124')]",
        "name": "producer_lke_inn"
    }
    action_button_lkp = {
        "xpath": "//div[@id='main']/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/button[1]",
        "name": "action_button_lkp"
    }
    action_button_vaz = {
        "xpath": "//button[.//span[contains(text(), 'Действия')]]",
        "name": "action_button_vaz"
    }
    go_to_account_button = {
        "xpath": "//button[.//span[contains(text(), 'Перейти в ЛК контрагента')]]",
        "name": "go_to_account_button"
    }
    assert_auto_lkp = {
        "reference_xpath": "//h4[@class='title' and text()='Auto LKP']",
        "reference": "Auto LKP"
    }
    assert_auto_vaz = {
        "reference_xpath": "//h4[@class='title' and text()='НАО АВТОВАЗ']",
        "reference": "НАО АВТОВАЗ"
    }
    accept_button = {
        "xpath": "(//button[contains(@class,'ant-btn ant-btn-primary')])",
        "name": "accept_button"
    }
    add_internal_contractor = {
        "xpath": "//button[@class='filter-button rounded box-shadow primary default']",
        "name": "add_internal_contractor"
    }
    first_radio_button = {
        "xpath": "(//input[@type='radio' and @class='ant-radio-input'])[3]",
        "name": "first_radio_button"
    }
    confirm_choice_button = {
        "xpath": "//button[@class='ant-btn margin-left-15 ant-btn-primary']",
        "name": "confirm_choice_button"
    }

    """Create inner producer"""
    button_inner_producer = {
        "xpath": "//p[contains(.,'Добавить внутреннего Контрагента')]",
        "name": "button_inner_producer"
    }
    inn_inner_producer = {
        "xpath": "//input[contains(@id,'inn')]",
        "name": "inn_inner_producer"
    }
    kpp_inner_producer = {
        "xpath": "//input[contains(@id,'kpp')]",
        "name": "kpp_inner_producer"
    }
    add_employee = {
        "xpath": "//button[contains(.,'Добавить сотрудника')]",
        "name": "add_employee"
    }
    last_name_field = {
        "xpath": "//*[@id='main']/div/div[3]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr/td[1]/label/div/div[1]/input",
        "name": "last_name_field"
    }
    first_name_field = {
        "xpath": "//*[@id='main']/div/div[3]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr/td[2]/label/div/div[1]/input",
        "name": "first_name_field"
    }
    middle_name_field = {
        "xpath": "",
        "name": "middle_name_field"
    }
    phone_field = {
        "xpath": "",
        "name": "phone_field"
    }
    create_producer_button = {
        "xpath": "//button[contains(.,'Создать')]",
        "name": "create_producer_button"
    }
    ok_popup = {
        "xpath": "//button[contains(.,'OK')]",
        "name": "ok_popup"
    }

    """Creation of a valid INN"""
    def find_valid_inn(self, api_login) -> str | None:

        token = api_login("lke")

        url = "https://api.vezubr.com/v1/api/organization/get"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        attempt = 1
        while True:
            generated_inn = self.generate_inn("entity")
            response = requests.post(
                url,
                json={"inn": generated_inn},
                headers=headers
            )

            print(f"[{attempt}] Проверка ИНН {generated_inn} — статус: {response.status_code}")
            attempt += 1

            if response.status_code == 200:
                data = response.json()
                if data:  # если список не пустой
                    print(f"Найден валидный ИНН: {generated_inn}")
                    return generated_inn

            time.sleep(1)  # антиспам


    """Inner producer"""
    general_information = {
        "xpath": "//div[contains(@class,'vz-tabs-modern vz-tabs-modern--has-matched-count-2 counterparty-tabs')]",
        "name": "general_information"
    }
