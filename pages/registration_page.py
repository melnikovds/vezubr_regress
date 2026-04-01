import time
from typing import NoReturn
import allure
from base.base_class import Base
import random
import re
import requests
from faker import Faker

from pages.sidebar import SideBar


class MailTmAPI:
    """Класс для работы с API mail.tm"""

    BASE_URL = "https://api.mail.tm"

    def __init__(self):
        self.session = requests.Session()
        self.email = None
        self.password = None
        self.token = None
        self.account_id = None

    def get_domains(self, page=1):
        """Получение списка доступных доменов"""
        response = self.session.get(
            f"{self.BASE_URL}/domains",
            params={"page": page}
        )
        response.raise_for_status()
        return response.json()

    def create_account(self, max_retries=3):
        """Создание временного почтового ящика с повторными попытками"""
        for attempt in range(max_retries):
            try:
                # Получаем доступные домены
                domains_data = self.get_domains()
                domains = domains_data['hydra:member']

                if not domains:
                    raise Exception("No available domains")

                # Берем первый активный домен
                domain = domains[0]['domain']

                # Генерируем случайный адрес с timestamp для уникальности
                fake = Faker()
                username = fake.user_name()
                username = re.sub(r'[^a-zA-Z0-9._-]', '', username)
                timestamp = int(time.time())
                self.email = f"{username}_{timestamp}@{domain}"
                self.password = fake.password(length=12)

                # Создаем аккаунт
                account_data = {
                    "address": self.email,
                    "password": self.password
                }

                response = self.session.post(
                    f"{self.BASE_URL}/accounts",
                    json=account_data
                )

                if response.status_code == 429:
                    wait_time = (attempt + 1) * 3
                    print(f"Rate limited (429), waiting {wait_time} seconds...")
                    time.sleep(wait_time)
                    continue

                if response.status_code == 422:
                    print(f"Email {self.email} already exists, retrying...")
                    time.sleep(1)
                    continue

                response.raise_for_status()
                self.account_data = response.json()
                self.account_id = self.account_data.get('id')

                # Получаем токен
                token_response = self.session.post(
                    f"{self.BASE_URL}/token",
                    json=account_data
                )

                if token_response.status_code == 429:
                    wait_time = (attempt + 1) * 3
                    print(f"Rate limited (429) on token, waiting {wait_time} seconds...")
                    time.sleep(wait_time)
                    continue

                token_response.raise_for_status()
                token_data = token_response.json()
                self.token = token_data['token']

                # Устанавливаем заголовки авторизации
                self.session.headers.update({
                    'Authorization': f'Bearer {self.token}',
                    'Content-Type': 'application/json'
                })

                return self.email

            except Exception as e:
                if attempt == max_retries - 1:
                    raise
                print(f"Attempt {attempt + 1} failed: {e}, retrying...")
                time.sleep(2)

    def get_messages(self, page=1):
        """Получение списка сообщений"""
        response = self.session.get(
            f"{self.BASE_URL}/messages",
            params={"page": page}
        )
        response.raise_for_status()
        return response.json()

    def get_message_by_id(self, message_id):
        """Получение полного сообщения по ID"""
        response = self.session.get(f"{self.BASE_URL}/messages/{message_id}")
        response.raise_for_status()
        return response.json()

    def wait_for_message(self, timeout=60, interval=2):
        """Ожидание письма (берет первое письмо из ящика)"""
        start_time = time.time()

        while time.time() - start_time < timeout:
            try:
                messages_data = self.get_messages()
                messages = messages_data.get('hydra:member', [])
                total_items = messages_data.get('hydra:totalItems', 0)

                print(f"Проверка сообщений: найдено {total_items} писем")

                if total_items > 0:
                    # Берем первое (самое новое) сообщение
                    message = messages[0]
                    # Получаем полное содержимое сообщения
                    full_message = self.get_message_by_id(message['id'])
                    print(f"Получено сообщение: {full_message.get('subject')}")
                    return full_message

            except Exception as e:
                print(f"Error checking messages: {e}")

            time.sleep(interval)

        raise TimeoutError(f"No message received within {timeout} seconds")

    def wait_for_second_message(self, timeout=60, interval=2):
        """Ожидание второго письма (после подтверждения регистрации)"""
        start_time = time.time()
        initial_count = 1  # Первое письмо уже есть

        while time.time() - start_time < timeout:
            try:
                messages_data = self.get_messages()
                current_count = messages_data.get('hydra:totalItems', 0)

                print(f"Проверка сообщений: найдено {current_count} писем")

                if current_count > initial_count:
                    # Появилось новое письмо (второе)
                    messages = messages_data.get('hydra:member', [])
                    if messages:
                        # Берем первое (самое новое) сообщение - это и будет второе письмо
                        message = messages[0]
                        full_message = self.get_message_by_id(message['id'])
                        print(f"Получено второе письмо: {full_message.get('subject')}")
                        return full_message

            except Exception as e:
                print(f"Error checking messages: {e}")

            time.sleep(interval)

        raise TimeoutError(f"No second message received within {timeout} seconds")

    def extract_confirmation_code(self, message):
        """Извлечение кода подтверждения из письма"""
        # Получаем текст письма (может быть в html или text формате)
        text_content = message.get('text', '')
        html_content = message.get('html', [''])[0] if message.get('html') else ''
        subject = message.get('subject', '')

        # Объединяем все содержимое для поиска
        full_content = f"{subject} {text_content} {html_content}"

        allure.attach(
            f"Subject: {subject}\n"
            f"Text preview: {text_content[:500]}\n"
            f"HTML preview: {html_content[:500] if html_content else 'No HTML'}",
            "Содержание письма",
            allure.attachment_type.TEXT
        )

        # Ищем 6-значный код подтверждения
        code_pattern = r'\b\d{6}\b'
        codes = re.findall(code_pattern, full_content)

        if codes:
            print(f"Найден код подтверждения: {codes[0]}")
            return codes[0]

        # Если код не найден, логируем все содержимое для отладки
        allure.attach(
            full_content,
            "Полное содержимое письма (код не найден)",
            allure.attachment_type.TEXT
        )

        raise Exception(f"Не удалось найти код подтверждения в письме. Содержимое: {full_content[:500]}")

    def extract_password_from_message(self, message):
        """Извлечение пароля из письма"""
        text_content = message.get('text', '')
        html_content = message.get('html', [''])[0] if message.get('html') else ''
        subject = message.get('subject', '')

        full_content = f"{subject} {text_content} {html_content}"

        allure.attach(
            f"Subject: {subject}\n"
            f"Text preview: {text_content[:500]}\n"
            f"HTML preview: {html_content[:500] if html_content else 'No HTML'}",
            "Содержание второго письма",
            allure.attachment_type.TEXT
        )

        # Ищем пароль в письме (обычно это комбинация букв и цифр)
        # Паттерн для поиска пароля: может быть от 6 до 20 символов, буквы и цифры
        password_pattern = r'(?:Пароль|Password)[:\s]+([a-zA-Z0-9]{6,20})'
        password_match = re.search(password_pattern, full_content, re.IGNORECASE)
        if password_match:
            password = password_match.group(1)
            print(f"Найден пароль: {password}")
            return password

        # Если не нашли по паттерну, ищем любую последовательность из 8-12 символов (буквы и цифры)
        fallback_pattern = r'\b([a-zA-Z0-9]{8,12})\b'
        passwords = re.findall(fallback_pattern, full_content)
        if passwords:
            # Берем первый найденный, который не похож на email
            for pwd in passwords:
                if '@' not in pwd and len(pwd) >= 6:
                    print(f"Найден возможный пароль: {pwd}")
                    return pwd

        raise Exception(f"Не удалось найти пароль в письме. Содержимое: {full_content[:500]}")


