# from database import DataBase

class ContextBuilder:
    """
    Creates a context object used for
    tracking call accross the application.

    <context_builder.ContextBuilder object ...>

    """
    def __init__(self, request, *args, **kwargs):
        self.context = dict()

        if request:
            self.context['request'] = request

    def get_context_object(self):
        return self
    
    def update_context(self, **kwargs):
        if kwargs:
            self.context['extra'] = kwargs
        return self.context