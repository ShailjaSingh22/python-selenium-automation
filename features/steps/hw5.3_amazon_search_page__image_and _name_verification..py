from selenium.webdriver.common.by import By
from behave import given, when, then

ALL_ITEM_IMAGES=(By.XPATH, "//img[@class='s-image']")
ALL_ITEM_DETAILS=(By.XPATH, "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']")
ALL_ITEM_NAME =(By.CSS_SELECTOR,'#search .s-line-clamp-1 span')


@then ('User finds count of all items on Page')
def count_all_items(context):
    #for i in each_item:

        list_a = context.driver.find_elements(*ALL_ITEM_NAME)
        print(len(list_a))
        list_b=context.driver.find_elements(*ALL_ITEM_DETAILS)
        print(len(list_b))
        list_c=context.driver.find_elements(*ALL_ITEM_IMAGES)
        print(len(list_c))

#assert len(list_a) == len(list_c), f'Expected {len(list_a)} but found a diff no. {len(list_b)}'
        #assert context.driver.find_element(*ALL_IMAGES).is_displayed()
        #assert context.driver.find_element(*ALL_PRODUCTS).is_displayed()




