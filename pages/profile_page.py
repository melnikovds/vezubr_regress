from base.base_class import Base


class Profile(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    general_info_tab = {
        "xpath": "//a[text()='Общая информация']",
        "name": "general_info_tab"
    }
    fact_address_input = {
        "xpath": "//*[@id='addressFact']",
        "name": "fact_address_input"
    }
    post_address_input = {
        "xpath": "//*[@id='addressPost']",
        "name": "post_address_input"
    }
    phone_input = {
        "xpath": "//*[@id='phone']",
        "name": "phone_input"
    }
    """VAT drop-down list"""
    vat_type_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(), 'НДС')]",
        "name": "vat_type_select"
    }
    """Direct request drop-down list"""
    direct_request_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(), 'Кому направлять рейсы')]",
        "name": "direct_request_select"
    }
    """Values in system drop-down list"""
    values_in_system_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[3]",
        "name": "values_in_system_select"
    }
    electronic_document_toggl = {
        "xpath": "//button[@id='docFlowConfiguration.electronicDocFlow']",
        "name": "electronic_document_toggl"
    }
    contour_link = {
        "xpath": "//td[@class='contour-links__col-action']/a[text()='Скопировать в буфер']",
        "name": "contour_link",
        "reference_xpath": "//span[text()='Ссылка скопирована']",
        "reference": "Ссылка скопирована"
    }
    additional_info_tab = {
        "xpath": "//a[text()='Дополнительная информация']",
        "name": "additional_info_tab",
        "reference_xpath": "//h2[@class='bold']",
        "reference": "Дополнительная информация о профиле"
    }
    checking_account_input = {
        "xpath": "//*[@id='checkingAccount']",
        "name": "checking_account_input",
    }
    bik_input = {
        "xpath": "//*[@id='bik']",
        "name": "bik_input",
    }
    groups_tab = {
        "xpath": "//a[text()='Группы']",
        "name": "groups_tab"
    }
    groups_delete_button = {
        "xpath": "//*[@id='main']/div/div[3]/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div/"
                 "table/tbody/tr[5]/td/div/div/div/img",
        "name": "groups_delete_button"
    }
    users_tab = {
        "xpath": "//a[text()='Пользователи']",
        "name": "users_tab",
        "reference_xpath": "//h2[@class='bold' and text()='Пользователи']",
        "reference": "Пользователи"
    }
    add_user_button = {
        "xpath": "//button[@class='mid element-button theme-primary']",
        "name": "add_user_button"
    }
    save_button = {
        "xpath": "//button[@class='semi-wide element-button theme-primary']",
        "name": "save_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Профиль успешно обновлен']",
        "reference": "Профиль успешно обновлен"
    }
    confirm_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "confirm_button",
        "reference_xpath": "//h2[@class='bold' and text()='Профиль']",
        "reference": "Профиль"
    }
    surname_filter = {
        "xpath": "//input[@placeholder='Ф.И.О пользователя']",
        "name": "surname_filter"
    }
    user_link = {
        "xpath": "//a[@class='link-back']",
        "name": "user_link"
    }
    delete_user_button = {
        "xpath": "//*[@id='main']/div/div[3]/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div/"
                 "table/tbody/tr[1]/td/div/div[2]/div[1]/img",
        "name": "delete_user_button"
    }
    password_input = {
        "xpath": "//input[@type='password']",
        "name": "password_input"
    }
    delete_confirm_button = {
        "xpath": "//button[@class='mid  element-button theme-primary']",
        "name": "delete_confirm_button",
        "reference_xpath": "//h2[contains(@class, 'bold') and contains(text(), 'Пользователи')]",
        "reference": "Пользователи"
    }

