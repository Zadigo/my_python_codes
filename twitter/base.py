import tweepy
from twitter_settings import CONSUMER_KEY, CONSUMER_SECRET
from twitter_settings import ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from tweepy.auth import OAuthHandler

class BaseTwitter(type):
    def __new__ (cls, clsname, bases, clsdict):
        auth = OAuthHandler(
            CONSUMER_KEY, CONSUMER_SECRET
        )
        auth.set_access_token(
            ACCESS_TOKEN, ACCESS_TOKEN_SECRET
        )
        api = tweepy.API(auth)
        clsdict['api'] = api
        new_class = super().__new__(cls, clsname, bases, clsdict)
        return new_class

class BaseManager(metaclass=BaseTwitter):
    api = None

class Manager(BaseManager):
    statuses = None
    def get_user_timeline(self, screen_name):
        self.statuses = tweepy.Cursor(self.api.user_timeline, screen_name=screen_name).items(50)
    
    def return_statuses(self):
        for status in self.statuses:
            return status

# class A(Manager):
#     def test(self):
#         super().get_user_timeline('frenchgirlnyc')

# A().test()