# VezubrWebAuto

Проект автоматизации тестирования Web приложения

общее количество тестов - 350

python -m pytest -s -v        # запуск всех тестов     
pytest -m smoke --domain=ru   # запуск быстрых тестов прода   
pytest -m smoke --domain=ru --collect-only -q  # список тестов