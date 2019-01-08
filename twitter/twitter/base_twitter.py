import tweepy
from tweepy.auth import OAuthHandler

class Base:
    def __init__(self):
        auth = OAuthHandler('CONSUMER_KEY', 'CONSUMER_SECRET')
        auth.set_access_token('ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET')
        self.twitter_api = tweepy.api.API(auth)

class QuerySelectors(Base):
    def get_user_timeline(self, user_screen_name, limit=50):
        statuses = tweepy.Cursor(self.twitter_api, user_screen_name).items(limit)
        return statuses

    def get_recent_tweets(self):
        recent_statuses = tweepy.Cursor(self.twitter_api.user_timeline).items(20)
        return recent_statuses

QuerySelectors().get_user_timeline()
