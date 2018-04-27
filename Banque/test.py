# def google(func):
#     def googla(name):
#         return 'Hello ' + name
#     return googla

# @google
# def googlx(name):
#     return name

# print(googlx('a'))

# from hash_helper import create_hash

# @create_hash
# def goo(*name):
#     return name

# print(goo('a', 'b', 'c'))

# import hash_helper as hs

# a = hs.create_hash('a')
# print(a('Constance-971'))

# STATEMENTS = {
#     'select': 'SELECT {} FROM {} WHERE {} {} {}'
# }

# args = ('a', 'b', 'c')
# s =''
# # if type(args) == 'tuple':
# for i in range(0, len(args)):
    

# print(STATEMENTS['select'].format(r, 'users', 'a', '>=', 'a'))

import hash_helper as hs

@hs.create_hash
def a(*n):
    return n

print(a('a', 'b'))

