def verify_landing_on_table_list(browser, locators):
    """ Verify landing on the table user list """

    return browser.is_element_present(locators.get("user_table"))
