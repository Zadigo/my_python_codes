class BaseManager:
    # To retain order, track each time a Manager instance is created.
    creation_counter = 0

    # Set to True for the 'objects' managers that are automatically created.
    auto_created = False

    #: If set to True the manager will be serialized into migrations and will
    #: thus be available in e.g. RunPython operations.
    use_in_migrations = False

    def __new__(cls, *args, **kwargs):
        # Capture the arguments to make returning them trivial.
        obj = super().__new__(cls)
        obj._constructor_args = (args, kwargs)
        obj._taste = (args)
        obj._test = True
        return obj

    def __init__(self):
        super().__init__()
        self.model = None
        self.name = None

    def __str__(self):
        return '%s.%s' % (self.model._meta.label, self.name)

print(BaseManager().__str__())
