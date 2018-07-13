import functools
def sensitive_post_parameters(*parameters):
    def decorator(view):
        # @functools.wraps(view)
        def sensitive_post_parameters_wrapper(request, *args, **kwargs):
            print('Request executed before:', request())
            print('These are parameters from', sensitive_post_parameters, parameters)
            return view(request, *args, **kwargs)
        return sensitive_post_parameters_wrapper
    return decorator

def request():
    return 'REQUESTS'

@sensitive_post_parameters('a')
def view(request, *args, **kwargs):
    print('This is a view', request,  'with args', args[0], 'and kwargs', kwargs.get('test'))
    print('Request executed after:', request())
    
view(request, 'test', test='test')
