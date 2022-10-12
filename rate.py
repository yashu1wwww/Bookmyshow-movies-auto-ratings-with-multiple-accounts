#I putted 25 automate rating codes if need more means copy 3rd line to where the you find first driver.close() line and paste in 1253 line if want more means.....from selenium import webdriver to driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com")  #replace here mail with your dot mails/10mins mail/temp mail do these replace place for below where mail asked

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

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

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(5)

driver.find_element_by_css_selector('#emailId').send_keys("bms123@gmail.com") 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(13) #delayed 13 sec for otp entry

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(4)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()


