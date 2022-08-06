from _ast import Assert

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

LINK_LIST=(By.CSS_SELECTOR, '#CardInstance-V2xJw98VsI2LvCht9BM2g li')
PAGE_HEADER=(By.CSS_SELECTOR, '#zg_banner_text')

@then('user verifies correct bestseller URL')
def correct_bestseller_verification(context):
     actual_result=context.driver.current_url.lower()
     expected_result='https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers'
     assert expected_result == actual_result, f"expected{expected_result} but got {actual_result}"


@then('user clicks through all bestseller sublinks and verifies page header text')
def click_all_bestseller_link(context):
    expected_link_name = ['Best Sellers','New Releases','Movers&Shakers','Most Wished For', 'Gift Ideas']

    link_list=context.driver.find_elements(*LINK_LIST) #//probably using Wait until was a better idea?
    for link in link_list:
      link.click()
      sleep(5)
      context.driver.find_element(*PAGE_HEADER).text
      context.driver.refresh()
      print(link_list)


