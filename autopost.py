from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(3)
driver.get("https://www.facebook.com")
# email (change ******* with your facebook email)
email_element = driver.find_element_by_xpath('.//*[@id="email"]')
email_element.send_keys('*******')
# password (change ***** with your facebook password)
password_element = driver.find_element_by_xpath('.//*[@id="pass"]')
password_element.send_keys('*****')
log_btm_element = driver.find_element_by_xpath('.//*[@id="loginbutton"]')
log_btm_element.click()
time.sleep(5)
# list of groups that you wanna post in (change *** with facebook group url)
groups_list = ["***","***","***","***","***","***"]
for group in groups_list:
    driver.get(group)
    start_disc_element = driver.find_element_by_xpath('./html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/ul/li[2]/a/span')
    start_disc_element.click()
    time.sleep(5)
    status_element = driver.find_element(By.XPATH,'.//div[@contenteditable="true"]')
    # the status that you wanna post (change the *** with the status that you wanna post)
    status_element.send_keys('***')
    style_element = driver.find_element_by_xpath('./html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/table/tbody/tr/td[12]/div/a/div')
    style_element.click()
    time.sleep(5)
    post_element = driver.find_element_by_xpath('./html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/div/div[2]/button')
    post_element.click()
    time.sleep(5)