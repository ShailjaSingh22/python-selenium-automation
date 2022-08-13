
Feature: Test Case for user to see sign in page when clicking orders

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given  user opens Amazon page
    When user clicks Amazon Orders link
    Then verify sign in page is opened
