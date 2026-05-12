import uuid
from datetime import datetime, timedelta

import allure
from typing import Dict, Optional

from api_pages.client import APIClient
from api_pages.drivers import DriverAPI
from api_pages.task import TaskAPI


class CreateEntities:
    """Центральный фасад для создания тестовых сущностей"""

    # Доступные роли и их возможности
    ROLE_CAPABILITIES = {
        'lke': ['driver', 'task'],  # LKE может создавать водителей и задания
        'lkp': ['driver'],  # LKP может создавать только водителей
        'lkz': ['task']  # LKZ может создавать только задания
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
