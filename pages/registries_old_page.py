from base.base_class import Base


class RegistriesOld(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    """Формирование регистров"""
    checkbox_one = {
        "xpath": "//td[@class='ant-table-selection-column ant-table-selection-column-custom']//input[@type='checkbox']",
        "name": "checkbox_one"
    }
    form_new_registry = {
        "xpath": "//p[@class='no-margin']",
        "name": "form_new_registry",
        "reference_xpath": "//div[@class='ant-modal-confirm-content']",
        "reference": "был успешно создан",
        "match_type": "contains"
    }
    registry_ok = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "registry_ok",
    }

    "Список регистров"
    # registry_click = {
    #     "xpath": "//td[@class='ant-table-row-cell-break-word']//a[@id='registries-number-2447-26-1']",
    #     "name": "registry_click",
    # }
