import pytest
from pytest_bdd import scenario, given, when, then, parsers
from playwright.sync_api import Playwright
from ..pages import web_form_page

import pytest

# pytest test_selenium_web_driver.py --html=test_results.html

@pytest.fixture(scope="function")
def browser(playwright: Playwright) -> None:
    # Launch the browser in a non-headless mode
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@scenario('tests.feature', 'user can use the selenium web form')
def test_selenium_web_form_tests():
    pass

@given('I navigate to the selenium web form')
def goto_selenium_webdriver(page):
    web_form_page.navigate_to_web_form_function(page)
    pass

@then('I check the title of the webpage')
def webpage_title(page):
    web_form_page.check_page_title_function(page)
    pass

@then(parsers.parse('I input "{input_field_text}" into the input field'))
def input_field(page, input_field_text):
    web_form_page.input_field_function(page, input_field_text)
    pass

@then(parsers.parse('I input "{password_field_text}" into the password field'))
def password_field(page, password_field_text):
    web_form_page.password_field_function(page, password_field_text)
    pass

@then('I make sure the disabled field is actually disabled')
def disabled_field(page):
    web_form_page.disabled_field_function(page)
    pass

@then('I verify the readonly input is actually readonly')
def readonly_field(page):
    web_form_page.readonly_field_function(page)
    pass

@then(parsers.parse('I select the option at index "{dropdown_field_index}" from the dropdown'))
def password_field(page, dropdown_field_index):
    web_form_page.dropdown_field_function(page, int(dropdown_field_index))
    pass

@then('I check the radio box')
def radio_box(page):
    web_form_page.radio_box_function(page)
    pass

@when('I click the submit button and make sure I am on the new page')
def submit_button(page):
    web_form_page.submit_button_function(page)