from inspect import Parameter, Signature

class A(type):
    fields = []
    def __new__(cls, clsname, bases, clsdict):
        new_class = super().__new__(cls, clsname, bases, clsdict)
        sig = cls._make_signature(new_class.fields)
        setattr(new_class, '__signature__', sig)
        return new_class

    @staticmethod
    def _make_signature(names):
        return Signature(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names)

class B(metaclass=A):
    pass

class C(B):
    fields = ['name', 'age']
    request = False
    show = False

C().request