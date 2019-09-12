import unittest
from startup_nation.nation.caches import questions_cache

class TestCache(unittest.TestCase):
    def setUp(self):
        @questions_cache
        def questions():
            return [
                {
                    'name': 'name',
                    'question': 'question'
                }
            ]

        self.cache = questions()

    def test_returns_array(self):
        self.assertIsInstance(self.cache, list)

    def test_values_in_array(self):
        self.assertIsInstance(self.cache[0], dict)
        self.assertIn('name', self.cache[0])

if __name__ == "__main__":
    unittest.main()