from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Set up the WebDriver for Safari
safari_browser = webdriver.Safari()

# Navigate to the demo page
safari_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

# Verify that the page title is as expected
assert "Selenium Easy Demo" in safari_browser.title

# Locate the 'Show Message' button by its class name
show_message_button = safari_browser.find_element(By.CLASS_NAME, "btn-primary")

# Verify that the button text 'Show Message' is present in the page source
assert "Show Message" in safari_browser.page_source

# Find the user message input box by ID, clear it, and type the custom message
user_message = safari_browser.find_element(By.ID, "user-message")
user_message.clear()
user_message.send_keys("I AM EXTRA COOL")

# Click the 'Show Message' button to display the message
show_message_button.click()

# Verify that the entered message 'Example Text' is displayed on the page
output_message = safari_browser.find_element(By.ID, "display")
assert "Example Text" in output_message.text

# Wait for 5 seconds to allow manual verification of the displayed message
time.sleep(5)

# Close the browser
safari_browser.quit()