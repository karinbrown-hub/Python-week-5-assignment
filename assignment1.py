#Assignment 1 : Design your own class 
# book.py

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

    def is_long_book(self):
        return self.pages > 300

# Example usage
if __name__ == "__main__":
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 218)
    book2 = Book("War and Peace", "Leo Tolstoy", 1225)

    book1.display_info()
    print("Is it a long book?", book1.is_long_book())
    print()
    book2.display_info()
    print("Is it a long book?", book2.is_long_book())