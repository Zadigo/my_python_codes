import random
import string

def generator(size=10, chars=''):
    if  not chars:
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))