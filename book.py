class Book:
    """
    A class to represent a book.

    Attributes
    ----------
    _books_quantity : int
        a class attribute to track the total number of books
    _book_id : int
        a unique id for each book instance
    title : str
        title of the book
    author : str
        author of the book
    publication_year : str
        publication year of the book
    genre : str
        genre of the book

    Methods
    -------
    edit_book(new_author="", new_publication_year="", new_genre="")
        Edit the details of the book.
    display_book()
        Return the details of the book.
    """
    # current quantity of books in library
    _books_quantity = 0
    
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
        
    def edit_book(self, new_author="", new_publication_year="", new_genre=""):
        """
        Edit the details of the book, empty string represent that the user 
        don't want to edit the corresponding attribute.

        Parameters
        ----------
        new_author : str, optional
            New author of the book (default is "")
        new_publication_year : str, optional
            New publication year of the book (default is "")
        new_genre : str, optional
            New genre of the book (default is "")

        Returns
        -------
        nothing
        """
        if new_author != "":
            self.author = new_author
        if new_publication_year != "":
            self.publication_year = new_publication_year
        if new_genre != "":
            self.genre = new_genre
            
    def display_book(self):
        """
        Return the details of the book.

        Returns
        -------
        tuple
            A tuple containing the title, author, publication year, and genre of the book.
        """
        return self.title, self.author, self.publication_year, self.genre
        
        