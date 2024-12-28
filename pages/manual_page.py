from base.base_class import Base


class Manual(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    filter_date_create = {
        "xpath": "//div[@class='ant-select-selection__rendered']",
        "name": "filter_date_create",
        "reference_xpath": "//div[text()='За год']",
        "reference": "За год"
    }

