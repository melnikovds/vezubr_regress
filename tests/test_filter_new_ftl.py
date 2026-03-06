import allure
import pytest
import time
from pages.filters_new_ftl_page import NewFtlFilters
from selenium.webdriver.common.by import By


@allure.story("Extended path test")
@allure.feature('Фильтры списка Заявок')
@allure.description('ЛКЗ, Тестирование фильтров в разделе "Заявки на доставки груза" ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_filters_new_ftl_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.cdr_active_list_button,
                           do_assert=True, wait="lst")

    add = NewFtlFilters(base.driver)
    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')

    # Проверка фильтра 'Тип доставки'
    add.dropdown_without_input(add.delivery_type, option_text='FTL')
    add.input_in_field(add.request_number, value='216')
    time.sleep(2)
    add.verify_text_on_page(text='gfghf333', should_exist=True)
    add.verify_text_on_page(text='мммм--990', should_exist=False)
    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)
    add.dropdown_without_input(add.delivery_type, option_text='LTL')
    add.backspace_and_input(add.request_number, value='176', num=10)
    time.sleep(2)
    add.verify_text_on_page(text='25-VZ-176', should_exist=True)
    add.verify_text_on_page(text='25-VZ-175', should_exist=False)
    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)

    # Проверка фильтра 'Номер заявки'
    add.input_in_field(add.request_number, value='193')
    time.sleep(2)
    add.verify_text_on_page(text='рувыарух', should_exist=True)
    add.verify_text_on_page(text='25-VZ-192', should_exist=False)
    time.sleep(2)
    add.backspace_and_input(add.request_number, value='26-VZ-4', num=10)
    time.sleep(2)
    add.verify_text_on_page(text='мммм--99', should_exist=True)
    add.verify_text_on_page(text='26-VZ-5', should_exist=False)
    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)

    # Проверка фильтра 'Статус заявки'
    add.dropdown_without_input(add.request_status, option_text='Формирование заявки')
    add.input_in_field(add.client_identifier, value='9539')
    time.sleep(2)
    add.verify_text_on_page(text='25-VZ-15', should_exist=True)
    add.verify_text_on_page(text='25-VZ-214', should_exist=False)
    add.dropdown_without_input(add.request_status, option_text='Подтверждён')
    add.backspace_and_input(add.client_identifier, value='льцпщняю', num=10)
    time.sleep(2)
    add.verify_text_on_page(text='25-VZ-203', should_exist=True)
    add.verify_text_on_page(text='25-VZ-202', should_exist=False)
    add.dropdown_without_input(add.request_status, option_text='Поиск исполнителя')
    add.backspace_and_input(add.client_identifier, value='', num=10)
    add.input_in_field(add.request_number, value='178')
    time.sleep(2)
    add.verify_text_on_page(text='7819', should_exist=True)
    add.verify_text_on_page(text='7572', should_exist=False)
    add.dropdown_without_input(add.request_status, option_text='Исполнитель не найден')
    add.backspace_and_input(add.request_number, value='', num=10)
    time.sleep(2)
    add.verify_text_on_page(text='24-VZ-103', should_exist=True)
    add.verify_text_on_page(text='25-VZ-103', should_exist=False)
    add.dropdown_without_input(add.request_status, option_text='В исполнении')
    add.backspace_and_input(add.request_number, value='', num=10)
    time.sleep(2)
    add.verify_text_on_page(text='kovalkov', should_exist=True)
    add.verify_text_on_page(text='мммм--', should_exist=False)
    add.dropdown_without_input(add.request_status, option_text='Завершен')
    add.backspace_and_input(add.request_number, value='205', num=10)
    time.sleep(2)
    add.verify_text_on_page(text='шиыюумаа', should_exist=True)
    add.verify_text_on_page(text='тьимим', should_exist=False)
    add.dropdown_without_input(add.request_status, option_text='Отменена Заказчиком')
    add.backspace_and_input(add.request_number, value='', num=10)
    time.sleep(2)
    add.verify_text_on_page(text='778ииитиссс', should_exist=True)
    add.verify_text_on_page(text='тнвэфвют', should_exist=False)
    add.dropdown_without_input(add.request_status, option_text='Отменена Исполнителем')
    add.backspace_and_input(add.request_number, value='', num=10)
    time.sleep(2)
    add.verify_text_on_page(text='кккр-29877', should_exist=True)
    add.verify_text_on_page(text='778ииитиссс', should_exist=False)

    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)

    # Проверка фильтра 'Идентификатор клиента'
    add.input_in_field(add.client_identifier, value='чрю')
    time.sleep(2)
    add.verify_text_on_page(text='25-VZ-195', should_exist=True)
    add.verify_text_on_page(text='25-VZ-194', should_exist=False)
    add.backspace_and_input(add.client_identifier, value='кищхму', num=10)
    time.sleep(2)
    add.verify_text_on_page(text='25-VZ-191', should_exist=True)
    add.verify_text_on_page(text='25-VZ-192', should_exist=False)
    add.backspace_and_input(add.client_identifier, value='6948', num=10)
    time.sleep(2)
    add.verify_text_on_page(text='25-VZ-179', should_exist=True)
    add.verify_text_on_page(text='25-VZ-178', should_exist=False)

    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)

    add.click_button(add.additional_filters)
    time.sleep(1)
    add.click_button(add.default_filters, wait_type='visible')
    time.sleep(1)
    add.click_button(add.checkbox_producer)
    add.click_button(add.checkbox_inn)
    add.click_button(add.checkbox_surname)
    add.click_button(add.checkbox_name)
    add.click_button(add.checkbox_plate)
    add.click_button(add.checkbox_publication_type)
    add.click_button(add.checkbox_transport_type)
    add.click_button(add.checkbox_first_point_address)
    add.click_button(add.apply_filters)
    time.sleep(1)

    # Проверка фильтра 'Подрядчик'
    add.input_in_field(add.producer_filter, value='Auto LKP')
    add.input_in_field(add.client_identifier, value='тьимим')
    time.sleep(3)
    add.verify_text_on_page(text='25-VZ-217', should_exist=True)
    add.verify_text_on_page(text='25-VZ-218', should_exist=False)
    add.backspace_and_input(add.producer_filter, value='Auto LKE', num=10)
    add.backspace_and_input(add.client_identifier, value='имс2', num=10)
    time.sleep(3)
    add.verify_text_on_page(text='25-VZ-214', should_exist=True)
    add.verify_text_on_page(text='25-VZ-217', should_exist=False)

    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)

    # Проверка фильтра 'ИНН подрядчика'
    add.input_in_field(add.inn_filter, value='5178')
    add.input_in_field(add.client_identifier, value='булк')
    time.sleep(3)
    add.verify_text_on_page(text='25-VZ-207', should_exist=True)
    add.verify_text_on_page(text='25-VZ-206', should_exist=False)
    add.backspace_and_input(add.inn_filter, value='68831', num=10)
    add.backspace_and_input(add.client_identifier, value='лсокп', num=10)
    time.sleep(3)
    add.verify_text_on_page(text='25-VZ-206', should_exist=True)
    add.verify_text_on_page(text='25-VZ-207', should_exist=False)

    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)

    # Проверка фильтра 'Фамилия водителя'
    add.input_in_field(add.surname_filter, value='бойко')
    add.input_in_field(add.request_number, value='11')
    time.sleep(3)
    add.verify_text_on_page(text='26-VZ-11', should_exist=True)
    add.verify_text_on_page(text='Ролов', should_exist=False)
    add.backspace_and_input(add.surname_filter, value='данов', num=10)
    add.backspace_and_input(add.request_number, value='12', num=10)
    time.sleep(3)
    add.verify_text_on_page(text='26-VZ-12', should_exist=True)
    add.verify_text_on_page(text='Бойко', should_exist=False)

    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)

    # Проверка фильтра 'Имя водителя'
    add.input_in_field(add.name_filter, value='олег')
    add.input_in_field(add.request_number, value='16')
    time.sleep(3)
    add.verify_text_on_page(text='26-VZ-16', should_exist=True)
    add.verify_text_on_page(text='Сергей', should_exist=False)
    add.backspace_and_input(add.name_filter, value='александр', num=10)
    add.backspace_and_input(add.request_number, value='17', num=10)
    time.sleep(3)
    add.verify_text_on_page(text='26-VZ-17', should_exist=True)
    add.verify_text_on_page(text='Глуховцев', should_exist=False)

    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)

    # Проверка фильтра 'Госномер ТС'
    add.input_in_field(add.plate_filter, value='ролл')
    time.sleep(5)
    add.verify_text_on_page(text='Ролов', should_exist=True)
    add.verify_text_on_page(text='Корнаухов', should_exist=False)
    add.backspace_and_input(add.plate_filter, value='5221626', num=10)
    time.sleep(5)
    add.verify_text_on_page(text='Ковальков', should_exist=True)
    add.verify_text_on_page(text='Бойко', should_exist=False)

    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)

    # Проверка фильтра 'Тип публикации'
    add.dropdown_without_input(add.publication_type_filter, option_text='Тариф')
    add.input_in_field(add.request_number, value='18')
    time.sleep(5)
    add.verify_text_on_page(text='26-VZ-18', should_exist=True)
    add.verify_text_on_page(text='25-VZ-218', should_exist=False)

    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)

    add.dropdown_without_input(add.publication_type_filter, option_text='Ставка')
    add.backspace_and_input(add.request_number, value='18', num=10)
    time.sleep(3)
    add.verify_text_on_page(text='25-VZ-218', should_exist=True)
    add.verify_text_on_page(text='26-VZ-18', should_exist=False)

    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)

    # Проверка фильтра 'Тип ТС'
    add.dropdown_without_input(add.transport_type_filter, option_text='1.5т / 9м3 / 4пал.')
    add.input_in_field(add.request_number, value='198')
    time.sleep(5)
    add.verify_text_on_page(text='25-VZ-198', should_exist=True)
    add.verify_text_on_page(text='25-VZ-199', should_exist=False)

    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)

    add.dropdown_without_input(add.transport_type_filter, option_text='до 0.5т')
    time.sleep(3)
    add.verify_text_on_page(text='24-VZ-188', should_exist=True)
    add.verify_text_on_page(text='25-VZ-188', should_exist=False)

    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)

    add.dropdown_without_input(add.transport_type_filter, option_text='20т / 90м3 / 33пал.')
    time.sleep(3)
    add.verify_text_on_page(text='25-VZ-121', should_exist=True)
    add.verify_text_on_page(text='25-VZ-122', should_exist=False)

    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)

    # Проверка фильтра 'Адрес подачи'
    add.input_in_field(add.first_point_address_filter, value='победы')
    add.input_in_field(add.request_number, value='158')
    time.sleep(5)
    add.verify_text_on_page(text='25-VZ-158', should_exist=True)
    add.verify_text_on_page(text='25-VZ-155', should_exist=False)
    add.backspace_and_input(add.first_point_address_filter, value='фрунзе', num=10)
    add.backspace_and_input(add.request_number, value='217', num=10)
    time.sleep(5)
    add.verify_text_on_page(text='25-VZ-217', should_exist=True)
    add.verify_text_on_page(text='25-VZ-216', should_exist=False)

    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)


