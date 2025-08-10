# Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login
# Проверить наличие элементов: "Email", "Password", "Login"
# Нажать на ссылку "Registration", после чего произойдет редирект на страницу Registration
# Проверить наличие элементов: "Email", "Password", "Registration"


# Импорт Playwright для синхронного режима и проверки
from playwright.sync_api import sync_playwright, expect

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()  # Создаем новую страницу

    # Переходим на страницу авторизации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Проверяем наличие элементов: "Email", "Password", "Login" на странице авторизации

    # Находим поле "Email" и проверяем видимость
    login_email_input = page.get_by_test_id('login-form-email-input').locator('input')
    expect(login_email_input).to_be_visible()

    # Находим поле "Password" и проверяем видимость
    login_password_input = page.get_by_test_id('login-form-password-input').locator('input')
    expect(login_password_input).to_be_visible()

    # Находим кнопку "Login" и проевряем видимость
    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_visible()

    # Пауза на 5 секунд, чтобы увидеть результат
    page.wait_for_timeout(5000)

    # Нажимаем на ссылку "Registration"
    registration_link = page.get_by_test_id("login-page-registration-link")
    registration_link.click()

    # Проверяем наличие элементов: "Email", "Password", "Registration" на странице регистрации

    # Проверяем наличие элементов: "Email"
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(registration_email_input).to_be_visible()

    # Проверяем наличие элементов: "Password"
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(registration_password_input).to_be_visible()

    # Проверяем наличие элементов: "Registration"
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_visible()


    # Пауза на 5 секунд, чтобы увидеть результат
    page.wait_for_timeout(5000)