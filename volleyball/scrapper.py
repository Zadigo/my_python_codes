import pandas
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

CHROME_DRIVER_PATH = r'D:\\Programs\\chromedriver\\chromedriver.exe'

class Start:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def get_website(self, url):
        self.driver.get(url)
        # wait_for_table = WebDriverWait(self.driver, 5)
        # wait_for_table.until(EC.presence_of_element_located('team-list'))

        team_picker = self.driver.find_elements_by_id('team-list')
        team_table = self.driver.find_elements_by_class_name('tabs-content')

        soup = BeautifulSoup(team_table[0].text, 'html.parser')
        data_table = pandas.read_html(soup.find('table'))
        print(data_table)

        # links = team_table[0].find_elements_by_xpath('//tbody/tr/td//a')
        # for i in range(0, len(links)):
        #     links[i].click()

Start().get_website('http://japan2018.fivb.com/en/competition/teams/arg%20argentina/team_roster')
