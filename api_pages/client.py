import requests
import allure
from typing import Dict, Any, Optional
from utilities.get_token import TokenManager


class APIClient:
    BASE_URL = "https://api.vezubr.com"

    def __init__(self, role: str = 'lkz'):
        self.role = role.lower()
        self.base_url = self.BASE_URL
        self.producer_id = TokenManager.get_producer_id(self.role)

        self.session = requests.Session()
        self.session.headers.update({
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

        self._refresh_token()          # первичное получение токена

    def _refresh_token(self, force_refresh: bool = False):
        """Обновляет токен и ставит заголовок"""
        token = TokenManager.get_token(self.role, force_refresh=force_refresh)
        # Самый надёжный способ записи заголовка
        self.session.headers['Authorization'] = f'Bearer {token}'

    def _request(self, method: str, endpoint: str, **kwargs) -> Dict:
        url = f"{self.base_url}{endpoint}"

        with allure.step(f"API {method.upper()} {endpoint} [{self.role.upper()}]"):

            # Принудительно обновляем токен ПЕРЕД каждым запросом
            self._refresh_token(force_refresh=True)

            # Добавляем заголовок вручную в этот конкретный запрос (для отладки)
            headers = kwargs.pop('headers', {})
            headers['Authorization'] = self.session.headers.get(
                'Authorization') or f"Bearer {TokenManager.get_token(self.role)}"
            kwargs['headers'] = headers

            response = self.session.request(method, url, **kwargs)

            # Логирование
            allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)
            if response.text:
                try:
                    import json
                    formatted = json.dumps(response.json(), indent=2, ensure_ascii=False)
                    allure.attach(formatted, name="Response Body", attachment_type=allure.attachment_type.JSON)
                except:
                    allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.TEXT)

            if response.status_code >= 400:
                raise Exception(f"API Error {response.status_code}: {response.text}")

            return response.json() if response.text else {}

    # Методы-хелперы
    def get(self, endpoint: str, params: Optional[Dict] = None):
        return self._request('GET', endpoint, params=params)

    def post(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None):
        return self._request('POST', endpoint, json=json or data)


