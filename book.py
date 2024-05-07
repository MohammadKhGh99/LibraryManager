class Book:
    """
    A class to represent a book.

    Attributes
    ----------
    _book_id (int): A unique id for each book instance
    title (str): The title of the book
    author (str): The name of the author of the book
    publication_year (str): The publication year of the book
    genre (str): The genre of the book

    Methods
    -------
    edit_book(new_author="", new_publication_year="", new_genre="")
        Edit the details of the book.
    display_book()
        Return the details of the book.
    """
    
    def __init__(self, id_number, title: str, author: str, publication_year: str, 
                 genre: str):
        # gives the books an automatic increment id number
        self._book_id = id_number
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        # we have new book created
        
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
        
        