# Простое создание задания НАДО БУДЕТ УДАЛИТЬ ПОСЛЕ ВСЕХ ТЕСТОВ
from api_pages.create_entities import CreateEntities

# Для создания заданий используем роль lkz
creator = CreateEntities(role='lkz')

# Создаем задание
task = creator.create_task(
    departure_point_id=28754,
    arrival_point_id=28756,
    title_prefix="Мой тест"
)

print(f"Задание создано: ID={task['id']}, Номер={task['task_number']}")