import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.LoginPage import Login
from utlities.readProperties import ReadConfig
from utlities.customLogger import LogGenerator


class Test_001_Login_Test:
    baseUrl = ReadConfig.getApplicationUrl()
    userName = ReadConfig.getApplicationUserName()
    password = ReadConfig.getLoginPassword()

    loggerTest = LogGenerator.logInfoGenerator()

    def test_loginPage(self, setup):
        self.loggerTest.info("******Test Login Page ******")
        self.loggerTest.info("****Verfiy Login Page*****")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        self.login = Login(self.driver)
        self.login.setUserName(self.userName)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        act_title = self.driver.title
        self.loggerTest.info("****Verifying the title after login")

        if act_title == "Free and open-source eCommerce platform. ASP.NET based shopping cart. - nopCommerce":
            assert True
            self.driver.close()
            self.loggerTest.info("Successfully verfiied")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "LoginPageTest.png")
            self.driver.close()
            self.loggerTest.error("***Verfication failed***")
            assert False

