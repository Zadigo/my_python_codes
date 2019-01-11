import requests

# COUNTRIES_ALL_URI = u'https://restcountries.eu/rest/v2/all'
class BaseCountries:
    request_uri = ''
    def __init__(self, *args, **kwargs):
        self.COUNTRIES = []
        try:
            result = requests.get(self.request_uri)
        except ConnectionError as error:
            print('There was an error %s' %
                error.args
            )
        else:
            self.countries = result.json()

class AllCountries(BaseCountries):
    """
    Get a tuple containing tuples of countries
    e.g. ((country, country), (..., ...))
    """
    fields = ['region', 'name']
    request_uri = 'https://restcountries.eu/rest/v2/all'
    def get_countries(self):
        for country in self.countries:
            for key, value in country.items():
                if key in self.fields:
                    self.COUNTRIES.append(
                        (value.lower(), value.lower())
                    )
        return self.COUNTRIES
    # def get_items(self):
    #     c = []
    #     for country in self.countries:
    #         for field in self.fields:
    #             c.append(country[field])
    #             self.COUNTRIES.append(c)
    #     return self.COUNTRIES





# COUNTRIES = []
# if result.status_code == 200:
#     fields = ['name']
#     countries = result.json()
#     for country in countries:
#         for key, value in country.items():
#             if key in fields:
#                 COUNTRIES.append(
#                     (value.lower(), value.lower())
#                 )

# print(COUNTRIES)