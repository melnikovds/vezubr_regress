import uuid
from datetime import datetime, timedelta
import time
import random
import allure
from typing import Dict, Optional

from api_pages.client import APIClient
from api_pages.drivers import DriverAPI
from api_pages.task import TaskAPI


class CreateEntities:
    """Центральный файл для создания тестовых сущностей"""

    # Доступные роли и их возможности
    ROLE_CAPABILITIES = {
        'lke': ['driver', 'task', 'old_ftl_order'],
        'lkp': ['driver', 'old_ftl_order'],
        'lkz': ['task', 'old_ftl_order']
    }

    def __init__(self, role: str = 'lke'):
        if role.lower() not in self.ROLE_CAPABILITIES:
            raise ValueError(
                f"Роль {role} не поддерживается. "
                f"Доступные роли: {', '.join(self.ROLE_CAPABILITIES.keys())}"
            )

        self.role = role.lower()
        self.client = APIClient(role=self.role)

        # Инициализация API-классов (доступны всем, но методы могут проверять права)
        self.driver = DriverAPI(self.client)
        self.task = TaskAPI(self.client)

        print(f"✅ CreateEntities инициализирован под ролью: {self.role.upper()}")
        print(f"   Доступные сущности: {', '.join(self.ROLE_CAPABILITIES[self.role])}")

    @allure.step("Создание водителя")
    def create_driver(self, surname_prefix: str = "Автотест") -> Dict:
        """Создание водителя (доступно для lke и lkp)"""
        if self.role not in ['lke', 'lkp']:
            raise PermissionError(
                f"Роль {self.role.upper()} не может создавать водителей. "
                f"Доступно для: lke, lkp"
            )

        driver = self.driver.create_driver(surname_prefix)

        full_name = f"{driver.get('surname', '')} {driver.get('name', '')}".strip()
        driver_id = driver.get('id')

        allure.attach(
            f"ID: {driver_id}\nФИО: {full_name}\nТелефон: {driver.get('applicationPhone')}",
            name="Созданный водитель",
            attachment_type=allure.attachment_type.TEXT
        )

        print(f"✅ Водитель создан → ID: {driver_id} | ФИО: {full_name}")
        return driver

    @allure.step("Создание задания")
    def create_task(
            self,
            departure_point_id: int,
            arrival_point_id: int,
            title_prefix: str = "Автотест",
            use_dates: bool = False,
            **kwargs
    ) -> Dict:
        """
        Создание задания (доступно для lke и lkz)

        Args:
            departure_point_id: ID точки отправления
            arrival_point_id: ID точки назначения
            title_prefix: Префикс для названия
            use_dates: использовать ли даты отправки/доставки
            **kwargs: дополнительные параметры задания
        """
        if self.role not in ['lke', 'lkz']:
            raise PermissionError(
                f"Роль {self.role.upper()} не может создавать задания. "
                f"Доступно для: lke, lkz"
            )

        task = self.task.create_task(
            departure_point_id=departure_point_id,
            arrival_point_id=arrival_point_id,
            title_prefix=title_prefix,
            use_dates=use_dates,
            **kwargs
        )

        task_id = task.get('id')
        task_number = task.get('task_number', task.get('number'))

        allure.attach(
            f"ID: {task_id}\nНомер: {task_number}\nНазвание: {task.get('task_title')}",
            name="Созданное задание",
            attachment_type=allure.attachment_type.TEXT
        )

        print(f"✅ Задание создано → ID: {task_id} | Номер: {task_number}")
        return task

    @allure.step("Создание старого FTL заказа для ЛКЕ")
    def create_old_ftl_order_for_lke(
            self,
            client_id: int = 2447,  # Кто заказчик (возможно ЛКЕ?)
            producer_id: int = 2449  # ЛКП как перевозчик
    ) -> Dict:
        """
        Создает старый FTL заказ от имени ЛКЕ
        Использует точный payload из рабочего curl
        """
        import random
        from datetime import datetime, timedelta

        # Генерируем уникальные идентификаторы
        unique_suffix = f"{random.randint(10000, 99999)}"
        client_number = f"AUTO-TEST-{unique_suffix}"
        order_identifier = f"ID-{unique_suffix}"

        # Даты
        now = datetime.now()
        publication_date = now.strftime("%d%m%Y")
        publication_date_from = (now - timedelta(days=1)).strftime("%d%m%Y")
        publication_date_to = (now + timedelta(days=1)).strftime("%d%m%Y")
        to_start_at_date = now.strftime("%Y-%m-%d")  # сегодня, как в curl
        to_start_at_time = "17:50"  # как в curl
        required_arrive_at = f"{to_start_at_date} {to_start_at_time}"

        # Точный payload из твоего curl
        payload = {
            "publishingType": "rate",
            "orderType": 1,
            "isInsuranceRequired": False,
            "clientNumber": client_number,
            "responsibleEmployees": [],
            "isLiftingValidationRequired": True,
            "isDangerousGoods": False,
            "insurance": False,
            "disabledFields": [],
            "customProperties": [],
            "client": client_id,
            "clientRate": 100000,  # как в curl
            "selectingStrategy": 1,
            "disabledLoadingTypesByVehicleAndBody": [3, 2, 3, 2, 3, 2, 3],
            "toStartAtTime": to_start_at_time,
            "cargoPlacesParams": [],
            "cargoPlaces": [],
            "newCargoPlaces": [],
            "toStartAtDate": to_start_at_date,
            "vehicleType": 1,
            "requiredPassesDetectionMode": 1,
            "bodyTypes": [3, 4, 7, 8],
            "publicComment": None,
            "trackEncoder": "google",
            "addresses": [
                {
                    "latitude": 56.869883497766445,
                    "longitude": 60.68690722033104,
                    "cityName": "Екатеринбург",
                    "cityFiasId": "34c59ff2ba25c381b9c9dbb12dea6c5e",
                    "timeZoneId": "Asia/Yekaterinburg",
                    "addressString": "Россия, г Екатеринбург, ул Отдыха, д 1",
                    "isLoadingWork": True,
                    "isUnloadingWork": False,
                    "requiredArriveAt": required_arrive_at,
                    "phone": "",
                    "secondPhone": "",
                    "statusFlowType": "",
                    "maxHeightFromGroundInCm": None,
                    "liftingCapacityMax": None,
                    "comment": None,
                    "loadingType": 1,
                    "position": 1
                },
                {
                    "latitude": 56.780313009023914,
                    "longitude": 60.64328413847388,
                    "cityName": "Екатеринбург",
                    "cityFiasId": "34c59ff2ba25c381b9c9dbb12dea6c5e",
                    "timeZoneId": "Asia/Yekaterinburg",
                    "addressString": "Россия, г Екатеринбург, ул Олега Кошевого, д 32 к 1",
                    "isLoadingWork": False,
                    "isUnloadingWork": True,
                    "phone": "",
                    "secondPhone": "",
                    "statusFlowType": "",
                    "maxHeightFromGroundInCm": None,
                    "liftingCapacityMax": None,
                    "comment": None,
                    "loadingType": 1,
                    "position": 2
                }
            ],
            "requiredContours": [],
            "requiredProducers": [producer_id],
            "clientRateProducers": None,
            "requiredDocumentsCategories": [1010, 1020, 1030, 2010, 2020, 2030],
            "orderCategory": 1,
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
            "clientCustomProperties": [],
            "parametersForProducers": [],
            "additionalData": {
                "ignoreEmptyNumeratorVars": True,
                "numeratorVars": []
            }
        }

        # Добавляем уникальный идентификатор
        payload["orderIdentifier"] = order_identifier

        # Отправляем запрос
        response = self.client.post("/v1/api/order/transport-request/create-and-publish", json=payload)

        order_nr = response.get("requestNr")
        order_id = response.get("id")
        expected_order_number = f"R-{order_nr}-1"

        response['test_data'] = {
            'order_nr': order_nr,
            'order_id': order_id,
            'client_number': client_number,
            'order_identifier': order_identifier,
            'order_number': expected_order_number,
            'publication_date': publication_date,
            'publication_date_from': publication_date_from,
            'publication_date_to': publication_date_to
        }

        print(f"✅ Старый FTL заказ (ЛКЕ) создан → Номер: {order_nr}")
        return response

    @allure.step("Создание старого FTL заказа (old_ftl_order) для теста фильтров")
    def create_old_ftl_order_for_filters(
            self,
            departure_point_id: int,
            arrival_point_id: int,
            producer_id: int = 2447
    ) -> Dict:
        """
        Создает старый FTL заказ через API
        Использует проверенный payload из GeneratorFTL
        """
        # Генерируем уникальные идентификаторы
        unique_suffix = f"{random.randint(10000, 99999)}"
        client_number = f"AUTO-TEST-{unique_suffix}"
        order_identifier = f"ID-{unique_suffix}"

        # Даты
        now = datetime.now()
        publication_date = now.strftime("%d%m%Y")
        publication_date_from = (now - timedelta(days=1)).strftime("%d%m%Y")
        publication_date_to = (now + timedelta(days=1)).strftime("%d%m%Y")
        to_start_at_date = (now + timedelta(days=10)).strftime("%Y-%m-%d")
        required_arrive_at = f"{to_start_at_date} 20:00"

        # Берем ПОЛНЫЙ payload из вашего рабочего примера
        payload = {"publishingType": "rate", "orderType": 1, "isInsuranceRequired": False, "responsibleEmployees": [],
                   "isLiftingValidationRequired": True, "pointChangeType": 1, "isDangerousGoods": False,
                   "insurance": False, "disabledFields": [], "customProperties": [], "client": None,
                   "clientRate": 500000, "selectingStrategy": 1,
                   "disabledLoadingTypesByVehicleAndBody": [3, 2, 3, 2, 3], "toStartAtTime": "20:00",
                   "cargoPlacesParams": [], "cargoPlaces": [], "newCargoPlaces": [], "toStartAtDate": to_start_at_date,
                   "vehicleType": 1, "requiredPassesDetectionMode": 1, "bodyTypes": [3, 4, 8],
                   "minVehicleBodyLengthInCm": None, "minVehicleBodyHeightInCm": None, "maxHeightFromGroundInCm": None,
                   "publicComment": None, "trackEncoder": "google", "addresses": [
                {
                    "id": departure_point_id,
                    "position": 1,
                    "addressString": "Россия, г Владимир, ул Луначарского, д 25",
                    "latitude": 56.137299333183,
                    "longitude": 40.417029863624,
                    "cityName": "Владимир",
                    "loadingType": 1,
                    "isLoadingWork": True,
                    "isUnloadingWork": False,
                    "requiredArriveAt": required_arrive_at,
                    "timeZoneId": "Europe/Moscow"
                },
                {
                    "id": arrival_point_id,
                    "position": 2,
                    "addressString": "Россия, г Сыктывкар, ул Юхнина, д 8",
                    "latitude": 61.672698192342,
                    "longitude": 50.815162623802,
                    "cityName": "Сыктывкар",
                    "loadingType": 1,
                    "isLoadingWork": False,
                    "isUnloadingWork": True,
                    "timeZoneId": "Europe/Moscow"
                }
            ], "requiredContours": [], "requiredProducers": [producer_id], "clientRateProducers": None,
                   "requiredDocumentsCategories": [1010, 1020, 1030, 2010, 2020, 2030], "orderCategory": 1,
                   "sanitaryPassportRequired": False, "sanitaryBookRequired": False, "hydroliftRequired": False,
                   "isCornerPillarRequired": False, "isChainRequired": False, "isStrapRequired": False,
                   "isTarpaulinRequired": False, "isNetRequired": False, "isWheelChockRequired": False,
                   "isGPSMonitoringRequired": False, "isWoodenFloorRequired": False, "isDoppelstockRequired": False,
                   "palletJackIsRequired": False, "conicsIsRequired": False, "fasteningIsRequired": False,
                   "isDriverLoaderRequired": False, "isTakeOutPackageRequired": False, "parametersForProducers": [],
                   "additionalData": {
                       "ignoreEmptyNumeratorVars": True,
                       "numeratorVars": []
                   }, "clientNumber": client_number, "orderIdentifier": order_identifier}

        # Добавляем уникальные идентификаторы

        # Отправляем запрос
        response = self.client.post("/v1/api/order/transport-request/create-and-publish", json=payload)

        order_nr = response.get("requestNr")
        expected_order_number = f"R-{order_nr}-1"

        response['test_data'] = {
            'order_nr': order_nr,
            'client_number': client_number,
            'order_identifier': order_identifier,
            'order_number': expected_order_number,
            'publication_date': publication_date,
            'publication_date_from': publication_date_from,
            'publication_date_to': publication_date_to
        }

        print(f"✅ Старый FTL заказ создан → Номер: {order_nr}")
        return response

    @allure.step("Создание заявки с заданием и публикация")
    def create_and_publish_delivery_request_with_task(
            self,
            task_id: str,
            departure_point_id: int,
            arrival_point_id: int,
            producer_id: int = 2447,
            rate: int = 500000
    ) -> Dict:
        """
        Создание и публикация заявки LKZ с привязкой задания
        """
        if self.role not in ['lkz']:
            raise PermissionError(f"Роль {self.role.upper()} не может создавать заявки. Доступно для: lkz")

        client_identifier = f"АВТОТЕСТ-{uuid.uuid4().hex[:8].upper()}"
        start_date = (datetime.now() + timedelta(days=1)).isoformat() + "Z"

        payload = {
            "deliveryType": "auto",
            "deliverySubType": "ftl",
            "parameters": {
                "orderCategory": 1,
                "bodyTypes": [3, 4, 7, 8],
                "isDangerousGoods": False,
                "vehicleTypeId": 1,
                "orderType": 1,
                "pointChangeType": 2,
                "route": [
                    {"position": 1, "point": departure_point_id, "isLoadingWork": True, "isUnloadingWork": False},
                    {"position": 2, "point": arrival_point_id, "isLoadingWork": False, "isUnloadingWork": True}
                ]
            },
            "shipmentTasks": [{"id": task_id, "departurePoint": departure_point_id, "arrivalPoint": arrival_point_id}],
            "clientIdentifier": client_identifier,
            "toStartAtFrom": start_date,
            "parametersForProducers": {
                "shares": [{"producer": producer_id, "rate": rate}],
                "selectingStrategy": "rate"
            }
        }

        response = self.client.post("/v1/api/cargo-delivery-requests/create-and-publish", json=payload)

        delivery_request = response
        delivery_request['client_identifier'] = client_identifier

        allure.attach(
            f"ID: {delivery_request.get('id')}\nНомер: {delivery_request.get('requestNr')}\nClient ID: {client_identifier}",
            name="Созданная заявка",
            attachment_type=allure.attachment_type.TEXT
        )

        return delivery_request


