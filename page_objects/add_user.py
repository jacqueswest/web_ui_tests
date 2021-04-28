from json import load


class Elements(object):
    add_btn = ["css_selector", ".btn"]
    username = ["name", "UserName"]
    customer = ["css_selector", ".radio.ng-scope.ng-binding"]
    role = ["name", "RoleId"]
    save_btn = ["css_selector", ".btn.btn-success"]
    search_box = ["xpath", "//input[@placeholder='Search']"]
    user_table_column = ["class_name", "smart-table-data-cell"]
    first_name = ["name", "FirstName"]
    last_name = ["name", "LastName"]
    password = ["name", "Password"]
    email = ["name", "Email"]
    cell = ["name", "Mobilephone"]


class Actions(object):

    def __init__(self, driver):
        self.driver = driver
        self.elem = Elements()

    def enter_text(self, elem, text):
        self.driver.find_element_by_locator(elem).clear()
        self.driver.find_element_by_locator(elem).send_keys(text)
        return ""

    def click(self, elem):
        self.driver.find_element_by_locator(elem).click()

    def select_radio_btn_by_text(self, elem, text):
        radio_btns_list = self.driver.find_elements_by_locator(elem)
        for radio_btn in radio_btns_list:
            if radio_btn.text == text:
                radio_btn.click()

    def select_elem_by_text(self, elem, text):
        self.driver.select_by_text(locator=elem, text=text)

    def get_elements(self, elem):
        return self.driver.find_elements_by_locator(elem)

    def username_exist(self, text):
        """ Determine if the username is unique, returns True if it exists """

        self.enter_text(elem=self.elem.search_box, text=text)
        # The third coloumn is the username column
        username_obj = self.get_elements(elem=self.elem.user_table_column)
        # If the table is empty, it returns an empty list
        return username_obj and username_obj[2].text == text or False

    def add_user(self, user):
        """ Adding an User """
        text_box_labels = ["first_name", "last_name", "username", "password", "email", "cell"]
        with open(file="./test_data_lib/user_data.json") as f:
            data = load(f)

        data = data.get(user)

        # Ensure that the user is unique
        if self.username_exist(text=data.get('username')):
            return "{0} already exists".format(data.get('username'))

        self.click(elem=self.elem.add_btn)

        for label in text_box_labels:
            self.enter_text(elem=getattr(self.elem, f"{label}"), text=data.get(label))

        radio_btns_list = self.get_elements(elem=self.elem.customer)
        for radio_btn in radio_btns_list:
            if radio_btn.text == data.get("customer"):
                radio_btn.click()

        self.select_elem_by_text(elem=self.elem.role, text=data.get("role"))
        self.click(elem=self.elem.save_btn)

        # Ensure that the user is created
        post_add_username_exist = self.username_exist(text=data.get("username"))
        return post_add_username_exist and "Add PASSED" or "Add FAILED"
