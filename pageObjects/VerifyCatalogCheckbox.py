import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class VerifyCatalogCheckbox:
    Catalog_text_xpath="//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']/li[2]"
    Product_XPath="//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']/li[2]/ul/li[1]"
    ListOfCheckBox="//*[@name='checkbox_products']"

    def __init__(self,driver):
        self.driver=driver

    def clickCatalogMenu(self): ############# Catalog Comments
        self.driver.find_element(By.XPATH,self.Catalog_text_xpath).click()

    def clickOnProduct(self):
        self.driver.find_element(By.XPATH,self.Product_XPath).click()

    def clickOnAllCheckbox(self):
        check=self.driver.find_elements(By.XPATH,self.ListOfCheckBox)
        time.sleep(2)
        for checkbox in check:
            checkbox.click()








