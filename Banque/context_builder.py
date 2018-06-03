class ContextBuilder:
    def __init__(self, request, **kwargs):
        self.request = request
        self.context = dict()
        print(self._unpack(kwargs))
    
    @staticmethod
    def _unpack(obj):
        new_pack = {}
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_pack[key] = value
        return new_pack
    
    def update_context(self, *args, **kwargs):
        pass

ContextBuilder('<class>', name='name', test='test')