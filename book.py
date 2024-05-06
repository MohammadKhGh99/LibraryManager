class Book:
    _books_quantity = 0
    _existing_books = 0
    
    def __init__(self, title: str, author: str, publication_year: str, 
                 genre: str):
        # gives the books an automatic increment id number
        self._book_id = Book._books_quantity
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        # we have new book created
        Book._books_quantity += 1
        Book._existing_books += 1
        
    @staticmethod
    def create_book(title, author, publication_year, genre):
        return Book(title, author, publication_year, genre)
        
    def edit_book(self, new_author="", new_publication_year="", new_genre=""):
        if new_author != "":
            self.author = new_author
        elif new_publication_year != "":
            self.publication_year = new_publication_year
        elif new_genre != "":
            self.genre = new_genre
            
    def display_book(self):
        print(f"{self._book_id + 1}. title: {self.title}\n"
              f"   author: {self.author}\n"
              f"   publication year: {self.publication_year}\n"
              f"   genre: {self.genre}\n")
    
        