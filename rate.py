#I putted 25 automate rating codes if need more means copy 3rd line to where the you find first driver.close() line and paste in  line if want more means.....from selenium import webdriver to driver.close()

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

with open("urls.txt") as f:
    for url in f:
        driver.get(url)  
        
driver.implicitly_wait(6)

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button').click()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys("mail123@gmail.com") #replace with your temp mail do for below code also opt must not enter manually you must enter it 10 second delayed for that if want more change no


driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(10)

driver.maximize_window()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(2)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(10,10).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()
