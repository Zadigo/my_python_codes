# import requests

# def decorator(function):
#     url = function()

#     def _requests(*args, *kwargs):
#         response = requests.get(url)
    
#         def test_response(*args, **kwargs):
#             if response.status_code == 200:
#                 return response
#             else:
#                 return [] 
#         return test_response(response)
#     return _requests


# def e():
#     return u'http://www.sawfirst.com'

# ta=decorator(e)
# ta()

class Base(type):
    def __new__(self, cls, bases, cls_dict):
        new_class = super().__new__(self, cls, bases, cls_dict)
        
        return new_class

class Goog(metaclass=Base):
    pass

class A(Goog):
    pass