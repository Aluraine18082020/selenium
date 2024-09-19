import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://google.com/")

# Implicit Wait
driver.implicitly_wait(10)  # Wait for up to 10 seconds

# Explicit Wait
wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds
wait.until(EC.visibility_of_element_located((By.ID, 'element_id')))


# Sleep
time.sleep(2)
