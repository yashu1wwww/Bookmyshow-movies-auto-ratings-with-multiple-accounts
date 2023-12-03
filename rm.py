from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

#replace with your 15 dot mails of one gmails and another 15 dot mails of another gmails here remaining all goes automatic process you only enter the otp in 11 seconds(use mobile for otp where fastly we can enter by seeing otp in mobile)....

a=['yashwanth6677+nash@gmail.com']
b=['ya.s.hw.anth.6.6.77@gmail.com'] 
c=['y.as.h.w.ant.h.6.677@gmail.com'] 
d=['y.ash.wan.t.h6.677@gmail.com']
e=['y.a.sh.w.a.n.th6.6.7.7@gmail.com']
f=['y.as.hw.a.n.th.6677@gmail.com']
g=['yashwanth6677+marva@gmail.com']
h=['ya.shw.a.n.th.66.77@gmail.com']
i=['yashwanth6677+derik@gmail.com']
j=['yashwanth6677+alvie@gmail.com']
k=['yash.w.a.nth.6677@gmail.com']
l=['yashwanth6677+gage@gmail.com']
m=['yashwanth6677+max@gmail.com']
n=['y.ash.w.ant.h.6.677@gmail.com']
o=['yashwanth6677+lita@gmail.com']
#here i added another id dot mails
p=['yashwanth6666+ginny@gmail.com']
q=['yashwanth6666+timmy@gmail.com']
r=['yashwanth6666+kent@gmail.com']
t=['yashwanth6666+kali@gmail.com']
u=['yashwanth6666+bryce@gmail.com']
v=['y.as.h.wa.n.t.h66.6.6@gmail.com']
w=['yashwanth6666+rosie@gmail.com']
x=['yashwanth6666+madge@gmail.com']
y=['ya.sh.wa.n.t.h.66.66@gmail.com']
z=['yashwanth6666+keily@gmail.com']
aa=['yas.h.wanth.66.66@gmail.com']
bb=['yashwanth6666+evans@gmail.com']
cc=['yashwanth6666+stan@gmail.com']
dd=['yashwanth6666+kaye@gmail.com']

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:9222")

driver = webdriver.Chrome(options=option)

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(a))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(b))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(c))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(d))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(e))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(f))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(g))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(h))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(i))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(j))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(k))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(l))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(m))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(n))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(o))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(p))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(q))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(r))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)
driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(s))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(t))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(u))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(v))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(w))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(x))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(y))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(z))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(aa))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(bb))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(cc))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com/bengaluru/movies/master/ET00110368") #first select the city then select the required movie url

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate now button

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click on continue with email

time.sleep(3)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(dd))  #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #email submit

time.sleep(15)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click() #click on rate button

time.sleep(3)

slider = driver.find_element_by_css_selector("#range") #automatically star move..

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click() #submit button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(20)


