import unittest
from games.bank.database.database import Database, TEST_PATH, QuerySet

class TestConnection(unittest.TestCase):
    def setUp(self):
        self.db = Database(TEST_PATH)

        # Create a fake table
        # self.db.run_sql('CREATE TABLE test_table(name TEXT, surname TEXT)')

        # Insert dummy data
        # self.db.run_sql('INSERT INTO test_table VALUES ("Aurélie Konaté)')

        # Drop the database

    def test_is_connected(self):
        # Test that we can connect
        # correctly to the database
        self.assertIsNotNone(self.db)

    def test_queryset(self):
        # Test that the return values
        # are wrapped in the QuerySet
        # class, thus an instance 
        sql = 'SELECT * FROM stars'
        value = self.db.manager._run_sql(sql)
        self.assertIsInstance(value, QuerySet)

    def tearDown(self):
        self.db.db.close()

class TestQuerySet(unittest.TestCase):
    def setUp(self):
        objs = Database().manager._all()
        self.queryset = QuerySet(objs)

    def test_is_list(self):
        self.assertIsInstance(self.queryset, list)

if __name__ == "__main__":
    unittest.main()
