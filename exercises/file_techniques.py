import requests
import csv

test_path='C:\\Users\\Zadigo\\Documents\\Programs\\my_python_codes\\exercises\\testa.csv'

response = requests.get('https://raw.githubusercontent.com/Zadigo/EmailsApp/master/test.csv')
# with open(test_path, 'wb') as f:
#     f.write(response.content)
