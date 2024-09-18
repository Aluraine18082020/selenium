import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_search_amazon():
    # Set up the WebDriver (Make sure the path to your WebDriver is correct)
    driver = webdriver.Firefox()

    try:
        # Go to Amazon
        driver.get("https://www.amazon.com")

        # Find the search bar using its name attribute value
        search_bar = driver.find_element(By.NAME, "field-keywords")
        search_bar.send_keys("laptop")  # Example search for laptops

        # Submit the search form
        search_bar.submit()

        # Verify search results page title
        assert "laptop" in driver.title.lower()
        
        # Log that the search was successful
        allure.step("Search for 'laptop' was successful.")

    except Exception as e:
        allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    pytest.main()
