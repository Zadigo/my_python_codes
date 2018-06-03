from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('http://www.tennisforum.com/')
inputElement = driver.find_element_by_id('navbar_username')
inputElement.send_keys('Vikapower')