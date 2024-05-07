import os.path
import argparse
import pickle

from book import Book
from rich.console import Console
from rich.table import Table


class Library:
    """
    A class representing a library.

    Attributes:
        _books_quantity (int): The number of books in the library.
        _books (dict): A dictionary containing all the books in the library.
        _books_by_author (dict): A dictionary mapping author names to lists of books by that author.
        _books_by_genre (dict): A dictionary mapping genres to lists of books in that genre.
        _filters (dict): A dictionary mapping filter codes to filter names.
        _display_table (Table): An instance of the Table class for displaying books.

    Methods:
        _add_book(book_title)
            Add a book to the library.
        _list_books(option)
            Display all books in the library.
        _edit_book(book_title)
            Edit a book in the library.
        _delete_book(book_title)
            Delete a book from the library.
        _parse_arguments()
            Parse command line arguments.
        run_library()
            Run the library management system.
    """
    def __init__(self):
        # number of current books in library
        self._books_quantity = 0
        # a dictionary to store all books in library
        self._books = dict()
        # a dictionary to store books by author name
        self._books_by_author = dict()
        # a dictionary to store books by genre
        self._books_by_genre = dict()

        # filters for displaying books
        self._filters = {"a": "all", "h": "author name", "g": "genre"}

        # display table for books using rich python library
        self._display_table = Table()
        self._display_table.add_column("Title", justify="center", style="green")
        self._display_table.add_column("Author", justify="center", style="red")
        self._display_table.add_column("Publication Year", justify="center", style="green")
        self._display_table.add_column("Genre", justify="center", style="red")
        self._display_table.show_lines = True

    def _add_book(self, book_title):
        """
        Add a book to the library.

        Args:
            book_title (str): The title of the book to add.
        """
        print("Adding Book to Library...")

        # the books' titles are unique
        if book_title not in self._books.keys():
            author_name = input(f"Author name, (q) to quit: ")
            publication_year = input(f"Publication year, (q) to quit: ")
            genre = input(f"Genre, (q) to quit: ")
            
            # create a new book instance
            new_book = Book(self._books_quantity, book_title, author_name, publication_year, genre)
            self._books_quantity += 1
            self._books[book_title] = new_book

            # add the book to the books_by_author and books_by_genre dictionaries
            if author_name not in self._books_by_author.keys():
                self._books_by_author[author_name] = [new_book]
            else:
                self._books_by_author[author_name].append(new_book)

            if genre not in self._books_by_genre.keys():
                self._books_by_genre[genre] = [new_book]
            else:
                self._books_by_genre[genre].append(new_book)

            print(f"Book [{book_title}] Added Successfully!")
        else:
            # book already exists
            print(f"ERROR: Book [{book_title}] is already in Library, "
                    f"try to add another book")
            print("Exiting...")
        
    def _list_books(self, option):
        """
        Display all books in the library.

        Args:
            option (str): The option to filter the books by.
        """
        print("Displaying All Books...")
        print()
        # display books based on the option
        if option == "all":
            self._display_table.title = "All Books in Library"
            for book in self._books.values():
                self._display_table.add_row(*book.display_book())
        elif option == "author":
            author_name = input("Enter author name to filter by: ")
            if author_name not in self._books_by_author.keys():
                print(f"ERROR: there are no books by author [{author_name}]")
                return
            self._display_table.title = "All Books in Library, Filtered by Author Name"
            for book in self._books_by_author[author_name]:
                self._display_table.add_row(*book.display_book())
        elif option == "genre":
            genre_name = input("Enter genre to filter by: ")
            if genre_name not in self._books_by_genre.keys():
                print(f"ERROR: there are no books in genre [{genre_name}]")
                return
            self._display_table.title = "All Books in Library, Filtered by Genre"
            for book in self._books_by_genre[genre_name]:
                self._display_table.add_row(*book.display_book())

        # display the table
        console = Console()
        console.print(self._display_table)

    def _edit_book(self, book_title):
        """
        Edit a book in the library.

        Args:
            book_title (str): The title of the book to edit.
        """
        print("Editing a Book...")
        
        # check if the book exists
        if book_title not in self._books.keys():
            print("ERROR: there is no book with this title!")
        else:
            cur_book = self._books[book_title]
            new_author = input("Enter new author name to edit or leave blank: ")
            new_publication_year = input("Enter new publication year "
                                            "to edit or leave blank: ")
            new_genre = input("Enter new genre to edit or leave blank: ")
            cur_book.edit_book(new_author, new_publication_year, new_genre)
            print(f"[{book_title}] book edited successfully!")
        
    def _delete_book(self, book_title):
        """
        Delete a book from the library.

        Args:
            book_title (str): The title of the book to delete.
        """
        print("Deleting a Book...")

        # check if the book exists
        if book_title not in self._books.keys():
            print("ERROR: there is no book with this title!")
        else:
            # remove the book from the books_by_author and books_by_genre dictionaries
            for book in self._books_by_author[self._books[book_title].author]:
                if book.title == book_title:
                    self._books_by_author[self._books[book_title].author].remove(book)
                    # if the author has no more books, remove the author from the dictionary
                    if len(self._books_by_author[self._books[book_title].author]) == 0:
                        self._books_by_author.pop(self._books[book_title].author)
                    break

            for book in self._books_by_genre[self._books[book_title].genre]:
                if book.title == book_title:
                    self._books_by_genre[self._books[book_title].genre].remove(book)
                    # if the genre has no more books, remove the genre from the dictionary
                    if len(self._books_by_genre[self._books[book_title].genre]) == 0:
                        self._books_by_genre.pop(self._books[book_title].genre)
                    break
            
            # remove the book from the books dictionary
            self._books.pop(book_title)
            self._books_quantity -= 1
            print(f"Book {book_title} deleted successfully!")

    def load_library_data(self):
        """
        Load the library data from the json file.
        """
        try:
            if os.path.exists("library_data.pkl"):
                with open("library_data.pkl", "rb") as pickle_file:
                    all_data = pickle.load(pickle_file)
                    self._books = all_data["books"]
                    self._books_by_author = all_data["books_by_author"]
                    self._books_by_genre = all_data["books_by_genre"]
        except Exception as e:
            print("ERROR: cannot load the library data from json file, "
                  "please run the library again")
            print("Exiting...")

    def save_library_data(self):
        """
        Save the library data to the json file.
        """
        try:
            # save the library data in json file
            all_data = {
                        "books": self._books, 
                        "books_by_author": self._books_by_author,
                        "books_by_genre": self._books_by_genre
                        }
            with open("library_data.pkl", "wb") as pickle_file:
                pickle.dump(all_data, pickle_file)
        except Exception:
            print("ERROR: cannot save the library data in json file")

    def run_library(self, parser):
        args = parser.parse_args()
        # check if any argument is provided
        if not any(vars(args).values()):
            parser.print_help()
            return
        if args.add:
            # Adding a book to the library
            self._add_book(args.add)
        elif args.list:
            # Listing all books from the library
            self._list_books(args.list)
        elif args.edit:
            # Editing a book from the library
            self._edit_book(args.edit)
        elif args.delete:
            # Deleting a book from the library
            self._delete_book(args.delete)
        