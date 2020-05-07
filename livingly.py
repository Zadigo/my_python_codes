import time
from urllib.parse import urlencode, urljoin

import selenium
from selenium.webdriver import ActionChains, Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

PATH = 'C:\\Users\\Pende\\Documents\\edge_driver\\msedgedriver.exe'

def livingly():
    url = 'https://www.livingly.com/runway/Milan+Fashion+Week+Fall+2019/Aigner/Details/browse'
    driver = Edge(executable_path=PATH)
    action_chains = ActionChains(driver)
    driver.get(url)
    WebDriverWait(driver, 5000).until(expected_conditions\
            .visibility_of_element_located((By.CLASS_NAME, 'thumbnail-strip')))
    content = driver.find_element_by_xpath('//ul[@class="thumbnail-strip"]')
    links = content.find_elements_by_tag_name('a')

    # Store the links beforehand because Selenium does
    # not update the driver with the new content
    paths = (link.get_attribute('href') for link in links)

    for path in paths:
        # link.click()
        driver.get(path)
        WebDriverWait(driver, 3000).until(expected_conditions\
                .visibility_of_element_located((By.CLASS_NAME, 'region-image')))
        try:
            slideshow = driver.find_element_by_xpath('//div[@class="slideshow-img-link"]')
        except Exception:
            driver.execute_script('window.history.go(-1);')
        else:
            if slideshow.is_displayed():
                big_image_url = slideshow.find_element_by_tag_name('img').get_attribute('data-zoom-url')

                if big_image_url:
                    # driver.get(big_image_url)
                    driver.execute_script(f'window.open("{big_image_url}", "_blank");')

                    # This part will right click on the image,
                    # download it locally
                    image = driver.find_elements_by_tag_name('img')
                    action_chains.context_click(image).perform()

                    # This section gets all the tabs in the
                    # browser, closes the newly opened image
                    # tab and returns the previous one
                    driver.switch_to_window(driver.window_handles[1])
                    driver.close()
                    driver.switch_to_window(driver.window_handles[0])
                    # Wait a couple of seconds before returning
                    # going back in history
                    driver.execute_script('window.history.go(-1);')
                else:
                    driver.execute_script('window.history.go(-1);')
    driver.close()
# livingly()