class Registration(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    sms_url = "https://cp.redsms.ru/"

    # Locators
    simple_registration_button = {
        "xpath": "(//button[@class='ant-btn wide margin-top-16 ant-btn-secondary'])[1]",
        "name": "simple_registration_button"
    }
    simple_lkz_button = {
        "xpath": "(//button[@type='button'])[1]",
        "name": "simple_lkz_button"
    }

    simple_lke_button = {
        "xpath": "(//button[@type='button'])[2]",
        "name": "simple_lke_button"
    }

    simple_lkp_button = {
        "xpath": "(//button[@type='button'])[3]",
        "name": "simple_lkp_button"
    }

    client_button = {
        "xpath": "//button[.//span[text()='Грузовладелец']]",
        "name": "client_button"
    }
    expeditor_button = {
        "xpath": "//button[.//span[text()='Экспедитор']]",
        "name": "expeditor_button"
    }
    producer_button = {
        "xpath": "//button[.//span[text()='Перевозчик']]",
        "name": "producer_button"
    }
    phone_input = {
        "xpath": "//input[@placeholder='+7 (___) ___-__-__']",
        "name": "phone_input"
    }
    privacy_policy_checkbox = {
        "xpath": "//label[@class='ant-checkbox-wrapper']",
        "name": "privacy_policy_checkbox"
    }
    get_code_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "get_code_button"
    }
    code_input = {
        "xpath": "//input[@class='ant-input']",
        "name": "code_input"
    }
    continue_button = {
        "xpath": "//button[.//span[text()='Продолжить']]",
        "name": "continue_button"
    }
    inn_input = {
        "xpath": "//input[@type='text']",
        "name": "inn_input"
    }
    email_input = {
        "xpath": "(//input[@type='text'])[3]",
        "name": "email_input"
    }
    user_name_input = {
        "xpath": "(//input[@type='text'])[5]",
        "name": "user_name_input"
    }
    user_surname_input = {
        "xpath": "(//input[@type='text'])[6]",
        "name": "user_surname_input"
    }
    password_input = {
        "xpath": "//input[@type='password']",
        "name": "password_input"
    }
    repeat_password_input = {
        "xpath": "(//input[@type='password'])[2]",
        "name": "repeat_password_input"
    }
    complete_button = {
        "xpath": "//button[.//span[text()='Завершить регистрацию']]",
        "name": "complete_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and contains(text(), 'Вы успешно')]",
        "reference": "Вы успешно зарегистрировались"
    }
    ok_button = {
        "xpath": "//div[@class='ant-modal-confirm-btns']//button[@type='button']",
        "name": "calendar_ok_button"
    }
    registration_new_account = {
        "xpath": "//button[.//span[contains(text(), 'Регистрация Нового')]]",
        "name": "registration_new_account"
    }
    confirmation_code_input = {

        'xpath': "(//input[@type='text'])[1]",
        'name': "Confirmation code input"
    }
    confirm_button = {

        'xpath': "(//button[@type='button'])[1]",
        'name': "Confirm button"
    }
    confirm_button_ok = {
        'xpath': "(//button[@class='ant-btn ant-btn-primary'])[1]",
        'name': "Confirm_button_ok"
    }
    register_new_lk_button = {
        "xpath": "(//button[@class='ant-btn ant-btn-secondary'])[1]",
        "name": "register_new_lk_button"
    }

    lkp_button_by_link = {
        "xpath": "(//button[@type='button'])[3]",
        "name": "lkp_button_by_link"
    }

    reset_password_link = {
        "xpath": "//a[contains(text(),'Восстановление пароля')]",
        "name": "reset_password_link"
    }

    reset_email_input = {
        "xpath": "(//input[@type='text'])[1]",
        "name": "reset_email_input"
    }

    reset_submit_button = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[1]",
        "name": "reset_submit_button"
    }

    reset_close_popup_button = {
        "xpath": "(//button[@type='button'])[4]",
        "name": "reset_close_popup_button"
    }
    new_password_input = {
        "xpath": "//input[@type='password']",
        "name": "new_password_input"
    }

    confirm_new_password_input = {
        "xpath": "(//input[@type='password'])[2]",
        "name": "confirm_new_password_input"
    }

    reset_password_confirm_button = {
        "xpath": "(//button[@type='button'])[1]",
        "name": "reset_password_confirm_button"
    }

    reset_password_success_popup_close = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[1]",
        "name": "reset_password_success_popup_close"
    }

    """ Assert text extraction by INN wait clickable"""

    def verify_text_by_inn(self, inn_value: str, reference_value: str, wait_type: str = 'located') -> NoReturn:
        """
        Проверяет наличие и соответствие конкретного текста для строки таблицы, содержащей заданный ИНН,
        с выбором типа ожидания элемента.

        Parameters
        ----------
        inn_value : str
            ИНН, используемый для поиска соответствующей строки в таблице.
        reference_value : str
            Ожидаемый текст для сравнения, который должен точно совпадать с текстом элемента.
        wait_type : str, optional
            Тип ожидания элемента ('clickable', 'visible', 'located', 'find').

        Raises
        ------
        AssertionError
            Если текст элемента не соответствует ожидаемому значению.
        """
        element_info = {
            "name": f"Text for INN {inn_value} matching '{reference_value}'",
            "xpath": f"//tr[.//a[contains(text(), '{inn_value}')]]//div[contains(text(), '{reference_value}')]"
        }
        element = self.get_element(element_info, wait_type=wait_type)['element']
        time.sleep(0.5)  # Фиксированная задержка
        value_word = element.text
        with allure.step(title=f"Assert \"{value_word}\" == \"{reference_value}\""):
            assert value_word == reference_value, f"Expected '{reference_value}', but found '{value_word}'."
            print(f"Assert \"{value_word}\" == \"{reference_value}\"")

    @staticmethod
    def generate_phone_number():
        # Выбираем префикс: либо "954", либо "955"
        prefix = random.choice(["954", "955"])

        # Генерируем 7 случайных цифр
        random_digits = ''.join(random.choices('0123456789', k=7))

        # Формируем полный номер телефона
        phone_number = prefix + random_digits

        return phone_number

    def create_temp_email(self, mail_api):
        """Создание временного почтового ящика"""
        temp_email = mail_api.create_account()
        allure.attach(temp_email, "Созданный email", allure.attachment_type.TEXT)
        allure.attach(mail_api.password, "Пароль от почты", allure.attachment_type.TEXT)
        assert mail_api.account_id is not None, "Не удалось создать почтовый ящик"
        print(f"\n✅ Почтовый ящик создан: {temp_email}")
        return temp_email

    def fill_registration_form(self, temp_email, first_name, last_name, password=None):
        """Заполнение формы регистрации"""
        if password is None:
            from pages.login import base_password
            password = base_password["password"]

        phone = self.generate_phone_number()
        self.input_in_field(self.phone_input, phone, click_first=True)
        self.click_button(self.privacy_policy_checkbox)
        self.input_in_field(self.email_input, temp_email)
        self.input_in_field(self.user_name_input, first_name)
        self.input_in_field(self.user_surname_input, last_name)
        self.input_in_field(self.password_input, password, safe=True)
        self.input_in_field(self.repeat_password_input, password, safe=True)
        inn = self.generate_inn("entity")
        self.input_in_field(self.inn_input, inn, click_first=True)
        self.click_button(self.complete_button, do_assert=True)
        print(f"✅ Форма регистрации отправлена")

        # Закрытие попапа об успешной регистрации
        try:
            self.click_button(self.ok_button)
            print(f"✅ Попап об успешной регистрации закрыт")
            time.sleep(2)
        except:
            print(f" Попап не появился или уже был закрыт")

        return inn

    def confirm_email(self, mail_api):
        """Подтверждение email через код из письма"""
        message = mail_api.wait_for_message(timeout=60)
        allure.attach(
            f"Subject: {message.get('subject', 'No subject')}",
            "Полученное письмо",
            allure.attachment_type.TEXT
        )
        confirmation_code = mail_api.extract_confirmation_code(message)
        allure.attach(confirmation_code, "Код подтверждения", allure.attachment_type.TEXT)
        self.input_in_field(self.confirmation_code_input, confirmation_code)
        self.click_button(self.confirm_button)
        print(f"✅ Код подтверждения введен")
        time.sleep(2)
        try:
            self.click_button(self.confirm_button_ok)
            print(f"✅ Email подтвержден")
        except:
            print(f" Окно подтверждения не появилось")

    def login_to_lk(self, login, email, password):
        """Вход в личный кабинет"""
        time.sleep(3)
        login.input_in_field(login.user_email_input, email, safe=True)
        login.input_in_field(login.password_input, password, safe=True)
        login.click_button(login.login_button)
        time.sleep(10)

        sidebar = SideBar(self.driver)
        try:
            sidebar.get_element(sidebar.sidebar_button, wait_type='visible')
            print(f"✅ Вход в ЛК выполнен")
            return sidebar
        except Exception as e:
            screenshot_path = self.driver.get_screenshot_as_file(
                f"screenshots/login_failed_{time.strftime('%Y%m%d_%H%M%S')}.png"
            )
            allure.attach.file(screenshot_path, "Screenshot on login failure", allure.attachment_type.PNG)
            raise AssertionError(f"Не удалось подтвердить вход в ЛК: {e}")

    def logout_from_lk(self, sidebar):
        """Выход из личного кабинета"""
        try:
            sidebar.click_button(sidebar.exit_button)
            print("✅ Выполнен выход из ЛК")
            time.sleep(3)
        except Exception as e:
            print(f"⚠️ Не удалось выйти из ЛК: {e}")

    def reset_password_request(self, login, email):
        """Запрос на восстановление пароля"""
        login.registration_start()
        time.sleep(2)
        login.click_button(login.reset_password_link)
        time.sleep(2)
        login.input_in_field(login.reset_email_input, email)
        time.sleep(1)
        login.click_button(login.reset_submit_button)
        time.sleep(2)
        login.click_button(login.reset_close_popup_button)
        time.sleep(2)

    def extract_reset_link_from_email(self, mail_api):
        """Извлечение ссылки для сброса пароля из письма"""
        reset_message = mail_api.wait_for_second_message(timeout=60)
        allure.attach(
            f"Subject: {reset_message.get('subject', 'No subject')}",
            "Письмо со ссылкой для сброса пароля",
            allure.attachment_type.TEXT
        )

        text_content = reset_message.get('text', '')
        html_content = reset_message.get('html', [''])[0] if reset_message.get('html') else ''
        full_content = f"{text_content} {html_content}"

        reset_link_pattern = r'https://enter\.vezubr\.(?:com|ru)/reset-password[^\s"\'>]+'
        reset_links = re.findall(reset_link_pattern, full_content)

        if not reset_links:
            reset_link_pattern = r'https://enter\.vezubr\.(?:com|ru)/[^\s"\'>]+?(?:reset|password)[^\s"\'>]+'
            reset_links = re.findall(reset_link_pattern, full_content, re.IGNORECASE)

        assert reset_links, "Не удалось найти ссылку для сброса пароля в письме"
        reset_url = reset_links[0]
        allure.attach(reset_url, "Ссылка для сброса пароля", allure.attachment_type.TEXT)
        return reset_url

    def set_new_password(self, new_password):
        """Установка нового пароля"""
        self.input_in_field(self.new_password_input, new_password)
        self.input_in_field(self.confirm_new_password_input, new_password)
        self.click_button(self.reset_password_confirm_button)
        print(f"✅ Установлен новый пароль: {new_password}")
        time.sleep(2)
        try:
            self.click_button(self.reset_password_success_popup_close)
            print("✅ Попап подтверждения закрыт")
            time.sleep(2)
        except:
            print(" Попап не появился или уже был закрыт")
