# Import required modules
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Set options for Chrome browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", True) # Add an option to detach the browser window

# Create a Service object for the Chrome browser
service_obj = Service("Chrome Browser/chromedriver_win32/chromedriver.exe")

# Use the Service object to instantiate a Chrome driver object
driver = webdriver.Chrome(service=service_obj, options=chrome_options) # Instantiate a Chrome driver object with the specified options

# Maximize the window
driver.maximize_window()

# Load the login page
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
time.sleep(5)  # Wait for the page to load

# Click on the link to access free interview questions and resume assistance
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

# Get the handles of all the windows opened by the driver
WindowsOpened = driver.window_handles

# Switch to the newly opened window
driver.switch_to.window(WindowsOpened[1])

# Get the email address displayed on the page
Email = driver.find_element(By.XPATH, "//strong/a").text

# Load the Angular practice page
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Fill out the form on the page
# Enter the name in the Name field
driver.find_element(By.CSS_SELECTOR, ".form-group input[name='name']").send_keys("Shaden Ghazalin")
# Enter the email address in the Email field
driver.find_element(By.CSS_SELECTOR, ".form-group input[name='email']").send_keys(Email)
# Enter the password in the Password field
driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").send_keys("test123")
# Check the checkbox to agree to the terms and conditions
driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()
# Instantiate a dropdown object for the Gender dropdown
dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
# Select the option "Female" from the Gender dropdown
dropdown.select_by_visible_text("Female")
# Select the option "Employed" for the Employment Status radio buttons
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
# Enter the birthdate in the Date of Birth field
driver.find_element(By.CSS_SELECTOR, "input[name='bday']").send_keys("11/11/1111")
# Click on the Submit button to submit the form
driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()

# Wait for the confirmation message to appear
confirmation_message = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text
assert confirmation_message, "Form submission failed"
print("Form submission Confirmed")
