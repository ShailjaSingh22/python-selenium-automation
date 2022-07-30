# Created by tosha at 7/27/2022
Feature: Test Case to verify  product image and name for every amazon search result
  # Enter feature description here

  Scenario: User verifies product image and name for all page items
    Given User opens Amazon page
    When Input Shoes into search field
    And Click on search icon
    Then Product results for Shoes are shown
    Then User finds count of all items on Page
