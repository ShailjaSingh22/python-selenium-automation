from behave import given, when, then


@when('user clicks cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()


@then("user verifies \'Your Amazon Cart is empty.\' text present")
def verify_empty_cart_text(context):
    context.app.cart_page.verify_empty_cart_text('Your Shopping Cart is empty.')


