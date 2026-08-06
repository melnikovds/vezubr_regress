import allure
import pytest
import time
from pages.profile_page import Profile


@allure.story("Smoke test")
@allure.feature('Редактирование профиля')
@allure.description('ЛКЭ. Тест проверка профиля')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
@pytest.mark.smoke
def test_profile_check_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к профилю
    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    # Изменение почтового адресов
    a = base.get_timestamp()
    profile.backspace_and_input(profile.post_address_input, a)
    # Копирование ссылки контура
    profile.click_button(profile.contour_link, do_assert=True)
    # Сохранение изменений
    profile.click_button(profile.save_button, do_assert=True)
    profile.click_button(profile.confirm_button)

    profile.reload_page()
    time.sleep(5)
    profile.verify_text_on_page(text=a, should_exist=True)

    # Переход к вкладке дополнительной информации
    profile.click_button(profile.additional_info_tab, do_assert=True)
    # Изменение расчетного счета и БИК
    b = base.random_value_float_str(40500000000000000000, 40599999999999999999)
    profile.backspace_and_input(profile.checking_account_input, b)
    profile.backspace_and_input(profile.bik_input, "046577904")
    # Сохранение изменений
    profile.click_button(profile.save_button, do_assert=True)
    profile.click_button(profile.confirm_button)

    profile.reload_page()
    time.sleep(5)
    profile.verify_text_on_page(text=b, should_exist=True)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Редактирование профиля')
@allure.description('ЛКЗ. Тест редактирования профиля: адреса - А-timestamp, тлф - Рандом, '
                    'налогообложение - Перебор всех вариантов без сохранения, документообор - Вкл./Выкл, '
                    'ссылка контура - Копирование, счет - 405+Рандом, бик - Фикс.')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_profile_edit_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к профилю
    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    # Изменение почтового адресов
    profile.backspace_and_input(profile.post_address_input, f"ПА-{base.get_timestamp()}")
    # Изменение номера телефона
    profile.backspace_and_input(profile.phone_input, base.random_value_float_str(9000000000, 9999999999))

    # Перебор всех вариантов налогообложения
    profile.dropdown_without_input(profile.vat_type_select, "Без НДС")
    profile.dropdown_without_input(profile.vat_type_select, "5%")
    profile.dropdown_without_input(profile.direct_request_select, "Только плательщикам НДС")
    profile.dropdown_without_input(profile.values_in_system_select, option_text="С НДС", index=1)
    profile.click_button(profile.save_button, do_assert=True)
    profile.click_button(profile.confirm_button)

    profile.reload_page()
    time.sleep(5)
    profile.verify_text_on_page(text="5%", should_exist=True)
    profile.verify_text_on_page(text="Только плательщикам НДС", should_exist=True)
    profile.verify_text_on_page(text="С НДС", should_exist=True)

    profile.dropdown_without_input(profile.vat_type_select, "7%")
    profile.dropdown_without_input(profile.vat_type_select, "22%")
    profile.dropdown_without_input(profile.direct_request_select, "Только неплательщикам НДС")
    profile.dropdown_without_input(profile.direct_request_select, "Всем")
    profile.dropdown_without_input(profile.values_in_system_select, option_text="Без НДС", index=2)
    profile.click_button(profile.save_button, do_assert=True)
    profile.click_button(profile.confirm_button)

    profile.reload_page()
    time.sleep(5)
    profile.verify_text_on_page(text="22%", should_exist=True)
    profile.verify_text_on_page(text="Всем", should_exist=True)
    profile.verify_text_on_page(text="Без НДС", should_exist=True)

    # Включение и отключение электронного документооборота
    profile.click_button(profile.electronic_document_toggl)
    profile.click_button(profile.electronic_document_toggl)
    # Копирование ссылки контура
    profile.click_button(profile.contour_link, do_assert=True)
    # Сохранение изменений
    profile.click_button(profile.save_button, do_assert=True)
    profile.click_button(profile.confirm_button)

    # Прокрутка страницы вверх
    base.driver.execute_script("window.scrollTo(0, 0);")

    # Переход к вкладке дополнительной информации
    profile.click_button(profile.additional_info_tab, do_assert=True)
    # Изменение расчетного счета и БИК
    profile.backspace_and_input(profile.checking_account_input,
                                base.random_value_float_str(40500000000000000000, 40599999999999999999))
    profile.backspace_and_input(profile.bik_input, "046577904")
    # Сохранение изменений
    profile.click_button(profile.save_button, do_assert=True)
    profile.click_button(profile.confirm_button)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Редактирование профиля')
