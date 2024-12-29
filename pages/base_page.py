class BasePage(): # Базовый класс для работы с браузером
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def change_options_browser(self, timeout=10):
        self.browser.maximize_window() # Развернуть окно
        self.browser.implicitly_wait(timeout) # Определение неявного ожидания

    def open(self):
        self.browser.get(self.url) # Открытие ссылки

    def close(self): # Закрытие браузера
        self.browser.quit()