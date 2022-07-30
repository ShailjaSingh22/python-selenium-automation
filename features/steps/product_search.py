from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.ID, 'nav-search-submit-text')


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    context.driver.wait = WebDriverWait(context, 10)
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_INPUT)).clear()
    #search.clear()
    #sleep(4)
    search.send_keys(search_word)


@when('Click on search icon')
def click_search_icon(context):
    #context.driver.find_element(*SEARCH_SUBMIT).click()
    #sleep(1)
    context.driver.wait = WebDriverWait(context, 10)
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_SUBMIT)).click()


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"
