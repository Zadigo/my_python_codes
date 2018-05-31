class ContextBuilder:
    def __init__(self, request, *args, **kwargs):
        self.request = request
        self.context = dict()
    
    def update_context(self, *args, **kwargs):
        pass