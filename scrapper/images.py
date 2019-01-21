import pandas
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

CHROME_DRIVER_PATH = r'D:\\Programs\\chromedriver\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get('https://www.sawfirst.com/kimberley-garner-booty-in-bikini-on-the-beach-in-miami-2018-12-31.html/kimberley-garner-shows-off-her-red-hot-bikini-bod-in-a-red-bikini-5')
driver.implicitly_wait(35)
inputElements = driver.find_elements_by_xpath('//div[@id="gallery-1"]/dl[@class="gallery-item"] \
                                    /dt[@class="gallery-icon portrait"]/a')


# WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(inputElements))
# inputElements[0].click()
# driver.implicitly_wait(10)
# inputElement = driver.find_element_by_class_name('attachment- size-')
# inputElement[0].click()

# actions = ActionChains(driver)
# actions.key_down(Keys.CONTROL).key_down(Keys.TAB).key_up(Keys.TAB).key_up(Keys.CONTROL).perform()
# actions.