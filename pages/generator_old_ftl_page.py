from base.base_class import Base
import allure
import requests
import random
import string
from faker import Faker
from datetime import datetime, timedelta


class GeneratorFTL:
    def __init__(self, api_base_url, api_login):
        """
        Инициализация класса GeneratorFTL.

        :param api_base_url: Базовый URL API.
        :param api_login: Функция для получения токена авторизации.
        """
        self.api_base_url = api_base_url
        self.api_login = api_login
        self.fake = Faker()

    def generate_dynamic_data(self):
        """генерирует динамические данные для POST-запросов"""

        # Текущая дата и время
        now = datetime.now()

        # Дата через 10 дней от текущей
        to_start_at_date = (now + timedelta(days=10)).strftime("%Y-%m-%d")

        # Дата и время через 20 дней от текущей
        required_arrive_at = (now + timedelta(days=20)).strftime("%Y-%m-%d %H:%M")

        # Случайное время в формате "HH:MM"
        to_start_at_time = f"{random.randint(0, 23):02}:{random.randint(0, 59):02}"

        # Значение в формате "XXX-NN-NN"
        client_number = f"{''.join(random.choices(string.ascii_uppercase, k=3))}-{random.randint(10, 99)}-{random.randint(10, 99)}"

        # Значение в формате "YY-NNNNNN"
        current_year_last_two_digits = datetime.now().strftime("%y")
        seal_number = f"{current_year_last_two_digits}-{random.randint(100000, 999999)}"

        return {
            "createdAt": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00"),
            "title": self.fake.sentence(nb_words=3),
            "barCode": f"{self.fake.random_number(digits=5)}0000",
            "quantity": random.randint(1, 500),
            "clientRate": round(random.uniform(100, 100000000), 2),
            "toStartAtTime": to_start_at_time,  # случайное время
            "weight": random.randint(1000, 900000),  # Вес
            "volume": random.randint(10000, 2000000),  # Объём
            "cost": random.randint(100000, 900000000),  # Стоимость
            "toStartAtDate": to_start_at_date,  # Дата через 10 дней
            "requiredArriveAt": required_arrive_at,  # Дата и время через 20 дней
            "clientNumber": client_number,  # Идентификатор заявки
            "sealNumber": seal_number  # номер пломбы
        }

    def create_entity_type_a_lkz(self):
        # Шаг 1: Авторизация
        try:
            token = self.api_login("lkz")  # Получаем токен для роли "lkz"
            if not token:
                raise ValueError("Токен не получен.")
            print(f"Получен токен: {token}")
        except Exception as e:
            print(f"Ошибка при авторизации: {e}")
            return None

        # Шаг 2: Создание сущности
        create_url = f"{self.api_base_url}/v1/api/order/transport-request/create-and-publish"

        create_headers = {
            "Authorization": token,
            "accept": "application/json",
            "Content-Type": "application/json"
        }

        # Генерация динамических данных
        dynamic_data = self.generate_dynamic_data()

        # Фиксируем время создания
        date_create = datetime.now().strftime("%d-%m-%Y")

        # базовые данные для запроса
        payload = {
            "publishingType": "rate",
            "orderType": 3,
            "isInsuranceRequired": False,
            "clientNumber": dynamic_data["clientNumber"],
            "responsibleEmployees": [],
            "isLiftingValidationRequired": True,
            "insurance": False,
            "disabledFields": [],
            "customProperties": [],
            "clientRate": dynamic_data["clientRate"],
            "selectingStrategy": 1,
            "disabledLoadingTypesByVehicleAndBody": [3, 2, 3, 2, 3, 2, 3],
            "toStartAtTime": dynamic_data["toStartAtTime"],
            "cargoPlacesParams": [],
            "cargoPlaces": [
                {
                    "id": 43284,
                    "type": "box",
                    "taskType": "task",
                    "externalId": None,
                    "status": "waiting_for_sending",
                    "statusAddress": {
                        "id": 17098,
                        "timezone": "Europe/Moscow",
                        "addressString": "г Владимир, ул Луначарского, д 25",
                        "externalId": None,
                        "status": True,
                        "cityFiasId": "f66a00e6-179e-4de9-8ecb-78b0277c9f10",
                        "latitude": 56.137299333183,
                        "longitude": 40.417029863624,
                        "cityName": "Владимир",
                        "addressType": None,
                        "necessaryPass": False,
                        "loadingType": "1",
                        "maxHeightFromGroundInCm": None,
                        "cart": None,
                        "elevator": None,
                        "isFavorite": False,
                        "comment": None,
                        "attachedFiles": [],
                        "addressOriginal": None,
                        "source": None,
                        "regionName": "Владимирская область",
                        "createdBy": {
                            "id": 8139,
                            "fullName": "auto@LKZ.com auto@LKZ.com",
                            "roles": [13, 1],
                            "name": "auto@LKZ.com",
                            "surname": "auto@LKZ.com",
                            "patronymic": None
                        },
                        "verifiedBy": {
                            "id": 8139,
                            "fullName": "auto@LKZ.com auto@LKZ.com",
                            "roles": [13, 1],
                            "name": "auto@LKZ.com",
                            "surname": "auto@LKZ.com",
                            "patronymic": None
                        }
                    },
                    "title": dynamic_data["title"],
                    "weight": dynamic_data["weight"],
                    "volume": dynamic_data["volume"],
                    "cost": dynamic_data["cost"],
                    "reverseCargoType": None,
                    "departurePoint": {
                        "id": 17098,
                        "timezone": "Europe/Moscow",
                        "addressString": "г Владимир, ул Луначарского, д 25",
                        "externalId": None,
                        "status": True,
                        "cityFiasId": "f66a00e6-179e-4de9-8ecb-78b0277c9f10",
                        "latitude": 56.137299333183,
                        "longitude": 40.417029863624,
                        "cityName": "Владимир",
                        "addressType": None,
                        "necessaryPass": False,
                        "loadingType": "1",
                        "maxHeightFromGroundInCm": None,
                        "cart": None,
                        "elevator": None,
                        "isFavorite": False,
                        "comment": None,
                        "attachedFiles": [],
                        "addressOriginal": None,
                        "source": None,
                        "regionName": "Владимирская область",
                        "createdBy": {
                            "id": 8139,
                            "fullName": "auto@LKZ.com auto@LKZ.com",
                            "roles": [13, 1],
                            "name": "auto@LKZ.com",
                            "surname": "auto@LKZ.com",
                            "patronymic": None
                        },
                        "verifiedBy": {
                            "id": 8139,
                            "fullName": "auto@LKZ.com auto@LKZ.com",
                            "roles": [13, 1],
                            "name": "auto@LKZ.com",
                            "surname": "auto@LKZ.com",
                            "patronymic": None
                        }
                    },
                    "deliveryPoint": {
                        "id": 16935,
                        "timezone": "Europe/Moscow",
                        "addressString": "г Сыктывкар, ул Юхнина, д 8",
                        "externalId": None,
                        "status": True,
                        "cityFiasId": "d2944a73-daf4-4a08-9b34-d9b0af7785a1",
                        "latitude": 61.672698192342,
                        "longitude": 50.815162623802,
                        "cityName": "Сыктывкар",
                        "addressType": None,
                        "necessaryPass": False,
                        "loadingType": "1",
                        "maxHeightFromGroundInCm": None,
                        "cart": None,
                        "elevator": None,
                        "isFavorite": False,
                        "comment": None,
                        "attachedFiles": [],
                        "addressOriginal": None,
                        "source": None,
                        "regionName": "Республика Коми",
                        "createdBy": {
                            "id": 8139,
                            "fullName": "auto@LKZ.com auto@LKZ.com",
                            "roles": [13, 1],
                            "name": "auto@LKZ.com",
                            "surname": "auto@LKZ.com",
                            "patronymic": None
                        },
                        "verifiedBy": {
                            "id": 8139,
                            "fullName": "auto@LKZ.com auto@LKZ.com",
                            "roles": [13, 1],
                            "name": "auto@LKZ.com",
                            "surname": "auto@LKZ.com",
                            "patronymic": None
                        }
                    },
                    "barCode": dynamic_data["barcode"],
                    "sealNumber": dynamic_data["sealNumber"],
                    "wmsNumber": None,
                    "employeeFullName": None,
                    "category": None,
                    "quantity": dynamic_data["quantity"],
                    "requiredSentAt": None,
                    "requiredDeliveredAt": None,
                    "invoiceNumber": None,
                    "invoiceNumbers": [],
                    "invoiceDate": None,
                    "createdAt": dynamic_data["createdAt"],
                    "length": None,
                    "width": None,
                    "height": None,
                    "parentBarCode": None,
                    "totalCost": None,
                    "isDeleted": False,
                    "comment": None,
                    "reverseCargoReason": None,
                    "lostReason": None,
                    "contractorOwner": {
                        "id": 2448,
                        "inn": "3123625054",
                        "kpp": None,
                        "title": "Auto LKZ",
                        "role": 2,
                        "isVatPayer": True,
                        "isPrivate": False
                    },
                    "direction": "forward",
                    "constrainTempMax": None,
                    "constrainTempMin": None,
                    "number": None,
                    "isPlanned": False,
                    "shipper": None,
                    "consignee": None,
                    "deliveryCost": 0,
                    "cargoDeliveryRequests": [],
                    "includedCount": 0,
                    "subType": None,
                    "feacnCode": None,
                    "departurePointPosition": 1,
                    "arrivalPointPosition": 2,
                    "cargoPlaceId": 43284
                }
            ],
            "newCargoPlaces": [],
            "toStartAtDate": dynamic_data["toStartAtDate"],
            "vehicleType": 1,
            "requiredPassesDetectionMode": 1,
            "bodyTypes": [3, 4, 7, 8],
            "maxHeightFromGroundInCm": None,
            "publicComment": self.fake.sentence(),
            "innerComment": self.fake.sentence(),
            "orderIdentifier": self.fake.random_number(digits=10),
            "trackEncoder": "google",
            "addresses": [
                {
                    "id": 17098,
                    "position": 1,
                    "addressString": "г Владимир, ул Луначарского, д 25",
                    "latitude": 56.137299333183,
                    "longitude": 40.417029863624,
                    "phone": None,
                    "secondPhone": None,
                    "comment": None,
                    "email": None,
                    "loadingType": 1,
                    "isLoadingWork": True,
                    "isUnloadingWork": False,
                    "workStartedAt": None,
                    "workCompletedAt": None,
                    "requiredArriveAt": dynamic_data["requiredArriveAt"],
                    "timeZoneId": "Europe/Moscow",
                    "cityName": "Владимир",
                    "cityFiasId": "f66a00e6-179e-4de9-8ecb-78b0277c9f10",
                    "isSkipped": False,
                    "pointOwnerInn": None,
                    "pointOwnerKpp": None,
                    "pointOwner": None,
                    "maxHeightFromGroundInCm": None,
                    "attachedFiles": []
                },
                {
                    "id": 16935,
                    "position": 2,
                    "addressString": "г Сыктывкар, ул Юхнина, д 8",
                    "latitude": 61.672698192342,
                    "longitude": 50.815162623802,
                    "phone": None,
                    "secondPhone": None,
                    "comment": None,
                    "email": None,
                    "loadingType": 1,
                    "isLoadingWork": False,
                    "isUnloadingWork": True,
                    "workStartedAt": None,
                    "workCompletedAt": None,
                    "requiredArriveAt": None,
                    "timeZoneId": "Europe/Moscow",
                    "cityName": "Сыктывкар",
                    "cityFiasId": "d2944a73-daf4-4a08-9b34-d9b0af7785a1",
                    "isSkipped": False,
                    "pointOwnerInn": None,
                    "pointOwnerKpp": None,
                    "pointOwner": None,
                    "maxHeightFromGroundInCm": None,
                    "attachedFiles": []
                }
            ],
            "requiredContours": [],
            "requiredProducers": [2447, 2449],
            "clientRateProducers": 0,
            "cargoDeclaredVolume": 2000000,
            "cargoDeclaredWeight": 456000,
            "cargoDeclaredPlacesCount": 1,
            "cargoPackagingType": None,
            "requiredDocumentsCategories": [1010, 1020, 1030, 2010, 2020, 2030],
            "orderCategory": 1,
            "loadersTime": None,
            "loadersRequiredOnAddress": None,
            "sanitaryPassportRequired": False,
            "sanitaryBookRequired": False,
            "hydroliftRequired": False,
            "isCornerPillarRequired": False,
            "isChainRequired": False,
            "isStrapRequired": False,
            "isTarpaulinRequired": False,
            "isNetRequired": False,
            "isWheelChockRequired": False,
            "isGPSMonitoringRequired": False,
            "isWoodenFloorRequired": False,
            "isDoppelstockRequired": False,
            "palletJackIsRequired": False,
            "conicsIsRequired": False,
            "fasteningIsRequired": False,
            "isDriverLoaderRequired": False,
            "isTakeOutPackageRequired": False,
            "parametersForProducers": [],
            "additionalData": {
                "ignoreEmptyNumeratorVars": True,
                "numeratorVars": []
            }
        }

        create_response = None  # инициализация переменной

        try:
            create_response = requests.post(create_url, headers=create_headers, json=payload)
            create_response.raise_for_status()
            response_data = create_response.json()
            print("Ответ на запрос создания сущности типа 'A':", response_data)

            return {
                "requestNr": response_data.get("requestNr"), # из ответа
                "date_create": date_create,  # время создания сущности
                "toStartAtDate": dynamic_data["toStartAtDate"],  # из запроса
                "clientNumber": dynamic_data["clientNumber"]  # из запроса
            }

        except requests.exceptions.HTTPError as e:
            # Обработка HTTP-ошибок
            if create_response is not None:  # проверяем, была ли переменная инициализирована
                print(f"HTTP ошибка при создании сущности типа 'A': {e}")
                print(f"статус-код: {create_response.status_code}")
                print(f"Ответ сервера: {create_response.text}")
            else:
                print(f"HTTP ошибка при создании сущности типа 'A': {e}")
            return None

        except requests.exceptions.RequestException as e:
            # обработка других ошибок (например проблемы с сетью)
            print(f"Ошибка при создании сущности типа 'A': {e}")
            return None

    def create_entity_type_b_lkz(self):
        # Шаг 1: Авторизация
        try:
            token = self.api_login("lkz")  # Получаем токен для роли "lkz"
            if not token:
                raise ValueError("Токен не получен.")
            print(f"Получен токен: {token}")
        except Exception as e:
            print(f"Ошибка при авторизации: {e}")
            return None

        # Шаг 2: Создание сущности
        create_url = f"{self.api_base_url}/v1/api/order/transport-request/create-and-publish"

        create_headers = {
            "Authorization": token,
            "accept": "application/json",
            "Content-Type": "application/json"
        }

        # Генерация динамических данных
        dynamic_data = self.generate_dynamic_data()

        # Фиксируем время создания
        date_create = datetime.now().strftime("%d-%m-%Y")

        # базовые данные для запроса
        payload = {
            "publishingType": "tariff",
            "orderType": 3,
            "isInsuranceRequired": False,
            "clientNumber": dynamic_data["clientNumber"],
            "responsibleEmployees": [
                8515
            ],
            "isLiftingValidationRequired": True,
            "pointChangeType": 2,
            "insurance": False,
            "disabledFields": [],
            "customProperties": [],
            "clientRate": None,
            "selectingStrategy": 1,
            "disabledLoadingTypesByVehicleAndBody": [
                2,
                3,
                2,
                3
            ],
            "toStartAtTime": dynamic_data["toStartAtTime"],
            "cargoPlacesParams": [],
            "cargoPlaces": [],
            "newCargoPlaces": [
                {
                    "volume": dynamic_data["volume"],
                    "title": dynamic_data["title"],
                    "cost": dynamic_data["cost"],
                    "departurePointPosition": 1,
                    "arrivalPointPosition": 2,
                    "quantity": dynamic_data["quantity"],
                    "weight": dynamic_data["weight"],
                    "type": "box"
                }
            ],
            "toStartAtDate": dynamic_data["toStartAtDate"],
            "vehicleType": 7,
            "requiredPassesDetectionMode": 1,
            "bodyTypes": [
                3,
                4,
                8
            ],
            "maxHeightFromGroundInCm": None,
            "publicComment": self.fake.sentence(),
            "trackEncoder": "google",
            "addresses": [
                {
                    "id": 16832,
                    "position": 1,
                    "addressString": "Россия, г Мурманск, ул Новое Плато, д 10",
                    "latitude": 68.96191508551,
                    "longitude": 33.096550103058,
                    "phone": None,
                    "secondPhone": None,
                    "comment": None,
                    "email": None,
                    "loadingType": 1,
                    "isLoadingWork": True,
                    "isUnloadingWork": False,
                    "workStartedAt": None,
                    "workCompletedAt": None,
                    "requiredArriveAt": dynamic_data["requiredArriveAt"],
                    "timeZoneId": "Europe/Moscow",
                    "cityName": "Мурманск",
                    "cityFiasId": "ea44e7c5e1d1126adbb485f0f6121a16",
                    "isSkipped": False,
                    "pointOwnerInn": None,
                    "pointOwnerKpp": None,
                    "pointOwner": None,
                    "maxHeightFromGroundInCm": 0,
                    "attachedFiles": []
                },
                {
                    "id": 16834,
                    "position": 2,
                    "addressString": "Россия, г Санкт-Петербург, Лиговский пр-кт, д 195",
                    "latitude": 59.911782519298,
                    "longitude": 30.347832878911,
                    "phone": None,
                    "secondPhone": None,
                    "comment": None,
                    "email": None,
                    "loadingType": 1,
                    "isLoadingWork": False,
                    "isUnloadingWork": True,
                    "workStartedAt": None,
                    "workCompletedAt": None,
                    "requiredArriveAt": None,
                    "timeZoneId": "Europe/Moscow",
                    "cityName": "Санкт-Петербург",
                    "cityFiasId": "a1070e513109e845285940c29822b4de",
                    "isSkipped": False,
                    "pointOwnerInn": "7702021163",
                    "pointOwnerKpp": "770601001",
                    "pointOwner": "ПАО АКЦИОНЕРНЫЙ КОММЕРЧЕСКИЙ БАНК АВАНГАРД -",
                    "maxHeightFromGroundInCm": 0,
                    "attachedFiles": []
                }
            ],
            "requiredContours": [],
            "requiredProducers": [
                2449,
                2447
            ],
            "clientRateProducers": 0,
            "cargoDeclaredVolume": 10000000,
            "cargoDeclaredWeight": 345000,
            "cargoDeclaredPlacesCount": 1,
            "cargoPackagingType": None,
            "requiredDocumentsCategories": [
                1010,
                1020,
                2010,
                2030
            ],
            "orderCategory": 1,
            "loadersTime": None,
            "loadersRequiredOnAddress": None,
            "sanitaryPassportRequired": False,
            "sanitaryBookRequired": False,
            "hydroliftRequired": False,
            "isCornerPillarRequired": False,
            "isChainRequired": True,
            "isStrapRequired": False,
            "isTarpaulinRequired": False,
            "isNetRequired": False,
            "isWheelChockRequired": True,
            "isGPSMonitoringRequired": False,
            "isWoodenFloorRequired": False,
            "isDoppelstockRequired": False,
            "palletJackIsRequired": False,
            "conicsIsRequired": True,
            "fasteningIsRequired": False,
            "isDriverLoaderRequired": False,
            "isTakeOutPackageRequired": False,
            "parametersForProducers": [
                {
                    "producer": "2449",
                    "tariff": "21385",
                    "contract": "18996"
                },
                {
                    "producer": "2447",
                    "tariff": "21386",
                    "contract": "18998"
                }
            ],
            "additionalData": {
                "ignoreEmptyNumeratorVars": True,
                "numeratorVars": []
            }
        }

        create_response = None  # инициализация переменной

        try:
            create_response = requests.post(create_url, headers=create_headers, json=payload)
            create_response.raise_for_status()
            response_data = create_response.json()
            print("Ответ на запрос создания сущности типа 'B':", response_data)

            return {
                "requestNr": response_data.get("requestNr"), # из ответа
                "date_create": date_create,  # время создания сущности
                "toStartAtDate": dynamic_data["toStartAtDate"],  # из запроса
                "clientNumber": dynamic_data["clientNumber"]  # из запроса
            }

        except requests.exceptions.HTTPError as e:
            # Обработка HTTP-ошибок
            if create_response is not None:  # проверяем, была ли переменная инициализирована
                print(f"HTTP ошибка при создании сущности типа 'B': {e}")
                print(f"статус-код: {create_response.status_code}")
                print(f"Ответ сервера: {create_response.text}")
            else:
                print(f"HTTP ошибка при создании сущности типа 'B': {e}")
            return None

        except requests.exceptions.RequestException as e:
            # обработка других ошибок (например проблемы с сетью)
            print(f"Ошибка при создании сущности типа 'B': {e}")
            return None

    def create_entity_type_c_lkz(self):
        # Шаг 1: Авторизация
        try:
            token = self.api_login("lkz")  # Получаем токен для роли "lkz"
            if not token:
                raise ValueError("Токен не получен.")
            print(f"Получен токен: {token}")
        except Exception as e:
            print(f"Ошибка при авторизации: {e}")
            return None

        # Шаг 2: Создание сущности
        create_url = f"{self.api_base_url}/v1/api/order/transport-request/create-and-publish"

        create_headers = {
            "Authorization": token,
            "accept": "application/json",
            "Content-Type": "application/json"
        }

        # Генерация динамических данных
        dynamic_data = self.generate_dynamic_data()

        # Фиксируем время создания
        date_create = datetime.now().strftime("%d-%m-%Y")

        # базовые данные для запроса
        payload = {
                "publishingType": "rate",
                "orderType": 3,
                "isInsuranceRequired": False,
                "clientNumber": dynamic_data["clientNumber"],
                "responsibleEmployees": [],
                "isLiftingValidationRequired": True,
                "pointChangeType": 3,
                "insurance": True,
                "disabledFields": [],
                "customProperties": [],
                "clientRate": dynamic_data["clientRate"],
                "selectingStrategy": 1,
                "disabledLoadingTypesByVehicleAndBody": [
                    2
                ],
                "toStartAtTime": dynamic_data["toStartAtTime"],
                "cargoPlacesParams": [],
                "cargoPlaces": [],
                "newCargoPlaces": [
                    {
                        "volume": dynamic_data["volume"],
                        "title": dynamic_data["title"],
                        "cost": dynamic_data["cost"],
                        "departurePointPosition": 1,
                        "arrivalPointPosition": 2,
                        "quantity": dynamic_data["quantity"],
                        "weight": dynamic_data["weight"],
                        "type": "vehicleBody"
                    }
                ],
                "toStartAtDate": dynamic_data["toStartAtDate"],
                "vehicleType": 108,
                "cargoCategoryId": 70,
                "assessedCargoValue": 120000000,
                "requiredPassesDetectionMode": 1,
                "bodyTypes": [
                    "14"
                ],
                "maxHeightFromGroundInCm": None,
                "publicComment": self.fake.sentence(),
                "trackEncoder": "google",
                "addresses": [
                    {
                        "id": 17097,
                        "position": 1,
                        "addressString": "Россия, г Ижевск, ул Крылова, д 34",
                        "latitude": 56.841997517662,
                        "longitude": 53.119767217843,
                        "contacts": [
                            "Гера Рафикович"
                        ],
                        "phone": "+7 (012) 000-00-07",
                        "secondPhone": None,
                        "comment": "Очень важный адрес",
                        "email": None,
                        "loadingType": 1,
                        "isLoadingWork": True,
                        "isUnloadingWork": False,
                        "workStartedAt": None,
                        "workCompletedAt": None,
                        "requiredArriveAt": dynamic_data["requiredArriveAt"],
                        "timeZoneId": "Europe/Samara",
                        "cityName": "Ижевск",
                        "cityFiasId": "c3bc0dfd16fa2e423611ddd0036caf31",
                        "isSkipped": False,
                        "pointOwnerInn": "6231041862",
                        "pointOwnerKpp": "771501001",
                        "pointOwner": "ООО ЭЛЕТЕК",
                        "maxHeightFromGroundInCm": 0,
                        "attachedFiles": []
                    },
                    {
                        "id": 17100,
                        "position": 2,
                        "addressString": "г Екатеринбург, ул Танкистов, д 4",
                        "latitude": 56.836466641162,
                        "longitude": 60.528300143856,
                        "phone": None,
                        "secondPhone": None,
                        "comment": None,
                        "email": None,
                        "loadingType": 1,
                        "isLoadingWork": False,
                        "isUnloadingWork": True,
                        "workStartedAt": None,
                        "workCompletedAt": None,
                        "requiredArriveAt": None,
                        "timeZoneId": "Asia/Yekaterinburg",
                        "cityName": "Екатеринбург",
                        "cityFiasId": "2763c110-cb8b-416a-9dac-ad28a55b4402",
                        "isSkipped": False,
                        "pointOwnerInn": None,
                        "pointOwnerKpp": None,
                        "pointOwner": None,
                        "maxHeightFromGroundInCm": None,
                        "attachedFiles": []
                    }
                ],
                "requiredContours": [],
                "requiredProducers": [
                    2449,
                    2447
                ],
                "clientRateProducers": 0,
                "cargoDeclaredVolume": 8000000,
                "cargoDeclaredWeight": 890000,
                "cargoDeclaredPlacesCount": 1,
                "cargoPackagingType": None,
                "requiredDocumentsCategories": [
                    1030,
                    2010,
                    2020
                ],
                "orderCategory": 7,
                "loadersTime": None,
                "loadersRequiredOnAddress": None,
                "sanitaryPassportRequired": False,
                "sanitaryBookRequired": False,
                "hydroliftRequired": False,
                "isCornerPillarRequired": True,
                "isChainRequired": False,
                "isStrapRequired": False,
                "isTarpaulinRequired": False,
                "isNetRequired": False,
                "isWheelChockRequired": False,
                "isGPSMonitoringRequired": False,
                "isWoodenFloorRequired": False,
                "isDoppelstockRequired": False,
                "palletJackIsRequired": False,
                "conicsIsRequired": False,
                "fasteningIsRequired": False,
                "isDriverLoaderRequired": False,
                "isTakeOutPackageRequired": False,
                "parametersForProducers": [],
                "additionalData": {
                    "ignoreEmptyNumeratorVars": True,
                    "numeratorVars": []
                }
            }

        create_response = None  # инициализация переменной

        try:
            create_response = requests.post(create_url, headers=create_headers, json=payload)
            create_response.raise_for_status()
            response_data = create_response.json()
            print("Ответ на запрос создания сущности типа 'C':", response_data)

            return {
                "requestNr": response_data.get("requestNr"), # из ответа
                "date_create": date_create,  # время создания сущности
                "toStartAtDate": dynamic_data["toStartAtDate"],  # из запроса
                "clientNumber": dynamic_data["clientNumber"]  # из запроса
            }

        except requests.exceptions.HTTPError as e:
            # Обработка HTTP-ошибок
            if create_response is not None:  # проверяем, была ли переменная инициализирована
                print(f"HTTP ошибка при создании сущности типа 'C': {e}")
                print(f"статус-код: {create_response.status_code}")
                print(f"Ответ сервера: {create_response.text}")
            else:
                print(f"HTTP ошибка при создании сущности типа 'C': {e}")
            return None

        except requests.exceptions.RequestException as e:
            # обработка других ошибок (например проблемы с сетью)
            print(f"Ошибка при создании сущности типа 'C': {e}")
            return None

    def create_entity_type_d_lkz(self):
        # Шаг 1: Авторизация
        try:
            token = self.api_login("lkz")  # Получаем токен для роли "lkz"
            if not token:
                raise ValueError("Токен не получен.")
            print(f"Получен токен: {token}")
        except Exception as e:
            print(f"Ошибка при авторизации: {e}")
            return None

        # Шаг 2: Создание сущности
        create_url = f"{self.api_base_url}/v1/api/order/transport-request/create-and-publish"

        create_headers = {
            "Authorization": token,
            "accept": "application/json",
            "Content-Type": "application/json"
        }

        # Генерация динамических данных
        dynamic_data = self.generate_dynamic_data()

        # Фиксируем время создания
        date_create = datetime.now().strftime("%d-%m-%Y")

        # базовые данные для запроса
        payload = {
                "publishingType": "rate",
                "orderType": 1,
                "isInsuranceRequired": False,
                "clientNumber": dynamic_data["clientNumber"],
                "responsibleEmployees": [
                    8139
                ],
                "isLiftingValidationRequired": True,
                "insurance": False,
                "disabledFields": [],
                "customProperties": [],
                "clientRate": dynamic_data["clientRate"],
                "selectingStrategy": 1,
                "disabledLoadingTypesByVehicleAndBody": [
                    2,
                    3,
                    2,
                    3
                ],
                "toStartAtTime": dynamic_data["toStartAtTime"],
                "cargoPlacesParams": [],
                "cargoPlaces": [],
                "newCargoPlaces": [
                    {
                        "volume": dynamic_data["volume"],
                        "title": dynamic_data["title"],
                        "cost": dynamic_data["cost"],
                        "departurePointPosition": 1,
                        "arrivalPointPosition": 2,
                        "quantity": dynamic_data["quantity"],
                        "weight": dynamic_data["weight"],
                        "type": "box"
                    }
                ],
                "toStartAtDate": dynamic_data["toStartAtDate"],
                "vehicleType": 97,
                "requiredPassesDetectionMode": 1,
                "bodyTypes": [
                    3,
                    7,
                    8
                ],
                "maxHeightFromGroundInCm": None,
                "innerComment": self.fake.sentence(),
                "publicComment": self.fake.sentence(),
                "trackEncoder": "google",
                "addresses": [
                    {
                        "id": 17101,
                        "position": 1,
                        "addressString": "Россия, г Ижевск, ул Дзержинского, д 48а",
                        "latitude": 56.882851576282,
                        "longitude": 53.249601370947,
                        "contacts": [
                            "Майор Громов"
                        ],
                        "phone": "+7 (912) 000-00-08",
                        "secondPhone": None,
                        "comment": "очень важный комментарий для QA",
                        "email": None,
                        "loadingType": 1,
                        "isLoadingWork": True,
                        "isUnloadingWork": False,
                        "workStartedAt": None,
                        "workCompletedAt": None,
                        "requiredArriveAt": dynamic_data["requiredArriveAt"],
                        "timeZoneId": "Europe/Samara",
                        "cityName": "Ижевск",
                        "cityFiasId": "c3bc0dfd16fa2e423611ddd0036caf31",
                        "isSkipped": False,
                        "pointOwnerInn": "7736643243",
                        "pointOwnerKpp": "773001001",
                        "pointOwner": "ООО КОНСАЛТ",
                        "maxHeightFromGroundInCm": 0,
                        "attachedFiles": []
                    },
                    {
                        "id": 17097,
                        "position": 2,
                        "addressString": "Россия, г Ижевск, ул Крылова, д 34",
                        "latitude": 56.841997517662,
                        "longitude": 53.119767217843,
                        "contacts": [
                            "Гера Рафикович"
                        ],
                        "phone": "+7 (012) 000-00-07",
                        "secondPhone": None,
                        "comment": "Очень важный адрес",
                        "email": None,
                        "loadingType": 1,
                        "isLoadingWork": False,
                        "isUnloadingWork": True,
                        "workStartedAt": None,
                        "workCompletedAt": None,
                        "requiredArriveAt": None,
                        "timeZoneId": "Europe/Samara",
                        "cityName": "Ижевск",
                        "cityFiasId": "c3bc0dfd16fa2e423611ddd0036caf31",
                        "isSkipped": False,
                        "pointOwnerInn": "6231041862",
                        "pointOwnerKpp": "771501001",
                        "pointOwner": "ООО ЭЛЕТЕК",
                        "maxHeightFromGroundInCm": 0,
                        "attachedFiles": []
                    }
                ],
                "requiredContours": [],
                "requiredProducers": [
                    2449,
                    2447
                ],
                "clientRateProducers": 0,
                "cargoDeclaredVolume": 2000000,
                "cargoDeclaredWeight": 300000,
                "cargoDeclaredPlacesCount": 1,
                "cargoPackagingType": None,
                "requiredDocumentsCategories": [
                    1010,
                    1020,
                    1030,
                    2010,
                    2020,
                    2030
                ],
                "orderCategory": 4,
                "loadersTime": None,
                "loadersRequiredOnAddress": None,
                "sanitaryPassportRequired": False,
                "sanitaryBookRequired": False,
                "hydroliftRequired": False,
                "isCornerPillarRequired": False,
                "isChainRequired": False,
                "isStrapRequired": False,
                "isTarpaulinRequired": False,
                "isNetRequired": False,
                "isWheelChockRequired": False,
                "isGPSMonitoringRequired": False,
                "isWoodenFloorRequired": False,
                "isDoppelstockRequired": False,
                "palletJackIsRequired": False,
                "conicsIsRequired": False,
                "fasteningIsRequired": False,
                "isDriverLoaderRequired": False,
                "isTakeOutPackageRequired": False,
                "parametersForProducers": [],
                "additionalData": {
                    "ignoreEmptyNumeratorVars": True,
                    "numeratorVars": []
                }
            }

        create_response = None  # инициализация переменной

        try:
            create_response = requests.post(create_url, headers=create_headers, json=payload)
            create_response.raise_for_status()
            response_data = create_response.json()
            print("Ответ на запрос создания сущности типа 'D':", response_data)

            return {
                "requestNr": response_data.get("requestNr"), # из ответа
                "date_create": date_create,  # время создания сущности
                "toStartAtDate": dynamic_data["toStartAtDate"],  # из запроса
                "clientNumber": dynamic_data["clientNumber"]  # из запроса
            }

        except requests.exceptions.HTTPError as e:
            # Обработка HTTP-ошибок
            if create_response is not None:  # проверяем, была ли переменная инициализирована
                print(f"HTTP ошибка при создании сущности типа 'D': {e}")
                print(f"статус-код: {create_response.status_code}")
                print(f"Ответ сервера: {create_response.text}")
            else:
                print(f"HTTP ошибка при создании сущности типа 'D': {e}")
            return None

        except requests.exceptions.RequestException as e:
            # обработка других ошибок (например проблемы с сетью)
            print(f"Ошибка при создании сущности типа 'D': {e}")
            return None

    def create_entity_type_e_lkz(self):
        # Шаг 1: Авторизация
        try:
            token = self.api_login("lkz")  # Получаем токен для роли "lkz"
            if not token:
                raise ValueError("Токен не получен.")
            print(f"Получен токен: {token}")
        except Exception as e:
            print(f"Ошибка при авторизации: {e}")
            return None

        # Шаг 2: Создание сущности
        create_url = f"{self.api_base_url}/v1/api/order/transport-request/create-and-publish"

        create_headers = {
            "Authorization": token,
            "accept": "application/json",
            "Content-Type": "application/json"
        }

        # Генерация динамических данных
        dynamic_data = self.generate_dynamic_data()

        # Фиксируем время создания
        date_create = datetime.now().strftime("%d-%m-%Y")

        # базовые данные для запроса
        payload = {
                "publishingType": "tariff",
                "orderType": 1,
                "isInsuranceRequired": False,
                "clientNumber": dynamic_data["clientNumber"],
                "responsibleEmployees": [],
                "isLiftingValidationRequired": True,
                "insurance": False,
                "disabledFields": [],
                "customProperties": [],
                "clientRate": None,
                "selectingStrategy": 1,
                "disabledLoadingTypesByVehicleAndBody": [
                    2,
                    3
                ],
                "toStartAtTime": dynamic_data["toStartAtTime"],
                "cargoPlacesParams": [],
                "cargoPlaces": [],
                "newCargoPlaces": [],
                "toStartAtDate": dynamic_data["toStartAtDate"],
                "vehicleType": 111,
                "requiredPassesDetectionMode": 1,
                "bodyTypes": [
                    "12"
                ],
                "maxHeightFromGroundInCm": None,
                "publicComment": self.fake.sentence(),
                "trackEncoder": "google",
                "addresses": [
                    {
                        "id": 17101,
                        "position": 1,
                        "addressString": "Россия, г Ижевск, ул Дзержинского, д 48а",
                        "latitude": 56.882851576282,
                        "longitude": 53.249601370947,
                        "contacts": [
                            "Майор Громов"
                        ],
                        "phone": "+7 (912) 000-00-08",
                        "secondPhone": None,
                        "comment": "Тоже очень важный комментарий для QA",
                        "email": None,
                        "loadingType": 1,
                        "isLoadingWork": True,
                        "isUnloadingWork": False,
                        "workStartedAt": None,
                        "workCompletedAt": None,
                        "requiredArriveAt": dynamic_data["requiredArriveAt"],
                        "timeZoneId": "Europe/Samara",
                        "cityName": "Ижевск",
                        "cityFiasId": "c3bc0dfd16fa2e423611ddd0036caf31",
                        "isSkipped": False,
                        "pointOwnerInn": "7736643243",
                        "pointOwnerKpp": "773001001",
                        "pointOwner": "ООО КОНСАЛТ",
                        "maxHeightFromGroundInCm": 0,
                        "attachedFiles": []
                    },
                    {
                        "id": 17097,
                        "position": 2,
                        "addressString": "Россия, г Ижевск, ул Крылова, д 34",
                        "latitude": 56.841997517662,
                        "longitude": 53.119767217843,
                        "contacts": [
                            "Гера Рафикович"
                        ],
                        "phone": "+7 (012) 000-00-07",
                        "secondPhone": None,
                        "comment": "адрес для QA",
                        "email": None,
                        "loadingType": 1,
                        "isLoadingWork": False,
                        "isUnloadingWork": True,
                        "workStartedAt": None,
                        "workCompletedAt": None,
                        "requiredArriveAt": None,
                        "timeZoneId": "Europe/Samara",
                        "cityName": "Ижевск",
                        "cityFiasId": "c3bc0dfd16fa2e423611ddd0036caf31",
                        "isSkipped": False,
                        "pointOwnerInn": "6231041862",
                        "pointOwnerKpp": "771501001",
                        "pointOwner": "ООО ЭЛЕТЕК",
                        "maxHeightFromGroundInCm": 0,
                        "attachedFiles": []
                    }
                ],
                "requiredContours": [],
                "requiredProducers": [
                    2449,
                    2447
                ],
                "clientRateProducers": 0,
                "cargoDeclaredVolume": 0,
                "cargoDeclaredWeight": 600000,
                "cargoDeclaredPlacesCount": 1,
                "cargoPackagingType": None,
                "requiredDocumentsCategories": [
                    1010,
                    1020,
                    2010,
                    2030
                ],
                "orderCategory": 8,
                "loadersTime": None,
                "loadersRequiredOnAddress": None,
                "sanitaryPassportRequired": False,
                "sanitaryBookRequired": False,
                "hydroliftRequired": False,
                "isCornerPillarRequired": False,
                "isChainRequired": False,
                "isStrapRequired": False,
                "isTarpaulinRequired": False,
                "isNetRequired": False,
                "isWheelChockRequired": False,
                "isGPSMonitoringRequired": False,
                "isWoodenFloorRequired": False,
                "isDoppelstockRequired": True,
                "palletJackIsRequired": False,
                "conicsIsRequired": True,
                "fasteningIsRequired": False,
                "isDriverLoaderRequired": False,
                "isTakeOutPackageRequired": False,
                "parametersForProducers": [
                    {
                        "producer": "2449",
                        "tariff": "21387",
                        "contract": "19000"
                    },
                    {
                        "producer": "2447",
                        "tariff": "21388",
                        "contract": "19002"
                    }
                ],
                "additionalData": {
                    "ignoreEmptyNumeratorVars": True,
                    "numeratorVars": []
                }
            }

        create_response = None  # инициализация переменной

        try:
            create_response = requests.post(create_url, headers=create_headers, json=payload)
            create_response.raise_for_status()
            response_data = create_response.json()
            print("Ответ на запрос создания сущности типа 'E':", response_data)

            return {
                "requestNr": response_data.get("requestNr"), # из ответа
                "date_create": date_create,  # время создания сущности
                "toStartAtDate": dynamic_data["toStartAtDate"],  # из запроса
                "clientNumber": dynamic_data["clientNumber"]  # из запроса
            }

        except requests.exceptions.HTTPError as e:
            # Обработка HTTP-ошибок
            if create_response is not None:  # проверяем, была ли переменная инициализирована
                print(f"HTTP ошибка при создании сущности типа 'E': {e}")
                print(f"статус-код: {create_response.status_code}")
                print(f"Ответ сервера: {create_response.text}")
            else:
                print(f"HTTP ошибка при создании сущности типа 'E': {e}")
            return None

        except requests.exceptions.RequestException as e:
            # обработка других ошибок (например проблемы с сетью)
            print(f"Ошибка при создании сущности типа 'E': {e}")
            return None















