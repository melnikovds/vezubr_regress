import time
import allure
import pytest
from pages.driver_add_page import DriverAdd
from pages.driver_list_page import DriverList
from pages.filter_directory_page import Manual

@allure.story("Smoke test")
@allure.feature('Создание и операции с водителями')
@allure.description('ЛКЭ. Тест создания водителя Экс: ФИО - ФИО-timestamp, паспорт/права - РФ, '
                    '№ паспорт/код/права/тлф.апп/тлф. - Рандом, добавить/убрать - 2 и 1 ТС, '
                    'работа - останавливаем/востанавливаем/увольняем')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_own_driver1_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку водителей
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                           do_assert=True, wait="lst")
    
    driver_list = DriverList(base.driver)
    # Клик по кнопке добавления водителя
    driver_list.click_button(driver_list.add_driver_button)
    time.sleep(2)
    add_driver = DriverAdd(base.driver)
    # Добавление нового водителя и получение его фамилии
    surname = add_driver.add_base_driver()
    
    # Фильтрация по фамилии водителя и переход к его профилю
    driver_filter = Manual(base.driver)
    driver_filter.move_to_element(driver_filter.status_in_system)
    driver_filter.click_on_the_cross(driver_filter.cross_two)
    driver_list.input_in_field(driver_list.surname_filter, value=surname)
    time.sleep(2)
    driver_list.click_button(driver_list.first_driver_link)
    time.sleep(2)
    
    # Включить тогл готов работать как грузчик
    add_driver.click_button(add_driver.work_as_loader_toggl)
    time.sleep(2)
    # Включить тогл никогда не делегировать
    add_driver.click_button(add_driver.never_delegate_toggl)
    time.sleep(2)
    # Клик по кнопке прикрепить ТС
    add_driver.click_button(add_driver.attach_button)
    time.sleep(5)
    # Прикрепить первый ТС в списке
    add_driver.click_button(add_driver.select_button)
    # Прикрепить второй ТС в списке
    add_driver.click_button(add_driver.select_button)
    # Клик по кнопке подтвердить прикрепление ТС
    add_driver.click_button(add_driver.assign_selected_button)
    time.sleep(2)
    # Клик по кнопке прикрепить ТС
    add_driver.click_button(add_driver.attach_button)
    time.sleep(5)
    # Открепить первый ТС в списке
    add_driver.click_button(add_driver.unselect_button)
    # Клик по кнопке подтвердить прикрепление ТС
    add_driver.click_button(add_driver.assign_selected_button)
    time.sleep(2)
    # Открытие меню действий - приостановка работы водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.suspend_work_button)
    time.sleep(2)
    # Открытие меню действий - возобновления работы водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.ready_to_work_button)
    time.sleep(2)
    # Открытие меню действий - увольнение водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.fire_button)
    # Клик по кнопке подтверждения увольнения водителя
    add_driver.click_button(add_driver.yes_button, do_assert=True)
    # Подтверждение успешного увольнения водителя
    add_driver.click_button(add_driver.ok_button)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание и операции с водителями')
