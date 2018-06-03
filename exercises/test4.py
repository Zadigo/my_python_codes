import requests
from bs4 import BeautifulSoup

def get_requests(www=''):
    def decorator(func=''):
        def wrapper():
            response = requests.get(www)
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup or []
        return wrapper
    return decorator

@get_requests('http://www.fivb.org')
def test(*args):
    return 'a'
    
print(test())