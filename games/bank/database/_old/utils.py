def cache(func):
    def _wrapper(*args, **kwargs):
        def _setter(port):
            return func('this'+port)
        return _setter

    def _s():
        return 'a'

    return _wrapper

@cache()
def test(x):
    return x

print(test()('289'))