# Импорт Playwright для синхронного режима и проверки
from playwright.sync_api import sync_playwright, expect

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()  # Создаем новую страницу

    # 1. Открываем страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # 2. Проверяем, что кнопка Login не активна
    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_disabled()

    # Если нужно проверить что кнопка активна
    # expect(login_button).not_to_be_disabled()


