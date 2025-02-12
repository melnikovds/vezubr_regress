from base.base_class import Base
import requests
import random
import string
from faker import Faker
from datetime import datetime


class OldFTL(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    custom_field = {
        "xpath": "",
        "name": "",
        "reference_xpath": ""
    }


    #  Methods

    fake = Faker()

    @staticmethod
    def random_string(length=8):
        """генератор случайных строк заданной длины."""
        return ''.join(random.choices(string.ascii_letters, k=length))


    date_str = Base.naw_time_change(180, 'date_dot')

    @staticmethod
    def convert_datetime(date_str):
        # разделяем строку на дату и время
        date_part, time_part = date_str.split()

        # преобразуем дату в нужный формат
        toStartAtDate = datetime.strptime(date_part, "%d%m%Y").strftime("%Y-%m-%d")

        # преобразуем время в нужный формат
        toStartAtTime = f"{time_part[:2]}:{time_part[2:]}"

        return toStartAtDate, toStartAtTime

    orderIdentifier = random_string(10)
    InnerComment = fake.sentence()
    publicComment = fake.sentence()
    publishingType = random.choice(['tariff', 'rate'])
    bargainType = random.choice(['open', 'closed'])
    clientRate = random.uniform(100, 100000000)


    """Generate Old FTL"""
    @staticmethod
    def generate_old_ftl(**kwargs):

        return {
        "toStartAtDate": kwargs.get("toStartAtDate"),
        "toStartAtTime": kwargs.get("toStartAtTime"),
        "requiredProducers": [
            2449
        ],
        "client": 0,
        "orderIdentifier": kwargs.get("orderIdentifier"),
        "innerComment": kwargs.get("InnerComment"),
        "publicComment": kwargs.get("publicComment"),
        "publishingType": kwargs.get("publishingType"),
        "clientRate": kwargs.get("clientRate"),
        "parametersForProducers": [
        ],
        "responsibleEmployees": [

        ],
        "additionalData": {
            "numeratorVars": [
            ],
            "ignoreEmptyNumeratorVars": True
        },
        "clientNumber": "string",
        "withoutDocFlow": True,
        "assessedCargoValue": 0,
        "cargoCategoryId": 0,
        "clientCustomProperties": [
            {
                "latinName": "string",
                "values": [
                    "string"
                ]
            }
        ],
        "cargoPlacesParams": [
        ],
        "customProperties": [
            {
                "latinName": "string",
                "values": [
                    "string"
                ]
            }
        ],
        "orderType": 3,
        "vehicleType": 1,
        "bodyTypes": [
            3, 4, 7, 8
        ],
        "hydroliftRequired": False,
        "rampCompatibilityRequired": False,
        "sanitaryPassportRequired": False,
        "palletJackIsRequired": False,
        "isCornerPillarRequired": False,
        "isChainRequired": False,
        "isStrapRequired": False,
        "isTarpaulinRequired": False,
        "isNetRequired": False,
        "isWheelChockRequired": False,
        "isGPSMonitoringRequired": False,
        "isWoodenFloorRequired": False,
        "isDoppelstockRequired": False,
        "isTakeOutPackageRequired": False,
        "isDriverLoaderRequired": False,
        "sanitaryBookRequired": False,
        "conicsIsRequired": False,
        "maxHeightFromGroundInCm": 5,
        "addresses": [
            {
                "loadingType": 1,
                "position": 1,
                "requiredArriveAt": "2025-02-15T15:14:55.932Z",
                "liftingCapacityMax": 0,
                "isLoadingWork": True,
                "isUnloadingWork": False,
                "addToFavourites": False,
                "addressString": "г Владимир, ул Луначарского, д 25",
                "latitude": 56.137299333183,
                "longitude": 56.137299333183,
                "contacts": [
                    "string"
                ],
                "phone": "string",
                "extraPhone": "string",
                "secondPhone": "string",
                "extraSecondPhone": "string",
                "email": "string",
                "comment": "string",
                "cityName": "Владимир",
                "cityFiasId": "f66a00e6-179e-4de9-8ecb-78b0277c9f10",
                "attachedFiles": [
                ],
                "timeZoneId": "Europe/Moscow",
                "isEntryPassRequire": False,
                "id": 17098,
                "externalId": "string",
                "addressType": 1,
                "statusFlowType": "fullFlow",
                "maxHeightFromGroundInCm": 0,
                "cart": {},
                "elevator": {},
                "pointOwnerInn": "string",
                "pointOwnerKpp": "string",
                "title": "string"
            }


        ],
        "requiredPassesDetectionMode": 0,
        "requiredPasses": [
            0
        ],
        "loadersCount": 0,
        "trackPolyline": "string",
        "trackEncoder": "osrm",
        "minVehicleBodyLengthInCm": 0,
        "minVehicleBodyHeightInCm": 0,
        "insurance": False,
        "requiredDocumentsCategories": [
            0
        ],
        "newCargoPlaces": [
            {
                "title": "string",
                "category": "string",
                "type": "box",
                "quantity": 67,
                "volume": 2000000,
                "weight": 4570,
                "cost": 46865600,
                "departurePointPosition": 1,
                "arrivalPointPosition": 2,
                "isPlanned": False
            }
        ],
        "cargoPackagingType": "string",
        "settings": {
            "pointChangeType": 1
        },
        "isLiftingValidationRequired": True,
        "isCargoPlaceAddToOrderAgreed": True,
        "isCargoPlaceExceedingAgreed": True
    }





    """Create base Old FTL"""
    @staticmethod
    def add_old_ftl_lkz(self, api_base_url, api_login) -> str:
        """
        Автоматизирует создание старых FTL-рейсов


        Returns
        -------
        str
            Уникальный номер созданного рейса.
        """

        # логинимся под ролью ЛКЗ
        token = api_login("lkz")

        # эндпоинт для тестирования
        url = f"{api_base_url}/v1/api/order/transport-request/create-and-publish"

        # выводим эндпоинт в консоль
        print(f"Request URL: {url}")

        headers = { "Authorisation": token,
                    "accept": "application/json",
                    "Content-Type": "application/json"
                    }

        data = self.generate_old_ftl()
        print("Отправка данных:", data)

        res = requests.post(url, headers=headers, json=data)
        print(res)
        return res.json()
















