import unittest
from library.book import Book
from library.library import Library

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book1 = Book("1984", "George Orwell")
        self.book2 = Book("Brave New World", "Aldous Huxley")

    def test_integration_add_and_find_book(self):
        self.library.add_book(self.book1)
        found_book = self.library.find_book_by_title("1984")
        self.assertEqual(found_book, self.book1)

    def test_integration_add_and_remove_book(self):
        self.library.add_book(self.book1)
        self.library.remove_book(self.book1)
        self.assertIsNone(self.library.find_book_by_title("1984"))

if __name__ == '__main__':
    unittest.main()
