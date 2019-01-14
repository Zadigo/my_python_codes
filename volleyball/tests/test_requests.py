import unittest
from volleyball.base import Requestor

class TestRequests(unittest.TestCase):
    def response_iscorrect(self, response):
        response = Requestor().create_request('http://japan2018.fivb.com/en/competition/teams/bra-brazil/players')
        self.assertEquals(response.status_code==200, 'Response is 200')

if __name__ == "__main__":
    unittest.main()
