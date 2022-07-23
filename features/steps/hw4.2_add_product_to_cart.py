import time

from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_BOX= (By.CSS_SELECTOR, '#twotabsearchtextbox')
SEARCHED_ITEM= (By.XPATH, "//div[@class='a-section a-spacing-none s-padding-right-small s-title-instructions-style']/h2/a")
ADD_TO_CART=(By.XPATH, "//input[@id='add-to-cart-button']")
COUNT_IN_CART=(By.ID, 'nav-cart-count')

@given('user navigates to Amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')

@when('user types item in search box')
def search_item(context):
    context.driver.find_element(*SEARCH_BOX).send_keys('power of Now by Eckhardt Tolle', '\n')

@then('user finds item in search results and clicks')
def search_item_found(context):
    results = context.driver.find_elements(*SEARCHED_ITEM)
    results[0].click()
    time.sleep(5)


@then('user adds item to cart')
def adds_item_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()

@then('user verifies correct count in cart')
def verifies_count_in_cart(context):
    expected_count = '1'
    actual_count = context.driver.find_element(*COUNT_IN_CART).text
    assert expected_count==actual_count , f'Expected{expected_count}, but got {actual_count}'



