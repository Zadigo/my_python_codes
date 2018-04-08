"""
Use this class to read the JSON country_list.json file.
It returns a Countries() object file.
"""

import json
from time import gmtime, strftime
from collections import namedtuple

class JsonCountryReader(object):
    """
    Get a singe country ro the SON ie as
    a coection obect:
    """
    def __init__(self):
        try:
            with open('country_list.json') as country_list_json_file:
                self._this = json.load(country_list_json_file)
        
        except FileNotFoundError as error:
            print(error.args[1])
            raise

    @staticmethod
    def _named_tuple_factory(json_result):
        """
        Creates a named tuple object for the
        class defintions
        """
        country_details = namedtuple('Countries', ['details', 'accessed_on'])
        current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        
        return country_details(json_result, current_time) or None

    def get_country_details(self, country_name):
        return self._named_tuple_factory(self._this[country_name])

    def get_countries_details(self, *country_names):
        return self._named_tuple_factory([self._this[country_key] for country_key in country_names])

    def get_countries_numbers(self, *country_names):
        return [self._this[country_key]['country_number'] for country_key in country_names]
    
    def get_countries_shortnames(self, *country_names):
        return self._named_tuple_factory([self._this[country_name]['shortname'] for country_name in country_names])

    def get_countries_key_list(self):
        return self._named_tuple_factory([country_name for country_name in self._this])

# print(JsonCountryReader().get_country_details('russia'))