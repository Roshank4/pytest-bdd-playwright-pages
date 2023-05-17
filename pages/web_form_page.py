from playwright.sync_api import Page

# Web Elements
selectors = {
    'page_title': '[class="display-6"]',
    'input_field':   '[id="my-text-id"]',
    'password_field': '[name="my-password"]',
    'disabled_field': '[name="my-disabled"]',
    'readonly_field': '[name="my-readonly"]',
    'dropdown_field': '[name="my-select"]',
    'radio_box': '[id="my-radio-2"]',
    'submit_button': '[type="submit"]',
    'page_header_after_submit': '[id="message"]',
}
# Other Consts

expected_variables = {
    'url': 'https://www.selenium.dev/selenium/web/web-form.html',
    'page_title_expected': 'Web form',
    'page_header_after_submit_expected': 'Received!',
}

def navigate_to_web_form_f(page: Page):
    page.goto(expected_variables['url'])

def check_page_title_f(page: Page):
    page.wait_for_selector(selectors['page_title'])
    page_title_object = page.locator(selectors['page_title'])
    page_title_actual = page_title_object.text_content()
    assert page_title_actual == expected_variables['page_title_expected'], f"Page Title - expected: [{expected_variables['page_title_expected']}], and received [{page_title_actual}]"
    print(f"Page Titled - expected: [{expected_variables['page_title_expected']}], and received [{page_title_actual}]")

def input_field_f(page: Page, input_field_text: str):
    page.wait_for_selector(selectors['input_field'])
    input_field_object = page.locator(selectors['input_field'])
    input_field_object.fill(input_field_text)
    input_field_actual = input_field_object.input_value()
    assert input_field_actual == input_field_text, f"Input Field - expected: [{input_field_text}], and received [{input_field_actual}]"
    print(f"Input Field - expected: [{input_field_text}], and  received [{input_field_actual}]")

def password_field_f(page: Page, password_field_text: str):
    page.wait_for_selector(selectors['password_field'])
    password_field_object = page.locator(selectors['password_field'])
    password_field_object.fill(password_field_text)
    password_field_actual = password_field_object.input_value()
    assert password_field_actual == password_field_text, f"Password Field - expected: [{password_field_text}], and received [{password_field_actual}]"
    print(f"Password Field - expected: [{password_field_text}], and received [{password_field_actual}]")

def disabled_field_f(page: Page):
    page.wait_for_selector(selectors['disabled_field'])
    disabled_field_object = page.locator(selectors['disabled_field'])
    assert not disabled_field_object.is_enabled(), f"Disabled field - expected field to be disabled, but is enabled"
    print("Disabled Field is not enabled")

def readonly_field_f(page: Page):
    page.wait_for_selector(selectors['readonly_field'])
    readonly_field_object = page.locator(selectors['readonly_field'])
    is_readonly = readonly_field_object.is_enabled() == False
    assert is_readonly, f"Readonly Field - does not have attribute readonly"
    print("Readonly Field - is readonly =", is_readonly)

def dropdown_field_f(page: Page, dropdown_field_index: int):
    page.wait_for_selector(selectors['dropdown_field'])
    dropdown_field_object = page.locator(selectors['dropdown_field'])
    dropdown_field_object.select_option(index=dropdown_field_index)
    dropdown_field_object2 = page.locator(selectors['dropdown_field'])
    dropdown_field_value = dropdown_field_object2.evaluate("el => el.value")
    print(f"Dropdown filed Field - expected: [{dropdown_field_index}], and received [{dropdown_field_value}]")
    assert dropdown_field_value == str(dropdown_field_index)


def radio_box_f(page: Page):
    page.wait_for_selector(selectors['radio_box'])
    radio_box_object = page.locator(selectors['radio_box'])
    assert not radio_box_object.is_checked(), "Radio Box - is checked by default when it should not be"
    radio_box_object.click()
    assert radio_box_object.is_checked(), "Radio Box - is not checked after clicking"
    print("Radio box - tested successfully ")

def submit_button_click_f(page: Page):
    page.wait_for_selector(selectors['submit_button'])
    submit_button_object = page.locator(selectors['submit_button'])
    submit_button_object.click()

def submit_button_verify_f(page: Page):
    page.wait_for_selector(selectors['page_header_after_submit'])
    page_header_after_submit_actual = page.locator(selectors['page_header_after_submit']).text_content()
    assert page_header_after_submit_actual == expected_variables['page_header_after_submit_expected'], f"Submit Button - expected: [{expected_variables['page_header_after_submit_expected']}], and received [{page_header_after_submit_actual}]"
    print(f"Submit Button - expected: [{expected_variables['page_header_after_submit_expected']}], and received [{page_header_after_submit_actual}]")
