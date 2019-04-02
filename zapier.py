import requests
from urllib.parse import urlencode

class Zapier:
    def create_request(self, url, return_response=False, **kwargs):
        try:
            response = requests.post(url, data=kwargs)
        except requests.HTTPError:
            pass
        else:
            if response:
                return response

class MailChimp(Zapier):
    url = 'https://hooks.zapier.com/hooks/catch/3490719/phh7m1/'

    def create_user(self, email):
        response = super().create_request(self.url, email=email)
        return response

class Slack(Zapier):
    def send_slack(self, msg):
        response = super().create_request('', msg)