@allure.description('ЛКЭ. Тест редактирования профиля: адреса - А-timestamp, тлф - Рандом, '
                    'налогообложение - Перебор всех вариантов без сохранения, документообор - Вкл./Выкл, '
                    'ссылка контура - Копирование, счет - 405+Рандом, бик - Фикс.')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_profile_edit_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к профилю
    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    # Изменение почтового адресов
    profile.backspace_and_input(profile.post_address_input, f"ПА-{base.get_timestamp()}")
    # Изменение номера телефона
    profile.backspace_and_input(profile.phone_input, base.random_value_float_str(9000000000, 9999999999))
    # Перебор всех вариантов налогообложения
    profile.dropdown_without_input(profile.vat_type_select, "Без НДС")
    profile.dropdown_without_input(profile.vat_type_select, "22%")
    profile.dropdown_without_input(profile.direct_request_select, "Только плательщикам НДС")
    profile.dropdown_without_input(profile.direct_request_select, "Только неплательщикам НДС")
    profile.dropdown_without_input(profile.direct_request_select, "Всем")
    profile.dropdown_without_input(profile.values_in_system_select, option_text="Без НДС", index=2)
    profile.dropdown_without_input(profile.values_in_system_select, option_text="С НДС", index=1)

    # Включение и отключение электронного документооборота
    profile.click_button(profile.electronic_document_toggl)
    profile.click_button(profile.electronic_document_toggl)
    # Копирование ссылки контура
    profile.click_button(profile.contour_link, do_assert=True)
    # Сохранение изменений
    profile.click_button(profile.save_button, do_assert=True)
    profile.click_button(profile.confirm_button)

    # Прокрутка страницы вверх
    base.driver.execute_script("window.scrollTo(0, 0);")

    # Переход к вкладке дополнительной информации
    profile.click_button(profile.additional_info_tab, do_assert=True)
    # Изменение расчетного счета и БИК
    profile.backspace_and_input(profile.checking_account_input,
                                base.random_value_float_str(40500000000000000000, 40599999999999999999))
    profile.backspace_and_input(profile.bik_input, "046577904")
    # Сохранение изменений
    profile.click_button(profile.save_button, do_assert=True)
    profile.click_button(profile.confirm_button)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Редактирование профиля')
@allure.description('ЛКП. Тест редактирования профиля: адреса - А-timestamp, тлф - Рандом, '
                    'налогообложение - Перебор всех вариантов без сохранения, документообор - Вкл./Выкл, '
                    'ссылка контура - Копирование, счет - 405+Рандом, бик - Фикс.')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_profile_edit_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к профилю
    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    # Изменение почтового адресов
    profile.backspace_and_input(profile.post_address_input, f"ПА-{base.get_timestamp()}")
    # Изменение номера телефона
    profile.backspace_and_input(profile.phone_input, base.random_value_float_str(9000000000, 9999999999))

    # Перебор всех вариантов налогообложения
    profile.dropdown_without_input(profile.vat_type_select, "Без НДС")
    profile.dropdown_without_input(profile.vat_type_select, "5%")
    profile.dropdown_without_input(profile.direct_request_select, "Только плательщикам НДС")
    profile.dropdown_without_input(profile.values_in_system_select, option_text="С НДС", index=1)
    profile.click_button(profile.save_button, do_assert=True)
    profile.click_button(profile.confirm_button)

    profile.reload_page()
    time.sleep(5)
    profile.verify_text_on_page(text="5%", should_exist=True)
    profile.verify_text_on_page(text="Только плательщикам НДС", should_exist=True)
    profile.verify_text_on_page(text="С НДС", should_exist=True)

    profile.dropdown_without_input(profile.vat_type_select, "7%")
    profile.dropdown_without_input(profile.vat_type_select, "22%")
    profile.dropdown_without_input(profile.direct_request_select, "Только неплательщикам НДС")
    profile.dropdown_without_input(profile.direct_request_select, "Всем")
    profile.dropdown_without_input(profile.values_in_system_select, option_text="Без НДС", index=2)
    profile.click_button(profile.save_button, do_assert=True)
    profile.click_button(profile.confirm_button)

    profile.reload_page()
    time.sleep(5)
    profile.verify_text_on_page(text="22%", should_exist=True)
    profile.verify_text_on_page(text="Всем", should_exist=True)
    profile.verify_text_on_page(text="Без НДС", should_exist=True)

    # Включение и отключение электронного документооборота
    profile.click_button(profile.electronic_document_toggl)
    profile.click_button(profile.electronic_document_toggl)
    # Копирование ссылки контура
    profile.click_button(profile.contour_link, do_assert=True)
    # Сохранение изменений
    profile.click_button(profile.save_button, do_assert=True)
    profile.click_button(profile.confirm_button)

    # Прокрутка страницы вверх
    base.driver.execute_script("window.scrollTo(0, 0);")

    # Переход к вкладке дополнительной информации
    profile.click_button(profile.additional_info_tab, do_assert=True)
    # Изменение расчетного счета и БИК
    profile.backspace_and_input(profile.checking_account_input,
                                base.random_value_float_str(40500000000000000000, 40599999999999999999))
    profile.backspace_and_input(profile.bik_input, "046577904")
    # Сохранение изменений
    profile.click_button(profile.save_button, do_assert=True)
    profile.click_button(profile.confirm_button)
    # Конец теста

