from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    EMPTY_CART_TEXT=(By.CSS_SELECTOR, '#sc-active-cart h2')


    def verify_empty_cart_text(self,expected_result):
        expected_result = 'Your Amazon Cart is empty'
        actual_result = self.driver.find_element(*self.EMPTY_CART_TEXT).text
        assert expected_result == actual_result, f"expected{expected_result} but got {actual_result}"



