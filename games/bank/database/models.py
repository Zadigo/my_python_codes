from games.bank.database.database import Database

class BaseModel(type):
    def __new__(cls_name, bases, cls_dict, **kwargs):
        pass

class Model(metaclass=BaseModel):
    pass

class A(Model, Database):
    pass
