
# Импорт Playwright для синхронного режима и проверки
from playwright.sync_api import sync_playwright, expect

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() # Создание контекста
    page = context.new_page()  # Создаем новую страницу

    # 1. Открываем страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # 2. Заполняем форму регистрации

    # Заполняем поле "Email" данными
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill("user.name@gmail.com")

    # Заполняем поле "Username" данными
    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill("username")

    # Заполняем поле "Password" данными
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill("password")

    # Нажимаем кнопку "Registration"
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # 3. Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser-state.json")

    # 4. Создаем новую сессию браузера с сохраненным контекстом

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
    page = context.new_page()

    # 5. Переходим на страницу "Courses"
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # 6. Проверить наличие и текст заголовка "Courses"
    header_courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(header_courses).to_be_visible()  # Проверяем видимость элемента
    expect(header_courses).to_have_text("Courses")  # Проверяем текст

    # 7. Проверить наличие и текст блока "There is no results"
    no_results = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_results).to_be_visible()  # Проверяем видимость элемента
    expect(no_results).to_have_text("There is no results")  # Проверяем текст

    # 8. Проверить наличие и видимость иконки пустого блока
    no_results_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(no_results_icon).to_be_visible()

    # 9. Проверить наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
    no_results_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(no_results_description).to_be_visible()  # Проверяем видимость элемента
    expect(no_results_description).to_have_text("Results from the load test pipeline will be displayed here")


    # Пауза на 5 секунд, чтобы увидеть результат
    page.wait_for_timeout(5000)