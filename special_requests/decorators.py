import re

def parser(function):
    values = function()
    if isinstance(values, list):
        pass

    def parse(**kwargs):
        if 'pattern' in kwargs:
            pattern=kwargs['pattern']
        else:
            raise TypeError()
        return [re.search(pattern, str(value)).group(0) for value in values]
    return parse

@parser
def par(**kwargs):
    return ['a','y','u']

print(par(pattern=r'[a-z]+'))