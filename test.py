import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://navisale.ru")
browser.implicitly_wait(5)

time.sleep(3)

mainscreen_catalog_button = browser.find_element(By.CSS_SELECTOR, ".header-rubrics-toggler__desktop.btn.btn_primary")
mainscreen_catalog_button.click()

category1_hud_male_button = browser.find_element(By.CSS_SELECTOR, ".mega-burger-sidebar-menu__link[title='Мужчинам']")
time.sleep(3)

actions = ActionChains(browser).move_to_element(category1_hud_male_button)
actions.perform()

category1_hud_tshirt_button = browser.find_element(By.CSS_SELECTOR, """.mega-burger-content-menu__column [data-event-click='{"event":"dropdown_menu_click","rubricId":1286190}']""")
category1_hud_tshirt_button.click()

tshirt_card = browser.find_element(By.CSS_SELECTOR, \
    """.product-listing-card [href="/p-zarahome-men-s-brown-t-shirt-V132381534"]""")
tshirt_card.click()

WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn[title="Добавить в корзину"]'))
)

tshirt_size = browser.find_element(By.CSS_SELECTOR, \
    '[data-selector="variations"] label[data-aspect-name="S"]')
tshirt_size.click()

add_to_cart_button = browser.find_element(By.CSS_SELECTOR, '.btn[title="Добавить в корзину"]')
add_to_cart_button.click()

time.sleep(1)

count_items = browser.find_element(By.CSS_SELECTOR, 'input[name="basket_add[quantity]"]')
count_items.clear()
count_items.send_keys(3)


# Второй товар

time.sleep(3)

mainscreen_catalog_button = browser.find_element(By.CSS_SELECTOR, ".header-rubrics-toggler__desktop.btn.btn_primary")
mainscreen_catalog_button.click()

category1_hud_male_button = browser.find_element(By.CSS_SELECTOR, ".mega-burger-sidebar-menu__link[title='Женщинам']")
time.sleep(3)

actions = ActionChains(browser).move_to_element(category1_hud_male_button)
actions.perform()

category1_hud_tshirt_button = browser.find_element(By.CSS_SELECTOR, """.mega-burger-content-menu__column [data-event-click='{"event":"dropdown_menu_click","rubricId":1286395}']""")
category1_hud_tshirt_button.click()

tshirt_card = browser.find_element(By.CSS_SELECTOR, \
    """.product-listing-card [data-event-click='{"event":"product_click","eventData":"","rubricId":1286395,"brandId":1120443,"productId":60711938,"productVariationId":189155660}']""")
tshirt_card.click()

WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn[title="Добавить в корзину"]'))
)

tshirt_size = browser.find_element(By.CSS_SELECTOR, \
    '[data-selector="variations"] label[data-aspect-name="S"]')
tshirt_size.click()

add_to_cart_button = browser.find_element(By.CSS_SELECTOR, '.btn[title="Добавить в корзину"]')
add_to_cart_button.click()

time.sleep(1)

count_items = browser.find_element(By.CSS_SELECTOR, 'input[name="basket_add[quantity]"]')
count_items.clear()
count_items.send_keys(2)


# Третий товар

time.sleep(3)

mainscreen_catalog_button = browser.find_element(By.CSS_SELECTOR, ".header-rubrics-toggler__desktop.btn.btn_primary")
mainscreen_catalog_button.click()

category1_hud_male_button = browser.find_element(By.CSS_SELECTOR, ".mega-burger-sidebar-menu__link[title='Сумки и чемоданы']")
time.sleep(3)

actions = ActionChains(browser).move_to_element(category1_hud_male_button)
actions.perform()

category1_hud_tshirt_button = browser.find_element(By.CSS_SELECTOR, """.mega-burger-content-menu__column [data-event-click='{"event":"dropdown_menu_click","rubricId":1286737}']""")
category1_hud_tshirt_button.click()

tshirt_card = browser.find_element(By.CSS_SELECTOR, \
    """.product-listing-card [data-event-click='{"event":"product_click","eventData":"","rubricId":1286996,"brandId":1162156,"productId":60028420,"productVariationId":185113253}']""")
browser.execute_script("arguments[0].scrollIntoView()", tshirt_card)
time.sleep(1)
tshirt_card.click()

WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn[title="Добавить в корзину"]'))
)

tshirt_size = browser.find_element(By.CSS_SELECTOR, \
    '[data-selector="variations"] label[data-aspect-name="Black"]')
tshirt_size.click()

add_to_cart_button = browser.find_element(By.CSS_SELECTOR, '.btn[title="Добавить в корзину"]')
add_to_cart_button.click()

time.sleep(1)

count_items = browser.find_element(By.CSS_SELECTOR, 'input[name="basket_add[quantity]"]')
time.sleep(1)
count_items.clear()
count_items.send_keys(2)

# Переход в корзину и проверка количества

time.sleep(3)

cart_button = browser.find_element(By.CSS_SELECTOR, '.header__toolbar-item[title="Перейти в корзину"]')
cart_button.click()


# Сравнение количества выбранных товаров и общего числа товаров в корзине

count_of_items = 0
items = browser.find_elements(By.CSS_SELECTOR, 'input[data-selector="quantity-group-input"]')
for item in items:
    count_of_items += int(item.get_attribute("value"))

count_in_order_WE = browser.find_element(By.CSS_SELECTOR, '.basket-summary__btn-more .js-more')
count_in_order = int(count_in_order_WE.text.split()[0])

assert count_of_items == count_in_order, "Количество товаров в корзине не совпадает с количеством выбранных товаров!"

time.sleep(30)

browser.quit()