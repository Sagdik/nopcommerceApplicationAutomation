from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class Login:
    textbox_username_id = ".//input[@class='username']"
    textbox_password_id = ".//input[@class='password']"
    button_login = "//input[@value='Log in']"
    link_logout = ".//*[@href='/en/logout']"
    profile_mouseHover=".//*[@class='ico-user sprite-image']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        elementToHover = self.driver.find_element_by_xpath(".//*[@class='ico-user sprite-image']")
        hov = ActionChains(self.driver).move_to_element(elementToHover)
        hov.perform()
        self.driver.find_element_by_xpath(".//*[@class='ico-login']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.textbox_username_id).clear()
        self.driver.find_element_by_xpath(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_id).click()
        self.driver.find_element_by_xpath(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login).click()

    def clickLogout(self):
        elementToHover = self.driver.find_element_by_xpath(".//*[@class='ico-user sprite-image']")
        hov=ActionChains(self.driver).move_to_element(elementToHover)
        hov.perform()
        self.driver.find_element_by_xpath(self.link_logout).click()
