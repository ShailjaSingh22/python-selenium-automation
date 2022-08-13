from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    SIGN_IN_TEXT=(By.CSS_SELECTOR, 'h1.a-spacing-small')


    def verify_element_text(self, expected_result):
        actual_text = self.driver.find_element(*self.SIGN_IN_TEXT).text
        assert expected_result == actual_text, f'Expected {expected_result}, but got {actual_text}'
