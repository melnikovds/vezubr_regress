import time
import allure
import pytest

from pages.login import base_password
from pages.registration_page import Registration, MailTmAPI
from pages.login_page import Login


# ==================== ТЕСТЫ ПО ССЫЛКАМ ====================

@allure.story("Smoke test")
@allure.feature('Регистрация личного кабинета')
@allure.description('Тест регистрации личного кабинета Грузовладельца: регистрация - По ссылке Экспедитора')
@pytest.mark.parametrize('base_fixture', ['via_link'], indirect=True)
def test_registration_new_lkz_with_email1(base_fixture, domain):
    base, login = base_fixture
    mail_api = MailTmAPI()
    reg = Registration(base.driver)

    with allure.step("Создание временного почтового ящика"):
        temp_email = reg.create_temp_email(mail_api)

    with allure.step("Переход на страницу регистрации"):
        reg.click_button(reg.registration_new_account)
        reg.click_button(reg.client_button)

    with allure.step("Заполнение формы регистрации"):
        reg.fill_registration_form(temp_email, "ГВ", "Регресс")

    with allure.step("Подтверждение email"):
        reg.confirm_email(mail_api)

    with allure.step("Вход в личный кабинет"):
        reg.login_to_lk(login, temp_email, base_password["password"])

    print(f"\n Тест успешно завершен! Пользователь {temp_email} успешно зарегистрирован")


@allure.story("Smoke test")
@allure.feature('Регистрация личного кабинета')
@allure.description('Тест регистрации личного кабинета Перевозчика: регистрация - По ссылке Экспедитора')
@pytest.mark.parametrize('base_fixture', ['via_link'], indirect=True)
def test_registration_new_lkp_by_expeditor_link(base_fixture, domain):
    base, login = base_fixture
    mail_api = MailTmAPI()
    reg = Registration(base.driver)

    with allure.step("Создание временного почтового ящика"):
        temp_email = reg.create_temp_email(mail_api)

    with allure.step("Переход на страницу регистрации"):
        reg.click_button(reg.registration_new_account)
        reg.click_button(reg.producer_button)

    with allure.step("Заполнение формы регистрации"):
        reg.fill_registration_form(temp_email, "ПВ", "Регресс")

    with allure.step("Подтверждение email"):
        reg.confirm_email(mail_api)

    with allure.step("Вход в личный кабинет"):
        reg.login_to_lk(login, temp_email, base_password["password"])

    print(f"\n Тест успешно завершен! Перевозчик {temp_email} успешно зарегистрирован")


@allure.story("Smoke test")
@allure.feature('Регистрация личного кабинета')
@allure.description('Тест регистрации личного кабинета Перевозчика: регистрация - По ссылке от Грузовладельца')
@pytest.mark.parametrize('base_fixture', ['via_link'], indirect=True)
def test_registration_new_lkp_by_lkz_link(base_fixture, domain):
    base, login = base_fixture
    mail_api = MailTmAPI()
    reg = Registration(base.driver)

    with allure.step("Создание временного почтового ящика"):
        temp_email = reg.create_temp_email(mail_api)

    with allure.step("Переход по ссылке от Грузовладельца"):
        correct_url = "https://enter.vezubr.com/contour-join?contourCode=7ZqGz8CXcc"
        base.driver.get(correct_url)
        time.sleep(3)
        base.get_current_url()
        base.driver.maximize_window()
        time.sleep(2)

    with allure.step("Выбор роли Перевозчик"):
        reg.click_button(reg.register_new_lk_button)
        time.sleep(1)
        reg.click_button(reg.lkp_button_by_link)
        time.sleep(2)

    with allure.step("Заполнение формы регистрации"):
        reg.fill_registration_form(temp_email, "ПВ", "Регресс")

    with allure.step("Подтверждение email"):
        reg.confirm_email(mail_api)

    with allure.step("Вход в личный кабинет"):
        reg.login_to_lk(login, temp_email, base_password["password"])

    print(f"\n Тест успешно завершен! Перевозчик {temp_email} успешно зарегистрирован")


# ==================== ТЕСТЫ ПРОСТОЙ РЕГИСТРАЦИИ ====================

