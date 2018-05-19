class HttpResponseBase:
    status_code = 200

    def __init__(self, content_type=None, status=None, reason=None, charset=None):
        print('Status:', status)

class HttpResponse(HttpResponseBase):
    streaming = False

    def __init__(self, content=b'', *args, **kwargs):
        self.content = content
        print('Content:', content)
        print('I sent an HTTP for', kwargs['caller'])

    def __repr__(self):
        return '<%(cls)s status_code=%(status_code)d%(content_type)s>' % {
            'cls':self.__class__.__name__,
            'status_code':self.status_code,
            'content_type':'',
        }