class UsersFilter(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    additional_filters = {
        "xpath": "//p[@class='no-margin']",
        "name": "additional_filters"
    }
    default_filters = {
        "xpath": "//button[contains(text(),'По умолчанию')]",
        "name": "default_filters"
    }
    first_add_filter = {
        "xpath": "//div[@class='flexbox wrap choose-additional-filters column size-1']//div[1]//label[1]//span[2]",
        "name": "first_add_filter"
    }
    second_add_filter = {
        "xpath": "//body//div[@id='main']//div[contains(@role,'dialog')]//div[contains(@role,'dialog')]//div[2]//label[1]//span[2]",
        "name": "second_add_filter"
    }
    third_add_filter = {
        "xpath": "//div[contains(@class,'modal-body')]//div[3]//label[1]//span[2]",
        "name": "third_add_filter"
    }
    apply_add_filter = {
        "xpath": "//button[contains(text(),'Применить')]",
        "name": "apply_add_filter"
    }
    reset_users_filter = {
        "xpath": "//button[contains(@class,'ant-btn semi-wide margin-left-16 ant-btn-ghost')]",
        "name": "reset_users_filter"
    }

    fio_filter = {
        "xpath": "//input[contains(@placeholder,'Ф.И.О пользователя')]",
        "name": "fio_filter"
    }
    type_filter = {
        "xpath": "//div[@class='ant-select-selection__placeholder']",
        "name": "type_filter"
    }
    role_filter = {
        "xpath": "//span[@class='ant-select-search__field__placeholder'][contains(text(),'Роль')]",
        "name": "role_filter"
    }
    dispatcher_role = {
        "xpath": "//span[contains(@title,'Диспетчер')]//span[1]",
        "name": "dispatcher_role"
    }
    manager_role = {
        "xpath": "//span[contains(@title,'Менеджер')]//span[1]",
        "name": "manager_role"
    }
    administrator_role = {
        "xpath": "//span[contains(@title,'Администратор')]//span[1]",
        "name": "administrator_role"
    }
    logistician_role = {
        "xpath": "//span[contains(@title,'Логист')]//span[1]",
        "name": "logistician_role"
    }
    office_worker_role = {
        "xpath": "//span[contains(@title,'Офисный сотрудник')]//span[1]",
        "name": "office_worker_role"
    }
    phone_filter = {
        "xpath": "//input[@placeholder='Телефон']",
        "name": "phone_filter"
    }
    email_filter = {
        "xpath": "//input[@placeholder='Электронная почта']",
        "name": "email_filter"
    }
    subdivision_filter = {
        "xpath": "//span[@class='ant-select-search__field__placeholder'][contains(text(),'Подразделение')]",
        "name": "subdivision_filter"
    }
    subdivision_one = {
        "xpath": "//span[contains(text(),'SIPRI')]",
        "name": "subdivision_one"
    }
    subdivision_two = {
        "xpath": "//span[contains(text(),'SEAL')]",
        "name": "subdivision_two"
    }
    driver_dispatcher_role = {
        "xpath": "//span[@title='Водитель - диспетчер']//span[1]",
        "name": "driver_dispatcher_role"
    }
    subdivision_lkp = {
        "xpath": "//span[@title='База']",
        "name": "subdivision_lkp"
    }

    groups_add_filter = {
        "xpath": "//div[1]//div[4]//label[1]//span[2]",
        "name": "groups_add_filter"
    }
    subdivision_lke = {
        "xpath": "//span[@title='второе подразделение']//span[1]",
        "name": "subdivision_lke"
    }
    groups_filter = {
        "xpath": "//body/div[@id='main']/div[@class='dashboard']/div[@class='dashboard-content margin-top-60']/div[@class='profile page-profile-users page-profile-users path-profile-users container']/div[@class='profile-view']/div[@class='flexbox center column']/div[@class='white-container flexbox margin-top-12 margin-bottom-20']/div[@class='center size-1 profile-view__users']/form[@class='ant-form ant-form-inline table-filters']/div[@class='table-filters-main-zone']/div[7]/div[1]/div[2]/div[1]/span[1]/span[1]/span[1]/span[1]",
        "name": "groups_filter"
    }
    x_group = {
        "xpath": "//span[@title='группа Икс']//span[1]",
        "name": "x_group"
    }






