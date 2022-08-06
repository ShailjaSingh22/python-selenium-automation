
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


PRIVACY_LINK=(By.XPATH,"//a[@href='https://www.amazon.com/privacy']")


@given('user opens Amazon T&C page')
def open_conditions_page(context):
    get_url = context.driver.current_url
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when ('user stores original window')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original Window:', context.original_window)


@then ('user clicks on Amazon Privacy Notice link')
def click_privacy_link(context):
    context.driver.wait.until(EC.element_to_be_clickable(PRIVACY_LINK))


@then('user switches to the newly opened window')
def switch_to_privacy_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print('Current Windows', context.driver.window_handles)
    new_window = context.driver.window_handles[0]  #//@Lana this gives index out of bound exception if I use '1'
    context.driver.switch_to.window(new_window)


@then ('user can verify Amazon Privacy Notice page is opened')
def privacy_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html/ref'))


@then ('user can close new window')
def close_privacy(context):
    context.driver.close()


@then ('switch back to original')
def switch_to_original(context):
    context.driver.switch_to.window(context.original_window)





