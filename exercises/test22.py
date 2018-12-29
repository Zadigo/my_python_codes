import itertools
import random
import statistics
import collections

# ['a', 'b', 'c', 'd', 'e'])
# list(itertools.chain(['a', 'b', 'c'], ['d', 'e']))

# a = [{'name': 'Emma', 'height': 195}, {'name': 'Julie', 'height': 195}, {'name': 'Constance', 'height': 175}]
# b = itertools.groupby(a, key=lambda x: x['height'])
# for key, values in b:
#     c = '{}: {}'.format(
#         key,
#         list(values)
#     )
#     print(c)

# print(random.shuffle(['a', 'b', 'c']))
# print(random.sample(['a', 'b', 'c'], 2))
# print(random.randrange(1,stop=15,step=1))

group = ('A', 'B')
players = ('Emma', 'Pauline', 'Yasmine')
# print(list(zip(group, itertools.islice(players, 2))))
# print(list(itertools.zip_longest(*players)))
for c in itertools.repeat(iter(players), times=2):
    print(list(itertools.takewhile(lambda x: x == 'Emma', c)))