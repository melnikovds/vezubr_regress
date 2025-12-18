import random
from datetime import datetime, timedelta

from faker import Faker

# Инициализация Faker
fake = Faker()


def generate_combined_client_id(prefix="FTL"):
    # Текущая дата в формате YYYYMMDD
    current_date = datetime.now().strftime("%Y%m%d")
    # Генерация случайного числа из 5 цифр
    number = str(random.randint(10000, 99999))
    return f"{prefix}-{current_date}-{number}"


def generate_random_future_date():
    # Текущая дата и время
    current_time = datetime.now()

    # Генерация случайного количества дней в будущем (например, от 1 до 30 дней)
    random_days = random.randint(1, 30)

    # Генерация случайного количества часов в будущем (например, от 1 до 24 часов)
    random_hours = random.randint(1, 24)

    # Добавляем случайное количество дней и часов к текущему времени
    future_date = current_time + timedelta(days=random_days, hours=random_hours)

    # Форматируем дату в ISO-формат с добавлением "Z" для UTC
    return future_date.isoformat() + "Z"


def generate_random_flight():
    # Генерация случайной даты и времени
    to_start_at_from = generate_random_future_date()

    # Генерация случайных точек загрузки/разгрузки
    departure_point = random.choice([17101, 16932, 17137])
    arrival_point = random.choice([17097, 17102, 16832])

    # Генерация случайного объема, веса и количества паллет
    volume = random.randint(1000000, 5000000)
    weight = random.randint(500000, 1000000)
    quantity = random.randint(1, 5)
    # Генерация случайного комментария
    comment = fake.sentence()
    # Подрядчики
    fixed_producers = [2447, 2449]
    # Генерация одной случайной ставки для всех подрядчиков
    rate = random.randint(10000000, 50000000)

    shares = [
        {
            "producer": producer,
            "rate": rate
        }
        for producer in fixed_producers
    ]
    # Генерация данных для рейса
    flight_data = {
        "deliveryType": "auto",
        "deliverySubType": "ftl",
        "parameters": {
            "orderCategory": 1,
            "bodyTypes": [3, 4, 7, 8],
            "vehicleTypeId": 1,
            "isCornerPillarRequired": random.choice([True, False]),
            "isStrapRequired": random.choice([True, False]),
            "isChainRequired": random.choice([True, False]),
            "isNetRequired": random.choice([True, False]),
            "isTarpaulinRequired": random.choice([True, False]),
            "isWheelChockRequired": random.choice([True, False]),
            "isGPSMonitoringRequired": random.choice([True, False]),
            "isWoodenFloorRequired": random.choice([True, False]),
            "isDoppelstockRequired": random.choice([True, False]),
            "isTakeOutPackageRequired": random.choice([True, False]),
            "isDriverLoaderRequired": random.choice([True, False]),
            "orderType": 1,
            "isHydroliftRequired": random.choice([True, False]),
            "isPalletJackRequired": random.choice([True, False]),
            "isConicsRequired": random.choice([True, False]),
            "isThermographRequired": random.choice([True, False]),
            "isLiftingValidationRequired": random.choice([True, False]),
            "pointChangeType": random.randint(1, 3),
            "isSanitaryPassportRequired": random.choice([True, False]),
            "isSanitaryBookRequired": random.choice([True, False]),
            "requiredDocuments": [1010, 1020, 1030, 2010, 2020, 2030],
            "route": [
                {
                    "loadingType": 1,
                    "position": 1,
                    "point": departure_point,
                    "isLoadingWork": True,
                    "isUnloadingWork": False
                },
                {
                    "loadingType": 1,
                    "position": 2,
                    "point": arrival_point,
                    "isLoadingWork": False,
                    "isUnloadingWork": True
                }
            ]
        },
        "responsibleEmployees": [],
        "comment": comment,
        "clientIdentifier": generate_combined_client_id(),
        "innerComment": comment,
        "toStartAtFrom": to_start_at_from,
        "toStartAtTill": None,
        "departurePoint": departure_point,
        "arrivalPoint": arrival_point,
        "cargoPlaces": [],
        "newCargoPlaces": [
            {
                "volume": volume,
                "title": fake.word() + " с продуктами",
                "cost": random.randint(1000000, 10000000),
                "departurePoint": departure_point,
                "arrivalPoint": arrival_point,
                "quantity": quantity,
                "weight": weight,
                "type": "pallet"
            }
        ],
        "additionalServices": [],
        "parametersForProducers": {
            "shares": shares,
            "selectingStrategy": "rate"
        }
    }

    return flight_data
