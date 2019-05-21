import unittest
import re
from base import PlayerData

class TestBase(unittest.TestCase):
    def setUp(self):
        self.start = PlayerData()

    def test_can_create_request(self):
        url = 'https://www.wtatennis.com/players/player/316161/title/eugenie-bouchard-0#matches'
        response = self.start.create_request(uri=url)
        self.assertEqual(response.status_code, 200)
        return response

    def test_is_player_profile(self):
        response = self.test_can_create_request()
        title = self.start._soup(response).find('title').text
        player = re.match(r'[a-zA-Z\s+]', title).group(0)
        self.assertEqual(player, 'Eugenie Bouchard')

    def test_height_conversion(self):
        converted_height = self.start.convert_height(194)
        self.assertEqual(converted_height, 6.4)

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite(TestBase)
    suite.addTest(TestBase)
    suite.run()
