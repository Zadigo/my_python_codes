import re
import time

from selenium.webdriver import Edge
from selenium.webdriver.support import expected_conditions, ui
from selenium.webdriver.common.by import By

PATH = 'C:\\Users\\Pende\\Downloads\\edgedriver_win32\\msedgedriver.exe'

class SawFirst:
    def __init__(self, url):
        self.driver = Edge(executable_path=PATH)
        self.driver.get(url)

    def _get_links(self, s):
        links = self.driver.find_elements_by_xpath('//a')
        sorted_links = [link for link in links if link.text.find(s, 0) != -1]
        return sorted_links

    def go_to_page(self, s):
        # for link in self._get_links(s):
        #     link.click()
        link = self._get_links(s)[0]
        link.click()
        time.sleep(2)
        try:
            gallery = self.driver.find_element_by_id('gallery-1')
            image_links = gallery.find_elements_by_tag_name('a')
        except Exception:
            pass
        else:
            time.sleep(1)
            image_links[0].click()
            ui.WebDriverWait(self.driver, 3000).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'featured-image2')))
            self.driver.find_element_by_class_name('featured-image2')
            
        

url = 'https://www.sawfirst.com/'
sawfirst = SawFirst(url)
sawfirst.go_to_page('Kimberley')
