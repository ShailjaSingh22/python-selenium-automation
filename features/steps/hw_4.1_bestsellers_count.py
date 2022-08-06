from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BESTSELLER_CLICK=(By.XPATH, "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
ALL_BESTSELLER_LINKS=(By.CSS_SELECTOR,'div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li')

@when('user clicks Bestsellers button')
def click_bestseller_link(context):
    context.driver.find_element(*BESTSELLER_CLICK).click()
    sleep(4)

@then('user verifies the bestseller URL')
def bestseller_url_verification(context):
    assert 'bestsellers' in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}" #@svetlana : this line is giving me attribute error but not sure what's wrong'
    print(context.current_url.lower())
    sleep(4)
    #assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"


@then('user verifies count of links in bestseller')
def bestseller_link_count_verification(context):
    bestseller_links= context.driver.find_elements(*ALL_BESTSELLER_LINKS)
    assert len(bestseller_links)== int(5) , f"Expected 5 links but got{len(bestseller_links)}"


