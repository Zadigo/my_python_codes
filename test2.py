import collections
import requests as req
import test3
from bs4 import BeautifulSoup

url = u'http://www.hawtcelebs.com/bella-hadid-leaves-tag-heuer-ginza-boutique-opening-ceremony-in-tokyo-04-09-2018/'

class ResponseHelper(object):
    def __init__(self, request_response):
        self._request_response = request_response.text
    
    def _get_text_response(self):
        tags = BeautifulSoup(self._request_response, 'html.parser')
        return tags

    def get_images(self, *args):
        images_group = self._get_text_response()
        images = images_group.find_all('img')
        return images

    def get_links(self, *args):
        links_group = self._get_text_response()
        links = links_group.find_all('a')
        return links

    @staticmethod
    def actory(html_object):
        pass
    


def _post_request():
    pass


def _request():
    try:
        response = req.get(url)
    except req.HTTPError as error:
        print('' % error.args)
        raise
    else:
        if response.status_code >= 200 and response.status_code <= 300:
            # Response Helper
            return response
        else:
            raise ConnectionAbortedError('')

res = _request()
print(ResponseHelper(res).get_images())


# u = [
#     u'http://www.a.io',
#     u'http://www.b.io',
#     u'http://www.c.io'
# ]

# from urllib.parse import urljoin

# z = map(lambda w: urljoin(w, 'wea'), u)
# print(set(z))

# from collections import abc
# import collections as c