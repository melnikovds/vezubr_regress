from base.base_class import Base


class Manual(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # insurer_info = {
        #     "xpath": "",
        #     "name": "insurer_info"
        # }