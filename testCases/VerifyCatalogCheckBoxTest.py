import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.VerifyCatalogCheckbox import VerifyCatalogCheckbox
from utilities.readProperties import readConfig
from utilities.customLogger import LogGen

class Test_002_catalog:
    baseurl=readConfig.getApplicationURL()
    username=readConfig.getUserEmail()
    password=readConfig.getUserPassword()
    logger=LogGen.loggen()


    @pytest.mark.smoke
    def test_catalog(self,setup):
        self.driver=setup
        self.logger.info("**************Launching the browser URL*********************")
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************Logged in Successfully****************")
        time.sleep(3)
        self.logger.info("****************Navigating to Catalog page**************************")

        self.cv=VerifyCatalogCheckbox(self.driver)
        self.cv.clickCatalogMenu()
        self.cv.clickOnProduct()
        time.sleep(2)
        self.logger.info("****************Click on All checkbox**************************")

        self.cv.clickOnAllCheckbox()
        time.sleep(2)
        self.driver.close()



