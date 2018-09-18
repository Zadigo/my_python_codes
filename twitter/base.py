"""
http://docs.tweepy.org/en/v3.6.0/api.html
"""

import tweepy
from twitter_settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from tweepy.auth import OAuthHandler

class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __set__(self, instance, text):
        instance.__dict__[self.name] = text

class Typed(Descriptor):
    text = ''
    def __set__(self, instance, text):
        text_len = len(text)
        if text_len > 280:
            raise TypeError('Error')
        super().__set__(instance, text)

class BaseTwitter(type):
    def __new__ (cls, clsname, bases, clsdict):
        new_class = super().__new__(cls, clsname, bases, clsdict)
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        setattr(new_class, 'api', tweepy.API(auth))
        # api = tweepy.API(auth)
        # api.update_status()
        return new_class

class BaseManager(metaclass=BaseTwitter):
    pass 

# class Manager(BaseManager):
#     pass
    # statuses = None
    # def get_user_timeline(self, screen_name):
    #     self.statuses = tweepy.Cursor(self.api.user_timeline, screen_name=screen_name).items(50)
    
    # def return_statuses(self):
    #     for status in self.statuses:
    #         return status

#     def create_tweet(self, text):
#         return self.api.update_status(status=text)

# Manager().create_tweet('this')

class CreateTweet(BaseManager):
    def _create(self, text):
        return self.api.update_status(status=text)
