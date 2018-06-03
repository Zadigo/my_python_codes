# from collections import deque

# class Rate(object):
#     def a(self):
#         print('This is a')

#     def b(self):
#         pass

# def test(cls):
#     parts = {}
#     for key, func in vars(cls).items():
#         if  callable(func):
#             # Something
#             parts[key] = func
#             parts['debug'] = False
    
#     Rate2 = type('Rate2', (), parts)
#     return Rate2

# p = test(Rate)
# print(vars(p))

def google(self, x):
    print('This is a %s' % x)

class Base:
    def create_attr(self, **kwargs):
        if kwargs:
            base_dict = vars(Base)
            copy_base_dict = base_dict.copy()
            values = self._unpack(kwargs)
            for key, value in values.items():
                if not key in copy_base_dict:
                    setattr(Base, key, value)
    
    def _unpack(self, dictionary={}):
        new_dict = {}
        for key, value in dictionary.items():
            if isinstance(value, dict):
                for k, v in value.items():
                    new_dict[k] = v
            else:
                new_dict[key] = value
        return new_dict

class A(Base):
    def __init__(self, **kwargs):
        super(A, self).create_attr(**kwargs)

class B(A):
    instance = A(this={'this':'this', 'that':'that'}, google=google)

    @property
    def get_instance(self):
        return self.instance

class C(B):
    def show(self):
        self.get_instance

C().show()