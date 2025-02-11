from base.base_class import Base
import requests


class OldFTL(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    custom_field = {
        "xpath": "//a[text()='Пользовательские поля']",
        "name": "custom_field",
        "reference_xpath": "(//a[@class='vz-tabs-modern__item'])[3]"
    }



    #  Methods
    """Create base Old FTL"""
    def add_old_ftl_lkz(self, api_base_url, api_login) -> str:
        """
        Автоматизирует создание старых FTL-рейсов

        Parameters
        ----------
        Нет входных параметров. Все необходимые данные генерируются или выбираются внутри метода.

        Returns
        -------
        str
            Уникальный номер созданного рейса. Побочные эффекты: изменения на веб-странице.
        """

        # логинимся под ролью ЛКЗ
        token = api_login("lkz")

        # эндпоинт для тестирования
        url = f"{api_base_url}/v1/api/order/transport-request/create-and-publish"

        # выводим эндпоинт в консоль
        print(f"Request URL: {url}")

        headers = { "Authorisation": token }

        body = {}



        res = requests.post(url, headers=headers, params=body)











