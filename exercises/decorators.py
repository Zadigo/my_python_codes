def start(func):
    def wrap():
        print(func('Start decorator'))
    return wrap

def start2(func):
    def wrap(**kwargs):
        print(func(f"Start decorator {kwargs['text']}"))
    return wrap

def start3(func, value):
    def wrap():
        def inside(*args, **kwargs):
            print(func(f"Start decorator"))
        return inside
    return wrap()

def z(text):
    pass

@start3(z,'a')
def master(text):
    return text

master