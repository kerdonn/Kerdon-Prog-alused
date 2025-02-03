"""Book store."""


class Book:
    def __init__(self, title: str, author: str, price: float, rating: float):
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

  
    



class Store:
    def __init__(self, name: str, rating: float):
        self.name = name
        self.rating = rating
        self.books = []

    def can_add_book(self, book: Book) -> bool:
        for existing_book in self.books:
            if existing_book.title == book.title and existing_book.author == book.author:
                return False
        return book.rating >= self.rating

    def add_book(self, book: Book) -> bool:
        if self.can_add_book(book):
            self.books.append(book)
            return True
        return False

    def can_remove_book(self, book: Book) -> bool:
        return book in self.books

    def remove_book(self, book: Book) -> bool:
        if self.can_remove_book(book):
            self.books.remove(book)
            return True
        return False

    def get_all_books(self):
        return self.books

    def get_books_by_price(self):
        return sorted(self.books, key=lambda book: book.price)

    def get_most_popular_book(self):
        if not self.books:
            return []
        max_rating = max(book.rating for book in self.books)
        return [book for book in self.books if book.rating == max_rating]




