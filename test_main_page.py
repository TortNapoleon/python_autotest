from selenium import webdriver # Импорт драйвера
from locators import CategoryLocators, ItemsLocators
from pages.stack_page import StackPage
from pages.item_page import ItemPage
from pages.main_page import MainPage
from pages.cart_page import CartPage

def test_open_catalog():
    link = "https://navisale.ru" # Ссылка на сайт
    browser = webdriver.Firefox() # Определение браузера

    page = MainPage(browser, link) # Определение экземпляра основной страницы
    page.change_options_browser() # Изменение параметров браузера
    page.open() # Открытие сайта 

    page.open_catalog() # Нажатие на кнопку Каталог
    page.move_to_category(CategoryLocators.BAGS_AND_SUITCASES_CATEGORY_LOCATOR) # Подвинуть мышь на категорию Сумки и чемоданы
    page.select_subcategory(CategoryLocators.BAGS_SUBCATEGORY_LOCATOR) # Нажатие на кнопку подкатегории Сумки

    stack_page = StackPage(browser, browser.current_url) # Создание экземляра страницы со стеллажём товаров 
    stack_page.scroll_to_element(ItemsLocators.BAG_LINK) # Проскролить до карточки товара
    stack_page.select_element(ItemsLocators.BAG_LINK) # Нажатие на карточку товара

    item_page = ItemPage(browser, browser.current_url) # Определение экземпляра страницы товара 
    item_page.select_specifications("Black") # Выбор характеристик товара
    item_page.add_to_cart() # Нажатие на кнопку Добавить в корзину
    item_page.change_count_of_items(3) # Изменение количества товара

    page.open_catalog()
    page.move_to_category(CategoryLocators.WOMEN_CATEGORY_LOCATOR) # Указатель на категории Женщинам
    page.select_subcategory(CategoryLocators.WOMEN_SET_SUBCATEGORY_LOCATOR) # Нажатие на кнопку подкатегории Комплекты 

    stack_page = StackPage(browser, browser.current_url)
    stack_page.scroll_to_element(ItemsLocators.SET_OF_CLOTHES_LINK)
    stack_page.select_element(ItemsLocators.SET_OF_CLOTHES_LINK)

    item_page = ItemPage(browser, browser.current_url)
    item_page.select_specifications("S")
    item_page.add_to_cart()
    item_page.change_count_of_items(2)

    page.open_catalog()
    page.move_to_category(CategoryLocators.MAN_CATEGORY_LOCATOR) # Указатель на категории Мужчинам
    page.select_subcategory(CategoryLocators.MAN_TSHIRT_SUBCATEGORY_LOCATOR) # Нажатие на кнопку подкатегории Футболки 

    stack_page = StackPage(browser, browser.current_url)
    stack_page.scroll_to_element(ItemsLocators.TSHIRT_LINK)
    stack_page.select_element(ItemsLocators.TSHIRT_LINK)

    item_page = ItemPage(browser, browser.current_url)
    item_page.select_specifications("M")
    item_page.add_to_cart()
    item_page.change_count_of_items(4)

    page.open_cart() # Переход на страницу Корзины
    cart_page = CartPage(browser, browser.current_url)
    cart_page.check_count_of_items() # Проверка количества выбранных товаров и общего числа товаров в корзине

    page.close()