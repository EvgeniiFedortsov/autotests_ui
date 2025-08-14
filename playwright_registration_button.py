from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # 1. Открыть страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    page.wait_for_load_state('networkidle')  # Ждем завершения сетевых запросов

    # 2. Проверяем, что кнопка "Registration" находится в состоянии disabled
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    # 3. Заполнить поле Email значением
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill("user.name@gmail.com")

    # 4. Заполнить поле Username значением: username
    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill("username")

    # 5. Заполнить поле Password значением: password
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill("password")

    # 6. Проверить, что кнопка "Registration" перешла в состояние enabled
    expect(registration_button).not_to_be_disabled()

    # Ждём 5 секунд для наглядности результата
    page.wait_for_timeout(5000)