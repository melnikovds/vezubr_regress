from base.base_class import Base
from pages.login_page import Login
from pages.sidebar import SideBar


def base_test_with_login(domain, role):
    base = Base.get_driver()

    login = Login(base.driver, domain)
    login.authorization(role)

    sidebar = SideBar(base.driver)
    sidebar.click_button(sidebar.sidebar_button)

    return base, sidebar


def base_test_without_login(domain):
    base = Base.get_driver()

    login = Login(base.driver, domain)
    login.registration_start()

    return base, login


def base_test_with_login_via_link(domain):
    base = Base.get_driver()

    login = Login(base.driver, domain)
    login.registration_via_link(domain)

    return base, login

def base_test_with_login_download(domain, role):
    """
    Создает драйвер с настройками скачивания, логинится и возвращает base и sidebar.
    Используется ТОЛЬКО для тестов с прямой выгрузкой файлов.
    """
    from pages.login_page import Login
    from pages.sidebar import SideBar
    from pages.login import accounts
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import time

    # Создаем драйвер с настройками скачивания
    base = Base.get_driver_with_download()

    # Логинимся (как в base_test_with_login)
    login_url = f"https://enter.vezubr.{domain}/login"
    base.driver.get(login_url)

    login_page = Login(base.driver, domain)
    login_page.input_in_field(login_page.user_email_input, accounts[role]["email"])
    login_page.input_in_field(login_page.password_input, accounts[role]["password"])
    login_page.click_button(login_page.login_button)

    # Ждем загрузки sidebar (как в base_test_with_login)
    sidebar = SideBar(base.driver)
    WebDriverWait(base.driver, 60).until(
        EC.visibility_of_element_located((By.XPATH, sidebar.sidebar_button["xpath"]))
    )
    time.sleep(2)

    return base, sidebar