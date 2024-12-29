from pages.base_page import BasePage
from selenium.webdriver.common.by import By # Модуль для определения способа поиска элементов на странице
from selenium.webdriver import ActionChains # Модуль для автоматизации взаимодействий
from selenium.webdriver.support.ui import WebDriverWait # Модуль для работы с ожиданиями
from selenium.webdriver.support import expected_conditions as EC # Модуль для работы со стоянием Веб-элементов

class MainPage(BasePage): # Класс для взаимодействия основными элементами страниц
    def open_catalog(self): # Нажатие на кнопку Каталог
        mainscreen_catalog_button = self.browser.find_element(By.CSS_SELECTOR, ".header-rubrics-toggler__desktop.btn.btn_primary")
        mainscreen_catalog_button.click()
    
    def move_to_category(self, input_category): # Перемещение указателя на категорию
        category = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((input_category[0], input_category[1]))
        )
        actions = ActionChains(self.browser).move_to_element(category)
        actions.perform()

    def select_subcategory(self, input_subcategory): # Нажатие на кнопку подкатегории / Переход на страницу
        subcategory = self.browser.find_element(input_subcategory[0], input_subcategory[1])
        subcategory.click()

    def open_cart(self): # Нажатие на кнопку Корзины / Переход на страницу
        cart_button = self.browser.find_element(By.CSS_SELECTOR, '.header__toolbar-item[title="Перейти в корзину"]')
        cart_button.click()

