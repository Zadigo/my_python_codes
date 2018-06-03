from functools import wraps

def simple1(func):
    save = {}
    def show():
       save[func] = func()
       print(save)
    return show

def simple2(func):
    save = {}
    def show(*args):
       save[func] = func(), args
       print(save)
    return show

def simple3(prefix=''):
    save = {}
    def decorator(func):
        wraps(func)
        def show(*args):
            save[func] = func(), prefix, args
            print(save)
        return show
    return decorator


# @simple3('prefix')
# def test(*args):
#     return 'This is a test'

# test('args')
