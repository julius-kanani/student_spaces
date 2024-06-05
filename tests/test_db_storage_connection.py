import unittest
from models.engine.db_storage import DBStorage

class TestDBStorageConnection(unittest.TestCase):
    def test_connection(self):
        # Attempt to initialize DBStorage
        storage = DBStorage()

        # Check if the connection is successful
        self.assertTrue(storage._DBStorage__engine)

if __name__ == "__main__":
    unittest.main()
