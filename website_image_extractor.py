import requests
import collections
from useragent.user_agent import get_rand_user_agent
from bs4 import BeautifulSoup

class Requester:
    def __init__(self, uri):
        try:
            response = requests.get(uri, get_rand_user_agent())
        except requests.HTTPError as e:
            print('There was an error %s' % e.args)
        else:
            print('Success for: %s' % uri)
            self.response = response

class ImagesExtractor(Requester):
    def get_all_images(self, **kwargs):
        soup = BeautifulSoup(self.response.text, 'html.parser')
        if not kwargs:
            tags = soup.find_all('img')
        else:
            if 'attribute' in kwargs:
                tags = soup.find_all('img', kwargs['attribute'])


        return tags
        

# def Main():
#     a = dict(class_='attachment-thumbnail size-thumbnail', id='')
#     ImagesExtractor(response=_send_requests())._get_all('img', a)

# Main()

ImagesExtractor('http://www.sawfirst.com/madison-beer-out-and-about-in-west-hollywood-2018-04-07.html/madison-beer-106').get_all_images()
