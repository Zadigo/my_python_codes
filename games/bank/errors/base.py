class BaseErrors:
    pass

class DiscoverError(BaseErrors):
    def __str__(self):
        print('There was an error')