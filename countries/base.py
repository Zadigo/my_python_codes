"""Use this module to request a list of countries from
a REST link.

Description
-----------

    The API returns a list of countries dictionnaries containing
    various values that can be parsed afterwards:

        [
            { name, topLevelDomain, ... }
        ]
"""

import requests

class Countries:
    def __init__(self):
        base_url = 'https://restcountries.eu/rest/v2/all'
        try:
            response = requests.get(base_url)
        except requests.HTTPError:
            self.countries = []
        else:
            self.countries = response.json()

    def _iterator(self, name):
        for country in self.countries:
            yield country[name]

    @property
    def names(self):
        return self._iterator('name')

    @property
    def alpha_three_code(self):
        return self._iterator('alpha3Code')

    @property
    def region(self):
        return self._iterator('region')

    @property
    def subregion(self):
        self._iterator('subregion')

    @property
    def choices(self):
        """Create a list of tuples used for instance
        in models or forms in Django
        """
        for country in self.countries:
            item = (country['name'].lower(), country['name'])
            yield item

    def choices_to_py(self, name=None, exclude:list=None):
        """Create a list of tuples used for instance
        in models or forms in Django and return it to file

        Parameters
        ----------

            name: the name of the file

            exclude: a list that excludes the countries to return
        """
        with open('choices.py', 'w', encoding='utf-8') as f:
            elements_to_write = f"COUNTRIES = {list(self.choices)}"
            f.write(elements_to_write)

    def find(self, name):
        """Find a specific country in the list
        """
        for country in self.countries:
            if name == country['name']:
                return country
            else:
                return {}
