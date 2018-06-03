def v(self,r):
    print(r)

def z(self):
    print('g')

def class_factory(class_name, *methods):
    method_dict = {}

    for method in methods:
        if callable(method):
            method_dict[method.__name__] = method
        
        else:
            print('%s is not callable. Received %s' % (method, method.__class__,))
        
    # Create class
    custom_class = type(class_name, (), method_dict)

    return custom_class

NewClass=class_factory('A',v,z)
i=NewClass()
i.v('prit')




def c():
    print('This is c')

def _class(y={}, *args):
    if args:
        w = {}
        for arg in args:
            w[arg.__name__] = arg
        w['a'] = 'This is a test'

        r = type('A', (), w)
        r.__doc__ = """This as test"""
    else:
        r = type('A', (), y)
    return r

# C = _class(c)

class T:
    def show(self):
        print('show')

    def this_show(self):
        print('This is a show')

p = dict()
y = T.__dict__
for u in y:
    o = y.get(u)
    if callable(o):
        p[o.__name__] = o

# print(p)
# print(_class(p))
# print(T.__dict__)

g = _class(p)
g.this_show('a')