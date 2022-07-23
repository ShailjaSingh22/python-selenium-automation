# Created by tosha at 7/13/2022
  Feature: Add to cart test

    Scenario: User adds item to cart and verifies
    Given user navigates to Amazon page
    When user types item in search box
    Then user finds item in search results and clicks
    Then user adds item to cart
    Then user verifies correct count in cart

