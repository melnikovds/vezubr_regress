from base.base_class import Base
import allure
import requests
import random
import string
from faker import Faker
from datetime import datetime


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
        "toStartAtTime": "08:00",
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
                "createdAt": "2025-02-12T06:58:08+00:00",
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
        "toStartAtDate": "2025-02-13",
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
                "requiredArriveAt": "2025-02-13 08:00",
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
        "requiredProducers": [2449],
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


