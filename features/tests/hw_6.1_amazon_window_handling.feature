# Created by tosha at 7/31/2022
Feature: Test Case to open and close multiple browser windows
  # Enter feature description here

  Scenario: User can open and close Amazon Privacy Notice
    Given user opens Amazon T&C page
    When user stores original window
    Then user clicks on Amazon Privacy Notice link
    Then user switches to the newly opened window
    Then user can verify Amazon Privacy Notice page is opened
    And user can close new window
    And switch back to original