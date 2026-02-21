Feature: Test Scenarios for Search functionality

  Scenario: User can open market tab and filter
    Given Open Reelly page
    When Log in to Reelly
    And Click on market
    And Verify the right page opens
    And Click on developer filter button
    Then Verify all cards have developer tag