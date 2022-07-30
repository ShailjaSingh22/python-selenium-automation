from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR=(By.CSS_SELECTOR, 'button.a-button-text img.imgSwatch')

@given('user opens Amazon product page')
#@given('user opens Amazon product {product_id} page')

def open_amazon_product(context):
#def open_amazon_product(context, product_id):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')
   #context.driver.get('https://www.amazon.com/gp/product/{product_id}/')


@then('user verifies clicking through different colors')
def click_through_colors(context):
    expected_colors=['Dark Wash','Indigo Wash', 'Light Blue Vintage', 'Light Khaki Brown', 'Black']
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    actual_colors=[]
    print(colors)

    for color in colors:
        color.click()
        actual_colors += [context.driver.find_element(*CURRENT_COLOR).text]
        print('Actual colors:', actual_colors)
    assert expected_colors == actual_colors, f'Expected {expected_colors} but found {actual_colors}'





