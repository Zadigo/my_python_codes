from werkzeug.wrappers import Request, Response

environ = {
    'REQUEST_METHOD': 'GET',
    'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; U; Mac OS X 10.5; en-US; ) Firefox/3.1',
    'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'HTTP_ACCEPT_LANGUAGE': 'de-at,en-us;q=0.8,en;q=0.5',
    'HTTP_ACCEPT_ENCODING': 'gzip,deflate',
    'HTTP_ACCEPT_CHARSET': 'utf-8',
    'HTTP_IF_MODIFIED_SINCE': 'Fri, 20 Feb 2009 10:10:25 GMT',
    'HTTP_CACHE_CONTROL': 'max-age=0'
}

# def app(status, headers):
#     print(status, headers)

# def create_application(environ, start_app):
#     request = Request(environ)
#     response = Response('Test', status=200, mimetype='text/plain')
#     return response(environ, app)

# print(create_application(environ, app))

response = Response('Text', status=200, headers=environ)
print(response)