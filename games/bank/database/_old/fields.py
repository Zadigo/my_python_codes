class Field:
    def __init__(self, max_length=None, verbose_name=None, **kwargs):
        self.max_length = max_length
        self.verbose_name = verbose_name

    def __setattr__(self, name, value):
        return super().__setattr__(name, value)

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return super().__str__()

class CharField(Field):
    pass

class IntegerField(Field):
    pass

class PositiveIntegerField(IntegerField):
    pass

print(CharField())
