class Elements(object):
    user_table = ["xpath", "//table[@table-title='Smart Table example']"]


class Actions(object):

    def __init__(self, driver):
        self.elem = Elements()
        self.driver = driver

    def verify_landing_on_table_list(self):
        """ Verify landing on the table user list """

        return self.driver.is_element_present(self.elem.user_table)
