from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://demo.automationtesting.in/")
driver.implicitly_wait(10)  # Wait for up to 10 seconds

driver.find_element(By.XPATH, '//button[@id="btn2"]').click()

skillsDropDown = driver.find_element(By.ID, 'Skills')
sel = Select(skillsDropDown)
sel.select_by_index(5)
sel.select_by_value("Analytics")
sel.select_by_visible_text("Configuration")
