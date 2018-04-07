import itertools as it
# from argparse import ArgumentParser

# def _parse_args():
#     args = ArgumentParser(
#         description='Create a Luhn number'
#     )
#     args.add_argument('number', help='Enter a 7 digit number', type=int)
#     args.add_argument('-e', '--encrypt', help='Encrypt nuner using 5')
#     args.parse_args()
#     return args

# def _create_nubers():
#     pass

# def Main():
#     arg = _parse_args()
#     if arg:
#         print('True')
#         print(arg._get_args())

# if __name__ == '__main__':
#     Main()

numbers = [9, 7, 2, 4, 8, 7, 0, 8, 6]

for i in range(1, len(numbers), 2):
    # We add the number to itself
    new_number = (numbers[i]).__add__(numbers[i])

    # Number should not be above 9
    # if so then te have to substract 9
    if new_number > 9:
        new_number = new_number - 9

    numbers[i] = new_number

remainder = sum(numbers) % 10

if remainder == 0:
    print('Your numbers are', numbers)
else:
    print('Numbers are not correct. Please change')