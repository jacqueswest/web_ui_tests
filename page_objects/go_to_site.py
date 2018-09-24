def go_to_site(browser, locators):
    """ Open a given url in a browser instance """

    return browser.is_element_present(locators.get("user_table"))
