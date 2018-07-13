import os
# from settt.configuration import BASE_DIR
# from importlib import import_module

a = 'd:/Programs/Python/python_codes/banque/'

r = {}

a = list(os.walk(a))
e = a[0][2]
for t in e:
    if t.endswith('py'):
        module, ext = t.rsplit('.', 1)
        # r[module] = t
        # r[module] = module

print(r)