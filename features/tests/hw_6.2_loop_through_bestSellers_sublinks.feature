# Created by tosha at 8/5/2022
Feature: Test Case to loop through Bestsellers
  # Enter feature description here

  Scenario: User can loop through all the Bestseller sublinks and verify page header
    Given user navigates to Amazon page
    When user clicks Bestsellers button
    Then user verifies correct bestseller URL
    Then user clicks through all bestseller sublinks and verifies page header text
