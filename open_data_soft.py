import requests
from urllib.parse import urlencode

BASE_URI = u'https://data.opendatasoft.com/api/records/1.0/search/?{query}'

class BaseOpenDataSoft:
    def __init__(self, dataset, **kwargs):
        params = {'dataset': '', 'sort': 'uo_lib'}
        
        if not isinstance(dataset, str):
            raise TypeError('Received %s instead of a string' %
                dataset.__class__.__name__ 
            )
        params.update({'dataset':dataset})

        if kwargs:
            for key, value in kwargs.items():
                params[key] = value

        request_url = BASE_URI.format(query=urlencode(params))

        try:
            # Send request
            response = requests.get(request_url)
        except requests.HTTPError as e:
            print('There was an error %s' % e.args)
            raise
        else:
            self.json_obj = response.json()['records'][0]['fields']

class OpenDataSoft(BaseOpenDataSoft):
    def _set(self):
        for key, value in self.json_obj.items():
            setattr(OpenDataSoft, key, value)
