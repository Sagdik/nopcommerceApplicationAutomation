from selenium import webdriver



class Login:
    textbox_username_id = ".//input[@class='username']"
    textbox_password_id = ".//input[@class='password']"
    button_login = "//input[@value='Log in']"
    link_logout = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_xpath(self.textbox_username_id).click()
        self.driver.find_element_by_xpath(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_id).click()
        self.driver.find_element_by_xpath(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.link_logout).click()
