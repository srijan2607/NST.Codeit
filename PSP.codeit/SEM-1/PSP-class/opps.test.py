import unittest
from opps import book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.test_book = book("Test Title", "Test Author", "Test Genre")

if __name__ == '__main__':
    unittest.main()
