# import time
# from urllib.parse import urljoin

# import selenium
# from selenium.webdriver import Edge
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import ui, expected_conditions

# URL = 'https://tinder.com/'

# PATH = 'C:\\Users\\Pende\\Documents\\edge_driver\\msedgedriver.exe'

# def tinder():
#     driver = Edge(executable_path=PATH)
#     driver.get(URL)
#     try:
#         time.sleep(5)
#         buttons = driver.find_element_by_xpath('/button[@type="button"]')
#     except AttributeError:
#         print('An error occured. Element is not visible')
#     else:
#         # facebook_connection.click()
#         print(buttons)
#         driver.quit()
#     # print(facebook_connection)

# tinder()
