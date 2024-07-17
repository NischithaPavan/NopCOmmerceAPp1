from importlib import metadata

from selenium import webdriver
import pytest
@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("Launching Firefox")
    return driver


def pytest_addoption(parser): #This will get the value from CLI/hook (what ever browser name will pass through command line so this method will get  the value of browser
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the browser value and above setup method will get thta value
    return request.config.getoption("--browser")

######################## PyTest Report #####################################################
#It is a hook for adding environmental info to HTML report

def pytest_configure(config):
    config._metadata = {
    "Project Name": "Senneheiser"
    }


def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
