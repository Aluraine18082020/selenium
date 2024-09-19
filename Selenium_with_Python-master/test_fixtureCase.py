import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def launchBrowser():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://google.com/")
    driver.implicitly_wait(10)
    yield
    driver.quit()

@pytest.fixture(scope="class")
def launchBrowserClass(request):
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    request.cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
    yield
    request.cls.driver.quit()

# function for printing current URL
def test_printURL(launchBrowser):
    driver.get("https://www.redbus.in/")
    print(driver.current_url)

@pytest.mark.usefixtures("launchBrowserClass")
class Test_Redbus:
    def test_enterURL(self):
        self.driver.get("https://www.amazon.in/")
