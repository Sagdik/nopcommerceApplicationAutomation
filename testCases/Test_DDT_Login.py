import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utlities import ExcelUtils
from pageObjects.LoginPage import Login
from utlities.readProperties import ReadConfig
from utlities.customLogger import LogGenerator
import time


class Test_DDT_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    path=".//testData/userLogin.xlsx"

    loggerTest = LogGenerator.logInfoGenerator()

    def test_loginPage(self, setup, lst_status=[None]):
        self.loggerTest.info("******Test Login Page ******")
        self.driver = setup
        self.loggerTest.info("****Verfiy Login Page*****")
        self.driver.maximize_window()
        self.loggerTest.info("****Launch Browser*****")
        self.driver.get(self.baseUrl)
        self.loggerTest.info("****Enter the url *****")
        self.login = Login(self.driver)

        self.row =ExcelUtils.getRowCount(self.path,'Sheet1')
        print("Number of row",self.row)

        for r in range(2,self.row+1):
            self.user=ExcelUtils.readData(self.path,'Sheet1',r,1)
            self.password=ExcelUtils.readData(self.path,'Sheet1',r,2)
            self.expected = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.login.setUserName(self.user)
            self.login.setPassword(self.password)
            self.login.clickLogin()

            time.sleep(5)

            act_title = self.driver.title
            self.loggerTest.info("****Verifying the title after login")
            exp_title = "Free and open-source eCommerce platform. ASP.NET based shopping cart. - nopCommerce"

            if act_title==exp_title:
                if self.expected=="Pass":
                    self.loggerTest.info("*****Successfully verfied******")
                    self.login.clickLogout();
                    lst_status.append("Pass")
                elif self.expected=="Fail":
                    self.loggerTest.info("Failed ")
                    self.login.clickLogout();
                    lst_status.append("Fail")

            elif act_title!=exp_title :
                if self.expected == "Pass":
                    self.loggerTest.info("failed")
                    lst_status.append("Fail")
                elif self.expected == "Fail":
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.loggerTest.info("************login DDT test Passed***********")
            self.driver.close()
            assert True

        else:
            self.loggerTest.info("*******Login DDT Test Failed**********")
            self.driver.close()
            assert False


