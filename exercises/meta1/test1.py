import requests

def send_request(self):
    response = requests.get('http://www.fivb.org')
    return response