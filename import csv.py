import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the Selenium WebDriver (Example for Chrome)
driver = webdriver.Chrome()

# Open the website
driver.get("https://example.com")

# Path to your CSV file
csv_file_path = 'path/to/your/file.csv'

# Read the CSV file
with open(csv_file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Assuming the CSV has multiple columns and you want to get the first column data
        csv_value = row[0]
        
        # Example: Find an element and use the value from the CSV file
        search_box = driver.find_element(By.NAME, 'q')  # Finding a search box element
        search_box.clear()
        search_box.send_keys(csv_value)  # Use the CSV value to interact with the browser
        search_box.send_keys(Keys.RETURN)

# Close the driver after operations
driver.quit()