import tweepy
from googlesearch import search


class WebSearch:
    def __init__(self):
        res=list(search('Ekaterina Efimova', num=5))
        print(res)

WebSearch()