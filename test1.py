from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
print("Sample Test case Started!!!!")
#Chrome Driver
driver=webdriver.Chrome()
#Maximize the windows size
driver.maximize_window()

driver.get('https://practice-automation.com/form-fields/')

#Form
#WebElement Name - has two text fields   Name
#Action performed here is entering or sneding some text in the field
Input_Field_Name=driver.find_element(By.ID,"name-input")
Input_Field_Name.send_keys("DemoForm")
time.sleep(1)
print("Entered Name Successfully")
#webelement Password -textbox
##Action performed here is entering or sneding some text in the field
#//*[@id="feedbackForm"]/label[2]/input
Input_Field_Password=driver.find_element(By.XPATH,"//*[@id='feedbackForm']/label[2]/input")
Input_Field_Password.send_keys("demo@1234")
time.sleep(2)
print("Entered Password Successfully")

#Webelement question What is your favorite drink-checkbox
#Action performed here clicking the desired CheckBox of our choice
check_boxes=driver.find_elements(By.NAME,"fav_drink")
print("No of check boxes for Drink",len(check_boxes)) #it should out put us 5
for drink in check_boxes:
    if drink.get_attribute('value')==   "Coffee":
        drink.click()
print("Selected Drink Successfully!!!!")


#Scrolling to the radio buttons section
radio_buttons_section = driver.find_element(By.XPATH, "//*[text()='What is your favorite color?']")
driver.execute_script("arguments[0].scrollIntoView(true);", radio_buttons_section)
time.sleep(1)


#Webelement Question -Radio Button
#Action performed here clicking the desired radiobuttons of our choice
radio_buttons=driver.find_elements(By.NAME,"fav_color")
print("No of radio buttons",len(radio_buttons))#it should give us 5 count
for color in radio_buttons:
    if color.get_attribute('value')==   "Green":
        color.click()
        break
time.sleep(2)
print("selected color sucessfully!!")
#Selecting Drop Down !!!
dropdown=driver.find_element(By.ID,"automation")
#dropdown=driver.find_elements(By.XPATH,"//*[@id='automation']")
select = Select(dropdown)
time.sleep(2)
select.select_by_value("yes")

#web element -text feild:
email=driver.find_element(By.CSS_SELECTOR,"#email")
email.send_keys("demoemail.123@gmail.com")
time.sleep(4)
#messsage text box-//*[@id="message"]
message=driver.find_element(By.XPATH,"//*[@id='message']")
message.send_keys("Thanks for demo automation site.")
time.sleep(3)

#Scrolling to the submit button
submitbutton_section = driver.find_element(By.ID,"submit-btn")
driver.execute_script("arguments[0].scrollIntoView(true);", submitbutton_section)
time.sleep(1)


#submitButton
submit_button=driver.find_element(By.ID,"submit-btn")
submit_button.click()
print("Submit Button Clicked!!!!")
print("Sucessfully Entered Everything!!!!!")