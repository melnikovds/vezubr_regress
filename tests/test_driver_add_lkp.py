import time
import allure
import pytest
from pages.driver_add_page import DriverAdd
from pages.driver_list_page import DriverList
from pages.filter_directory_page import Manual


@allure.story("Smoke test")
@allure.feature('Создание водителей')
@allure.description('ЛКП. Тест создания водителя: ФИО - ФИО-timestamp, паспорт/права - РФ, '
                    '№ паспорт/код/права/тлф.апп/тлф. - Рандом, добавить/убрать - 2 и 1 ТС, '
                    'работа - останавливаем/востанавливаем/увольняем')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_driver1_add_lkp(base_fixture, domain):
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
    surname = add_driver.add_base_driver()

    reset_filter = Manual(base.driver)

    # Фильтрация по фамилии водителя и переход к его профилю
    reset_filter.move_to_element(reset_filter.status_in_system)
    reset_filter.click_on_the_cross(reset_filter.cross_two)
    time.sleep(1)
    reset_filter.move_to_element(reset_filter.status_on_flight)
    reset_filter.click_on_the_cross(reset_filter.cross_three)
    time.sleep(1)
    driver_list.backspace_and_input(driver_list.surname_filter, value=surname, click_first=True)
    time.sleep(3)
    driver_list.click_button(driver_list.first_driver_link, wait="form")

    # Включить тогл готов работать как грузчик
    add_driver.click_button(add_driver.work_as_loader_toggl, wait="form")
    # Включить тогл никогда не делегировать
    add_driver.click_button(add_driver.never_delegate_toggl, wait="form")
    # Клик по кнопке прикрепить ТС
    add_driver.click_button(add_driver.attach_button, wait="form")
    time.sleep(4)
    # Прикрепить первый ТС в списке
    add_driver.click_button(add_driver.select_button)
    # Прикрепить второй ТС в списке
    add_driver.click_button(add_driver.select_button)
    # Клик по кнопке подтвердить прикрепление ТС
    add_driver.click_button(add_driver.assign_selected_button, wait="form")
    time.sleep(3)
    # Клик по кнопке прикрепить ТС
    add_driver.click_button(add_driver.attach_button, wait="form")
    time.sleep(2)
    # Открепить первый ТС в списке
    add_driver.click_button(add_driver.unselect_button)
    # Клик по кнопке подтвердить прикрепление ТС
    add_driver.click_button(add_driver.assign_selected_button, wait="form")
    time.sleep(1)
    # Открытие меню действий - приостановка работы водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.suspend_work_button, wait="form")
    # Открытие меню действий - возобновления работы водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.ready_to_work_button, wait="form")
    # Открытие меню действий - увольнение водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.fire_button)
    # Клик по кнопке подтверждения увольнения водителя
    add_driver.click_button(add_driver.yes_button, do_assert=True)
    # Подтверждение успешного увольнения водителя
    add_driver.click_button(add_driver.ok_button)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание водителей')
