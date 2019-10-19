import pandas
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


CHROME_DRIVER_PATH = r'D:\\Programs\\chromedriver\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

# gallery-icon portrait
driver.get('https://www.sawfirst.com/')
inputElement = driver.find_elements_by_xpath('//a[@title="Permanent Link to Metisha Schaefer Booty in Bikini on Miami Beach"]')
inputElement[0].click()
# inputElement.send_keys('Kendall Jenner')
# inputElement.submit()
# try:
#     WebDriverWait(driver, 10).until(expected_conditions.title_contains('Kendall Jenner'))
# except BaseException:
#     raise
# else:
#     # print(driver.title)
#     # driver.save_screenshot('google.png')
#     driver.execute_script("window.scrollTo(0, 70);")
#     pass
# BeautifulSoup(driver.page_source, 'lxml')
# driver.quit()
