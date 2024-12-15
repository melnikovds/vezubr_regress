import allure
import pytest
import time
from pages.settings_page_lkz import Settings
from pages.settings_page_lkz import CustomFieldsParam
from pages.settings_page_lkz import EditFieldsParam


@allure.story("Extended test")
@allure.feature('Кастомные поля')
@allure.description('ЛКЗ. Тест изменения настроек кастомных полей')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_custom_settings_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход в раздел настройки
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.settings_button,
                           do_assert=True, wait="lst")

    time.sleep(2)
    settings = Settings(base.driver)
    # переход в раздел кастомные поля
    settings.click_button(settings.custom_fields_tab)

    # клик по кнопке добавления поля
    settings.click_button(settings.add_field_button)

    add_param = CustomFieldsParam(base.driver)

    add_param.input_in_field(add_param.add_ru, value="контрагент")

    add_param.input_in_field(add_param.add_en, value="contractor")

    add_param.dropdown_without_input(add_param.add_role, option_text="Контрагент")

    add_param.dropdown_without_input(add_param.add_type, option_text="Текстовое значение")

    time.sleep(2)
    # сохраняем поле
    add_param.click_button(add_param.save_custom)
    time.sleep(2)
    add_param.click_button(add_param.done_pop_up)
    time.sleep(2)

    edit_param = EditFieldsParam(base.driver)

    # редактируем кастомное поле
    edit_param.click_button(edit_param.e_p)

    add_param.backspace_and_input(add_param.add_ru, value="рейс", click_first=True)

    add_param.backspace_and_input(add_param.add_en, value="flight")

    add_param.dropdown_without_input(add_param.add_role, option_text="Рейс")

    add_param.dropdown_without_input(add_param.add_type, option_text="Числовое значение")

    # сохраняем поле
    add_param.click_button(add_param.save_custom)
    time.sleep(2)
    add_param.click_button(add_param.done_pop_up)
    time.sleep(2)

    # удаляем кастомное поле
    edit_param.click_button(edit_param.del_custom)
    edit_param.click_button(edit_param.rej_del)
    edit_param.click_button(edit_param.del_custom)
    edit_param.click_button(edit_param.acc_del)
    # конец теста









