class A(object):
    pass

class B(A):
    def test(self, request, *args, **kwargs):
        return super().test(*args, **kwargs)

print(B().test('a'))