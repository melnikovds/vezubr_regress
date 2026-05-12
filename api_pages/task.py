import allure
from typing import Dict, Optional
from api_pages.client import APIClient
from .task_data_generator import TaskGenerator


class TaskAPI:
    """API методы для работы с заданиями (shipment/tasks)"""

    def __init__(self, client: APIClient):
        self.client = client
        self.generator = TaskGenerator()

    @allure.step("Создание задания через API")
    def create_task(
            self,
            departure_point_id: int,
            arrival_point_id: int,
            title_prefix: str = "Автотест",
            use_dates: bool = False,
            **kwargs
    ) -> Dict:
        """
        Создание задания

        Args:
            departure_point_id: ID точки отправления
            arrival_point_id: ID точки назначения
            title_prefix: Префикс для названия
            use_dates: использовать ли даты отправки/доставки
            **kwargs: дополнительные параметры для переопределения
        """
        if use_dates:
            task_data = self.generator.generate_task_data_with_dates(
                departure_point_id=departure_point_id,
                arrival_point_id=arrival_point_id,
                title_prefix=title_prefix
            )
        else:
            task_data = self.generator.generate_task_data(
                departure_point_id=departure_point_id,
                arrival_point_id=arrival_point_id,
                title_prefix=title_prefix
            )

        # Переопределяем параметры, если переданы в kwargs
        task_data.update(kwargs)

        # Логируем данные перед отправкой
        allure.attach(
            f"Номер: {task_data['number']}\n"
            f"Название: {task_data['title']}\n"
            f"Точка отправления ID: {departure_point_id}\n"
            f"Точка назначения ID: {arrival_point_id}\n"
            f"Объем: {task_data['volume']} см³\n"
            f"Вес: {task_data['weight']} г\n"
            f"Стоимость: {task_data['cost']} коп\n"
            f"Количество мест: {task_data['quantity']}\n"
            f"Типы груза: {task_data['types']}\n"
            f"Дата отправки с: {task_data.get('requiredSentAtFrom')}\n"
            f"Дата отправки по: {task_data.get('requiredSentAtTill')}\n"
            f"Дата доставки с: {task_data.get('requiredDeliveredAtFrom')}\n"
            f"Дата доставки по: {task_data.get('requiredDeliveredAtTill')}",
            name="Создаваемое задание",
            attachment_type=allure.attachment_type.TEXT
        )

        response = self.client.post("/v1/api/shipment/tasks/create", json=task_data)

        # Извлекаем созданное задание из ответа
        task = response.get('task', response)

        # Добавляем дополнительные поля для удобства
        if 'number' in task_data:
            task['task_number'] = task_data['number']
        if 'title' in task_data:
            task['task_title'] = task_data['title']

        return task

    @allure.step("Получение задания по ID")
    def get_task(self, task_id: int) -> Dict:
        """Получение информации о задании по ID"""
        response = self.client.get(f"/v1/api/shipment/tasks/{task_id}")
        return response.get('task', response)

    @allure.step("Обновление задания")
    def update_task(self, task_id: int, update_data: Dict) -> Dict:
        """Обновление задания"""
        response = self.client.put(f"/v1/api/shipment/tasks/{task_id}/update", json=update_data)
        return response.get('task', response)

    @allure.step("Удаление задания")
    def delete_task(self, task_id: int) -> Dict:
        """Удаление задания (если API поддерживает)"""
        response = self.client.delete(f"/v1/api/shipment/tasks/{task_id}/delete")
        return response

    @allure.step("Назначить водителя на задание")
    def assign_driver_to_task(self, task_id: int, driver_id: int) -> Dict:
        """Назначение водителя на задание"""
        data = {"driverId": driver_id}
        response = self.client.post(f"/v1/api/shipment/tasks/{task_id}/assign-driver", json=data)
        return response