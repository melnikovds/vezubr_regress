# tests/conftest_api.py
import pytest
from api_pages.client import APIClient
from api_pages.task import TaskAPI
from api_pages.create_entities import CreateEntities
from typing import Dict
import os

# ============= КОНФИГУРАЦИЯ =============
# ID точек отправления/назначения (можно через переменные окружения)
API_POINTS_CONFIG = {
    'lkz': {
        'departure_point_id': int(os.getenv('LKZ_DEPARTURE_POINT_ID', 28754)),
        'arrival_point_id': int(os.getenv('LKZ_ARRIVAL_POINT_ID', 28756))
    },
    'lke': {
        'departure_point_id': int(os.getenv('LKE_DEPARTURE_POINT_ID', 28754)),
        'arrival_point_id': int(os.getenv('LKE_ARRIVAL_POINT_ID', 28756))
    }
}


# ============= БАЗОВЫЕ API ФИКСТУРЫ =============

@pytest.fixture
def api_client_lkz() -> APIClient:
    """API клиент для роли LKZ"""
    client = APIClient(role='lkz')
    yield client
    client.session.close()


@pytest.fixture
def api_client_lke() -> APIClient:
    """API клиент для роли LKE"""
    client = APIClient(role='lke')
    yield client
    client.session.close()


@pytest.fixture
def task_api_lkz(api_client_lkz) -> TaskAPI:
    """Task API для LKZ"""
    return TaskAPI(api_client_lkz)


@pytest.fixture
def task_api_lke(api_client_lke) -> TaskAPI:
    """Task API для LKE"""
    return TaskAPI(api_client_lke)


@pytest.fixture
def create_entities_lkz() -> CreateEntities:
    """CreateEntities для роли LKZ"""
    return CreateEntities(role='lkz')


@pytest.fixture
def create_entities_lke() -> CreateEntities:
    """CreateEntities для роли LKE"""
    return CreateEntities(role='lke')


# ============= ФИКСТУРЫ ДЛЯ СОЗДАНИЯ ЗАДАНИЙ =============

@pytest.fixture
def created_task_lkz(create_entities_lkz) -> Dict:
    """
    Создает задание через API для LKZ перед тестом
    Возвращает созданное задание
    """
    config = API_POINTS_CONFIG['lkz']
    task = create_entities_lkz.create_task(
        departure_point_id=config['departure_point_id'],
        arrival_point_id=config['arrival_point_id'],
        title_prefix="Автотест_API",
        use_dates=False
    )
    yield task

    # Очистка после теста (опционально, раскомментировать если нужно)
    # try:
    #     task_id = task.get('id')
    #     if task_id:
    #         create_entities_lkz.client.delete(f"/v1/api/shipment/tasks/{task_id}")
    #         print(f"🗑️ Задание {task_id} удалено")
    # except Exception as e:
    #     print(f"⚠️ Ошибка при удалении задания: {e}")


@pytest.fixture
def created_task_lke(create_entities_lke) -> Dict:
    """Создает задание через API для LKE перед тестом"""
    config = API_POINTS_CONFIG['lke']
    task = create_entities_lke.create_task(
        departure_point_id=config['departure_point_id'],
        arrival_point_id=config['arrival_point_id'],
        title_prefix="Автотест_API",
        use_dates=False
    )
    yield task


@pytest.fixture
def task_number_lkz(created_task_lkz) -> str:
    """Возвращает только номер задания для LKZ"""
    return created_task_lkz.get('task_number') or created_task_lkz.get('number')


@pytest.fixture
def task_number_lke(created_task_lke) -> str:
    """Возвращает только номер задания для LKE"""
    return created_task_lke.get('task_number') or created_task_lke.get('number')


# ============= ПАРАМЕТРИЗИРОВАННЫЕ ФИКСТУРЫ =============

@pytest.fixture
def api_client(request):
    """
    Универсальный API клиент с указанием роли через параметр
    Использование: @pytest.mark.parametrize('api_client', ['lkz'], indirect=True)
    """
    role = request.param if hasattr(request, 'param') else 'lkz'
    client = APIClient(role=role)
    yield client
    client.session.close()


@pytest.fixture
def create_entities(request):
    """
    Универсальный CreateEntities с указанием роли через параметр
    Использование: @pytest.mark.parametrize('create_entities', ['lkz'], indirect=True)
    """
    role = request.param if hasattr(request, 'param') else 'lkz'
    return CreateEntities(role=role)


@pytest.fixture
def created_task(request, create_entities):
    """
    Универсальная фикстура создания задания
    Можно передать параметры:
    @pytest.mark.parametrize('created_task', [{'role': 'lkz', 'prefix': 'Test'}], indirect=True)
    """
    params = request.param if hasattr(request, 'param') else {}
    role = params.get('role', 'lkz')
    prefix = params.get('prefix', 'Автотест')

    # Создаем свой экземпляр CreateEntities для указанной роли
    entities = CreateEntities(role=role)

    config = API_POINTS_CONFIG.get(role, API_POINTS_CONFIG['lkz'])
    task = entities.create_task(
        departure_point_id=config['departure_point_id'],
        arrival_point_id=config['arrival_point_id'],
        title_prefix=prefix,
        use_dates=params.get('use_dates', False)
    )
    yield task