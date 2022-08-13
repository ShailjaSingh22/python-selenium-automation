# Created by tosha at 8/12/2022
Feature: Test case to verify empty cart if no product chosen


  Scenario: 'Your Amazon Cart is empty' shown if no product added
    Given user opens Amazon page
    When user clicks cart icon
    Then user verifies 'Your Amazon Cart is empty.' text present
