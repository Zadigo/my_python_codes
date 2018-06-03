from importlib import import_module

class Base:
    module = 'test1'
    def __init__(self):
        try:
            self.module = import_module(self.module)
        except ImportError:
            print('The module "%(module)s" could not be found.' % {
                'module': self.module
            })
            raise

        module_dict = self.module.__dict__.copy()
        funcs = {}
        for key, value in module_dict.items():
            if callable(value):
                funcs[key] = value

        if funcs:
            for key, value in funcs.items():
                setattr(Base, key, value)
        else:
            raise TypeError('There was no methods in "%s"' % 
                            self.module.__name__)

class A(Base):
    instance = Base()

    @property
    def get_instance(self):
        return self.instance
        