@allure.description('ЛКЭ. Тест создания водителя Экс: ФИО - ФИО-timestamp, паспорт/права - РФ, '
                    '№ паспорт/код/права/тлф.апп/тлф. - Рандом, добавить/убрать - 1 ТС, '
                    'добавляем ЭПД, работа - останавливаем/востанавливаем/увольняем')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_own_driver2_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку водителей
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                           do_assert=True, wait="lst")

    driver_list = DriverList(base.driver)
    # Клик по кнопке добавления водителя
    driver_list.click_button(driver_list.add_driver_button)
    time.sleep(2)
    add_driver = DriverAdd(base.driver)
    # Добавление нового водителя
    surname = f"Ф-{base.get_timestamp()}"
    name = f"И-{base.get_timestamp()}"
    patronymic = f"О-{base.get_timestamp()}"
    add_driver.input_in_field(add_driver.surname_input, surname)
    add_driver.input_in_field(add_driver.name_input, name)
    add_driver.input_in_field(add_driver.patronymic_input, patronymic)

    passport_id = add_driver.random_value_float_str(1000000000, 9999999999)
    add_driver.input_in_field(add_driver.passport_id_input, passport_id)
    add_driver.input_in_field(add_driver.passport_by_input, "Водитель ЛКЭ с ЭПД")
    passport_code = add_driver.random_value_float_str(100000, 999999)
    add_driver.input_in_field(add_driver.passport_code_input, passport_code, click_first=True)
    license_id = add_driver.random_value_float_str(1000000000, 9999999999)
    add_driver.input_in_field(add_driver.license_id_input, license_id)
    add_driver.click_button(add_driver.license_date_input_close)
    add_driver.backspace_and_input(add_driver.license_date_input_open, num=2, value="45")
    add_driver.click_outside()
    time.sleep(2)

    # Ввод контактной информации
    app_phone = base.random_value_float_str(9650000000, 9659999999)
    add_driver.input_in_field(add_driver.app_phone_input, app_phone, click_first=True)
    contact_phone = base.random_value_float_str(9650000000, 9659999999)
    add_driver.input_in_field(add_driver.contact_phone_input, contact_phone,click_first=True)
    add_driver.input_in_field(add_driver.reg_address_input, "Спб, ул. Белы Куна, д.15, кв. 115")
    add_driver.input_in_field(add_driver.fact_address_input, "Спб, ул. Бассейная, д. 21, кв. 63")
    time.sleep(2)

    # Заполнение блока ЭПД
    inn = add_driver.generate_inn('individual')
    # inn = '333801077600'
    add_driver.input_in_field(add_driver.inn, value=inn)
    add_driver.click_button(add_driver.signatory_epd_toggl)
    # snils = '39548071726'
    snils = add_driver.generate_snils(True)
    add_driver.input_in_field(add_driver.snils, value=snils)
    add_driver.input_in_field(add_driver.driver_position, value='электронно-документооборотный водитель')
    add_driver.dropdown_without_input(add_driver.confirmation_method, option_text='Из подписи (директор)')

    # Управление настройками санитарной книжки и подтверждение создания водителя
    add_driver.click_button(add_driver.sanitary_book_toggl)
    add_driver.click_button(add_driver.create_driver_button, do_assert=True)
    add_driver.click_button(add_driver.confirm_button, wait="lst")
    time.sleep(2)

    # Фильтрация по фамилии водителя и переход к его профилю
    driver_filter = Manual(base.driver)
    driver_filter.move_to_element(driver_filter.status_in_system)
    driver_filter.click_on_the_cross(driver_filter.cross_two)
    driver_list.input_in_field(driver_list.surname_filter, value=surname)
    time.sleep(2)
    driver_list.click_button(driver_list.first_driver_link)
    time.sleep(2)

    # Проверка наличия введённой информации о водителе
    driver_filter.verify_text_on_page(text=surname)
    driver_filter.verify_text_on_page(text=name)
    driver_filter.verify_text_on_page(text=inn)
    driver_filter.verify_text_on_page(text=snils)
    driver_filter.verify_text_on_page(text='Да')
    driver_filter.verify_text_on_page(text='Бассейная')
    add_driver.click_button(add_driver.tab_passport)
    time.sleep(1)
    driver_filter.verify_text_on_page(text=surname)
    driver_filter.verify_text_on_page(text=patronymic)
    driver_filter.verify_text_on_page(text='Белы Куна')
    driver_filter.verify_text_on_page(text='ЭПД')
    driver_filter.verify_text_on_page(text=passport_id)
    add_driver.click_button(add_driver.tab_license)
    time.sleep(1)
    driver_filter.verify_text_on_page(text=license_id)
    driver_filter.verify_text_on_page(text='2045')
    add_driver.click_button(add_driver.tab_personal_data)
    time.sleep(1)
    driver_filter.verify_text_on_page(text=app_phone)
    driver_filter.verify_text_on_page(text=contact_phone)

    # Включить тогл готов работать как грузчик
    add_driver.click_button(add_driver.work_as_loader_toggl)
    time.sleep(2)
    # Включить тогл никогда не делегировать
    add_driver.click_button(add_driver.never_delegate_toggl)
    time.sleep(2)
    # Клик по кнопке прикрепить ТС
    add_driver.click_button(add_driver.attach_button)
    time.sleep(20)
    # Прикрепить первый ТС в списке
    add_driver.click_button(add_driver.select_button)
    # Клик по кнопке подтвердить прикрепление ТС
    add_driver.click_button(add_driver.assign_selected_button)
    time.sleep(2)
    # Клик по кнопке прикрепить ТС
    add_driver.click_button(add_driver.attach_button)
    time.sleep(5)
    # Открепить первый ТС в списке
    add_driver.click_button(add_driver.unselect_button)
    # Клик по кнопке подтвердить прикрепление ТС
    add_driver.click_button(add_driver.assign_selected_button)
    time.sleep(2)
    # Открытие меню действий - приостановка работы водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.suspend_work_button)
    time.sleep(2)
    # Открытие меню действий - возобновления работы водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.ready_to_work_button)
    time.sleep(2)
    # Открытие меню действий - увольнение водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.fire_button)
    # Клик по кнопке подтверждения увольнения водителя
    add_driver.click_button(add_driver.yes_button, do_assert=True)
    # Подтверждение успешного увольнения водителя
    add_driver.click_button(add_driver.ok_button)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание и операции с водителями')
