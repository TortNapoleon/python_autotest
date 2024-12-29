import time # Импорт библиотеки для работы со временем и паузами
from pages.base_page import BasePage

class StackPage(BasePage): # Класс для работы со страницей со стеллажом товаров
    def scroll_to_element(self, item): # Проскролить до карточки товара
        item_card = self.browser.find_element(item[0], item[1])
        self.browser.execute_script("arguments[0].scrollIntoView()", item_card)

        time.sleep(1)

    def select_element(self, item): # Нажатие на товар / Переход на страницу
        item_card = self.browser.find_element(item[0], item[1])
        item_card.click()