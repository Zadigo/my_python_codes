import unittest
from volleyball.base import Requestor

class TestRequests(unittest.TestCase):
    def response_iscorrect(self):
        url = 'http://japan2018.fivb.com/en/competition/teams/bra-brazil/players'
        response = Requestor().create_request(url, 'Mozilla/2.5')
        self.assertEquals(response.status_code, 200, 'This')

if __name__ == "__main__":
    unittest.main()
