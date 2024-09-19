from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://google.com/")
driver.implicitly_wait(10)  # Wait for up to 10 seconds

searchBox = driver.find_element(By.XPATH, '//textarea[@class="gLFyf"]')
searchBox.send_keys("IPhone 15")

driver.find_element(By.XPATH, '(//input[@class="gNO89b"])[2]').click()