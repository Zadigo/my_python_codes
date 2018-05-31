class Base(type):
    def __new__(cls, clsname, bases, clsdict):
        new_class = super().__new__(cls, clsname, bases, clsdict)
        setattr(new_class, 'a', 'a')
        return new_class

class BaseBank(metaclass=Base):
    pass

class Bank(BaseBank):
    pass

class Manager(Bank):
    pass

# class Manager(Bank):
#     pass


