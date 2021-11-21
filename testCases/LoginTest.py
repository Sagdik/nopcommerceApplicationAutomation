import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.LoginPage import Login


class Test_001_Login_Test:

    baseUrl = "https://www.nopcommerce.com/en/login?returnUrl=%2Fen"
    userName = "sanutiwari7@gmail.com"
    password = ""

    def test_loginPage(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        self.login = Login(self.driver)
        self.login.setUserName(self.userName)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        act_title = self.driver.title

        if act_title=="Free and open-source eCommerce platform. ASP.NET based shopping cart. - nopCommerce":
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(".\\screenshots\\"+"LoginPageTest.png")
            self.driver.close()
            assert False