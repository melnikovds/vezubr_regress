import allure
import pytest
import requests
import time
from pages.generator_old_ftl_page import GeneratorFTL
from pages.login import accounts
from tests.base_test import base_test_with_login, base_test_without_login, base_test_with_login_via_link


def pytest_addoption(parser):
    parser.addoption("--domain", choices=['dev', 'com', 'ru'], action="store", default="com",
                     help="Set the domain for tests")


# Фикстура для базового URL API на основе домена
@pytest.fixture
def api_base_url(domain):
    return f"https://api.vezubr.{domain}/v1/api"


@pytest.fixture
def api_login(api_base_url):
    def _login(role: str):
        if role not in accounts:
            raise KeyError(f"Role '{role}' not found in accounts")
        
        login_url = f"{api_base_url}/user/login"
        payload = {
            "username": accounts[role]["email"],
            "password": accounts[role]["password"]
        }
        
        # Отправляем запрос на логин
        response = requests.post(login_url, json=payload)
        assert response.status_code == 200, f"Login failed for role {role}"
        
        # Получаем токен
        token = response.json().get("token")
        
        # Выводим сообщение о получении токена в консоль
        print(f"Token received for role '{role}'")
        
        # Логируем получение токена в Allure
        with allure.step(f"Token received for role '{role}'"):
            pass  # Шаг отображается в Allure, но без токена
        
        return token
    
    return _login


@pytest.fixture
def domain(request):
    return request.config.getoption("--domain")


@pytest.fixture
def base_fixture(request, domain):
    # Проверяем, используется ли отчет Allure
    allure_dir = request.config.getoption("--alluredir", default=None)
    
    # Получаем параметр из теста, который определяет тип теста и роль
    role = request.param
    
    # Логика для выбора базового теста
    if role == 'without_login':
        base, login = base_test_without_login(domain)
        base.allure_dir = allure_dir  # Устанавливаем директорию в base, если используется Allure
        yield base, login
    elif role == 'via_link':
        base, login = base_test_with_login_via_link(domain)
        base.allure_dir = allure_dir
        yield base, login
    else:
        base, sidebar = base_test_with_login(domain, role)
        base.allure_dir = allure_dir
        yield base, sidebar
    
    # Завершаем сессию драйвера после выполнения теста
    base.test_finish()


# Хук для сохранения скриншота в случае провала теста
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Вызов теста и получение его результата
    outcome = yield
    report = outcome.get_result()
    
    # Получаем кортеж (base, sidebar) через фикстуру
    base_fixture = item.funcargs.get('base_fixture', None)
    
    if base_fixture:
        base, _ = base_fixture  # Извлекаем base из кортежа
        
        # Если тест завершился с ошибкой и base доступен
        if report.when == "call" and report.failed and base:
            # Получаем имя теста
            test_name = item.nodeid.replace("::", "_").replace("/", "_")
            base.get_screenshot(test_name)  # Передаем имя теста в метод скриншота


@pytest.fixture(scope="session")
def create_entities(api_base_url, api_login):
    generator = GeneratorFTL(api_base_url, api_login)

    entity_creators = [
        generator.create_entity_type_a_lkz,
        generator.create_entity_type_b_lkz,
        generator.create_entity_type_c_lkz,
        generator.create_entity_type_d_lkz,
        generator.create_entity_type_e_lkz
    ]

    entity_results = []
    for creator in entity_creators:
        result = creator()
        if result:
            entity_results.append(result)
        else:
            entity_results.append({})  # Если ошибка, добавляем пустой словарь
        time.sleep(5)

    lkz_a_one = entity_results[0].get("requestNr")
    lkz_a_two = entity_results[0].get("date_create")
    lkz_a_three = entity_results[0].get("toStartAtDate")
    lkz_a_four = entity_results[0].get("clientNumber")

    lkz_b_one = entity_results[1].get("requestNr")
    lkz_b_two = entity_results[1].get("date_create")
    lkz_b_three = entity_results[1].get("toStartAtDate")
    lkz_b_four = entity_results[1].get("clientNumber")

    lkz_c_one = entity_results[2].get("requestNr")
    lkz_c_two = entity_results[2].get("date_create")
    lkz_c_three = entity_results[2].get("toStartAtDate")
    lkz_c_four = entity_results[2].get("clientNumber")

    lkz_d_one = entity_results[3].get("requestNr")
    lkz_d_two = entity_results[3].get("date_create")
    lkz_d_three = entity_results[3].get("toStartAtDate")
    lkz_d_four = entity_results[3].get("clientNumber")

    lkz_e_one = entity_results[4].get("requestNr")
    lkz_e_two = entity_results[4].get("date_create")
    lkz_e_three = entity_results[4].get("toStartAtDate")
    lkz_e_four = entity_results[4].get("clientNumber")

    return locals()
