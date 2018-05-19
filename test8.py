# def send(w):
#     import requests
    
#     def sent(*args, **kwargs):
#         if len(args) >= 1:
#             responses = [requests.get(p) for p in args]
#         else:
#             response = requests.get(p)
#         return w(*args, **kwargs)
#     return sent

# @send
# def get_response(*url):
#     print('Nice')

# get_response('http://www.wta.com', 'http://www.atp-tennis.com')



# def a(p):
#     return p + 2

# def b(v, w):
#     if v.__class__.__name__ != 'function':
#         raise TypeError('Got %s instead of a function' % type(v))
#     return [a(e) for e in w]

# print(b('a', [1, 2, 3, 4, 5]))



# class A(object):
#     def __init__(self, b):
#         self._b = b

#     def add(self):
#         return self._b + 5

# def c(this_is_a_class, iterables):
#     if isinstance(this_is_a_class, A):
#         print('Instance')
#     return [this_is_a_class(i).add() for i in iterables]

# print(c(A, [0, 1, 2, 3, 4, 5]))


# def tag_factory():
#     class alerts(object):
#         def __init__(self, tag, msg):
#             self._tag = tag
#             self._msg = msg

#         def alerts(self):
#             create = "<div class='alert alert-{tag}'>{msg}</div>"
#             return create.format(tag=self._tag, msg=self._msg)
#     return alerts

# a = tag_factory()
# print(a('success', 'success').alerts())


# def tag_factory():
#     def alerts(tag, msg):
#         create = "<div class='alert alert-{tag}'>{msg}</div>"
#         return create.format(tag=tag, msg=msg)
#     return alerts

# success = tag_factory()
# print(success('success', 'success'))


# def a():
#     var = 2
#     def b():
#         print('w')
#     return b

# this = a()
# this()


# def tag(t):
#     def msg(m):
#         h = '<' + t + '>' + m + '</' + t + '>'
#         return h
#     return msg

# u = tag('h1')
# print(u('success'))


# def a():
#     def b(*args):
#         return [arg for arg in args]
#     return b

# t = a()
# print(t(0, 1, 2, 3))


# class A(object):
#     name = None

#     @classmethod
#     def show(cls):
#         print(cls.name)

# class B(A):
#     name = 'Aurélie'

# B().show()




# def first():
#     print('Pierre')

# class A(object):
#     name = first

#     @classmethod
#     def show(cls):
#         cls.name()

# # Overide name
# def second():
#     print('Pierrette')

# class B(A):
#     name = second

# B().show()
    