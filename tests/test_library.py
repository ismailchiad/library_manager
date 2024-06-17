import unittest
from library.book import Book
from library.library import Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book1 = Book("1984", "George Orwell")
        self.book2 = Book("Brave New World", "Aldous Huxley")

    def test_add_book(self):
        self.library.add_book(self.book1)
        self.assertIn(self.book1, self.library.books)

    def test_remove_book(self):
        self.library.add_book(self.book1)
        self.library.remove_book(self.book1)
        self.assertNotIn(self.book1, self.library.books)

    def test_remove_book_not_in_library(self):
        with self.assertRaises(ValueError):
            self.library.remove_book(self.book1)

    def test_find_book_by_title(self):
        self.library.add_book(self.book1)
        self.assertEqual(self.library.find_book_by_title("1984"), self.book1)

    def test_find_book_by_title_not_found(self):
        self.assertIsNone(self.library.find_book_by_title("Nonexistent Book"))

    def test_list_books(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.assertEqual(self.library.list_books(), ["1984 by George Orwell", "Brave New World by Aldous Huxley"])

if __name__ == '__main__':
    unittest.main()
