from page_objects.username_check import username_exist


def add_user(browser, user, **kwargs):
    """ Adding a User """
    text_box_labels = ["first_name", "last_name", "username", "password", "email", "cell"]
    locators = kwargs.get("locator_data")
    data = kwargs.get(user)

    # Ensure that the user is unique
    usrname_exist = username_exist(browser, text=data.get("username"), locators=locators)
    if usrname_exist:
        return "{0} already exists".format(data.get('username'))

    browser.find_element_by_locator(locators.get("add_btn")).click()

    for label in text_box_labels:
        browser.find_element_by_locator(locators.get(label)).clear()
        browser.find_element_by_locator(locators.get(label)).send_keys(data.get(label))

    radio_btns_list = browser.find_elements_by_locator(locators.get("customer"))
    for radio_btn in radio_btns_list:
        if radio_btn.text == data.get("customer"):
            radio_btn.click()

    browser.select_by_text(locator=locators.get("role"), text=data.get("role"))
    browser.find_element_by_locator(locators.get("save_btn")).click()
    # Ensure that the user is created
    post_add_usrname_exist = username_exist(browser, text=data.get("username"), locators=locators)
    return post_add_usrname_exist and "Add PASSED" or "Add FAILED"
