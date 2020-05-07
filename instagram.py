import selenium
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, ui
import time
# from selenium.webdriver.support

PATH = 'C:\\Users\\Pende\\Downloads\\edgedriver_win32\\msedgedriver.exe'

class Instagram:
    def __init__(self):
        self.driver = selenium.webdriver.Edge(executable_path=PATH)
        self.url ='https://instagram.com'

    def open_instagram(self, username, password):
        self.driver.get(self.url)
        ui.WebDriverWait(self.driver, 5000).until(expected_conditions\
                            .visibility_of_element_located((By.XPATH, '//input')))
        return self._login(self.driver, username, password)

    @staticmethod
    def already_logged_in(driver, username):
        try:
            profile_link = driver.find_element_by_xpath(f'//a[href="/{username}/"]')
        except:
            return False
        else:
            return profile_link, True

    def _login(self, driver, username, password):
        if not self.already_logged_in(driver, username):
            username_input = driver.find_element_by_xpath('//input[@name="username"]')
            password_input = driver.find_element_by_xpath('//input[@name="password"]')

            if username_input and password_input:
                try:
                    username_input.send_keys(username)
                    password_input.send_keys(password)
                except TypeError:
                    print('An error occured')
                    driver.quit()
                    return False
                else:
                    driver.find_element_by_xpath('//button[@type="submit"]').click()
                    time.sleep(3)
                    return driver
        else:
            return True

# class PersonalPage(Instagram):
#     def go_to_personal_page(self, username):
#         self.driver.find_elements_by_xpath(f'//a[href="/{username}/"]').click()
#         return True

class Search(Instagram):
    def __init__(self, username, password):
        super().__init__()
        self.open_instagram(username, password)

    def do_search(self, q):
        search_box = self.driver.find_elements_by_xpath('//input[placeholder="Search"]')
        try:
            search_box.send_keys(q)
            search_box.send_keys(keys.Keys.ENTER)
        except:
            print('An error occured')
            return False
        else:
            # document.body.scrollHeight
            search_box.execute_script('window.scrollTo(0, 1235.5)')

# instagram = Instagram()
# instagram.open_instagram('iamjohnsson', 'Constance97170-Jac')

search = Search('iamjohnsson', 'Constance97170-Jac')
search.do_search('Selena Gomez')