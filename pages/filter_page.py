from base.base_class import Base


class Contractors(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    """Contractors LKE list"""

    contractor_name = {
    "xpath": "(//input[@class='ant-input'])[3]",
    "name": "contractor_name"
    }



    """Contractors settings page LKE"""

    users_for_delegation = {
    "xpath": "//input[@class='ant-input']",
    "name": "users_for_delegation"
    }
    email_user_for_delegation = {
    "xpath": "(//input[@class='ant-input'])[3]",
    "name": "email_user_for_delegation"
    }
    cross_users_for_delegation = {
    "xpath": "/html/body/div[2]/div/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/div[1]/div/div[2]/div/span/span/span/i[1]",
    "name": "cross_users_for_delegation"
    }



    """Client LKE list"""


