from collections import namedtuple

def create_luhn(numbers=[]):
    """
    The Luhn algorithm or Luhn formula, also known as the "modulus 10" or "mod 10" algorithm, 
    named after its creator, IBM scientist Hans Peter Luhn, is a simple checksum formula 
    used to validate a variety of identification numbers, 
    such as credit card numbers, IMEI numbers [...] 
    https://en.wikipedia.org/wiki/Luhn_algorithm
    """
    if not isinstance(numbers, list):
        raise TypeError('Numbers should a list. Got %s.' % 
            numbers.__class__.__name__)

    for i in range(1, len(numbers), 2):
        # We add the number to itself
        # new_number = (numbers[i]).__add__(numbers[i])
        new_number = sum([numbers[i], numbers[i]])

        # Number should not be > 9.
        # If so, substract 9
        if new_number > 9:
            new_number = new_number - 9

        # Replace the old number
        numbers[i] = new_number

    # Remainder of the sum of all
    # numbers divided by the 
    # list count should be 0
    remainder = sum(numbers) % 10
    if remainder == 0:
        luhn = namedtuple('Luhn', ['numbers'])
        return luhn(numbers)
    else:
        return 'Numbers are not correct. Please change'
