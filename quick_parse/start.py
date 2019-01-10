from bs4 import BeautifulSoup
import re
import csv

HTML_FILE = 'D:\\Programs\\Repositories\\my_python_codes\\quick_parse\\items.html'

OUTPUT_FILE = 'D:\\Programs\\Repositories\\my_python_codes\\quick_parse\\output.csv'

def _table():
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        content = soup.find('tbody').find_all('tr')
        for row in content:
            country_code = row.find('span',class_='monospaced').text.strip()
            country_tag = row.find('a', title=re.compile(r'[a-zA-Z]{7,}'))
            if country_tag:
                country = country_tag['title'].strip()
            yield tuple((country_code, country))

def _write():
    with open(OUTPUT_FILE, 'w', newline='') as f:
        csv_file = csv.writer(f)
        values = _table()
        csv_file.writerow(['country_code', 'country'])
        for row in values:
            csv_file.writerow(row)

_write()