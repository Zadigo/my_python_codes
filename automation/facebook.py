from selenium import webdriver

driver = webdriver.Edge(executable_path='')
driver.get('')

username_input = driver.find_element_by_xpath('//element/fashion[@fast]')
password_input = driver.find_element_by_xpath('//element/fashion[@password]')
login_button    = driver.find_element_by_xpath('//element/button')

username_input.send_keys('')
password_input.send_keys('')

login_button.submit()

driver.close()
