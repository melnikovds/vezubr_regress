import time
import allure
import pytest
from pages.uploading_documents_page import UploadingDocumentsPage

MIN_FILE_SIZE = 1000  # Минимальный размер файла в байтах


# ==================== ТЕСТЫ LKZ ====================

@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKZ')
@allure.description('Тест выгрузки заявок на доставку груза для роли LKZ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_export_cdr_lkz(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Активные заявки'"):
        sidebar.move_and_click(
            move_to=sidebar.requests_hover,
            click_to=sidebar.cdr_active_list_button,
            do_assert=True,
            wait="lst"
        )
        time.sleep(2)

    with allure.step("Выгрузка заявок"):

        status, filename, content = page.export_cargo_delivery_requests_lkz()
        base.get_screenshot("step_2_export_completed")

    with allure.step("Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки заявок",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ЗАЯВОК УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKZ')
@allure.description('Тест выгрузки ГМ для роли LKZ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_export_gm_lkz(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Грузовые модули'"):
        sidebar.move_and_click(
            move_to=sidebar.assignments_hover,
            click_to=sidebar.cargo_place_list_button,
            do_assert=True,
            wait="lst"
        )
        time.sleep(2)

    with allure.step("Выгрузка ГМ"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки ГМ",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ГМ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKZ')
@allure.description('Тест выгрузки Контрагентов (Подрядчиков) для роли LKZ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_export_producer_lkz(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("Переход на страницу 'Подрядчики'"):
        sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                               do_assert=True, wait="lst")
        time.sleep(2)

    with allure.step("Выгрузка Подрядчиков"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки подрядчиков",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ПОДРЯДЧИКОВ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKZ')
@allure.description('Тест выгрузки Адресов для роли LKZ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_export_address_lkz(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("Переход на страницу 'Адреса'"):
        sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                               do_assert=True, wait="lst")
        time.sleep(2)

    with allure.step("Выгрузка Адресов"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки адресов",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА АДРЕСОВ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKZ')
@allure.description('Тест выгрузки Заявок OLD для роли LKZ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_export_active_order_lkz(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Активные заявки OLD'"):
        sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_active_list_button,
                               do_assert=True, wait="lst")
        time.sleep(2)

    with allure.step("2. Выгрузка заявок"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки заявок",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА АКТИВНЫХ ЗАЯВОК УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKZ')
@allure.description('Тест выгрузки Все рейсы OLD для роли LKZ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_export_all_order_lkz(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Все рейсы OLD'"):
        sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_list_button,
                               do_assert=True, wait="lst")
        time.sleep(2)

    with allure.step("2. Выгрузка Рейсов"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки рейсов",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА РЕЙСОВ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKZ')
@allure.description('Тест выгрузки Архив заявок для роли LKZ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_export_archive_order_lkz(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Архив заявок'"):
        sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_archive_list_button,
                               do_assert=True, wait="lst")
        time.sleep(2)

    with allure.step("2. Выгрузка Заявок"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки заявок",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА АРХИВА ЗАЯВОК УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKZ')
@allure.description('Тест выгрузки Пользователей для роли LKZ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_export_users_lkz(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Профиль'"):
        sidebar.click_button(sidebar.profile_button, do_assert=True)
        time.sleep(2)

    with allure.step("2. Выгрузка Пользователей"):
        status, filename, content = page.export_users_lkz()
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки пользователей",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ПОЛЬЗОВАТЕЛЕЙ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKZ')
@allure.description('Тест выгрузки Застрахованных рейсов для роли LKZ')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)
def test_export_insured_flights_lkz(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Страховщики'"):
        sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.insurers_list_button,
                               do_assert=True, wait="lst")
        time.sleep(2)

    with allure.step("2. Выгрузка Застрахованных рейсов"):
        status, filename, content = page.export_insurance_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки рейсов",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ЗАСТРАХОВАННЫХ РЕЙСОВ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)

@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKZ')
@allure.description('Тест выгрузки Тарифов для роли LKZ (прямая выгрузка)')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_export_tariffs_lkz(base_fixture):
    """
    Тест выгрузки тарифов для LKZ.
    Переход: Боковое меню -> Справочники -> Тарифы -> Выгрузить
    """
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Тарифы'"):
        sidebar.move_and_click(
            move_to=sidebar.directories_hover,
            click_to=sidebar.tariffs_list_button,
            do_assert=True,
            wait="lst"
        )
        time.sleep(2)
        base.get_screenshot("step_1_tariffs_page")

    with allure.step("2. Выгрузка тарифов (прямая выгрузка)"):
        status, filename, content = page.export_direct_download(
            expected_filename_pattern="Тарифы"
        )
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.csv') or filename.endswith('.xlsx'), \
            f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > 1000, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}",
            "Результат выгрузки тарифов",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ТАРИФОВ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


# ==================== ТЕСТЫ LKE ====================

@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKE')
@allure.description('Тест выгрузки Заявки на доставку Груза для роли LKE')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_export_cdr_lke(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Заявки на доставку Груза'"):
        sidebar.move_and_click(
            move_to=sidebar.requests_hover,
            click_to=sidebar.cdr_active_list_button,
            do_assert=True,
            wait="lst"
        )

    with allure.step("2. Выгрузка Заявок"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки заявок",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА АРХИВА ЗАЯВОК НА ДОСТАВКУ ГРУЗА УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKE')
@allure.description('Тест выгрузки ГМ для роли LKE')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_export_gm_lke(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Грузоместа'"):
        sidebar.move_and_click(
            move_to=sidebar.assignments_hover,
            click_to=sidebar.cargo_place_list_button,
            do_assert=True,
            wait="lst"
        )
        time.sleep(2)

    with allure.step("Выгрузка ГМ"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки ГМ",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ГМ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKE')
@allure.description('Тест выгрузки Контрагентов (Заказчиков) для роли LKE')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_export_client_lke(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("Переход на страницу 'Заказчики'"):
        sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                               do_assert=True, wait="lst")
        time.sleep(2)

    with allure.step("Выгрузка Заказчиков"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки Заказчиков",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ЗАКАЗЧИКОВ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKE')
@allure.description('Тест выгрузки Контрагентов (Подрядчиков) для роли LKE')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_export_producer_lke(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("Переход на страницу 'Подрядчики'"):
        sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                               do_assert=True, wait="lst")
        time.sleep(2)

    with allure.step("Выгрузка Подрядчиков"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки подрядчиков",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ПОДРЯДЧИКОВ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKE')
@allure.description('Тест выгрузки Адресов для роли LKE')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_export_address_lke(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("Переход на страницу 'Адреса'"):
        sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                               do_assert=True, wait="lst")
        time.sleep(2)

    with allure.step("Выгрузка Адресов"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки адресов",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА АДРЕСОВ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKE')
@allure.description('Тест выгрузки Заявок OLD для роли LKE')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_export_active_order_lke(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Активные заявки OLD'"):
        sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_active_list_button,
                               do_assert=True, wait="lst")
        time.sleep(2)

    with allure.step("2. Выгрузка заявок"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки заявок",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА АКТИВНЫХ ЗАЯВОК УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKE')
@allure.description('Тест выгрузки Все рейсы OLD для роли LKE')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_export_all_order_lke(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Все рейсы OLD'"):
        sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_list_button,
                               do_assert=True, wait="lst")
        time.sleep(2)

    with allure.step("2. Выгрузка Рейсов"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки рейсов",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА РЕЙСОВ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKE')
@allure.description('Тест выгрузки Архив заявок для роли LKE')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_export_archive_order_lke(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Архив заявок'"):
        sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_archive_list_button,
                               do_assert=True, wait="lst")
        time.sleep(2)

    with allure.step("2. Выгрузка Заявок"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки заявок",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА АРХИВА ЗАЯВОК УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKE')
@allure.description('Тест выгрузки Пользователей для роли LKE')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_export_users_lke(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Профиль'"):
        sidebar.click_button(sidebar.profile_button, do_assert=True)
        time.sleep(2)

    with allure.step("2. Выгрузка Пользователей"):
        status, filename, content = page.export_users_lkz()
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки пользователей",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ПОЛЬЗОВАТЕЛЕЙ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKE')
@allure.description('Тест выгрузки Застрахованных рейсов для роли LKE')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_export_insured_flights_lke(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Страховщики'"):
        sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.insurers_list_button,
                               do_assert=True, wait="lst")
        time.sleep(2)

    with allure.step("2. Выгрузка Застрахованных рейсов"):
        status, filename, content = page.export_insurance_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки рейсов",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ЗАСТРАХОВАННЫХ РЕЙСОВ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKE')
@allure.description('Тест выгрузки Водителей для роли LKE (прямая выгрузка)')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_export_drivers_lke(base_fixture):
    """
    Тест выгрузки водителей для LKE.
    Переход: Боковое меню -> Справочники -> Водители -> Выгрузить
    """
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Водители'"):
        sidebar.move_and_click(
            move_to=sidebar.directories_hover,
            click_to=sidebar.drivers_list_button,
            do_assert=True,
            wait="lst"
        )
        time.sleep(2)
        base.get_screenshot("step_1_drivers_page")

    with allure.step("2. Выгрузка водителей (прямая выгрузка)"):
        status, filename, content = page.export_direct_download(
            expected_filename_pattern="Список_водителей"
        )
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.csv') or filename.endswith('.xlsx'), \
            f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > 1000, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}",
            "Результат выгрузки водителей",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ВОДИТЕЛЕЙ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKE')
@allure.description('Тест выгрузки ТС для роли LKE (прямая выгрузка)')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_export_ts_lke(base_fixture):
    """
    Тест выгрузки ТС (транспортных средств) для LKE.
    Переход: Боковое меню -> Справочники -> ТС -> Выгрузить
    """
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'ТС'"):
        sidebar.move_and_click(
            move_to=sidebar.directories_hover,
            click_to=sidebar.transports_list_button,
            do_assert=True,
            wait="lst"
        )
        time.sleep(2)
        base.get_screenshot("step_1_ts_page")

    with allure.step("2. Выгрузка ТС (прямая выгрузка)"):
        status, filename, content = page.export_direct_download(
            expected_filename_pattern="Список_ТС"
        )
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.csv') or filename.endswith('.xlsx'), \
            f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > 1000, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}",
            "Результат выгрузки ТС",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ТС УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)

@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKE')
@allure.description('Тест выгрузки Тягачей для роли LKE (прямая выгрузка)')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_export_tractors_lke(base_fixture):
    """
    Тест выгрузки тягачей для LKP.
    Переход: Боковое меню -> Справочники -> Тягачи -> Выгрузить
    """
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Тягачи'"):
        sidebar.move_and_click(
            move_to=sidebar.directories_hover,
            click_to=sidebar.tractors_list_button,
            do_assert=True,
            wait="lst"
        )
        time.sleep(2)
        base.get_screenshot("step_1_tractors_page")

    with allure.step("2. Выгрузка тягачей (прямая выгрузка)"):
        status, filename, content = page.export_direct_download(
            expected_filename_pattern="Список_Тягачей"
        )
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.csv') or filename.endswith('.xlsx'), \
            f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > 1000, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}",
            "Результат выгрузки тягачей",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ТЯГАЧЕЙ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)

@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKE')
@allure.description('Тест выгрузки Полуприцепов для роли LKE (прямая выгрузка)')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_export_trailers_lke(base_fixture):
    """
    Тест выгрузки полуприцепов для LKP.
    Переход: Боковое меню -> Справочники -> Полуприцепы -> Выгрузить
    """
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Полуприцепы'"):
        sidebar.move_and_click(
            move_to=sidebar.directories_hover,
            click_to=sidebar.trailers_list_button,
            do_assert=True,
            wait="lst"
        )
        time.sleep(2)
        base.get_screenshot("step_1_trailers_page")

    with allure.step("2. Выгрузка полуприцепов (прямая выгрузка)"):
        status, filename, content = page.export_direct_download(
            expected_filename_pattern="Список_Полуприцепов"
        )
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.csv') or filename.endswith('.xlsx'), \
            f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > 1000, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}",
            "Результат выгрузки полуприцепов",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ПОЛУПРИЦЕПОВ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)

@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKE')
@allure.description('Тест выгрузки Тарифов для роли LKE (прямая выгрузка)')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)
def test_export_tariffs_lke(base_fixture):
    """
    Тест выгрузки тарифов для LKE.
    Переход: Боковое меню -> Справочники -> Тарифы -> Выгрузить
    """
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Тарифы'"):
        sidebar.move_and_click(
            move_to=sidebar.directories_hover,
            click_to=sidebar.tariffs_list_button,
            do_assert=True,
            wait="lst"
        )
        time.sleep(2)
        base.get_screenshot("step_1_tariffs_page")

    with allure.step("2. Выгрузка тарифов (прямая выгрузка)"):
        status, filename, content = page.export_direct_download(
            expected_filename_pattern="Тарифы"
        )
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.csv') or filename.endswith('.xlsx'), \
            f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > 1000, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}",
            "Результат выгрузки тарифов",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ТАРИФОВ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


# ==================== ТЕСТЫ LKP ====================

@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKP')
@allure.description('Тест выгрузки Заявки на доставку Груза для роли LKP')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_export_cdr_lkp(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Заявки на доставку Груза'"):
        sidebar.move_and_click(
            move_to=sidebar.requests_hover,
            click_to=sidebar.cdr_active_list_button,
            do_assert=True,
            wait="lst"
        )

    with allure.step("2. Выгрузка Заявок"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки заявок",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА АРХИВА ЗАЯВОК НА ДОСТАВКУ ГРУЗА УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKP')
@allure.description('Тест выгрузки Контрагентов (Заказчиков) для роли LKP')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_export_client_lkp(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("Переход на страницу 'Заказчики'"):
        sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                               do_assert=True, wait="lst")
        time.sleep(2)

    with allure.step("Выгрузка Заказчиков"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки Заказчиков",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ЗАКАЗЧИКОВ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKP')
@allure.description('Тест выгрузки Заявок OLD для роли LKP')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_export_active_order_lkp(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Активные заявки OLD'"):
        sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_active_list_button,
                               do_assert=True, wait="lst")
        time.sleep(2)

    with allure.step("2. Выгрузка заявок"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки заявок",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА АКТИВНЫХ ЗАЯВОК УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKP')
@allure.description('Тест выгрузки Все рейсы OLD для роли LKP')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_export_all_order_lkp(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Все рейсы OLD'"):
        sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_list_button,
                               do_assert=True, wait="lst")
        time.sleep(2)

    with allure.step("2. Выгрузка Рейсов"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки рейсов",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА РЕЙСОВ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKP')
@allure.description('Тест выгрузки Архив заявок для роли LKP')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_export_archive_order_lkp(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Архив заявок'"):
        sidebar.move_and_click(move_to=sidebar.orders_old_hover, click_to=sidebar.ftl_archive_list_button,
                               do_assert=True, wait="lst")
        time.sleep(2)

    with allure.step("2. Выгрузка Заявок"):
        status, filename, content = page.export_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки заявок",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА АРХИВА ЗАЯВОК УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKP')
@allure.description('Тест выгрузки Пользователей для роли LKP')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_export_users_lkp(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Профиль'"):
        sidebar.click_button(sidebar.profile_button, do_assert=True)
        time.sleep(2)

    with allure.step("2. Выгрузка Пользователей"):
        status, filename, content = page.export_users_lkz()
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки пользователей",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ПОЛЬЗОВАТЕЛЕЙ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKP')
@allure.description('Тест выгрузки Застрахованных рейсов для роли LKP')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_export_insured_flights_lkp(base_fixture):
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Страховщики'"):
        sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.insurers_list_button,
                               do_assert=True, wait="lst")
        time.sleep(2)

    with allure.step("2. Выгрузка Застрахованных рейсов"):
        status, filename, content = page.export_insurance_all()
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.xlsx'), f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > MIN_FILE_SIZE, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        if content[:4] == b'PK\x03\x04':
            print("✅ Сигнатура файла: ZIP (Microsoft Excel .xlsx)")
        elif content[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            print("✅ Сигнатура файла: OLE (Microsoft Excel .xls)")
        else:
            print(f"⚠️ Неизвестная сигнатура файла: {content[:8].hex()}")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}\n"
            f"🔢 Первые 20 байт: {content[:20].hex()}",
            "Результат выгрузки рейсов",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ЗАСТРАХОВАННЫХ РЕЙСОВ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKP')
@allure.description('Тест выгрузки Водителей для роли LKP (прямая выгрузка)')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_export_drivers_lkp(base_fixture):
    """
    Тест выгрузки водителей для LKP.
    Переход: Боковое меню -> Справочники -> Водители -> Выгрузить
    """
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Водители'"):
        sidebar.move_and_click(
            move_to=sidebar.directories_hover,
            click_to=sidebar.drivers_list_button,
            do_assert=True,
            wait="lst"
        )
        time.sleep(2)
        base.get_screenshot("step_1_drivers_page")

    with allure.step("2. Выгрузка водителей (прямая выгрузка)"):
        status, filename, content = page.export_direct_download(
            expected_filename_pattern="Список_водителей"
        )
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.csv') or filename.endswith('.xlsx'), \
            f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > 1000, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}",
            "Результат выгрузки водителей",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ВОДИТЕЛЕЙ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKP')
@allure.description('Тест выгрузки ТС для роли LKP (прямая выгрузка)')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_export_ts_lkp(base_fixture):
    """
    Тест выгрузки ТС (транспортных средств) для LKP.
    Переход: Боковое меню -> Справочники -> ТС -> Выгрузить
    """
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'ТС'"):
        sidebar.move_and_click(
            move_to=sidebar.directories_hover,
            click_to=sidebar.transports_list_button,
            do_assert=True,
            wait="lst"
        )
        time.sleep(2)
        base.get_screenshot("step_1_ts_page")

    with allure.step("2. Выгрузка ТС (прямая выгрузка)"):
        status, filename, content = page.export_direct_download(
            expected_filename_pattern="Список_ТС"
        )
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.csv') or filename.endswith('.xlsx'), \
            f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > 1000, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}",
            "Результат выгрузки ТС",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ТС УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)

@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKP')
@allure.description('Тест выгрузки Тягачей для роли LKP (прямая выгрузка)')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_export_tractors_lkp(base_fixture):
    """
    Тест выгрузки тягачей для LKP.
    Переход: Боковое меню -> Справочники -> Тягачи -> Выгрузить
    """
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Тягачи'"):
        sidebar.move_and_click(
            move_to=sidebar.directories_hover,
            click_to=sidebar.tractors_list_button,
            do_assert=True,
            wait="lst"
        )
        time.sleep(2)
        base.get_screenshot("step_1_tractors_page")

    with allure.step("2. Выгрузка тягачей (прямая выгрузка)"):
        status, filename, content = page.export_direct_download(
            expected_filename_pattern="Список_Тягачей"
        )
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.csv') or filename.endswith('.xlsx'), \
            f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > 1000, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}",
            "Результат выгрузки тягачей",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ТЯГАЧЕЙ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)

@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKP')
@allure.description('Тест выгрузки Полуприцепов для роли LKP (прямая выгрузка)')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_export_trailers_lkp(base_fixture):
    """
    Тест выгрузки полуприцепов для LKP.
    Переход: Боковое меню -> Справочники -> Полуприцепы -> Выгрузить
    """
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Полуприцепы'"):
        sidebar.move_and_click(
            move_to=sidebar.directories_hover,
            click_to=sidebar.trailers_list_button,
            do_assert=True,
            wait="lst"
        )
        time.sleep(2)
        base.get_screenshot("step_1_trailers_page")

    with allure.step("2. Выгрузка полуприцепов (прямая выгрузка)"):
        status, filename, content = page.export_direct_download(
            expected_filename_pattern="Список_Полуприцепов"
        )
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.csv') or filename.endswith('.xlsx'), \
            f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > 1000, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}",
            "Результат выгрузки полуприцепов",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ПОЛУПРИЦЕПОВ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)


@allure.story("Выгрузки документов")
@allure.feature('Экспорт данных LKP')
@allure.description('Тест выгрузки Тарифов для роли LKP (прямая выгрузка)')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)
def test_export_tariffs_lkp(base_fixture):
    """
    Тест выгрузки тарифов для LKP.
    Переход: Боковое меню -> Справочники -> Тарифы -> Выгрузить
    """
    base, sidebar = base_fixture
    page = UploadingDocumentsPage(base.driver)

    with allure.step("1. Переход на страницу 'Тарифы'"):
        sidebar.move_and_click(
            move_to=sidebar.directories_hover,
            click_to=sidebar.tariffs_list_button,
            do_assert=True,
            wait="lst"
        )
        time.sleep(2)
        base.get_screenshot("step_1_tariffs_page")

    with allure.step("2. Выгрузка тарифов (прямая выгрузка)"):
        status, filename, content = page.export_direct_download(
            expected_filename_pattern="Тарифы"
        )
        base.get_screenshot("step_2_export_completed")

    with allure.step("3. Проверка результата"):
        assert status == 200, f"Ошибка скачивания: статус {status}"
        print(f"✅ Статус ответа: {status} (OK)")

        assert filename.endswith('.csv') or filename.endswith('.xlsx'), \
            f"Неверный формат файла: {filename}"
        print(f"✅ Формат файла: {filename.split('.')[-1].upper()}")

        file_size_kb = len(content) / 1024
        assert len(content) > 1000, f"Файл слишком маленький: {len(content)} байт"
        print(f"✅ Размер файла: {len(content)} байт ({file_size_kb:.2f} KB)")

        assert len(content) > 0, "Файл пустой"
        print(f"✅ Файл содержит данные: {len(content)} байт")

        print(f"📄 Имя файла: {filename}")

        allure.attach(
            f"✅ Статус: {status}\n"
            f"📄 Имя файла: {filename}\n"
            f"📊 Размер: {len(content)} байт ({file_size_kb:.2f} KB)\n"
            f"📁 Формат: {filename.split('.')[-1].upper()}",
            "Результат выгрузки тарифов",
            allure.attachment_type.TEXT
        )

        print("\n" + "=" * 50)
        print("🎉 ВЫГРУЗКА ТАРИФОВ УСПЕШНО ЗАВЕРШЕНА!")
        print(f"📄 Файл: {filename}")
        print(f"📊 Размер: {file_size_kb:.2f} KB ({len(content)} байт)")
        print("=" * 50)
