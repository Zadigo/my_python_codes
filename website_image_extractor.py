import requests
import collections
# import useragent as agent
from bs4 import BeautifulSoup

agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"
UR = 'http://www.sawfirst.com/madison-beer-out-and-about-in-west-hollywood-2018-04-07.html/madison-beer-106'

def _send_requests():
    try:
        response = requests.get(UR, agent)
    except Exception as error:
        raise Exception('Error: %s' % error.args)
    else:
        print('Success: %s' % response.status_code)
        return response

class ImagesExtractor(object):
    def __init__(self, **paras):
        self._soup = BeautifulSoup(paras['response'].text, 'html.parser')

    def _get_all(self, attribute, args):
        tags = ''
        
        if  len(args) == 0:
            tags = self._soup.find_all(attribute)
        
        else:  
            # tags = self._soup.has_attr('class')
            if args['class_'] != '':
                tags = self._soup.find_all(attribute, args['class_'])
            elif args['id'] != '':
                tags = self._soup.find_all(attribute, args['id'])
            else:
                tags = ''

        if tags is not None:
            images = collections.namedtuple('Images', ['links'])
            group_iages = images(self._tag_helper(tags))
            print(group_iages)
        else:
            print(tags)
    
    @staticmethod
    def _tag_helper(vas):
        tag_group = [va for va in vas]
        return tag_group

def Main():
    a = dict(class_='attachment-thumbnail size-thumbnail', id='')
    ImagesExtractor(response=_send_requests())._get_all('img', a)

Main()
