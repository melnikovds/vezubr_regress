import allure
import pytest
import time
from pages.settings_page import Settings
from pages.settings_page import CustomFieldsParam
from pages.settings_page import EditFieldsParam


@allure.story("Extended test")
@allure.feature('Кастомные поля')
@allure.description('ЛКП. Тест изменения настроек кастомных полей')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_custom_settings_lkp(base_fixture, domain):