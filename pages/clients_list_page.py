from typing import Optional

from base.base_class import Base
import requests
import time


class ClientsList(Base):
    def __init__(self, driver, api_login=None):
        super().__init__(driver)
        self.driver = driver
        self.api_login = api_login

    # Locators
    client_lkz_inn = {
        "xpath": "//a[@class='link-back' and contains(text(), '3123625054')]",
        "name": "client_lkz_inn"
    }
    client_lke_inn = {
        "xpath": "//a[@class='link-back' and contains(text(), '5178860124')]",
        "name": "client_lkz_inn"
    }
    action_button = {
        "xpath": "(//button[contains(@class,'ant-btn ant-dropdown-trigger')])[2]",
        "name": "action_button"
    }
    go_to_account_button = {
        "xpath": "//button[.//span[contains(text(), 'Перейти в ЛК контрагента')]]",
        "name": "go_to_account_button"
    }
    assert_auto_lkz = {
        "reference_xpath": "//h4[@class='title' and text()='Auto LKZ']",
        "reference": "Auto LKZ"
    }
    accept_button = {
        "xpath": "(//button[contains(@class,'ant-btn ant-btn-primary')])",
        "name": "accept_button"
    }


    """Create inner client"""
    button_inner_client = {
        "xpath": "//p[contains(.,'Добавить внутреннего Контрагента')]",
        "name": "button_inner_client"
    }
    inn_inner_client = {
        "xpath": "//input[contains(@id,'inn')]",
        "name": "inn_inner_client"
    }
    kpp_inner_client = {
        "xpath": "//input[contains(@id,'kpp')]",
        "name": "kpp_inner_client"
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
        "xpath": "//*[@id='main']/div/div[3]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr/td[3]/label/div/div[1]/input",
        "name": "middle_name_field"
    }
    email_field = {
        "xpath": "//*[@id='main']/div/div[3]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr/td[4]/label/div/div[1]/input",
        "name": "email_field"
    }
    phone_field = {
        "xpath": "//*[@id='main']/div/div[3]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr/td[5]/label/div/div[1]/input",
        "name": "phone_field"
    }
    create_client_button = {
        "xpath": "//button[contains(.,'Создать')]",
        "name": "create_client_button"
    }

    """Creation of a valid INN"""
    def find_valid_inn(self) -> Optional[str]:

        # получения токена
        try:
            token = self.api_login("lke")
            if not token:
                raise ValueError("Токен не получен")
            print(f" Получен токен: {token}")
        except Exception as e:
            print(f"Ошибка при авторизации: {e}")
            return None

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

            time.sleep(1)  # чтобы не спамить API







    
