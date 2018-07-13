# from inspect import Parameter, Signature
# from collections import OrderedDict

# # def make_signature(names):
# #     return Signature(
# #         Parameter(
# #             name, Parameter.POSITIONAL_OR_KEYWORD
# #         ) for name in names
# #     )

# class Descriptor:
#     def __init__(self, name=None):
#         self.name = name

#     def __get__(self, instance, cls):
#         return instance.__dict__[self.name]
    
#     def __set__(self, instance, value):
#         instance.__dict__[self.name] = value

#     def __delete__(self, instance):
#         del instance.__dict__[self.name]

# class Typed(Descriptor):
#     ty = object
#     def __set__(self, instance, value):
#         if isinstance(value, self.ty):
#             raise TypeError('There was an error')
#         super().__set__(instance, value)

# class IntegerTyped(Typed):
#     ty = int

