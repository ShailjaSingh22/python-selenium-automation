from behave import given, when, then


@when('user clicks Amazon Orders link')
def click_orders_link(context):
    context.app.header.click_orders_link()


@then('verify sign in page is opened')
def verify_url_contains_query(context):
    context.app.sign_in_page.verify_element_text('Sign-In')



