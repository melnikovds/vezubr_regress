import os
import signal
import subprocess
import sys

# Константы
ALLURE_RESULTS_DIR = "C:\\Users\\l2new\\PycharmProjects\\Vezubr_Autotests\\result_new"
ALLURE_REPORT_DIR = "C:\\Users\\l2new\\PycharmProjects\\Vezubr_Autotests\\allure-report"

os.chdir("C:\\Users\\l2new\\PycharmProjects\\Vezubr_Autotests")


def signal_handler(sig, frame):
    """
    Обработчик сигнала Ctrl+C.
    """
    print("\nВыполнение тестов прервано пользователем.")
    generate_allure_report()
    sys.exit(0)


def run_tests():
    """
    Запускает тесты с использованием pytest и сохраняет результаты в Allure.
    """
    print("Запуск тестов...")
    pytest_command = f"pytest -s -v --alluredir={ALLURE_RESULTS_DIR}"
    try:
        # Запуск pytest
        pytest_result = subprocess.run(pytest_command, shell=True)
        if pytest_result.returncode != 0:
            print("Некоторые тесты завершились с ошибками, но выполнение продолжается.")
    except Exception as e:
        print(f"Ошибка при запуске тестов: {e}")
        sys.exit(1)


def generate_allure_report():
    """
    Генерирует отчет Allure из результатов тестов.
    """
    print("Генерация отчета...")
    if not os.path.exists(ALLURE_RESULTS_DIR) or not os.listdir(ALLURE_RESULTS_DIR):
        print("Нет данных для генерации отчета.")
        return

    allure_generate_command = f"allure generate {ALLURE_RESULTS_DIR} -o {ALLURE_REPORT_DIR} --clean"
    try:
        # Генерация отчета
        subprocess.run(allure_generate_command, shell=True, check=True)
        print("Отчет успешно сгенерирован.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при генерации отчета: {e}")
        sys.exit(1)


def open_allure_report():
    """
    Открывает сгенерированный отчет Allure в браузере.
    """
    print("Открытие отчета...")
    if not os.path.exists(ALLURE_REPORT_DIR):
        print("Отчет не найден. Возможно, генерация отчета завершилась с ошибкой.")
        return

    allure_open_command = f"allure open {ALLURE_REPORT_DIR}"
    try:
        # Открытие отчета
        subprocess.run(allure_open_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при открытии отчета: {e}")


if __name__ == "__main__":
    # Регистрация обработчика сигнала Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    # 1. Запуск тестов
    run_tests()

    # 2. Генерация отчета
    generate_allure_report()

    # 3. Открытие отчета
    open_allure_report()
