def go_to_site(browser, locators):
    return browser.is_element_present(locators.get("user_table"))
