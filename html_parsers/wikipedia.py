from bs4 import BeautifulSoup
import re
import csv
import os
import datetime
import secrets
from urllib.parse import unquote
import argparse


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HTML_FILE = os.path.join(BASE_DIR, 'items.html')


def create_new_file():
    current_date = datetime.datetime.now().date()
    token = secrets.token_hex(5)
    return f'{current_date.day}_{current_date.month}_{current_date.year}_{token}.csv'

OUTPUT_FILE = os.path.join(BASE_DIR, create_new_file())

def write_csv(func):
    def wrapper(headers=[], filename=None):
        with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as f:
            csv_file = csv.writer(f)
            universities = func(headers)
            for row in universities:
                csv_file.writerow(row)
    return wrapper


def get_soup():
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    return soup

@write_csv
def parse_university_table(headers=[]):
    universities = []
    soup = get_soup()
    table_rows = soup.find_all('tr')
    for table_row in table_rows:
        table_row_children = list(table_row.children)
        try:
            university_population = table_row_children[3].text.strip()
        except IndexError:
            university_population = None

        # Get the universisty's
        # Wiki link
        link = table_row.find('a')

        try:
            university_title = link['title']
            university_wiki = unquote(link['href'])
        except KeyError:
            university_title = ''
            university_wiki = ''

        universities.append([university_title, university_population, 
                                university_wiki])
    # Header can be empty
    # as in most tables
    # with headers
    universities.pop(0)
    if headers:
        universities.insert(0, headers)
    return universities

# parse_university_table()

# def _table():
#     with open(HTML_FILE, 'r', encoding='utf-8') as f:
#         soup = BeautifulSoup(f, 'html.parser')
#         content = soup.find('tbody').find_all('tr')
#         for row in content:
#             country_code = row.find('span',class_='monospaced').text.strip()
#             country_tag = row.find('a', title=re.compile(r'[a-zA-Z]{7,}'))
#             if country_tag:
#                 country = country_tag['title'].strip()
#             yield tuple((country_code, country))

# def _write():
#     with open(OUTPUT_FILE, 'w', newline='') as f:
#         csv_file = csv.writer(f)
#         values = _table()
#         csv_file.writerow(['country_code', 'country'])
#         for row in values:
#             csv_file.writerow(row)

# _write()

if __name__ == "__main__":
    args = argparse.ArgumentParser(description='Parse a Wikipedia table content')
    args.add_argument('--filename', help='Override the automated filename')
    args.add_argument('--headers', help='Indicate file headers', type=list)
    parsed_args = args.parse_args()

    parse_university_table()
