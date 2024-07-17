import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import readConfig
from utilities.customLogger import LogGen

class Test_001_login:
    baseurl=readConfig.getApplicationURL()
    username=readConfig.getUserEmail()
    password=readConfig.getUserPassword()
    logger=LogGen.loggen()#call loggen method

    @pytest.mark.sanity
    def test_homePageTitle(self,setup):
        self.logger.info("******TestCase_001**********")
        self.logger.info("*********Verifying Home Page Title**********")
        self.driver=setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title

        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("Home page title is passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepagetitle.png")
            self.driver.close()
            assert False

    @pytest.mark.smoke
    def test_login(self,setup):
        self.logger.info("Login test got started")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        act_hometitle=self.driver.title
        self.driver.close()
        if act_hometitle=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("Login Test is Passed*********")
        else:
            self.logger.error("Login test is failed******************")
            assert False







