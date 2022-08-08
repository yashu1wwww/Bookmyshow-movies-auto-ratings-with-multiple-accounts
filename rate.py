#I putted 10 automate rating codes if need more means copy 3rd line to where the you find first driver.close() line and paste in 470 line if want more means.....from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #change your required movie url which movie you want to auto rate and do below codes also

time.sleep(6)

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys("yashwanth6671+nita@gmail.com") #change email to yours and below change put same email 
#exa:-viratvk@gmail.com
#viratv.k@gmail.com
#v.iratvk@gmail.com
#or use temp mail or gmail dot generator for more

#put one dot where you required or use other emails if you have more

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(20) #depends on how speed you enter otp 

driver.maximize_window()
time.sleep(6)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(5)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform() #i entered 90% ratings values change which percentage rating your required same change in below code also i entered 90% rating for all 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368")

time.sleep(4)

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys("yashwanth6671@gmail.com") 

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(20)

driver.maximize_window()
time.sleep(6)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(5)

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
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368")

time.sleep(5)

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys("y.ash.w.an.th6.6.7.1@gmail.com") 

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(20)

driver.maximize_window()
time.sleep(6)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(5)

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
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368")

time.sleep(5)

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys("yashwanth6671@gmail.com") 

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(20)

driver.maximize_window()
time.sleep(6)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(5)

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
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368")

time.sleep(5)

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys("ya.s.hw.anth.6.6.71@gmail.com") 

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(20)

driver.maximize_window()
time.sleep(6)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(5)

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
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368")

time.sleep(5)

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys("y.as.h.w.ant.h.6.671@gmail.com") 

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(20)

driver.maximize_window()
time.sleep(6)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(5)

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
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368")

time.sleep(5)

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys("y.a.sh.wa.n.th667.1@gmail.com") 

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(20)

driver.maximize_window()
time.sleep(6)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(5)

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
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368")

time.sleep(5)

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys("y.ash.wan.t.h6.671@gmail.com") 

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(20)

driver.maximize_window()
time.sleep(6)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(5)

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
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368")

time.sleep(5)

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys("yash.w.ant.h.6.671@gmail.com") 

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(20)

driver.maximize_window()
time.sleep(6)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(5)

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
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368")

time.sleep(5)

driver.find_element_by_css_selector('#super-container > div.sc-11q8erw-0.jJDMQQ > section.sc-qswwm9-0.ljnioe > div > div > div.sc-qswwm9-5.ehwnas > section.sc-ycjzp1-0.duexLW > div.sc-ycjzp1-1.fdWjQB > button > span').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys("y.a.sh.w.a.n.th6.6.7.1@gmail.com") 

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(20)

driver.maximize_window()
time.sleep(6)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(5)

slider = driver.find_element_by_css_selector("#range")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[3]/div/button').click()

driver.close()

#if you want url from text file where once enter url its take process for reamaining codes use below codes by removing hastags add the below codes 
#after these line
#driver = webdriver.Chrome()
#with open("urls.txt") as f:  #put your required rating movie url in url text file once you enter there no needed to change url for below codes 
    #for url in f:
        #driver.get(url)
