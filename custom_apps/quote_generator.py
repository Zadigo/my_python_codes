import re

def create_quote(*args):
    if not args:
        return []

    phrases = []
    _new = ''
    for arg in args:
        words = arg.rsplit(' ')
        for word in words:
            _new += word + '-'
            _new_word = re.search(r'([a-zA-Z\-]+)(\-)', _new).group(1)
    
        phrases.append(_new_word.lower())
        _new = ''
    return phrases

def inverse_quote(*args):
    if not args:
        return []

    phrases = []
    _new = ''
    for arg in args:
        words = arg.rsplit('-')
        for word in words:
            _new += word + ' '
    
        phrases.append(_new.capitalize().strip())
        _new = ''
    return phrases

