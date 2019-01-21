from datetime import datetime
import random
import time
from itertools import combinations
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


path = r'D:\\Programs\\chromedriver\\chromedriver.exe'

def reservation_date():
    d = random.choice(range(1, 30))
    m = random.choice(range(3, 12))
    full_date = '%s-%s-%s' % (d, m, 2019)

    get_weekday = datetime.strptime(full_date, '%d-%m-%Y').weekday()
    if get_weekday == 'Sunday':
        reservation_date()

    return full_date


def reservation_time():
    hours = [h for h in range(19, 22)]
    minutes = [m for m in range(5, 55, 5)]

    return '%s:%s' % (random.choice(hours), random.choice(minutes))


driver = webdriver.Chrome(executable_path=path)
driver.get('https://restaurant.hippopotamus.fr/restaurant/paris-place-de-clichy-8e/112')
# wait = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located('guests'))
time.sleep(10)
page_element = driver.find_elements_by_class_name('ButtonReservation')
page_element[1].click()
time.sleep(8)
date_next = driver.find_element_by_xpath('//div[@class="fancybox-desktop"] \
                                    //a[@class="ui-datepicker-next"]')
date_next.click()
# time.sleep(5)
# dates_elements = driver.find_elements_by_tag_name('td')
# dates_elements[random.randrange(1, len(dates_elements))].click()