@allure.description('ЛКП. Тест создания водителя: ФИО - ФИО-timestamp, паспорт/права - РФ, '
                    '№ паспорт/код/права/тлф.апп/тлф. - Рандом, добавить/убрать - 1 ТС, '
                    'добавляем ЭПД, работа - останавливаем/востанавливаем/увольняем')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_driver2_add_lkp(base_fixture, domain):
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
    add_driver.input_in_field(add_driver.passport_by_input, "Водитель ЛКП с ЭПД")
    passport_code = add_driver.random_value_float_str(100000, 999999)
    add_driver.input_in_field(add_driver.passport_code_input, passport_code, click_first=True)
    license_id = add_driver.random_value_float_str(1000000000, 9999999999)
    add_driver.input_in_field(add_driver.license_id_input, license_id)
    add_driver.click_button(add_driver.license_date_input_close)
    add_driver.backspace_and_input(add_driver.license_date_input_open, num=2, value="45")
    time.sleep(2)
    add_driver.click_outside()

    # Ввод контактной информации
    app_phone = base.random_value_float_str(9650000000, 9659999999)
    add_driver.input_in_field(add_driver.app_phone_input, app_phone, click_first=True)
    contact_phone = base.random_value_float_str(9650000000, 9659999999)
    add_driver.input_in_field(add_driver.contact_phone_input, contact_phone, click_first=True)
    add_driver.input_in_field(add_driver.reg_address_input, "Спб, ул. Орджоникидзе, д.31, кв. 103")
    add_driver.input_in_field(add_driver.fact_address_input, "Спб, ул. Турку, д. 3, кв. 78")
    time.sleep(2)

    # Заполнение блока ЭПД
    inn = add_driver.generate_inn('individual')
    add_driver.input_in_field(add_driver.inn, value=inn)
    add_driver.click_button(add_driver.signatory_epd_toggl)
    snils = add_driver.generate_snils(True)
    add_driver.input_in_field(add_driver.snils, value=snils)
    add_driver.input_in_field(add_driver.driver_position, value='электронно-документооборотный водитель')
    add_driver.dropdown_without_input(add_driver.confirmation_method, option_text='Бумажная доверенность')
    add_driver.click_button(add_driver.attorney_date)
    time.sleep(1)
    add_driver.click_button(add_driver.attorney_date_today)
    add_driver.input_in_field(add_driver.attorney_number, value=str(add_driver.random_value_int(56, 89)))

    # Подтверждение создания водителя
    add_driver.click_button(add_driver.create_driver_button, do_assert=True)
    add_driver.click_button(add_driver.confirm_button, wait="lst")
    time.sleep(2)

    # Фильтрация по фамилии водителя и переход к его профилю
    reset_filter = Manual(base.driver)
    reset_filter.move_to_element(reset_filter.status_in_system)
    reset_filter.click_on_the_cross(reset_filter.cross_two)
    time.sleep(1)
    reset_filter.move_to_element(reset_filter.status_on_flight)
    reset_filter.click_on_the_cross(reset_filter.cross_three)
    time.sleep(1)
    driver_list.backspace_and_input(driver_list.surname_filter, value=surname, click_first=True)
    time.sleep(3)
    driver_list.click_button(driver_list.first_driver_link, wait="form")

    # Проверка наличия введённой информации о водителе
    add_driver.verify_text_on_page(text=surname)
    add_driver.verify_text_on_page(text=name)
    add_driver.verify_text_on_page(text=inn)
    add_driver.verify_text_on_page(text=snils)
    add_driver.verify_text_on_page(text='Да')
    add_driver.verify_text_on_page(text='Турку')
    add_driver.click_button(add_driver.tab_passport)
    time.sleep(1)
    add_driver.verify_text_on_page(text=surname)
    add_driver.verify_text_on_page(text=patronymic)
    add_driver.verify_text_on_page(text='Орджоникидзе')
    add_driver.verify_text_on_page(text='ЭПД')
    add_driver.verify_text_on_page(text=passport_id)
    add_driver.click_button(add_driver.tab_license)
    time.sleep(1)
    add_driver.verify_text_on_page(text=license_id)
    add_driver.verify_text_on_page(text='2045')
    add_driver.click_button(add_driver.tab_personal_data)
    time.sleep(1)
    add_driver.verify_text_on_page(text=app_phone)
    add_driver.verify_text_on_page(text=contact_phone)

    # Включить тогл готов работать как грузчик
    add_driver.click_button(add_driver.work_as_loader_toggl, wait="form")
    # Включить тогл никогда не делегировать
    add_driver.click_button(add_driver.never_delegate_toggl, wait="form")
    # Клик по кнопке прикрепить ТС
    add_driver.click_button(add_driver.attach_button, wait="form")
    time.sleep(4)
    # Прикрепить первый ТС в списке
    add_driver.click_button(add_driver.select_button)
    # Клик по кнопке подтвердить прикрепление ТС
    add_driver.click_button(add_driver.assign_selected_button, wait="form")
    time.sleep(3)
    # Клик по кнопке прикрепить ТС
    add_driver.click_button(add_driver.attach_button, wait="form")
    time.sleep(2)
    # Открепить первый ТС в списке
    add_driver.click_button(add_driver.unselect_button)
    # Клик по кнопке подтвердить прикрепление ТС
    add_driver.click_button(add_driver.assign_selected_button, wait="form")
    time.sleep(1)
    # Открытие меню действий - приостановка работы водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.suspend_work_button, wait="form")
    # Открытие меню действий - возобновления работы водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.ready_to_work_button, wait="form")
    # Открытие меню действий - увольнение водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.fire_button)
    # Клик по кнопке подтверждения увольнения водителя
    add_driver.click_button(add_driver.yes_button, do_assert=True)
    # Подтверждение успешного увольнения водителя
    add_driver.click_button(add_driver.ok_button)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание водителей')
