from base.base_class import Base


class Journal(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_history_cargo_place = {
        "xpath": "//a[contains(text(),'История')]",
        "name": "tab_history_cargo_place"
    }
    tab_history_address = {
        "xpath": "//a[contains(text(),'История')]",
        "name": "tab_history_address"
    }
    tab_history_order = {
        "xpath": "//a[contains(text(),'История')]",
        "name": "tab_history_order"
    }
    time_event = {
        "xpath": "//div[@title='Пользовательский']",
        "name": "time_event"
    }


