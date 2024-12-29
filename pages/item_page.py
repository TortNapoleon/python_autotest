from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ItemPage(BasePage): # Класс для работы со страницей товара
    def select_specifications(self, spec): # Выбор характеристик товара
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn[title="Добавить в корзину"]'))
        )
        specification = self.browser.find_element(By.CSS_SELECTOR, \
                                                  f'[data-selector="variations"] label[data-aspect-name="{spec}"]')
        specification.click()

    def add_to_cart(self): # Нажатие на кнопку Добавить в корзину
        add_to_cart_button = self.browser.find_element(By.CSS_SELECTOR, '.btn[title="Добавить в корзину"]')
        add_to_cart_button.click()

    def change_count_of_items(self, count): # Изменение количества товаров
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.btn[data-selector="go-to-cart"]'))
        )
        count_items = self.browser.find_element(By.CSS_SELECTOR, 'input[name="basket_add[quantity]"]')
        count_items.clear()
        count_items.send_keys(count)
        
        WebDriverWait(self.browser, 10).until(
            EC.element_attribute_to_include((By.CSS_SELECTOR, 'input[name="basket_add[quantity]"]'), "disabled")
        )
