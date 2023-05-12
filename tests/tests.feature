Feature: Selenium Web Form Test

    Scenario: user can use the selenium web form
        Given I navigate to the selenium web form
        Then I check the title of the webpage
        Then I input "Hello" into the input field
        Then I input "Password" into the password field
        Then I make sure the disabled field is actually disabled
        Then I verify the readonly input is actually readonly
        Then I select the option at index "1" from the dropdown
        Then I check the radio box
        When I click the submit button and make sure I am on the new page
