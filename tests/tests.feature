Feature: Selenium Web Form Test

    Scenario: user can use the selenium web form
        Given I navigate to the selenium web form
        Then I check the title of the webpage
        And I input "input_field" into the input field
        And I input "password_field" into the password field
        And I make sure the disabled field is actually disabled
        And I verify the readonly input is actually readonly
        And I select the option at index "1" from the dropdown
        And I check the radio box
        When I click the submit button
        Then I verify I am on the new page