# ====================== ЗАПУСК ПРОВЕРКИ ======================
if __name__ == "__main__":
    print("=== Проверка создания сущностей ===\n")

    # Тестовые ID точек (замените на реальные)
    TEST_DEPARTURE_POINT_ID = 28754
    TEST_ARRIVAL_POINT_ID = 28756

    # Тестируем разные роли
    for role in ["lke", "lkp", "lkz"]:
        print(f"\n{'=' * 50}")
        print(f"--- Тест под ролью {role.upper()} ---")
        print(f"{'=' * 50}")

        try:
            creator = CreateEntities(role=role)

            # Пробуем создать водителя
            try:
                driver = creator.create_driver(surname_prefix=f"Автотест_{role.upper()}")
                print(f"  ✓ Водитель создан успешно")
            except PermissionError as e:
                print(f"  ✗ Водитель: {e}")
            except Exception as e:
                print(f"  ✗ Ошибка при создании водителя: {e}")

            # Пробуем создать задание
            try:
                task = creator.create_task(
                    departure_point_id=TEST_DEPARTURE_POINT_ID,
                    arrival_point_id=TEST_ARRIVAL_POINT_ID,
                    title_prefix=f"Автотест_{role.upper()}"
                )
                print(f"  ✓ Задание создано успешно")
            except PermissionError as e:
                print(f"  ✗ Задание: {e}")
            except Exception as e:
                print(f"  ✗ Ошибка при создании задания: {e}")

        except Exception as e:
            print(f"❌ Ошибка инициализации для роли {role.upper()}: {e}")

    print(f"\n{'=' * 50}")
    print("✅ Все проверки завершены")

