import requests

def get_access_token():
    # URL для получения токена
    auth_url = "https://api.vezubr.com/v1/api/user/login"

    # Данные для аутентификации (логин и пароль)
    auth_payload = {
        "username": "auto@LKZ.com",  # Замените на ваш логин
        "password": "auto@LKZ.com"   # Замените на ваш пароль
    }

    # Заголовки для запроса
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    try:
        # Отправка POST-запроса для получения токена
        response = requests.post(auth_url, headers=headers, json=auth_payload)

        # Проверка статуса ответа
        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data.get("token")  # Извлекаем токен из ответа
            if access_token:
                return access_token
            else:
                raise ValueError("Токен не найден в ответе сервера.")
        else:
            # Если статус-код не 200, выводим ошибку
            error_message = f"Ошибка при получении токена. Код ошибки: {response.status_code}, Сообщение: {response.text}"
            raise Exception(error_message)
    except Exception as e:
        # Обработка исключений
        print(f"Произошла ошибка при получении токена: {str(e)}")
        raise