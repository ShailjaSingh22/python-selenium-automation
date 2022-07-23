# Created by tosha at 7/19/2022
Feature: Best Seller count of links test case


  Scenario: User verifies the total number of links in Bestsellers
    Given user navigates to Amazon page
    When user clicks Bestsellers button
    Then user verifies the bestseller URL
    Then user verifies count of links in bestseller
