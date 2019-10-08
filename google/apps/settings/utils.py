def create_cache(*args):
    def _cache():
        cache = dict()
        for arg in args:
            if arg not in cache:
                if callable(arg):
                    cache.update({arg.__name__: arg})
                else:
                    cache.update({arg: arg})
        return cache
    return _cache
