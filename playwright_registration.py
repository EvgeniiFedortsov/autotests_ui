# 1.Откроет страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
# 2.Заполнит поле "Email" значением "user.name@gmail.com"
# 3.Заполнит поле "Username" значением "username"
# 4.Заполнит поле "Password" значением "password"
# 5.Нажмет на кнопку "Registration". После нажатия кнопки "Registration" произойдет редирект на страницу "Dashboard"
# 6.Проверит, что на странице "Dashboard" отображается заголовок "Dashboard"


# Импорт Playwright для синхронного режима и проверки
from playwright.sync_api import sync_playwright, expect

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() # Создание контекста
    page = context.new_page()  # Создаем новую страницу

    # 1.Открываем страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")


    # 2. Проверяем наличие элементов: "Email" и заполняем данными
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    #expect(registration_email_input).to_be_visible()
    registration_email_input.fill("user.name@gmail.com")

    # 3. Проверяем наличие элементов: "Username" и заполняем данными
    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    #expect(registration_username_input).to_be_visible()
    registration_username_input.fill("username")

    # 4. Проверяем наличие элементов: "Password"
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    #expect(registration_password_input).to_be_visible()
    registration_password_input.fill("password")

    # 5. Проверяем наличие элементов: "Registration" и нажимаем кнопку
    registration_button = page.get_by_test_id('registration-page-registration-button')
    #expect(registration_button).to_be_visible()
    registration_button.click()

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser-state.json")





    # # 6. Проверяем наличие элементов: "Dashboard"
    # dashboard_page = page.get_by_test_id('dashboard-toolbar-title-text')
    # expect(dashboard_page).to_be_visible()
    # expect(dashboard_page).to_have_text("Dashboard")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    # Пауза на 5 секунд, чтобы увидеть результат
    page.wait_for_timeout(5000)