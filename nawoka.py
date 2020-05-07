import selenium
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time
from urllib.parse import urljoin

PATH = 'C:\\Users\\Pende\\Downloads\\edgedriver_win32\\msedgedriver.exe'

class Nawoka:
    driver = Edge(executable_path=PATH)

    def __init__(self):
        url = 'https://nawoka.fr/shop/collections/sacs/'
        self.driver.get(url)

    def check_tunnel(self):
        # Check that we can click on a given product
        WebDriverWait(self.driver, 4000).until(expected_conditions.element_to_be_clickable((By.ID, 'btn_product_details')))
        self.driver.find_element_by_id('btn_product_details').click()
        # Check that we can add an item to the cart,
        # and that we can access the cart for checkout
        WebDriverWait(self.driver, 2000).until(expected_conditions.element_to_be_clickable((By.ID, 'btn_add_to_cart')))
        self.driver.find_element_by_id('btn_add_to_cart').click()
        time.sleep(3)
        self.driver.find_element_by_id('link_cart').click()
        # driver.quit()

    def check_products_links(self, path=None):
        truth_array = []
        errors = []
        links = self.driver.find_elements_by_id('btn_product_details')
        WebDriverWait(self.driver, 3000).until(expected_conditions\
                    .presence_of_all_elements_located((By.ID, 'btn_product_details')))
        for link in links:
            try:
                # link.click()
                path = link.get_attribute('href')
                self.driver.get(path)
            except Exception:
                # errors.append(link.current_url())
                truth_array.append(False)
            else:
                truth_array.append(True)
                self.driver.back()
                # self.driver.execute_script('window.history.go(-1)')
                WebDriverWait(self.driver, 3000).until(expected_conditions\
                            .presence_of_all_elements_located((By.ID, 'btn_product_details')))
        # self.driver.quit()
        return all(truth_array)


nawoka = Nawoka()
nawoka.check_products_links('/')