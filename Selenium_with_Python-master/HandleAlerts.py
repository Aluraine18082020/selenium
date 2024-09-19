import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://demo.automationtesting.in/")
driver.implicitly_wait(10)  # Wait for up to 10 seconds


driver.find_element(By.XPATH, '//button[@id="btn2"]').click()
driver.find_element(By.XPATH, '//a[text()="SwitchTo"]').click()
driver.find_element(By.XPATH, '//a[text()="Alerts"]').click()

alertBtn = driver.find_element(By.ID, 'OKTab')
alertBtn.click()
time.sleep(2)

# OK - accept
driver.switch_to.alert.accept()
time.sleep(2)


# Confirmation
driver.find_element(By.XPATH, '//a[@href="#CancelTab"]').click()
confirmBtn = driver.find_element(By.ID, 'CancelTab')
confirmBtn.click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)


# Dismiss
driver.find_element(By.XPATH, '//a[@href="#Textbox"]').click()
textArea = driver.find_element(By.ID, 'Textbox')
textArea.click()
time.sleep(2)
# Reading TextArea data
text = driver.switch_to.alert.text
print(text)
# Send data inside TextArea
driver.switch_to.alert.send_keys("Hi there!, Varun Here")
driver.switch_to.alert.accept()


time.sleep(2)
driver.quit()
