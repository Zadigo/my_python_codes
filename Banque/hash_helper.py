"""
Use this class to create a hash
that can be used for various operations
withi the program
"""

import hashlib as hs

def create_hash(name):
    """
    Use this module to create a hash for various
    banking operations like password generation,
    client_id generation.
    """
    def _unpack_hash(*kwargs):
        results = []
        for kwarg in kwargs:
            result = hs.md5(kwarg.encode('utf-8')).hexdigest()
            results.append(result)
        return results
    return _unpack_hash

@create_hash
def goo(*name):
    return name

print(goo('a', 'b', 'i'))