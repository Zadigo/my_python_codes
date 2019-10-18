import unittest

from mailchimp import Lists, MailChimp, QuerySet, Stores


class TestMailChimp(unittest.TestCase):
    def setUp(self):
        self.mailchimp = MailChimp('us15', '03351c2235cfe08e38995805b658311c-us15')
        
    def test_headers(self):
        self.assertIsInstance(self.mailchimp.headers, dict)

if __name__ == "__main__":
    unittest.TestCase()