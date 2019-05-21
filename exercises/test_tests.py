import unittest

class TestTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_ignore(self):
        pass

class MoreTests(TestTests):
    def runTest(self):
        pass

if __name__ == "__main__":
    # loader = unittest.TestLoader().loadTestsFromTestCase(TestTests)
    # unittest.TextTestRunner().run(loader)

    suite = unittest.TestSuite((TestTests,))
    suite.addTest(TestTests('test_ignore'))
    
