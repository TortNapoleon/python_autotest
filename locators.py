from selenium.webdriver.common.by import By

class CategoryLocators(): # Класс с определёнными локаторами категорий
    MAN_CATEGORY_LOCATOR = (By.CSS_SELECTOR, ".mega-burger-sidebar-menu__link[title='Мужчинам']")
    MAN_TSHIRT_SUBCATEGORY_LOCATOR = (By.CSS_SELECTOR, """.mega-burger-content-menu__column [data-event-click='{"event":"dropdown_menu_click","rubricId":1286190}']""")

    WOMEN_CATEGORY_LOCATOR = (By.CSS_SELECTOR, ".mega-burger-sidebar-menu__link[title='Женщинам']")
    WOMEN_SET_SUBCATEGORY_LOCATOR = (By.CSS_SELECTOR, """.mega-burger-content-menu__column [data-event-click='{"event":"dropdown_menu_click","rubricId":1286395}']""")
    
    BAGS_AND_SUITCASES_CATEGORY_LOCATOR = (By.CSS_SELECTOR, ".mega-burger-sidebar-menu__link[title='Сумки и чемоданы']")
    BAGS_SUBCATEGORY_LOCATOR = category1_hud_tshirt_button = (By.CSS_SELECTOR, """.mega-burger-content-menu__column [data-event-click='{"event":"dropdown_menu_click","rubricId":1286737}']""")

class ItemsLocators(): # Локаторы товаров
    TSHIRT_LINK = (By.CSS_SELECTOR, \
                   """.product-listing-card [href="/p-zarahome-men-s-brown-t-shirt-V132381534"]""")
    SET_OF_CLOTHES_LINK = (By.CSS_SELECTOR, \
                      """.product-listing-card [data-event-click='{"event":"product_click","eventData":"","rubricId":1286395,"brandId":1120443,"productId":60711938,"productVariationId":189155660}']""")
    BAG_LINK = (By.CSS_SELECTOR, \
                """.product-listing-card [data-event-click='{"event":"product_click","eventData":"","rubricId":1286996,"brandId":1162156,"productId":60028420,"productVariationId":185113253}']""")