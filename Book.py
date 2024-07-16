class Book:
    def __init__(self, title, author, publication_year, borrowed_status):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.borrowed_status = borrowed_status

    def display_info(self):
        borrowed = "Borrowed" if self.borrowed_status else "Available"
        return f"Title: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publication_year}\nBorrowed Status: {borrowed}"

# Create a book instance with borrowed_status set to False
book1 = Book("The Ones", "Carter", 1923, False)

# Borrow the book if it is available
if not book1.borrowed_status:
    book1.borrowed_status = True
    print("The book has been borrowed.")
else:
    print("The book is already borrowed.")
print(book1.display_info())  # Call the method to display info

# Return the book if it is borrowed
if book1.borrowed_status:
    book1.borrowed_status = False
    print("The book has been returned.")
else:
    print("The book was not borrowed.")
print(book1.display_info())  # Call the method to display info
