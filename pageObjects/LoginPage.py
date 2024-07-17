from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
class LoginPage:
    textbox_username_xpath="//*[@id='Email']"
    textbox_password_xpath="//*[@id='Password']"
    button_login_xpath="//*[@type='submit']"
    link_logout_linkText="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_linkText).click()


























