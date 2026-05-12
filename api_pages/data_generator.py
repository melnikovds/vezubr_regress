import random
import time
from typing import Optional


class DataGenerators:
    """Класс с генераторами тестовых данных"""

    # Реальные коды регионов РФ
    REAL_REGIONS = [
        1, 2, 3, 4, 5, 7, 10, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
        28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
        40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
        52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63,
        64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,
        76, 77, 78, 79, 82, 86, 87, 89
    ]

    # Коды налоговых инспекций
    REAL_IFNS = [
        1, 2, 3, 4, 5, 6, 7, 8, 9,
        10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
        20, 21, 22, 23, 24, 25
    ]

    @classmethod
    def get_timestamp(cls) -> str:
        """Получить timestamp"""
        return str(int(time.time()))

    @classmethod
    def generate_inn(cls, entity_type: str) -> str:
        """
        Генерация реального ИНН

        Args:
            entity_type: 'individual' (для физлица) или 'entity' (для юрлица)

        Returns:
            str: валидный ИНН
        """

        def calc(nums, coeffs):
            return sum(a * b for a, b in zip(nums, coeffs)) % 11 % 10

        # Формируем реальные первые 4 цифры
        region = random.choice(cls.REAL_REGIONS)
        ifns = random.choice(cls.REAL_IFNS)

        prefix = [
            region // 10, region % 10,
            ifns // 10, ifns % 10
        ]

        if entity_type == "entity":
            # ИНН для юрлица (10 цифр)
            body = prefix + [random.randint(0, 9) for _ in range(5)]
            coeffs = [2, 4, 10, 3, 5, 9, 4, 6, 8]
            control = calc(body, coeffs)
            return ''.join(map(str, body)) + str(control)

        elif entity_type == "individual":
            # ИНН для физлица (12 цифр)
            body = prefix + [random.randint(0, 9) for _ in range(6)]
            coeffs1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
            coeffs2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 5]
            d11 = calc(body, coeffs1)
            d12 = calc(body + [d11], coeffs2)
            return ''.join(map(str, body)) + str(d11) + str(d12)

        else:
            raise ValueError("Тип должен быть 'individual' или 'entity'")

    @classmethod
    def generate_snils(cls) -> str:
        """
        Генерация реального СНИЛС

        Формат: XXX-XXX-XXX YY
        Контрольная сумма вычисляется по алгоритму

        Returns:
            str: валидный СНИЛС (11 цифр без разделителей)
        """
        # Генерируем первые 9 цифр
        while True:
            # Первые 9 цифр (номер)
            number = [random.randint(0, 9) for _ in range(9)]

            # Вычисляем контрольную сумму
            total = 0
            for i, digit in enumerate(number):
                total += digit * (9 - i)

            # Контрольное число
            if total < 100:
                control = total
            elif total == 100 or total == 101:
                control = 0
            else:
                control = total % 101
                if control == 100:
                    control = 0

            # Проверяем последние 2 цифры
            if 0 <= control <= 99:
                # Формируем СНИЛС: 9 цифр + 2 контрольные
                snils = ''.join(map(str, number)) + f"{control:02d}"
                return snils

    @classmethod
    def generate_random_name(cls, prefix: str = "") -> str:
        """Генерация случайного имени"""
        names = ["Иван", "Петр", "Сергей", "Алексей", "Дмитрий", "Андрей", "Михаил", "Владимир"]
        if prefix:
            return f"{prefix}{random.choice(names)}{cls.get_timestamp()}"
        return f"{random.choice(names)}{cls.get_timestamp()}"

    @classmethod
    def generate_random_surname(cls, prefix: str = "Тест") -> str:
        """Генерация случайной фамилии"""
        surnames = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Соколов", "Михайлов", "Федоров"]
        return f"{prefix}{random.choice(surnames)}{cls.get_timestamp()}"

    @classmethod
    def generate_random_patronymic(cls) -> str:
        """Генерация отчества (всегда test)"""
        return "test"

    @classmethod
    def generate_random_phone(cls) -> str:
        """Генерация случайного телефона в формате +7 (XXX) XXX-XX-XX"""
        return f"+7 (9{random.randint(10, 99)}) {random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(10, 99)}"

    @classmethod
    def generate_random_passport_id(cls) -> str:
        """Генерация номера паспорта (серия + номер)"""
        # Серия: 4 цифры, Номер: 6 цифр
        series = random.randint(1000, 9999)
        number = random.randint(100000, 999999)
        return f"{series}{number}"

    @classmethod
    def generate_random_passport_code(cls) -> str:
        """Генерация кода подразделения (XXX-XXX)"""
        return f"{random.randint(100, 999)}-{random.randint(100, 999)}"

    @classmethod
    def generate_random_passport_issued_by(cls) -> str:
        """Генерация кем выдан паспорт"""
        issuers = [
            "ОВД района Хамовники",
            "УФМС России по г. Москве",
            "Отделом УФМС по району",
            "МП №1 ОУФМС России",
            "ТП УФМС России по МО",
            "Отделом полиции №1",
            "ОВД района Арбат"
        ]
        return random.choice(issuers)

    @classmethod
    def generate_random_license_id(cls) -> str:
        """Генерация номера водительского удостоверения"""
        # Формат: 2 серия + 6 номер
        series = random.randint(10, 99)
        number = random.randint(100000, 999999)
        return f"{series}{number}"

    @classmethod
    def generate_random_address(cls, address_type: str = "registration") -> str:
        """Генерация случайного адреса"""
        cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань", "Нижний Новгород"]
        streets = ["Ленина", "Советская", "Центральная", "Мира", "Пушкина", "Гагарина"]

        city = random.choice(cities)
        street = random.choice(streets)
        house = random.randint(1, 200)
        apartment = random.randint(1, 500)

        if address_type == "registration":
            return f"г {city}, ул {street}, д {house}, кв {apartment}"
        else:
            return f"г {city}, ул {street}, д {house}, кв {apartment}"

    @classmethod
    def generate_random_date(cls, year_start: int, year_end: int) -> str:
        """Генерация случайной даты в формате ISO"""
        year = random.randint(year_start, year_end)
        month = random.randint(1, 12)
        day = random.randint(1, 28)  # Упрощенно, без проверки високосности

        # Формат: YYYY-MM-DDThh:mm:ss.sssZ
        return f"{year}-{month:02d}-{day:02d}T{random.randint(10, 18)}:{random.randint(10, 59)}:{random.randint(10, 59)}.{random.randint(100, 999)}Z"

    @classmethod
    def generate_random_inn_individual(cls) -> str:
        """Генерация ИНН для физического лица"""
        return cls.generate_inn("individual")

    @classmethod
    def generate_random_inn_entity(cls) -> str:
        """Генерация ИНН для юридического лица"""
        return cls.generate_inn("entity")
