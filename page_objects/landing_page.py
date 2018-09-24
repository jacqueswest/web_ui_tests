def verify_landing_on_table_list(browser, locators):
    """ Open a given url in a browser instance """

    return browser.is_element_present(locators.get("user_table"))
