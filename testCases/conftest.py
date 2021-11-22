from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path='C://Users//Nirbhay//Downloads//geckodriver-v0.30.0-win64//geckodriver.exe')

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


################# Pytest Report HTML ####################


def pytest_configure(config):
    config._metadata['Project Name']='nop Commerce'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='Sagar Tripathi'


### Hook for delete and modify ENv in HTML report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
