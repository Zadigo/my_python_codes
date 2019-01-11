import requests
import math
import re
from pprint import pprint
from bs4 import BeautifulSoup
from threading import Thread
from collections import deque
from time import sleep

class SearchResults(list):
    def __init__(self, title=None, url=None, *args):
        if title or url:
            self.append([title, url])

        if args:
            for arg in args:
                self.append(arg)
                    

    def __str__(self):
        return super().__str__()

class Base:
    def __init__(self):
        self.search_url = 'https://google.com/search'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 58.0.3029.81 Safari/537.36',
            'Accept-Language':'en-US,en;q=0.5'
        }

    def _send_request(self, query, language='en', start=''):
        response = requests.get(self.search_url, \
            params={'q': query, 'hl': language, 'start': start}, \
            headers=self.headers)

        return response

    def _create_soup(self, response):
        return BeautifulSoup(response.text, 'lxml')

class GoogleSearch(Base):
    def search(self, query, num_results=5, language='en'):
        pages = int(math.ceil(num_results / float(10)))
        total = None
        for i in range(pages):
            start = i * 10
            if start == 0:
                start = ''

                response = self.create_soup(
                    self.send_request(q, language=language, start=start)
                )
            
            # search_items = soup.select('#resultStats')[0]
    
    @staticmethod
    def parse_result(results):
        s = SearchResults()
        for result in results:
            url = result['href']
            title = result.text
            s.append([title, url])
            
        yield result
            
GoogleSearch().search('Kendall Jenner')