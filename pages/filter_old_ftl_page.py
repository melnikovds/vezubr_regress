from base.base_class import Base


class OldFTL(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    custom_field = {
        "xpath": "//a[text()='Пользовательские поля']",
        "name": "custom_field",
        "reference_xpath": "(//a[@class='vz-tabs-modern__item'])[3]"
    }