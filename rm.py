import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
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


driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626") #first select the city and movie url and replace here which you want and do same process below code also where required..

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(a)) 
time.sleep(1)
driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(b)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(c)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(d)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(e)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(f)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(g)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(h)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()


driver = webdriver.Chrome()
driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(i)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(j)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()


driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(k)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(l)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(m)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(n)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(o)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(p)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(q)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(r)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()


driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(s)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(t)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(u)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(v)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()


driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(w)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(x)) 

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()


driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(y)) 
time.sleep(1)
driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(z)) 
time.sleep(1)
driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()


driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(aa)) 
time.sleep(1)
driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(bb)) 
time.sleep(1)
driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(cc)) 
time.sleep(1)
driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get("https://in.bookmyshow.com/bengaluru/movies/virupaksha/ET00346626")

driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_css_selector('#emailId').send_keys(random.choice(dd)) 
time.sleep(1)
driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(11)

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section[2]/div[1]/button/span').click()

time.sleep(1)

#slider = driver.find_element_by_css_selector("#range")
slider = driver.find_element_by_css_selector("#super-container > div.sc-11q8erw-0.cPZFLW > div > div.sc-10qvp23-0.bAXHgy > div > div > div > div:nth-child(2) > div.main.scroll-out.false.desktop-main > div > div.rating-wrapper.false > div.rating-section > div.rating-slider-wrapper")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(100,100).release().perform()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()

driver.close()

