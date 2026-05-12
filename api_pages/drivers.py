import allure
from typing import Dict
from api_pages.client import APIClient
from .driver_data_generator import DriverGenerator


class DriverAPI:
    """API методы для работы с водителями"""

    def __init__(self, client: APIClient):
        self.client = client
        self.generator = DriverGenerator()

    @allure.step("Создание водителя через API")
    def create_driver(self, surname_prefix: str = "Автотест") -> Dict:
        driver_data = self.generator.generate_driver_data(
            producer_id=self.client.producer_id,
            surname_prefix=surname_prefix
        )

        # Логируем данные перед отправкой
        allure.attach(
            f"Фамилия: {driver_data['surname']}\n"
            f"Имя: {driver_data['name']}\n"
            f"Телефон: {driver_data['applicationPhone']}\n"
            f"Дата рождения: {driver_data.get('dateOfBirth')}\n"
            f"ВУ: {driver_data.get('driverLicenseId')}",
            name="Создаваемый водитель",
            attachment_type=allure.attachment_type.TEXT
        )

        response = self.client.post("/v1/api/driver/create", json=driver_data)

        driver = response.get('driver', response)

        # Добавляем ФИО в возвращаемый объект для удобства
        if 'surname' in driver_data and 'name' in driver_data:
            driver['full_name'] = f"{driver_data['surname']} {driver_data['name']}".strip()

        return driver
