import random
from typing import List, Dict, Optional
from datetime import datetime, timedelta


class TaskGenerator:
    """Генератор тестовых данных для заданий (shipment/tasks)"""

    def __init__(self):
        self.counter = 0

    def generate_task_data(
            self,
            producer_id: Optional[int] = None,
            departure_point_id: Optional[int] = None,
            arrival_point_id: Optional[int] = None,
            title_prefix: str = "Автотест"
    ) -> Dict:
        """
        Генерация данных для создания задания

        Args:
            producer_id: ID продюсера (если нужен)
            departure_point_id: ID точки отправления
            arrival_point_id: ID точки назначения
            title_prefix: Префикс для названия задания
        """
        self.counter += 1
        unique_suffix = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{self.counter}"

        task_data = {
            "number": f"{title_prefix} задание {unique_suffix}",
            "title": f"{title_prefix} товар {unique_suffix}",
            "shipBy": "vezubr",  # или "client"
            "requiredSentAtFrom": None,
            "requiredSentAtTill": None,
            "requiredDeliveredAtTill": None,
            "requiredDeliveredAtFrom": None,
            "consignee": None,
            "shipper": None,
            "volume": random.randint(100000, 5000000),  # от 0.1 до 5 м³ в см³
            "weight": random.randint(10000, 500000),  # от 10 до 500 кг в граммах
            "cost": random.randint(10000, 1000000),  # стоимость в копейках
            "quantity": random.randint(1, 10),
            "types": self._generate_types(),
            "isCargoPlacesEnabled": True
        }

        # Добавляем точки, если они переданы
        if departure_point_id:
            task_data["departurePoint"] = {"id": departure_point_id}

        if arrival_point_id:
            task_data["arrivalPoint"] = {"id": arrival_point_id}

        # Добавляем producer_id, если передан (может понадобиться для некоторых ролей)
        if producer_id:
            task_data["producerId"] = producer_id

        return task_data

    def _generate_types(self) -> list:
        """Генерация случайных типов груза"""
        possible_types = ["box", "pallet", "bag"]
        num_types = random.randint(1, 2)
        return random.sample(possible_types, num_types)

    def generate_task_data_with_dates(
            self,
            departure_point_id: int,
            arrival_point_id: int,
            days_offset_from: int = 1,
            days_offset_till: int = 3,
            title_prefix: str = "Автотест"
    ) -> Dict:
        """
        Генерация данных с датами отправки и доставки

        Args:
            departure_point_id: ID точки отправления
            arrival_point_id: ID точки назначения
            days_offset_from: через сколько дней отправить
            days_offset_till: до какой даты отправить
            title_prefix: Префикс для названия
        """
        task_data = self.generate_task_data(
            departure_point_id=departure_point_id,
            arrival_point_id=arrival_point_id,
            title_prefix=title_prefix
        )

        now = datetime.now()

        # Добавляем даты отправки
        task_data["requiredSentAtFrom"] = (now + timedelta(days=days_offset_from)).isoformat() + "Z"
        task_data["requiredSentAtTill"] = (now + timedelta(days=days_offset_till)).isoformat() + "Z"

        # Добавляем даты доставки
        task_data["requiredDeliveredAtFrom"] = (now + timedelta(days=days_offset_from + 1)).isoformat() + "Z"
        task_data["requiredDeliveredAtTill"] = (now + timedelta(days=days_offset_till + 2)).isoformat() + "Z"

        return task_data

    def build_update_task_data(self, cargo_place_ids: Optional[List[int]] = None, **overrides) -> Dict:
        data = {
            "number": "2405",
            "title": "authority000",
            "shipBy": "fm_logistic",
            "arrivalPoint": {"id": 16934},
            "departurePoint": {"id": 18466},
            "types": ["free"],
            "isCargoPlacesEnabled": True,
            "cargoPlaces": []
        }

        if cargo_place_ids:
            data["cargoPlaces"] = [
                {"id": cid, "externalId": None}
                for cid in cargo_place_ids
            ]

        data.update(overrides)
        return data