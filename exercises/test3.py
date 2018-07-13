from collections import OrderedDict

class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class Typed(Descriptor):
    ty = object
    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise TypeError('There was an error.'
            ' Expected "%s"' % self.ty.__name__)
        super().__set__(instance, value)

class Integer(Typed):
    ty = int


class Structure(type):
    @classmethod
    def __prepare__(cls, name, bases):
        return OrderedDict()

    def __new__(cls, clsname, bases, clsdict):
        # Method 1
        # new_class = super().__new__(cls, clsname, bases, clsdict)
        # for value in new_class.values:
        #     setattr(new_class, value, value)

        # Method to collect descriptors
        fields = [key for key, val in clsdict.items() if isinstance(val, Descriptor)]
        for name in fields:
            clsdict[name].name = name
        new_class = super().__new__(cls, clsname, bases, dict(clsdict))
        return new_class

class SubStructure(metaclass=Structure):
    # values = []
    pass

class A(SubStructure):
    value = Integer()
    price = Integer()
    # values = ['price', 'value']

A().value = 175
