class ContextBuilder:
    """
    Creates chained context whenever an application is called.
    
    It stores elements such as the class objects or callable definitions.
    """
    context = {}
    def __init__(self, *args, **kwargs):
        if args:
            for arg in args:
                if isinstance(arg, list) or isinstance(arg, tuple):
                    for value in args:
                        self.context[value] = value
                else:
                    self.context[arg] = arg

        if kwargs:
            for key, value in kwargs.items():
                if callable(value):
                    self.context[value.__class__.__name__] = value

                if value.__class__.__name__ == 'cls':
                    self.context[value.__class__.__name__] = value()

                self.context[key] = value

    @property
    def get_context(self):
        return self.context

    def update_context(self, context={}):
        self.context.update(context)
        return self.context