@allure.story("Extended path test")
@allure.feature('Фильтры списка Заявок')
@allure.description('ЛКЭ, Тестирование фильтров в разделе "Заявки на доставки груза" ')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_filters_new_ftl_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.cdr_active_list_button,
                           do_assert=True, wait="lst")

    add = NewFtlFilters(base.driver)
    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')

    # Проверка фильтра 'Тип доставки'
    add.dropdown_without_input(add.delivery_type, option_text='FTL')
    add.input_in_field(add.request_number, value='178')
    time.sleep(2)
    add.verify_text_on_page(text='10.09.2025-7819', should_exist=True)
    add.verify_text_on_page(text='10.09.2025-3796', should_exist=False)
    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)
    add.dropdown_without_input(add.delivery_type, option_text='LTL')
    add.backspace_and_input(add.request_number, value='132', num=10)
    time.sleep(2)
    add.verify_text_on_page(text='24-VZ-132', should_exist=True)
    add.verify_text_on_page(text='24-VZ-135', should_exist=False)
    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)

    # Проверка фильтра 'Номер заявки'
    add.input_in_field(add.request_number, value='127')
    time.sleep(2)
    add.verify_text_on_page(text='2025-8481', should_exist=True)
    add.verify_text_on_page(text='25-VZ-124', should_exist=False)
    time.sleep(2)
    add.backspace_and_input(add.request_number, value='25-VZ-81', num=10)
    time.sleep(2)
    add.verify_text_on_page(text='FTL-12.03.2025-5349', should_exist=True)
    add.verify_text_on_page(text='VZ-80', should_exist=False)
    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)

    # Проверка фильтра 'Тип заявки'
    add.dropdown_without_input(add.request_type, option_text='Входящая заявка')
    add.input_in_field(add.request_number, value='25-VZ-137')
    time.sleep(2)
    add.verify_text_on_page(text='2025-7267', should_exist=True)
    add.verify_text_on_page(text='2025-3288', should_exist=False)
    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)
    add.dropdown_without_input(add.request_type, option_text='Исходящая заявка')
    add.backspace_and_input(add.request_number, value='26-VZ-14', num=10)
    time.sleep(2)
    add.verify_text_on_page(text='2026-4742', should_exist=True)
    add.verify_text_on_page(text='2026-7081', should_exist=False)
    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)
    add.dropdown_without_input(add.request_type, option_text='Входящая заявка')
    add.input_in_field(add.request_number, value='VZ-15')
    time.sleep(2)
    add.verify_text_on_page(text='25-VZ-156', should_exist=True)
    add.verify_text_on_page(text='26-VZ-15', should_exist=False)
    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)
    add.dropdown_without_input(add.request_type, option_text='Исходящая заявка')
    add.backspace_and_input(add.request_number, value='VZ-15', num=10)
    time.sleep(2)
    add.verify_text_on_page(text='26-VZ-15', should_exist=True)
    add.verify_text_on_page(text='25-VZ-156', should_exist=False)
    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)


