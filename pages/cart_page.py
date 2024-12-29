from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage): # Класс для работы со страницей Корзины
    def check_count_of_items(self): # Проверка совпадения количества выбранных товаров с общим количеством товаров в карзине
        count_of_items = 0
        items = self.browser.find_elements(By.CSS_SELECTOR, 'input[data-selector="quantity-group-input"]')
        for item in items:
            count_of_items += int(item.get_attribute("value"))

        count_in_order_WE = self.browser.find_element(By.CSS_SELECTOR, '.basket-summary__btn-more .js-more')
        count_in_order = int(count_in_order_WE.text.split()[0])

        assert count_of_items == count_in_order, "Количество товаров в корзине не совпадает с количеством выбранных товаров!" # В случае не сопадения - укажет ошибку