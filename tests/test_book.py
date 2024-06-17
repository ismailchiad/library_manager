import unittest
from library.book import Book

class TestBook(unittest.TestCase):
    
    def test_book_initialization(self):
        book = Book("1984", "George Orwell")
        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "George Orwell")

    def test_book_str(self):
        book = Book("1984", "George Orwell")
        self.assertEqual(str(book), "1984 by George Orwell")

if __name__ == '__main__':
    unittest.main()
