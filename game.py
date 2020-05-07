class Rating:
    total = 1000
    def __init__(self, score, **kwargs):
        pass
    
    @property
    def is_negative(self):
        return self.total <= 0

    @property
    def is_over_thousand(self):
        return self.total >= 1000

    def __call__(self, value):
        result = self.__add__(value)
        if result > 1000:
            print(result)

    def __add__(self, n):
        if n <= 0:
            raise ValueError('%s should be over 0' % n)
        return self.total + n

s = Rating(14)
print(s(4))
