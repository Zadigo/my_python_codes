a = ['a', 'b', 'c', 'e']
b = ['r', 't', 'u', 'p']

# for key, value in enumerate(a):
#     print(key, value) 

# for y in  zip(a, b):
#     print(y)

# p = [y for y in zip(a, b)]
# for e, z in p:
#     print(e, z)

# p = {'a':'b', 'e':'t'}
# # for k, v in p.items():

# print(dict(zip(a, b)))

# def cache(func):
#     save = {}
#     # @wraps(func)
#     def new_func(*args):
#         if args in save:
#             return new_func(*args)
#         result = func(*args)
#         save[args] = result
#         return result
#     return new_func

# @cache
# def p(*args):
#     return 'This'

# p('This is it')

