import allure
import pytest
import time
from pages.custom_page import Settings, CustomFieldParam


@allure.story("Extended path test")
@allure.feature('Кастомные поля')
@allure.description('ЛКП. Создание поля Заявка')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_create_custom_field_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # переход в раздел 'Настройки'
    sidebar.click_button(sidebar.settings_button, do_assert=True)
    settings = Settings(base.driver)

    # переход в таб 'Пользовательские поля'
    settings.click_button(settings.custom_field)

    # клик по кнопке 'Добавить поле'
    settings.click_button(settings.add_field)
    add_param = CustomFieldParam(base.driver)

    # добавляем кастомное поле
    add_param.backspace_and_input(add_param.add_ru, value="заявказ")
    add_param.backspace_and_input(add_param.add_en, value="bid")
    add_param.dropdown_without_input(add_param.add_role, option_text="Заявка")
    add_param.dropdown_without_input(add_param.add_type, option_text="Выбор из нескольких значений")

    # добавляем первое значение для кастомного поля
    add_param.click_button(add_param.click_meaning)
    add_param.input_in_field(add_param.unic_n, value="24-001")
    add_param.input_in_field(add_param.named_n, value="1323")
    add_param.click_button(add_param.confirm_add)

    # добавляем второе значение для кастомного поля
    add_param.click_button(add_param.click_meaning)
    add_param.input_in_field(add_param.unic_n, value="25-002")
    add_param.input_in_field(add_param.named_n, value="1324")
    add_param.click_button(add_param.confirm_add)

    # сохраняем кастомное поле
    time.sleep(1)
    add_param.click_button(add_param.click_save)
    time.sleep(1)
    add_param.click_button(add_param.click_ok)
    time.sleep(1)

    # проверяем наличие кастомного поля на странице
    add_param.reload_page()
    time.sleep(3)
    add_param.verify_text_on_page(text='заявказ')

    # Конец теста


@allure.story("Extended path test")
@allure.feature('Кастомные поля')
@allure.description('ЛКП. Редактирование поля Заявка на Договор')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_edit_custom_field_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # переход в раздел 'Настройки'
    sidebar.click_button(sidebar.settings_button, do_assert=True)
    settings = Settings(base.driver)

    # переход в таб 'Пользовательские поля'
    settings.click_button(settings.custom_field)

    # клик по кнопке редактирования кастомного поля
    settings.click_button(settings.edit_field)
    add_param = CustomFieldParam(base.driver)

    # ввод новых данных кастомного поля
    add_param.backspace_and_input(add_param.add_ru, value="договорчик")
    add_param.backspace_and_input(add_param.add_en, value="contractng")
    add_param.dropdown_without_input(add_param.add_role, option_text="Договор")
    add_param.dropdown_without_input(add_param.add_type, option_text="Текстовое значение")

    # сохраняем кастомное поле
    time.sleep(1)
    add_param.click_button(add_param.click_save_two)
    time.sleep(1)
    add_param.click_button(add_param.click_ok)
    time.sleep(1)

    # проверяем изменение кастомного поля
    add_param.reload_page()
    time.sleep(3)
    add_param.verify_text_on_page(text='договорчик')

    # Конец теста


@allure.story("Extended path test")
@allure.feature('Кастомные поля')
@allure.description('ЛКП. Удаления поля Договор')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_delete_custom_field_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # переход в раздел 'Настройки'
    sidebar.click_button(sidebar.settings_button, do_assert=True)
    settings = Settings(base.driver)

    # переход в таб 'Пользовательские поля'
    settings.click_button(settings.custom_field)

    # удаляем кастомное поле
    settings.click_button(settings.delete_field)
    time.sleep(1)
    settings.click_button(settings.delete_ok)
    time.sleep(1)

    # проверяем отсутствие кастомного поля на странице
    settings.reload_page()
    time.sleep(3)
    settings.verify_text_on_page(text='договорчик', should_exist=False)

    # Конец теста


@allure.story("Extended path test")
@allure.feature('Кастомные поля')
@allure.description('ЛКП. Создание поля Договор')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_create_custom_field2_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # переход в раздел 'Настройки'
    sidebar.click_button(sidebar.settings_button, do_assert=True)
    settings = Settings(base.driver)

    # переход в таб 'Пользовательские поля'
    settings.click_button(settings.custom_field)

    # клик по кнопке 'Добавить поле'
    settings.click_button(settings.add_field)
    add_param = CustomFieldParam(base.driver)

    # добавляем кастомное поле
    add_param.input_in_field(add_param.add_ru, value="Новоеп поле")
    add_param.input_in_field(add_param.add_en, value="new field2")
    add_param.dropdown_without_input(add_param.add_role, option_text="Договор")
    add_param.dropdown_without_input(add_param.add_type, option_text="Текстовое значение")

    # сохраняем кастомное поле
    add_param.click_button(add_param.click_save_two)
    add_param.click_button(add_param.click_ok)

    # проверяем наличие кастомного поля на странице
    add_param.reload_page()
    time.sleep(3)
    add_param.verify_text_on_page(text='Новоеп')

    # Конец теста


@allure.story("Extended path test")
@allure.feature('Кастомные поля')
@allure.description('ЛКП. Редактирование поля Договор на Контрагент')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_edit_custom_field2_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # переход в раздел 'Настройки'
    sidebar.click_button(sidebar.settings_button, do_assert=True)
    settings = Settings(base.driver)

    # переход в таб 'Пользовательские поля'
    settings.click_button(settings.custom_field)

    # клик по кнопке редактирования кастомного поля
    settings.click_button(settings.edit_field)
    add_param = CustomFieldParam(base.driver)

    # ввод новых данных кастомного поля
    add_param.backspace_and_input(add_param.add_ru, value="77878127")
    add_param.backspace_and_input(add_param.add_en, value="0000127")
    add_param.dropdown_without_input(add_param.add_role, option_text="Контрагент")
    add_param.dropdown_without_input(add_param.add_type, option_text="Числовое значение")

    # убираем параметр 'обязательное поле'
    add_param.click_button(add_param.click_require_field)
    time.sleep(1)

    # сохраняем кастомное поле
    add_param.click_button(add_param.click_save_two)
    time.sleep(1)
    add_param.click_button(add_param.click_ok)
    time.sleep(1)

    # проверяем изменение кастомного поля
    add_param.reload_page()
    time.sleep(3)
    add_param.verify_text_on_page(text='77878127')

    # Конец теста


@allure.story("Extended path test")
@allure.feature('Кастомные поля')
@allure.description('ЛКП. Удаление поля Контрагент')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_delete_custom_field2_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # переход в раздел 'Настройки'
    sidebar.click_button(sidebar.settings_button, do_assert=True)
    settings = Settings(base.driver)

    # переход в таб 'Пользовательские поля'
    settings.click_button(settings.custom_field)

    # удаляем кастомное поле
    settings.click_button(settings.delete_field)
    time.sleep(1)
    settings.click_button(settings.delete_ok)
    time.sleep(1)

    # проверяем отсутствие кастомного поля
    settings.reload_page()
    time.sleep(3)
    settings.verify_text_on_page(text='77878127', should_exist=False)

    # Конец теста
