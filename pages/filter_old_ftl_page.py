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
    reset_filters = {
        "xpath": "//button[contains(@class,'ant-btn semi-wide')]",
        "name": "reset_filters"
    }
    request_number = {
        "xpath": "(//input[@class='ant-input'])[3]",
        "name": "request_number"
    }
    request_status = {
        "xpath": "//div[@data-__field='[object Object]']",
        "name": "request_status"
    }
    request_identifier = {
        "xpath": "//input[@placeholder='Идентификатор Заявки']",
        "name": "request_identifier"
    }
    publication_date = {
        "xpath": "(//span[@class='ant-calendar-picker']//span)[3]",
        "name": "publication_date"
    }
    publication_from = {
        "xpath": "//input[@class='ant-calendar-input ']",
        "name": "publication_from"
    }
    publication_before = {
        "xpath": "(//input[@class='ant-calendar-input '])[2]",
        "name": "publication_before"
    }
    order_number = {
        "xpath": "//input[@placeholder='Номер рейса']",
        "name": "order_number"
    }

    order_number_two = {
        "xpath": "(//input[@class='ant-input'])[3]",
        "name": "order_number_two"
    }
    request_number_two = {
        "xpath": "//input[@placeholder='Номер заявки']",
        "name": "request_number_two"
    }
    order_stage = {
        "xpath": "//span[@class='ant-select-selection ant-select-selection--multiple']",
        "name": "order_stage"
    }
    checkbox_one = {
        "xpath": "//span[@title='Подбор']",
        "name": "checkbox_one"
    }
    checkbox_two = {
        "xpath": "//span[@title='Исполнение']",
        "name": "checkbox_two"
    }
    checkbox_three = {
        "xpath": "//span[@title='Подтверждение и расчет']",
        "name": "checkbox_three"
    }
    checkbox_four = {
        "xpath": "//span[@title='Отменен']",
        "name": "checkbox_four"
    }
    responsible_user = {
        "xpath": "//div[@data-__field='[object Object]']",
        "name": "responsible_user"
    }

    cross = {
        "xpath": "//*[@id='deferred-maindate-rangepicker']/span/i[1]",
        "name": "cross"
    }
    menu_calendar = {
        "xpath": "//span[@class='ant-calendar-picker']//span",
        "name": "menu_calendar"
    }
    order_identifier = {
        "xpath": "//input[@placeholder='Идентификатор Рейса']",
        "name": "order_identifier"
    }

    template_name = {
        "xpath": "//input[@class='ant-input']",
        "name": "template_name"
    }
    template_status = {
        "xpath": "//div[contains(@class,'ant-select-selection ')]",
        "name": "template_status"
    }
    order_type = {
        "xpath": "(//div[@data-__field='[object Object]'])[2]",
        "name": "order_type"
    }
    filing_address = {
        "xpath": "(//input[@class='ant-input'])[3]",
        "name": "filing_address"
    }
    delivery_address = {
        "xpath": "//input[@placeholder='Адрес доставки']",
        "name": "delivery_address"
    }
    cross_two = {
        "xpath": "//*[@id='orderType']/div/span[1]",
        "name": "cross_two"
    }

    vsk = {
        "xpath": "(//a[@href='/insurers/043af8af-4e3d-4a6f-86bf-14f4498e3e23'])[2]",
        "name": "vsk"
    }
    insured_orders = {
        "xpath": "(//a[@class='vz-tabs-modern__item'])[2]",
        "name": "insured_orders"
    }
    cross_three = {
        "xpath": "//*[@id='main']/div/div[3]/div[2]/div/div[2]/div[2]/div/form/div[2]/div[1]/div/div[2]/div/span/span/span/span[1]",
        "name": "cross_three"
    }
    order_number_three = {
        "xpath": "//input[@placeholder='№ Рейса']",
        "name": "order_number_three"
    }
    contract_number = {
        "xpath": "//label[text()='Номер договора']/following::input",
        "name": "contract_number"
    }
    cross_four = {
        "xpath": "//*[@id='undefined-rangepicker']/span/i[1]",
        "name": "cross_four"
    }





    # start_at_from_button = {
    #
    #
    # }
    #
    # def change_date_time(self) -> None:
    #     new_time = self.naw_time_change(30)
    #     # Клик по кнопке выбора даты и времени начала подачи
    #     self.click_button(self.start_at_from_button)
    #     # Клик по кнопке выбора сегодняшней даты
    #     self.click_button(self.today_button)
    #     # Еще раз клик по кнопке выбора даты и времени начала подачи
    #     self.click_button(self.start_at_from_button)
    #     # Ввод новой временной метки в соответствующее поле
    #     self.backspace_and_input(self.start_at_from_input, num=5, value=new_time)
    #     # Клик по кнопке подтверждения выбора даты и времени
    #     self.click_button(self.calendar_ok_button)