@allure.story("Smoke test")
@allure.feature('Регистрация личного кабинета')
@allure.description('Тест простой регистрации личного кабинета Грузовладельца')
@pytest.mark.parametrize('base_fixture', ['without_login'], indirect=True)
def test_simple_registration_new_lkz_with_email(base_fixture, domain):
    base, login = base_fixture
    mail_api = MailTmAPI()
    reg = Registration(base.driver)

    with allure.step("Переход на сайт enter.vezubr.com"):
        base.driver.get("https://enter.vezubr.com/")
        time.sleep(2)

    with allure.step("Нажатие на кнопку регистрации и выбор роли"):
        reg.click_button(reg.simple_registration_button)
        time.sleep(1)
        reg.click_button(reg.simple_lkz_button)
        time.sleep(2)

    with allure.step("Создание временного почтового ящика"):
        temp_email = reg.create_temp_email(mail_api)

    with allure.step("Заполнение формы регистрации"):
        reg.fill_registration_form(temp_email, "Тест", "Пользователь")

    with allure.step("Подтверждение email"):
        reg.confirm_email(mail_api)

    with allure.step("Вход в личный кабинет"):
        reg.login_to_lk(login, temp_email, base_password["password"])

    print(f"\n Тест успешно завершен! Пользователь {temp_email} успешно зарегистрирован")


@allure.story("Smoke test")
@allure.feature('Регистрация личного кабинета')
@allure.description('Тест простой регистрации личного кабинета Экспедитора (ЛКЭ)')
@pytest.mark.parametrize('base_fixture', ['without_login'], indirect=True)
def test_simple_registration_new_lke_with_email(base_fixture, domain):
    base, login = base_fixture
    mail_api = MailTmAPI()
    reg = Registration(base.driver)

    with allure.step("Переход на сайт enter.vezubr.com"):
        base.driver.get("https://enter.vezubr.com/")
        time.sleep(2)

    with allure.step("Нажатие на кнопку регистрации и выбор роли"):
        reg.click_button(reg.simple_registration_button)
        time.sleep(1)
        reg.click_button(reg.simple_lke_button)
        time.sleep(2)

    with allure.step("Создание временного почтового ящика"):
        temp_email = reg.create_temp_email(mail_api)

    with allure.step("Заполнение формы регистрации"):
        reg.fill_registration_form(temp_email, "Экспедитор", "Тестовый")

    with allure.step("Подтверждение email"):
        reg.confirm_email(mail_api)

    with allure.step("Вход в личный кабинет"):
        reg.login_to_lk(login, temp_email, base_password["password"])

    print(f"\n Тест успешно завершен! Экспедитор {temp_email} успешно зарегистрирован")


@allure.story("Smoke test")
@allure.feature('Регистрация личного кабинета')
@allure.description('Тест простой регистрации личного кабинета Перевозчика (ЛКП)')
@pytest.mark.parametrize('base_fixture', ['without_login'], indirect=True)
def test_simple_registration_new_lkp_with_email(base_fixture, domain):
    base, login = base_fixture
    mail_api = MailTmAPI()
    reg = Registration(base.driver)

    with allure.step("Переход на сайт enter.vezubr.com"):
        base.driver.get("https://enter.vezubr.com/")
        time.sleep(2)

    with allure.step("Нажатие на кнопку регистрации и выбор роли"):
        reg.click_button(reg.simple_registration_button)
        time.sleep(1)
        reg.click_button(reg.simple_lkp_button)
        time.sleep(2)

    with allure.step("Создание временного почтового ящика"):
        temp_email = reg.create_temp_email(mail_api)

    with allure.step("Заполнение формы регистрации"):
        reg.fill_registration_form(temp_email, "Перевозчик", "Тестовый")

    with allure.step("Подтверждение email"):
        reg.confirm_email(mail_api)

    with allure.step("Вход в личный кабинет"):
        reg.login_to_lk(login, temp_email, base_password["password"])

    print(f"\n Тест успешно завершен! Перевозчик {temp_email} успешно зарегистрирован")


# ==================== ТЕСТЫ ВОССТАНОВЛЕНИЯ ПАРОЛЯ ====================

