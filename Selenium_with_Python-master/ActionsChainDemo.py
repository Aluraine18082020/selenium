import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/")

# Implicit Wait
driver.implicitly_wait(10)

men = driver.find_element(By.XPATH, '//a[@id="ui-id-5"]')

# Performing Mouse Hover and Keyboard Actions
action = ActionChains(driver)
action.move_to_element(men).perform()

tops = driver.find_element(By.XPATH, '//a[@id="ui-id-17"]')
action.move_to_element(tops).perform()

jackets = driver.find_element(By.XPATH, '//a[@id="ui-id-19"]')
action.click(jackets).perform()

searchBox = driver.find_element(By.ID, 'search')
action.click(searchBox).key_down(Keys.SHIFT).send_keys("Test").key_up(Keys.SHIFT).send_keys(Keys.ENTER).perform()


time.sleep(5)
driver.quit()
