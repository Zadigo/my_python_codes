import unittest
import aws_manager

class TestPathCreator(unittest.TestCase):
    def setUp(self):
        self.new_name = aws_manager.unique_path_creator('nawoka', 'image1.jpg')

    def test_is_dict(self):
        self.assertIsInstance(self.new_name, dict)

    def test_object_name(self):
        object_name = self.new_name['object_name']
        self.assertIsInstance(object_name, list)
        # .. [image1, (image/jpeg, None)]
        self.assertEqual(object_name[0], 'image1')
    
    def test_object_path(self):
        object_path = self.new_name['object_path']
        self.assertRegex(object_path, r'[\w+\/\w+]+\.\w+', object_path)

class TestAWS(unittest.TestCase):
    def setUp(self):
        pass

if __name__ == "__main__":
    unittest.main()