@allure.description('ЛКП. Тест создания водителя: ФИО - ФИО-timestamp, паспорт/права - РФ, '
                    '№ паспорт/код/права/тлф.апп/тлф. - Рандом, добавить/убрать - 1 ТС, '
                    'добавляем ЭПД, работа - останавливаем/востанавливаем/увольняем')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_driver3_add_lkp(base_fixture, domain):
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
    add_driver.input_in_field(add_driver.passport_by_input, "Водитель ЛКП с ЭПД")
    passport_code = add_driver.random_value_float_str(100000, 999999)
    add_driver.input_in_field(add_driver.passport_code_input, passport_code, click_first=True)
    license_id = add_driver.random_value_float_str(1000000000, 9999999999)
    add_driver.input_in_field(add_driver.license_id_input, license_id)
    add_driver.click_button(add_driver.license_date_input_close)
    add_driver.backspace_and_input(add_driver.license_date_input_open, num=2, value="45")
    time.sleep(2)
    add_driver.click_outside()

    # Ввод контактной информации
    app_phone = base.random_value_float_str(9650000000, 9659999999)
    add_driver.input_in_field(add_driver.app_phone_input, app_phone, click_first=True)
    contact_phone = base.random_value_float_str(9650000000, 9659999999)
    add_driver.input_in_field(add_driver.contact_phone_input, contact_phone, click_first=True)
    add_driver.input_in_field(add_driver.reg_address_input, "Спб, пр. Славы, д.44, кв. 36")
    add_driver.input_in_field(add_driver.fact_address_input, "Спб, ул. Бухарестская, д. 67, кв. 4")
    time.sleep(2)

    # Заполнение блока ЭПД
    inn = add_driver.generate_inn('individual')
    add_driver.input_in_field(add_driver.inn, value=inn)
    add_driver.click_button(add_driver.signatory_epd_toggl)
    snils = add_driver.generate_snils(True)
    add_driver.input_in_field(add_driver.snils, value=snils)
    add_driver.input_in_field(add_driver.driver_position, value='электронно-документооборотный водитель')
    add_driver.dropdown_without_input(add_driver.confirmation_method, option_text='МЧД')
    add_driver.click_button(add_driver.attorney_date)
    time.sleep(1)
    add_driver.click_button(add_driver.attorney_date_today)
    add_driver.input_in_field(add_driver.attorney_number, value=str(add_driver.random_value_int(144, 404)))
    add_driver.input_in_field(add_driver.information_system_info,
                              value=str(add_driver.random_value_int(100000, 999999)))
    # Подтверждение создания водителя
    add_driver.click_button(add_driver.create_driver_button, do_assert=True)
    add_driver.click_button(add_driver.confirm_button, wait="lst")
    time.sleep(2)

    # Фильтрация по фамилии водителя и переход к его профилю
    reset_filter = Manual(base.driver)
    reset_filter.move_to_element(reset_filter.status_in_system)
    reset_filter.click_on_the_cross(reset_filter.cross_two)
    time.sleep(1)
    reset_filter.move_to_element(reset_filter.status_on_flight)
    reset_filter.click_on_the_cross(reset_filter.cross_three)
    time.sleep(1)
    driver_list.backspace_and_input(driver_list.surname_filter, value=surname, click_first=True)
    time.sleep(3)
    driver_list.click_button(driver_list.first_driver_link, wait="form")

    # Проверка наличия введённой информации о водителе
    add_driver.verify_text_on_page(text=surname)
    add_driver.verify_text_on_page(text=name)
    add_driver.verify_text_on_page(text=inn)
    add_driver.verify_text_on_page(text=snils)
    add_driver.verify_text_on_page(text='Да')
    add_driver.verify_text_on_page(text='Бухарестская')
    add_driver.click_button(add_driver.tab_passport)
    time.sleep(1)
    add_driver.verify_text_on_page(text=surname)
    add_driver.verify_text_on_page(text=patronymic)
    add_driver.verify_text_on_page(text='Славы')
    add_driver.verify_text_on_page(text='ЭПД')
    add_driver.verify_text_on_page(text=passport_id)
    add_driver.click_button(add_driver.tab_license)
    time.sleep(1)
    add_driver.verify_text_on_page(text=license_id)
    add_driver.verify_text_on_page(text='2045')
    add_driver.click_button(add_driver.tab_personal_data)
    time.sleep(1)
    add_driver.verify_text_on_page(text=app_phone)
    add_driver.verify_text_on_page(text=contact_phone)

    # Включить тогл готов работать как грузчик
    add_driver.click_button(add_driver.work_as_loader_toggl, wait="form")
    # Включить тогл никогда не делегировать
    add_driver.click_button(add_driver.never_delegate_toggl, wait="form")
    # Клик по кнопке прикрепить ТС
    add_driver.click_button(add_driver.attach_button, wait="form")
    time.sleep(4)
    # Прикрепить первый ТС в списке
    add_driver.click_button(add_driver.select_button)
    # Клик по кнопке подтвердить прикрепление ТС
    add_driver.click_button(add_driver.assign_selected_button, wait="form")
    time.sleep(3)
    # Клик по кнопке прикрепить ТС
    add_driver.click_button(add_driver.attach_button, wait="form")
    time.sleep(2)
    # Открепить первый ТС в списке
    add_driver.click_button(add_driver.unselect_button)
    # Клик по кнопке подтвердить прикрепление ТС
    add_driver.click_button(add_driver.assign_selected_button, wait="form")
    time.sleep(1)
    # Открытие меню действий - приостановка работы водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.suspend_work_button, wait="form")
    # Открытие меню действий - возобновления работы водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.ready_to_work_button, wait="form")
    # Открытие меню действий - увольнение водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.fire_button)
    # Клик по кнопке подтверждения увольнения водителя
    add_driver.click_button(add_driver.yes_button, do_assert=True)
    # Подтверждение успешного увольнения водителя
    add_driver.click_button(add_driver.ok_button)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание водителей')
