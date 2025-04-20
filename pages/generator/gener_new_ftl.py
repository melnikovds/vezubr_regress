import json
import time

import requests
from pages.get_token import get_access_token  # Импортируем функцию получения токена
from pages.generator.flight_generator import generate_random_flight

# URL эндпоинта API
API_URL = "https://api.vezubr.com/v1/api/cargo-delivery-requests/create-and-publish"


def create_and_publish_flight():
    """
    Создает и публикует рейс через API.
    Выполняет все необходимые шаги: получение токена, генерацию данных рейса,
    отправку запроса и обработку ответа.
    """
    try:
        # Получение токена
        access_token = get_access_token()
        print("Токен успешно получен:", access_token)

        # Генерация данных рейса
        flight_data = generate_random_flight()

        # Создание заголовков
        headers = {
            "Content-Type": "application/json",
            "Authorization": access_token
        }

        # Отправка POST-запроса
        response = requests.post(API_URL, headers=headers, data=json.dumps(flight_data))

        # Проверка ответа
        if response.status_code in (200, 201):
            print("Рейс успешно создан!")
            print("Ответ сервера:", response.json())
        else:
            print(f"Ошибка при создании рейса. Код ошибки: {response.status_code}")
            print("Ответ сервера:", response.text)

    except Exception as e:
        print("Произошла ошибка:", str(e))


def create_multiple_flights(num_flights=1, interval=2):
    """
    Создает несколько рейсов с заданным интервалом между ними.

    :param num_flights: Количество рейсов для создания (по умолчанию 10).
    :param interval: Интервал между созданием рейсов в секундах (по умолчанию 2).
    """
    for i in range(num_flights):
        print(f"\nСоздание рейса {i + 1} из {num_flights}")
        create_and_publish_flight()

        # Добавляем задержку перед следующим вызовом (если это не последний рейс)
        if i < num_flights - 1:
            print(f"Ожидание {interval} секунд перед созданием следующего рейса...")
            time.sleep(interval)

    print("\nВсе рейсы были обработаны.")


# Пример использования
if __name__ == "__main__":
    create_multiple_flights()