@allure.story("Extended path test")
@allure.feature('Фильтры списка Заявок')
@allure.description('ЛКП, Тестирование фильтров в разделе "Заявки на доставки груза" ')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_filters_new_ftl_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.cdr_active_list_button,
                           do_assert=True, wait="lst")

    add = NewFtlFilters(base.driver)
    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')

    # Проверка фильтра 'Тип доставки'
    add.dropdown_without_input(add.delivery_type, option_text='FTL')
    add.input_in_field(add.request_number, value='59')
    time.sleep(2)
    add.verify_text_on_page(text='2026-4410', should_exist=True)
    add.verify_text_on_page(text='2026-8857', should_exist=False)
    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)
    add.dropdown_without_input(add.delivery_type, option_text='LTL')
    add.backspace_and_input(add.request_number, value='173', num=10)
    time.sleep(2)
    add.verify_text_on_page(text='25-VZ-173', should_exist=True)
    add.verify_text_on_page(text='25-VZ-170', should_exist=False)
    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)

    # Проверка фильтра 'Номер заявки'
    add.input_in_field(add.request_number, value='195')
    time.sleep(2)
    add.verify_text_on_page(text='25-VZ-195', should_exist=True)
    add.verify_text_on_page(text='25-VZ-194', should_exist=False)
    time.sleep(2)
    add.backspace_and_input(add.request_number, value='25-VZ-166', num=10)
    time.sleep(2)
    add.verify_text_on_page(text='2025-9672', should_exist=True)
    add.verify_text_on_page(text='2025-8022', should_exist=False)
    add.click_button(add.clear)
    add.dropdown_without_input(add.execution_start_sate, option_text='За все время')
    time.sleep(2)





























































