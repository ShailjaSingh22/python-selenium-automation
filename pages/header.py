from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    CLICK_ORDERS_LINK=(By.CSS_SELECTOR,'#nav-orders .nav-line-2')
    CLICK_CART_ICON=(By.CSS_SELECTOR, '.nav-cart-icon')

    def click_orders_link(self):
        self.click(*self.CLICK_ORDERS_LINK)


    def click_cart_icon(self):
        self.click(*self.CLICK_CART_ICON)

