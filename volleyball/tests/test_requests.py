import unittest

class TestRequests(unittest.TestCase):
    def response_iscorrect(self, response):
        self.assertEquals(response.status_code==200, 'Response is 200')