@allure.description('ЛКП. Тест создания водителя: ФИО - ФИО-timestamp, паспорт/права - РФ, '
                    '№ паспорт/код/права/тлф.апп/тлф. - Рандом '
                    'работа - увольняем')
@pytest.mark.smoke
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_driver4_add_lkp(base_fixture, domain):
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
    surname = add_driver.add_base_driver()

    reset_filter = Manual(base.driver)

    # Фильтрация по фамилии водителя и переход к его профилю
    reset_filter.move_to_element(reset_filter.status_in_system)
    reset_filter.click_on_the_cross(reset_filter.cross_two)
    time.sleep(1)
    reset_filter.move_to_element(reset_filter.status_on_flight)
    reset_filter.click_on_the_cross(reset_filter.cross_three)
    time.sleep(1)
    driver_list.backspace_and_input(driver_list.surname_filter, value=surname, click_first=True)
    time.sleep(3)
    driver_list.click_button(driver_list.first_driver_link, wait="form")

    time.sleep(4)

    # Открытие меню действий - увольнение водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.fire_button)
    # Клик по кнопке подтверждения увольнения водителя
    add_driver.click_button(add_driver.yes_button, do_assert=True)
    # Подтверждение успешного увольнения водителя
    add_driver.click_button(add_driver.ok_button)
    # Конец теста
