def go_to_site(browser, locators):
    # browser.get("http://www.way2automation.com/angularjs-protractor/webtables/")
    return browser.is_element_present(locators.get("user_table"))
