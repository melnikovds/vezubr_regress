from base.base_class import Base


class TopBar(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Delivery Monitor"""
    delivery_monitor_button = {
        "xpath": "//body/div[@id='main']/div[contains(@class,'dashboard')]/header[contains(@class,'flexbox top-nav')]/div[contains(@class,'flexbox size-1 top-nav__center justify-right')]/div[contains(@class,'top-nav__center-wrapper')]/div[@class='nav-group']/a[2]",
        "name": "delivery_monitor_button",
        "reference_xpath": "//li[@id='requestMonitor']",
        "reference": "МОНИТОРИНГ FTL ЗАЯВОК"
    }

    """New Requests"""
    new_order_hover = {
        "xpath": "//body/div[@id='main']/div[contains(@class,'dashboard')]/header[contains(@class,'flexbox top-nav')]/div[contains(@class,'flexbox size-1 top-nav__center justify-right')]/div[contains(@class,'top-nav__center-wrapper')]/div[contains(@class,'nav-group')]/a[1]",
        "name": "new_order_hover"
    }
    new_delivery_request_button = {
        "xpath": "//span[contains(@class,'text-big close-menu')][contains(text(),'Заявка на доставку груза')]",
        "name": "new_delivery_request_button",
        "reference_xpath": "//div[@class='order-form__title']",
        "reference": "Создание Заявки"
    }

    """Requests"""
    requests_hover = {
        "xpath": "//body/div[@id='main']/div[contains(@class,'dashboard')]/header[contains(@class,'flexbox top-nav')]/div[contains(@class,'flexbox size-1 top-nav__center justify-right')]/div[contains(@class,'top-nav__center-wrapper')]/div[contains(@class,'nav-group')]/a[3]",
        "name": "requests_hover"
    }
    cdr_active_list_button = {
        "xpath": "//span[contains(text(),'Заявки на доставку Груза')]",
        "name": "cdr_active_list_button",
        "reference_xpath": "//h2[contains(text(),'Заявки на доставку Груза')]",
        "reference": "Заявки на доставку Груза"
    }

    """Assignments"""
    assignments_hover = {
        "xpath": "//header[contains(@class,'flexbox top-nav')]//a[4]",
        "name": "assignments_hover"
    }
    assignments_hover_lkz = {
        "xpath": "//body/div[@id='main']/div[contains(@class,'dashboard')]/header[contains(@class,'flexbox top-nav')]/div[contains(@class,'flexbox size-1 top-nav__center justify-right')]/div[contains(@class,'top-nav__center-wrapper')]/div[contains(@class,'nav-group')]/a[4]",
        "name": "assignments_hover_lkz"
    }
    tasks_list_button = {
        "xpath": "//span[contains(@class,'text-big close-menu')][contains(text(),'Задания')]",
        "name": "tasks_list_button",
        "reference_xpath": "//h2[contains(text(),'Задания')]",
        "reference": "Задания"
    }

    """Contractor"""
    contractor_hover = {
        "xpath": "//body/div[@id='main']/div[contains(@class,'dashboard')]/header[contains(@class,'flexbox top-nav')]/div[contains(@class,'flexbox size-1 top-nav__center justify-right')]/div[contains(@class,'top-nav__center-wrapper')]/div[@class='nav-group']/a[2]",
        "name": "contractor_hover"
    }
    clients_list_button = {
        "xpath": "//span[contains(text(),'Заказчики')]",
        "name": "clients_list_button",
        "reference_xpath": "//h2[contains(text(),'Список контрагентов')]",
        "reference": "Список контрагентов"
    }

    """Documents"""
    documents_hover = {
        "xpath": "//body/div[@id='main']/div[@class='dashboard']/header[@class='flexbox top-nav']/div[@class='flexbox size-1 top-nav__center justify-right']/div[1]/div[1]/a[3]",
        "name": "documents_hover"
    }
    registries_client_list_button = {
        "xpath": "//li[@id='registriesRequestListOutgoing']//span[contains(@class,'text-big close-menu')][contains(text(),'Реестры для ГВ')]",
        "name": "registries_client_list_button",
        "reference_xpath": "//h2[contains(text(),'Реестры для заказчика')]",
        "reference": "Реестры для заказчика"
    }

    """Directories"""
    directories_hover = {
        "xpath": "//body/div[@id='main']/div[@class='dashboard']/header[@class='flexbox top-nav']/div[@class='flexbox size-1 top-nav__center justify-right']/div[1]/div[1]/a[4]",
        "name": "directories_hover"
    }
    addresses_list_button = {
        "xpath": "//span[contains(@class,'text-big close-menu')][contains(text(),'Адреса')]",
        "name": "addresses_list_button",
        "reference_xpath": "//h2[contains(text(),'Адреса')]",
        "reference": "Адреса"
    }

    """Orders (OLD)"""
    orders_old_hover = {
        "xpath": "//body/div[@id='main']/div[@class='dashboard']/header[@class='flexbox top-nav']/div[@class='flexbox size-1 top-nav__center justify-right']/div[1]/div[1]/a[1]",
        "name": "orders_old_hover"
    }
    ftl_active_list_button = {
        "xpath": "//span[contains(text(),'Активные FTL Заказы (OLD)')]",
        "name": "ftl_active_list_button",
        "reference_xpath": "//h2[contains(text(),'Активные заявки')]",
        "reference": "Активные заявки"
    }

    """Profile"""
    profile_button = {
        "xpath": "//body/div[@id='main']/div[@class='dashboard']/header[@class='flexbox top-nav']/div[@class='flexbox size-1 top-nav__center justify-right']/div[1]/div[1]/a[2]",
        "name": "profile_button",
        "reference_xpath": "//h2[contains(text(),'Общая информация о профиле')]",
        "reference": "Общая информация о профиле"
    }

    """Settings"""
    settings_button = {
        "xpath": "//body/div[@id='main']/div[@class='dashboard']/header[@class='flexbox top-nav']/div[@class='flexbox size-1 top-nav__center justify-right']/div[1]/div[1]/a[3]",
        "name": "settings_button",
        "reference_xpath": "//h1[contains(text(),'Настройки')]",
        "reference": "Настройки"
    }



