from base.base_class import Base


class NewFtlFilters(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    clear = {
        "xpath": "//button[contains(@class,'ant-btn semi-wide')]",
        "name": "clear"
    }