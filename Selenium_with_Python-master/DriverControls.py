from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)  # Wait for up to 10 seconds

driver.get("https://google.com/")

# get current URL
print(driver.current_url)

# Navigate different URL
driver.get("https://amazon.in/")
print(driver.current_url)

# Back
driver.back()

# Refresh
driver.refresh()

# forward
driver.forward()

# quit
driver.quit()