@allure.description('ЛКЭ. Тест создания водителя внутр КА: ка - Первый в списке, ФИО - ВФИО-timestamp, '
                    'паспорт/права - РФ, № паспорт/код/права/тлф. - Рандом, добавить/убрать - 2 и 1 ТС, '
                    'работа - останавливаем/востанавливаем/увольняем')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_inner_driver_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку водителей
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                           do_assert=True, wait="lst")
    
    driver_list = DriverList(base.driver)
    # Клик по кнопке добавления водителя
    driver_list.click_button(driver_list.add_driver_button, wait="form")
    
    add_driver = DriverAdd(base.driver)
    # Добавление нового водителя и получение его фамилии
    surname = add_driver.add_base_inner_driver()
    
    # Фильтрация по фамилии водителя и переход к его профилю
    driver_filter = Manual(base.driver)
    driver_filter.move_to_element(driver_filter.status_in_system)
    driver_filter.click_on_the_cross(driver_filter.cross_two)
    driver_list.input_in_field(driver_list.surname_filter, value=surname)
    time.sleep(2)
    driver_list.click_button(driver_list.first_driver_link)
    time.sleep(2)
    # Включить тогл готов работать как грузчик
    add_driver.click_button(add_driver.work_as_loader_toggl)
    time.sleep(2)
    # Включить тогл никогда не делегировать
    add_driver.click_button(add_driver.never_delegate_toggl)
    time.sleep(2)
    # Клик по кнопке прикрепить ТС
    add_driver.click_button(add_driver.attach_button)
    time.sleep(5)
    # Прикрепить первый ТС в списке
    add_driver.click_button(add_driver.select_button)
    # Прикрепить второй ТС в списке
    add_driver.click_button(add_driver.select_button)
    # Клик по кнопке подтвердить прикрепление ТС
    add_driver.click_button(add_driver.assign_selected_button)
    time.sleep(2)
    # Клик по кнопке прикрепить ТС
    add_driver.click_button(add_driver.attach_button)
    time.sleep(5)
    # Открепить первый ТС в списке
    add_driver.click_button(add_driver.unselect_button)
    # Клик по кнопке подтвердить прикрепление ТС
    add_driver.click_button(add_driver.assign_selected_button)
    time.sleep(2)
    # Открытие меню действий - приостановка работы водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.suspend_work_button)
    time.sleep(2)
    # Открытие меню действий - возобновления работы водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.ready_to_work_button)
    time.sleep(2)
    # Открытие меню действий - увольнение водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.fire_button)
    # Клик по кнопке подтверждения увольнения водителя
    add_driver.click_button(add_driver.yes_button, do_assert=True)
    # Подтверждение успешного увольнения водителя
    add_driver.click_button(add_driver.ok_button)
    # Конец теста
