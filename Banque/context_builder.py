class ContextBuilder:
    context = {}
    def __init__(self, *args, **kwargs):
        if args:
            for arg in args:
                if isinstance(arg, list) or isinstance(arg, tuple):
                    for a in args:
                        self.context[a] = a
                else:
                    self.context[arg] = arg

        if kwargs:
            for key, value in kwargs.items():
                # if callable(value):
                #     self.context[value.__class__.__name__] = value

                # if value.__class__.__name__ == 'cls':
                #     self.context[value.__class__.__name__] = value()

                self.context[key] = value

    @property
    def get_context(self):
        return self.context

    def update_context(self, context={}):
        self.context.update(context)
        return self.context
