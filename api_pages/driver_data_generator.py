from typing import Dict
from .data_generator import DataGenerators


class DriverGenerator:

    @classmethod
    def generate_driver_data(
        cls,
        producer_id: int,
        surname_prefix: str = "Автотест"
    ) -> Dict:
        """Генерирует полный и валидный payload для создания водителя"""

        surname = DataGenerators.generate_random_surname(surname_prefix)
        name = DataGenerators.generate_random_name()

        birth_date = DataGenerators.generate_random_date(1975, 2000)
        license_issued = DataGenerators.generate_random_date(2018, 2024)
        license_expires = DataGenerators.generate_random_date(2026, 2035)

        return {
            "producerId": producer_id,

            # Личные данные
            "surname": surname,
            "name": name,
            "patronymic": "test",
            "dateOfBirth": birth_date,
            "placeOfBirth": "г Москва",
            "country": "RU",

            # Контакты
            "applicationPhone": DataGenerators.generate_random_phone(),

            # Паспорт
            "passportId": DataGenerators.generate_random_passport_id(),
            "passportCode": DataGenerators.generate_random_passport_code(),
            "passportIssuedBy": DataGenerators.generate_random_passport_issued_by(),
            "passportIssuedAtDate": license_issued,

            # Водительское удостоверение (все обязательные поля)
            "driverLicenseId": DataGenerators.generate_random_license_id(),
            "driverLicenseSurname": surname,
            "driverLicenseName": name,
            "driverLicensePatronymic": "test",
            "driverLicenseDateOfBirth": birth_date,
            "driverLicensePlaceOfBirth": "г Москва",
            "driverLicenseIssuedBy": "ГИБДД ГУ МВД России по г. Москве",
            "driverLicenseIssuedAtDate": license_issued,
            "driverLicenseExpiresAtDate": license_expires,

            # Дополнительно
            "inn": DataGenerators.generate_random_inn_individual(),
            "snils": DataGenerators.generate_snils(),
            "registrationAddress": DataGenerators.generate_random_address("registration"),

            "status": "active",
        }