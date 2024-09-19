from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)  # Wait for up to 10 seconds

driver.get("https://demo.automationtesting.in/")

driver.find_element(By.XPATH, '//button[@id="btn2"]').click()

# Radio Buttons
maleRadioBtn = driver.find_element(By.XPATH, '//input[@value="Male"]')
femaleRadioBtn = driver.find_element(By.XPATH, '//input[@value="FeMale"]')
maleRadioBtn.click()

# Check-Box List and Get Attributes
checkBoxList = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')

for ele in checkBoxList:
    val = ele.get_attribute('value')
    print(val)
    if val == "Cricket":
        ele.click()
