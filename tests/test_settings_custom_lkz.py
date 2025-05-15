import allure
import pytest
import time
from pages.settings_page import Settings
from pages.settings_page import CustomFieldsParam
from pages.settings_page import EditFieldsParam


@allure.story("Extended test")
@allure.feature('Кастомные поля')
@allure.description('ЛКЗ. Тест №1 Редактирование кастомных полей')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_one_custom_settings_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход в раздел 'Настройки'
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.settings_button,
                           do_assert=True)

    time.sleep(2)
    settings = Settings(base.driver)
    # переход в раздел кастомные поля
    settings.click_button(settings.custom_fields_tab)

    # клик по кнопке добавления поля
    settings.click_button(settings.add_field_button)
    add_param = CustomFieldsParam(base.driver)

    # добавляем кастомное поле
    add_param.input_in_field(add_param.add_ru, value="амбрелла")
    add_param.input_in_field(add_param.add_en, value="ambrella")
    add_param.dropdown_without_input(add_param.add_role, option_text="Контрагент")
    add_param.dropdown_without_input(add_param.add_type, option_text="Текстовое значение")
    time.sleep(2)

    # сохраняем кастомное поле
    add_param.click_button(add_param.save_custom)
    time.sleep(2)
    add_param.click_button(add_param.done_pop_up)
    time.sleep(2)

    # проверяем наличие кастомного поля
    add_param.reload_page()
    time.sleep(3)
    add_param.verify_text_on_page(text='амбрелла')

    edit_param = EditFieldsParam(base.driver)

    # редактируем кастомное поле
    edit_param.click_button(edit_param.e_p)
    add_param.backspace_and_input(add_param.add_ru, value="З24-00275", click_first=True)
    add_param.backspace_and_input(add_param.add_en, value="Z24-0013")
    add_param.dropdown_without_input(add_param.add_role, option_text="Рейс")
    add_param.dropdown_without_input(add_param.add_type, option_text="Выбор из нескольких значений")

    # добавляем несколько значений
    edit_param.click_button(edit_param.add_val)
    edit_param.input_in_field(edit_param.unique_number_value, value="0041", click_first=True)
    edit_param.input_in_field(edit_param.name_value, value="Z24-0679", click_first=True, press_enter=True)
    edit_param.click_button(edit_param.save_unique_value)

    edit_param.click_button(edit_param.add_val)
    edit_param.input_in_field(edit_param.unique_number_value, value="0042", click_first=True)
    edit_param.input_in_field(edit_param.name_value, value="Z24-0680", click_first=True, press_enter=True)
    edit_param.click_button(edit_param.save_unique_value)

    edit_param.click_button(edit_param.add_val)
    edit_param.input_in_field(edit_param.unique_number_value, value="0043", click_first=True)
    edit_param.input_in_field(edit_param.name_value, value="Z24-0685", click_first=True, press_enter=True)
    edit_param.click_button(edit_param.save_unique_value)

    # редактируем и удаляем одно из значений
    edit_param.click_button(edit_param.edit_value)
    edit_param.backspace_and_input(edit_param.name_value, value="88", click_first=True)
    edit_param.click_button(edit_param.save_unique_value)
    edit_param.click_button(edit_param.delete_value)

    # сохраняем поле
    add_param.click_button(add_param.save_custom)
    time.sleep(2)
    add_param.click_button(add_param.done_pop_up)
    time.sleep(2)

    # проверяем изменение кастомного поля
    add_param.reload_page()
    time.sleep(3)
    add_param.verify_text_on_page(text='00275')

    # удаляем кастомное поле
    edit_param.click_button(edit_param.del_custom)
    time.sleep(3)
    edit_param.click_button(edit_param.rej_del)
    time.sleep(3)
    edit_param.click_button(edit_param.del_custom)
    time.sleep(3)
    edit_param.click_button(edit_param.acc_del)
    time.sleep(2)

    # проверяем отсутствие кастомного поля на странице
    add_param.reload_page()
    time.sleep(3)
    edit_param.verify_text_on_page(text="00275", should_exist=False)

    # конец теста


@allure.story("Extended test")
@allure.feature('Кастомные поля')
@allure.description('ЛКЗ. Тест №2 Редактирование кастомных полей')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_two_custom_settings_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход в раздел настройки
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.settings_button,
                           do_assert=True)

    time.sleep(2)
    settings = Settings(base.driver)
    # переход в раздел кастомные поля
    settings.click_button(settings.custom_fields_tab)

    # клик по кнопке добавления поля
    settings.click_button(settings.add_field_button)
    add_param = CustomFieldsParam(base.driver)

    # ввод данных кастомного поля
    # add_param.backspace_and_input(add_param.add_ru, value="З24-05485")
    add_param.backspace_and_input(add_param.add_ru, value="фыва")
    add_param.backspace_and_input(add_param.add_en, value="oldj")
    add_param.dropdown_without_input(add_param.add_role, option_text="Рейс")
    add_param.dropdown_without_input(add_param.add_type, option_text="Выбор из нескольких значений")

    edit_param = EditFieldsParam(base.driver)

    # добавляем несколько значений
    edit_param.click_button(edit_param.add_val)
    edit_param.input_in_field(edit_param.unique_number_value, value="0037", click_first=True)
    edit_param.input_in_field(edit_param.name_value, value="Z25-0128", click_first=True, press_enter=True)
    edit_param.click_button(edit_param.save_unique_value)

    edit_param.click_button(edit_param.add_val)
    edit_param.input_in_field(edit_param.unique_number_value, value="0038", click_first=True)
    edit_param.input_in_field(edit_param.name_value, value="Z25-0421", click_first=True, press_enter=True)
    edit_param.click_button(edit_param.save_unique_value)

    edit_param.click_button(edit_param.add_val)
    edit_param.input_in_field(edit_param.unique_number_value, value="0039", click_first=True)
    edit_param.input_in_field(edit_param.name_value, value="Z25-056", click_first=True, press_enter=True)
    edit_param.click_button(edit_param.save_unique_value)
    time.sleep(2)

    # сохраняем поле
    add_param.click_button(add_param.save_custom)
    time.sleep(2)
    add_param.click_button(add_param.done_pop_up_second)
    time.sleep(2)

    # проверяем наличие кастомного поля
    add_param.reload_page()
    time.sleep(3)
    add_param.verify_text_on_page(text='фыва')

    # редактируем кастомное поле
    edit_param.click_button(edit_param.e_p)

    add_param.backspace_and_input(add_param.add_ru, value="537683")
    add_param.backspace_and_input(add_param.add_en, value="537683")
    add_param.dropdown_without_input(add_param.add_role, option_text="Договор")
    add_param.dropdown_without_input(add_param.add_type, option_text="Числовое значение")

    # сохраняем поле
    add_param.click_button(add_param.save_custom)
    time.sleep(2)
    add_param.click_button(add_param.done_pop_up_second)
    time.sleep(2)

    # проверяем изменение кастомного поля
    add_param.reload_page()
    time.sleep(3)
    add_param.verify_text_on_page(text='537683')

    # удаляем кастомное поле
    edit_param.click_button(edit_param.del_custom)
    time.sleep(3)
    edit_param.click_button(edit_param.acc_del)
    time.sleep(2)

    # проверяем отсутствие кастомного поля на странице
    add_param.reload_page()
    time.sleep(3)
    edit_param.verify_text_on_page(text="537683", should_exist=False)

    # конец теста




