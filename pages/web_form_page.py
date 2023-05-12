from playwright.sync_api import Page
import time

# Web Elements
page_title: str = '[class="display-6"]'
input_field: str = '[id="my-text-id"]'
password_field: str = '[name="my-password"]'
disabled_field: str = '[name="my-disabled"]'
readonly_field: str = '[name="my-readonly"]'
dropdown_field: str = '[name="my-select"]'
radio_box: str = '[id="my-radio-2"]'
submit_button: str = '[type="submit"]'
submit_button_page_2: str = '[id="message"]'

# Other Consts
url: str = 'https://www.selenium.dev/selenium/web/web-form.html'
page_title_expected: str = 'Web form'
input_field_expected: str = 'Hello'
password_field_expected: str = 'Password'
submit_button_page_2_expected: str = 'Received!'


def navigate_to_web_form_function(page: Page):
    page.goto(url)

def check_page_title_function(page: Page):
    page.wait_for_selector(page_title)
    page_title_object = page.locator(page_title)
    page_title_actual = page_title_object.text_content()
    assert page_title_actual == page_title_expected, f"Page Title - expected: [{page_title_expected}], and received [{page_title_actual}]"
    print(f"Page Titled - expected: [{page_title_expected}], and received [{page_title_actual}]")

def input_field_function(page: Page, input_field_text: str):
    page.wait_for_selector(input_field)
    input_field_object = page.locator(input_field)
    input_field_object.fill(input_field_text)
    input_field_actual = input_field_object.input_value()
    assert input_field_actual == input_field_expected, f"Input Field - expected: [{input_field_expected}], and received [{input_field_actual}]"
    print(f"Input Field - expected: [{input_field_expected}], and  received [{input_field_actual}]")

def password_field_function(page: Page, password_field_text: str):
    page.wait_for_selector(password_field)
    password_field_object = page.locator(password_field)
    password_field_object.fill(password_field_text)
    password_field_actual = password_field_object.input_value()
    assert password_field_actual == password_field_expected, f"Password Field - expected: [{password_field_expected}], and received [{password_field_actual}]"
    print(f"Password Field - expected: [{password_field_expected}], and received [{password_field_actual}]")

def disabled_field_function(page: Page):
    page.wait_for_selector(disabled_field)
    disabled_field_object = page.locator(disabled_field)
    assert not disabled_field_object.is_enabled(), f"Disabled field - expected field to be disabled, but is enabled"
    print("Disabled Field is not enabled")

def readonly_field_function(page: Page):
    page.wait_for_selector(readonly_field)
    readonly_field_object = page.locator(readonly_field)
    is_readonly = readonly_field_object.is_enabled() == False
    assert is_readonly, f"Readonly Field - does not have attribute readonly"
    print("Readonly Field - is readonly =", is_readonly)

def dropdown_field_function(page: Page, dropdown_field_index: int):
    page.wait_for_selector(dropdown_field)
    dropdown_field_object = page.locator(dropdown_field)
    dropdown_field_object.select_option(index=dropdown_field_index)
    dropdown_field_object2 = page.locator(dropdown_field)
    dropdown_field_value = dropdown_field_object2.evaluate("el => el.value")
    print("Dropdown Field - Value:", dropdown_field_value)
    assert dropdown_field_value == "1"

def radio_box_function(page: Page):
    page.wait_for_selector(radio_box)
    radio_box_object = page.locator(radio_box)
    assert not radio_box_object.is_checked(), "Radio Box - is checked by default when it should not be"
    radio_box_object.click()
    assert radio_box_object.is_checked(), "Radio Box - is not checked after clicking"
    print("Radio box - tested successfully ")

def submit_button_function(page: Page):
    page.wait_for_selector(submit_button)
    submit_button_object = page.locator(submit_button)
    submit_button_object.click()
    submit_button_page_2_actual = page.locator(submit_button_page_2).text_content()
    assert submit_button_page_2_actual == submit_button_page_2_expected, f"Submit Button - expected: [{submit_button_page_2_expected}], and received [{submit_button_page_2_actual}]"
    print(f"Submit Button - expected: [{submit_button_page_2_expected}], and received [{submit_button_page_2_actual}]")
