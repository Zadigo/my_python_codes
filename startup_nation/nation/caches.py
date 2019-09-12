
def questions_cache(func):
    """A decorator function that returns a cached object 
    of the questions in order to create some sort of 
    passive memory for the application.

    Description
    -----------
        
        @questions_cache
        def test():
            return questions


    Result
    ------

    The cache() definition returns the inner array such as:

        _cache = [
            [
                { id: 1, ...}
            ]
        ]
    """
    cache = []

    def _cache(**kwargs):
        questions = func()
        cache.append(questions)
        return cache[0]
    return _cache
