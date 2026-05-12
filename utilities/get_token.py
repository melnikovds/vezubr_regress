import requests
import time
from typing import Dict

class TokenManager:
    """Менеджер токенов для внутреннего API vezubr"""

    _tokens = {}   # role -> чистый JWT токен (eyJ...)

    ROLES = {
        'lkz': {
            'username': 'auto@LKZ.com',
            'password': 'auto@LKZ.com',
            'producer_id': 2448,
            'role_name': 'Клиент',
            'can_create_driver': False
        },
        'lke': {
            'username': 'auto@LKE.com',
            'password': 'auto@LKE.com',
            'producer_id': 2447,
            'role_name': 'Экспедитор',
            'can_create_driver': True
        },
        'lkp': {
            'username': 'auto@LKP.com',
            'password': 'auto@LKP.com',
            'producer_id': 2449,
            'role_name': 'Продюсер',
            'can_create_driver': True
        }
    }

    AUTH_URL = "https://api.vezubr.com/v1/api/user/login"   # ← прод, у тебя был .com

    @classmethod
    def get_token(cls, role: str, force_refresh: bool = False) -> str:
        role = role.lower()
        if role not in cls.ROLES:
            raise ValueError(f"Неизвестная роль: {role}")

        if not force_refresh and role in cls._tokens:
            return cls._tokens[role]

        config = cls.ROLES[role]
        token = cls._login(config['username'], config['password'])
        cls._tokens[role] = token
        return token

    @classmethod
    def _login(cls, username: str, password: str) -> str:
        """Логин и получение чистого токена (без префикса Bearer)"""
        payload = {"username": username, "password": password}

        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }

        for attempt in range(4):
            resp = requests.post(cls.AUTH_URL, headers=headers, json=payload, timeout=15)

            if resp.status_code == 200:
                data = resp.json()
                raw_token = data.get("token")

                if not raw_token:
                    raise ValueError("Поле 'token' отсутствует в ответе")

                # УБИРАЕМ ПРЕФИКС "Bearer ", если он есть
                clean_token = raw_token.replace("Bearer ", "").strip()

                print(
                    f"✅ Токен получен для {username} | Длина: {len(clean_token)} | Начинается с: {clean_token[:30]}...")
                return clean_token

            elif resp.status_code == 429:
                wait = (2 ** attempt) + 1
                print(f"⚠️ 429 Rate limit. Ждём {wait} сек...")
                time.sleep(wait)
                continue
            else:
                raise Exception(f"Login error {resp.status_code}: {resp.text[:300]}")

        raise Exception("Не удалось получить токен после нескольких попыток")

    @classmethod
    def get_producer_id(cls, role: str) -> int:
        return cls.ROLES[role.lower()]['producer_id']