def create_entity():
    # Шаг 1: Авторизация (первый POST-запрос)
    auth_url = "https://api.vezubr.com/v1/api/user/login"
    auth_payload = {
        "username": "auto@LKZ.com",
        "password": "auto@LKZ.com"
    }
    auth_headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    try:
        auth_response = requests.post(auth_url, headers=auth_headers, json=auth_payload)
        auth_response.raise_for_status()  # Проверка на ошибки HTTP
        auth_data = auth_response.json()
        print("Ответ на запрос авторизации:", auth_data)

        # Извлекаем токен из ответа
        token = auth_data.get("token")
        if not token:
            raise ValueError("Токен не найден в ответе авторизации.")

        print(f"Получен токен: {token}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при авторизации: {e}")
        return None

    # Шаг 2: Создание сущности (второй POST-запрос)
    create_url = "https://api.vezubr.com/v1/api/order/transport-request/create-and-publish"
    create_payload = {
        "publishingType": "rate",
        "orderType": 3,
        "isInsuranceRequired": False,
        "clientNumber": None,
        "responsibleEmployees": [],
        "isLiftingValidationRequired": True,
        "insurance": False,
        "disabledFields": [],
        "customProperties": [],
        "clientRate": 540000,
        "selectingStrategy": 1,
        "disabledLoadingTypesByVehicleAndBody": [3, 2, 3, 2, 3, 2, 3],
        "toStartAtTime": "14:30",
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
                "title": "ghfhgfhgf",
                "weight": 456000,
                "volume": 2000000,
                "cost": 576576500,
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
                "barCode": "2448432840000",
                "sealNumber": None,
                "wmsNumber": None,
                "employeeFullName": None,
                "category": None,
                "quantity": 123,
                "requiredSentAt": None,
                "requiredDeliveredAt": None,
                "invoiceNumber": None,
                "invoiceNumbers": [],
                "invoiceDate": None,
                "createdAt": "2025-02-20T09:58:08+00:00",
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
        "toStartAtDate": "2025-03-14",
        "vehicleType": 1,
        "requiredPassesDetectionMode": 1,
        "bodyTypes": [3, 4, 7, 8],
        "maxHeightFromGroundInCm": None,
        "publicComment": None,
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
                "requiredArriveAt": "2025-03-20 08:00",
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
    create_headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": token
    }

    try:
        create_response = requests.post(create_url, headers=create_headers, json=create_payload)
        create_response.raise_for_status()  # Проверка на ошибки HTTP
        create_data = create_response.json()
        print("Ответ на запрос создания сущности:", create_data)

        # Извлекаем requestNr из ответа
        request_nr = create_data.get("requestNr")
        if not request_nr:
            raise ValueError("Поле 'requestNr' не найдено в ответе.")

        print(f"Получен requestNr: {request_nr}")
        return request_nr

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при создании сущности: {e}")
        return None

# Вызов функции
if __name__ == "__main__":
    request_nr = create_entity()
    if request_nr:
        print(f"Функция завершена успешно. requestNr: {request_nr}")
    else:
        print("Что-то пошло не так.")
















