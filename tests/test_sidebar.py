import allure
import pytest
import time


@allure.story("Smoke test")
@allure.feature('Боковое меню')
@allure.description('ЛКЗ. Тест бокового меню: переход по всем вкладкам, '
                    'ожидание прогрузки, проверка вкладки по названию')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_sidebar_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Монитор и создание Заявок
    sidebar.click_button(sidebar.delivery_monitor_button, do_assert=True)
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_delivery_request_button,
                           do_assert=True, wait="form")
    sidebar.click_button(sidebar.delivery_monitor_button, do_assert=True)
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_delivery_regular_request_button,
                           do_assert=True)
    sidebar.click_button(sidebar.delivery_monitor_button, do_assert=True)
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_additional_request_button)
    time.sleep(1)

    # Заявки
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.cdr_active_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.delivery_regular_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.routing_results_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.asr_active_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Задания
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.tasks_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.dispatch_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Контрагенты
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.insurers_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.go_gp_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Реестры
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.registries_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Документооборот
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.ezz_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.etrn_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.for_signing_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.paper_documents_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Справочники
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Рейсы (OLD)
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.monitor_button)
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.new_ftl_city_button,
                           do_assert=True)
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.new_ftl_inter_button,
                           do_assert=True)
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_active_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.new_ftl_regular_button,
                           do_assert=True)
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.new_loaders_button,
                           do_assert=True)
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.deferred_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.regular_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_archive_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.transport_doc_old_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.registries_old_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Профиль
    sidebar.click_button(sidebar.profile_button, do_assert=True)
    time.sleep(1)

    # Настройки
    sidebar.click_button(sidebar.settings_button, do_assert=True)
    time.sleep(1)

    # Инструкции
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_client_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_producer_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_dispatcher_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_app_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.faq_button)
    time.sleep(1)

    # Выход
    sidebar.switch_to_original_window()
    sidebar.click_button(sidebar.exit_button)

    # Конец теста


@allure.story("Smoke test")
@allure.feature('Боковое меню')
@allure.description('ЛКЭ. Тест бокового меню: переход по всем вкладкам, ожидание прогрузки, '
                    'проверка вкладки по названию')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_sidebar_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Монитор и создание Заявок
    sidebar.click_button(sidebar.delivery_monitor_button, do_assert=True)
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_delivery_request_button,
                           do_assert=True, wait="form")
    sidebar.click_button(sidebar.delivery_monitor_button, do_assert=True)
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_delivery_regular_request_button,
                           do_assert=True)
    sidebar.click_button(sidebar.delivery_monitor_button, do_assert=True)
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_additional_request_button)
    time.sleep(1)

    # Заявки
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.cdr_active_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.delivery_regular_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.routing_results_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.asr_active_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Задания
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.tasks_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.dispatch_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Контрагенты
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.insurers_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.go_gp_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Реестры
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.reg_client_create_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.reg_producer_create_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.registries_client_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.registries_producer_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Документооборот
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.ezz_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.etrn_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.for_signing_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.paper_documents_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Справочники
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tractors_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.trailers_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Рейсы (OLD)
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.monitor_button)
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.new_ftl_city_button,
                           do_assert=True)
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.new_ftl_inter_button,
                           do_assert=True)
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_active_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.new_ftl_regular_button,
                           do_assert=True)
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.new_loaders_button,
                           do_assert=True)
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.deferred_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.regular_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_archive_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.reg_client_create_old_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.reg_producer_create_old_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.transport_doc_old_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.verification_doc_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.reg_client_old_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.reg_producer_old_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Профиль
    sidebar.click_button(sidebar.profile_button, do_assert=True)
    time.sleep(1)

    # Настройки
    sidebar.click_button(sidebar.settings_button, do_assert=True)
    time.sleep(1)

    # Инструкции
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_client_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_producer_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_dispatcher_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_app_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.faq_button)
    time.sleep(1)

    # Выход
    sidebar.switch_to_original_window()
    sidebar.click_button(sidebar.exit_button)

    # Конец теста


@allure.story("Smoke test")
@allure.feature('Боковое меню')
@allure.description('ЛКП. Тест бокового меню: '
                    'переход по всем вкладкам, ожидание прогрузки, проверка вкладки по названию')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_sidebar_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Монитор и Заявки
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.cdr_active_list_button,
                           do_assert=True, wait="lst")
    sidebar.click_button(sidebar.delivery_monitor_button, do_assert=True)
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.asr_active_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Отправления
    sidebar.click_button(sidebar.dispatch_list_button, do_assert=True, wait="lst")
    time.sleep(1)

    # Контрагенты
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.insurers_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Реестры
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.reg_client_create_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.registries_client_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Документооборот
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.ezz_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.etrn_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.for_signing_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.paper_documents_list_button,
                           do_assert=True, wait="lst")

    # Справочники
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tractors_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.trailers_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Рейсы (OLD)
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.monitor_button)
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_active_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_archive_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.reg_client_create_old_list_button_lkp,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.transport_doc_old_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.reg_client_old_list_button_lkp,
                           do_assert=True, wait="lst")
    time.sleep(1)

    # Профиль
    sidebar.click_button(sidebar.profile_button, do_assert=True)
    time.sleep(1)

    # Настройки
    sidebar.click_button(sidebar.settings_button, do_assert=True)
    time.sleep(1)

    # Инструкции
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_client_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_producer_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_dispatcher_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_app_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.faq_button)
    time.sleep(1)

    # Выход
    sidebar.switch_to_original_window()
    sidebar.click_button(sidebar.exit_button)

    # Конец теста

































