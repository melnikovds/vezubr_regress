import uuid
from datetime import datetime, timedelta
import allure
from typing import List, Dict, Optional
from api_pages.client import APIClient
from api_pages.drivers import DriverAPI
from api_pages.task import TaskAPI


class UpdateEntities:
    """Центральный фасад для обновления тестовых сущностей"""

    # Доступные роли и их возможности
    ROLE_CAPABILITIES = {
        'lke': ['driver', 'task'],
        'lkp': ['driver'],
        'lkz': ['task']
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

    @allure.step("Обновление задания")
    def update_task(
            self,
            task_id: int,
            task_number: str,
            cargo_place_ids: Optional[List[int]] = None,
            **overrides
    ):
        if self.role not in ['lke', 'lkz']:
            raise PermissionError(
                f"Роль {self.role.upper()} не может обновлять Задания."
            )

        # 1. билдим данные
        update_data = self.task.generator.build_update_task_data(
            cargo_place_ids=cargo_place_ids,
            number=task_number,
            **overrides
        )

        # 2. отправляем запрос
        task = self.task.update_task(
            task_id=task_id,
            update_data=update_data
        )

        # 3. логирование
        allure.attach(
            f"ID: {task_id}\nНомер: {task_number}",
            name="Обновлённое задание",
            attachment_type=allure.attachment_type.TEXT
        )

        print(f"✅ Задание обновлено → ID: {task_id} | Номер: {task_number}")

        return task

