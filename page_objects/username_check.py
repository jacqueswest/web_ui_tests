def username_exist(browser, text, locators):
    """ Determine if the username is unique, returns True if it exists """

    browser.find_element_by_locator(locators.get("search_box")).clear()
    browser.find_element_by_locator(locators.get("search_box")).send_keys(text)
    # The third coloumn is the username column
    username_obj = browser.find_elements_by_locator(locators.get("user_table_column"))
    # If the table is empty, it returns an empty list
    return username_obj and username_obj[2].text == text or False
