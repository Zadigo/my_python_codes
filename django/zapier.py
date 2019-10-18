import requests

class Zapier:
    def create_request(self, url, **kwargs):
        try:
            response = requests.post(url, data=kwargs)
        except requests.HTTPError:
            raise
        return response

class MailChimp(Zapier):
    url = ''

    def create_user(self, email):
        response = super().create_request(self.url, email=email)
        return response

class Slack(Zapier):
    url = ''

    def send_slack(self, msg):
        response = super().create_request(self.url, msg=msg)
        return response
