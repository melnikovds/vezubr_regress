from base.base_class import Base
import time


class ShipmentTaskAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    task_create_button = {
        "xpath": "//p[@class='no-margin']",
        "name": "task_create_button"
    }




