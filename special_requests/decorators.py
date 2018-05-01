def login_required(r):
    print(r)

def is_staff(a, b):
    print(a, b)

def wraps(a):
    def staff_required(view_func):
        def _is_staff(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return login_required(view_func)(request, *args, **kwargs)
            elif is_staff(request, request.user):
                return view_func(request, *args, **kwargs)
            else:
                raise TypeError
        return wraps(view_func)(_is_staff)


def view_func():
    pass

def request():
    pass

wraps(view_func)