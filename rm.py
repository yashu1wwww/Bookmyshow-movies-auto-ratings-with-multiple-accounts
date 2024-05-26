from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import random

# List of email addresses change to your required..
email_list = [
    'ys@gmail.com', 'my@gmai.l.com', 'my@gma.il.com', 'my@.gmail.com', 'my@gm.ail.com',
    'my@gma.il.com', 'mygmail+marva@gmail.com', 'my@gmail.com', 'mygmail+derik@gmail.com',
    'mygmail+alvie@gmail.com', 'my@gmail.com', 'mygmail+gage@gmail.com', 'mygmail+max@gmail.com',
    'my@gmail.com', 'mygmail+lita@gmail.com', 'mygmail+ginny@gmail.com', 'mygmail+timmy@gmail.com',
    'mygmail+kent@gmail.com', 'mygmail+kali@gmail.com', 'mygmail+bryce@gmail.com', 'my@gmail.com',
    'mygmail+rosie@gmail.com', 'mygmail+madge@gmail.com', 'my@gmail.com', 'mygmail+keily@gmail.com',
    'my@gmail.com', 'mygmail+evans@gmail.com', 'mygmail+stan@gmail.com', 'mygmail+kaye@gmail.com'
]

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=option)
driver.maximize_window()

def visit_bookmyshow(email):
    driver.get("https://in.bookmyshow.com") #change with required movie(auto ratings movie url)
    time.sleep(5)
    
    # Click on "Rate Now" button
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[1]/button").click() 
    time.sleep(1)

    # Click on "Continue with email"
    driver.find_element(By.XPATH, '//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()
    time.sleep(3)

    # Enter email and submit
    email_input = driver.find_element(By.CSS_SELECTOR, '#emailId')
    email_input.send_keys(email)
    time.sleep(2)
    email_input.send_keys(Keys.ENTER)

    # Wait for OTP entry
    time.sleep(16)

    # Click on "Rate" button
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[1]/button").click()
    time.sleep(3)

    # Move slider for rating
    slider = driver.find_element(By.CSS_SELECTOR, "#range")
    move = ActionChains(driver)
    move.click_and_hold(slider).move_by_offset(100, 100).release().perform()
    time.sleep(3)

    # Click on "Submit" button
    driver.find_element(By.XPATH, '//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()
    time.sleep(2)

    # Click on human logo to go back
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div[1]/div/div/div/div[2]/div[2]/span").click()
    time.sleep(2)

    # Click on "Signout"
    driver.find_element(By.XPATH, '//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click()
    time.sleep(2)

# Main script execution
for email in email_list:
    visit_bookmyshow(email)

driver.quit()
