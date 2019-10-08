# """
# """

import os
import re
# import gspread
from oauth2client.service_account import ServiceAccountCredentials


# SCOPE = [
#     'https://spreadsheets.google.com/feeds',
#     'https://www.googleapis.com/auth/drive'
# ]

# PATH = os.path.join(os.getcwd(), 'google_spread\\secret_keys.json')

BASE_PATH = os.path.join(os.getcwd(), 'google_spread')
SECRET_KEYS = os.listdir(BASE_PATH)


def get_json(function):
    def special_map(*iterables):
        a = [function(i) for i in iterables]
        return a
    return special_map

@get_json
def w(*others):
    pattern = r'\w+\.(json)'
    return re.search(pattern, str(others))

z = w(SECRET_KEYS)
print(z)



# class GoogleSheetAPI(object):
#     """
#     """
#     def __init__(self, sheet_name):
#         _credentials = ServiceAccountCredentials.from_json_keyfile_name(PATH, SCOPE)
#         _client = gspread.authorize(_credentials)
#         self._sheet_object = _client.open(sheet_name).sheet1
    
#     # def get_all_records(self):
#     #     """
#     #     """
#     #     return self._sheet_object.get_all_records()

# class AllRecords(GoogleSheetAPI)
#     def get_all_records(self):
#         return self._sheet_object.get_all_records()


# Use creds to create a client for google API
# scope = [
#     'https://spreadsheets.google.com/feeds',
#     'https://www.googleapis.com/auth/drive'
#     ]
# creds = ServiceAccountCredentials.from_json_keyfile_name('secret_keys.json', scope)
# client = gs.authorize(creds)
# # Find a workbook by name
# sheet = client.open('Data').sheet1

# # Extract data
# list_of_data = sheet.get_all_records()
# t = 0
# for data in list_of_data:
#     print(data)
#     t = t + 1
#     if t == 3:
#         break

# Update cells
# sheet.update_cell(2, 1, 8)

# Get sheet title
# table_title = sheet.title

# print(sheet.insert_row([1, 1], index=5))