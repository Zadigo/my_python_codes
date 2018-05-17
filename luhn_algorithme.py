import itertools as it

def create_luhn(function):
    def wrapper():
        numbers = function()

        if not isinstance(numbers, list):
            raise TypeError('Numbers should a list. Got %s.' % numbers.__class__.__name__)

        for i in range(1, len(numbers), 2):
            # We add the number to itself
            new_number = (numbers[i]).__add__(numbers[i])

            # Number should not be above 9
            # if so, substract 9
            if new_number > 9:
                new_number = new_number - 9

            numbers[i] = new_number

        # Remainder of the sum of all
        # numbers divided by the 
        # list count should be 0
        remainder = sum(numbers) % 10
        if remainder == 0:
            return numbers
        else:
            return 'Numbers are not correct. Please change'

        # Return new number list
        return numbers
    return wrapper

@create_luhn
def r():
    return [9, 7, 2, 4, 8, 7, 0, 8, 6]

print(r())