@allure.story("Smoke test")
@allure.feature('Восстановление пароля')
@allure.description('Тест восстановления пароля для Грузовладельца (ЛКЗ)')
@pytest.mark.parametrize('base_fixture', ['without_login'], indirect=True)
def test_reset_password_lkz(base_fixture, domain):
    base, login = base_fixture
    mail_api = MailTmAPI()
    reg = Registration(base.driver)
    new_password = "NewTestPass123!"

    with allure.step("Регистрация нового пользователя"):
        base.driver.get("https://enter.vezubr.com/")
        time.sleep(2)
        reg.click_button(reg.simple_registration_button)
        time.sleep(1)
        reg.click_button(reg.simple_lkz_button)
        time.sleep(2)
        temp_email = reg.create_temp_email(mail_api)
        reg.fill_registration_form(temp_email, "Тест", "Пользователь")
        reg.confirm_email(mail_api)

    with allure.step("Вход и выход из ЛК"):
        sidebar = reg.login_to_lk(login, temp_email, base_password["password"])
        reg.logout_from_lk(sidebar)

    with allure.step("Восстановление пароля"):
        reg.reset_password_request(login, temp_email)

    with allure.step("Установка нового пароля"):
        reset_url = reg.extract_reset_link_from_email(mail_api)
        base.driver.get(reset_url)
        time.sleep(3)
        reg.set_new_password(new_password)

    with allure.step("Вход с новым паролем"):
        reg.login_to_lk(login, temp_email, new_password)

    print(f"\n Тест успешно завершен! Аккаунт {temp_email} создан, пароль успешно сброшен")


@allure.story("Smoke test")
@allure.feature('Восстановление пароля')
@allure.description('Тест восстановления пароля для Экспедитора (ЛКЭ)')
@pytest.mark.parametrize('base_fixture', ['without_login'], indirect=True)
def test_reset_password_lke(base_fixture, domain):
    base, login = base_fixture
    mail_api = MailTmAPI()
    reg = Registration(base.driver)
    new_password = "NewTestPass123!"

    with allure.step("Регистрация нового пользователя"):
        base.driver.get("https://enter.vezubr.com/")
        time.sleep(2)
        reg.click_button(reg.simple_registration_button)
        time.sleep(1)
        reg.click_button(reg.simple_lke_button)
        time.sleep(2)
        temp_email = reg.create_temp_email(mail_api)
        reg.fill_registration_form(temp_email, "Экспедитор", "Тестовый")
        reg.confirm_email(mail_api)

    with allure.step("Вход и выход из ЛК"):
        sidebar = reg.login_to_lk(login, temp_email, base_password["password"])
        reg.logout_from_lk(sidebar)

    with allure.step("Восстановление пароля"):
        reg.reset_password_request(login, temp_email)

    with allure.step("Установка нового пароля"):
        reset_url = reg.extract_reset_link_from_email(mail_api)
        base.driver.get(reset_url)
        time.sleep(3)
        reg.set_new_password(new_password)

    with allure.step("Вход с новым паролем"):
        reg.login_to_lk(login, temp_email, new_password)

    print(f"\n Тест успешно завершен! Аккаунт {temp_email} создан, пароль успешно сброшен")


@allure.story("Smoke test")
@allure.feature('Восстановление пароля')
@allure.description('Тест восстановления пароля для Перевозчика (ЛКП)')
@pytest.mark.parametrize('base_fixture', ['without_login'], indirect=True)
def test_reset_password_lkp(base_fixture, domain):
    base, login = base_fixture
    mail_api = MailTmAPI()
    reg = Registration(base.driver)
    new_password = "NewTestPass123!"

    with allure.step("Регистрация нового пользователя"):
        base.driver.get("https://enter.vezubr.com/")
        time.sleep(2)
        reg.click_button(reg.simple_registration_button)
        time.sleep(1)
        reg.click_button(reg.simple_lkp_button)
        time.sleep(2)
        temp_email = reg.create_temp_email(mail_api)
        reg.fill_registration_form(temp_email, "Перевозчик", "Тестовый")
        reg.confirm_email(mail_api)

    with allure.step("Вход и выход из ЛК"):
        sidebar = reg.login_to_lk(login, temp_email, base_password["password"])
        reg.logout_from_lk(sidebar)

    with allure.step("Восстановление пароля"):
        reg.reset_password_request(login, temp_email)

    with allure.step("Установка нового пароля"):
        reset_url = reg.extract_reset_link_from_email(mail_api)
        base.driver.get(reset_url)
        time.sleep(3)
        reg.set_new_password(new_password)

    with allure.step("Вход с новым паролем"):
        reg.login_to_lk(login, temp_email, new_password)

    print(f"\n Тест успешно завершен! Аккаунт {temp_email} создан, пароль успешно сброшен")
