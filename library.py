import json
import os.path

from book import Book
from rich.console import Console
from rich.table import Table
import argparse
import pickle


class Library:
    
    def __init__(self):
        self._books_quantity = 0
        self._books = dict()
        self._books_by_author = dict()
        self._books_by_genre = dict()

        self._filters = {"a": "all", "t": "title", "h": "author name",
                         "p": "publication year", "g": "genre"}
        self._display_table = Table()
        self._display_table.add_column("Title", justify="center", style="cyan")
        self._display_table.add_column("Author", justify="center", style="magenta")
        self._display_table.add_column("Publication Year", justify="center", style="green")
        self._display_table.add_column("Genre", justify="center", style="blue")
        self._display_table.show_lines = True

    def _add_book(self, book_title):
        print("Adding Book to Library...")

        if book_title not in self._books.keys():
            author_name = input(f"Enter author name of book {book_title},"
                                f" (q) to quit: ")
            publication_year = input(f"Enter publication year of book"
                                        f" {book_title}, (q) to quit: ")
            genre = input(f"Enter genre of book {book_title}, (q) to quit: ")
            
            new_book = Book(book_title, author_name, publication_year, genre)
            self._books_quantity += 1
            self._books[book_title] = new_book

            if author_name not in self._books_by_author.keys():
                self._books_by_author[author_name] = [new_book]
            else:
                self._books_by_author[author_name].append(new_book)

            if genre not in self._books_by_genre.keys():
                self._books_by_genre[genre] = [new_book]
            else:
                self._books_by_genre[genre].append(new_book)

            print(f"Book {book_title} Added Successfully!")
            print()
        else:
            print(f"ERROR: Book {book_title} is already in Library, "
                    f"try to add another book")
            print("Exiting...")
        
    def _list_books(self, option):
        print("Displaying All Books...")
        if option == "all":
            self._display_table.title = "All Books in Library"
            for book in self._books.values():
                self._display_table.add_row(*book.display_book())
        elif option == "author":
            self._display_table.title = "All Books in Library, Filtered by Author Name"
            for book in self._books_by_author.values():
                self._display_table.add_row(*book.display_book())
        elif option == "genre":
            self._display_table.title = "All Books in Library, Filtered by Genre"
            for book in self._books_by_genre.values():
                self._display_table.add_row(*book.display_book())

        console = Console()
        console.print(self._display_table)

    def _edit_book(self, book_title):
        print("Editing a Book...")
        if book_title not in self._books.keys():
            print("ERROR: there is no book with this title!")
        else:
            cur_book = self._books[book_title]
            new_author = input("Enter new author name to edit or "
                                "leave blank: ")
            new_publication_year = input("Enter new publication year "
                                            "to edit or leave blank: ")
            new_genre = input("Enter new genre to edit or leave blank: ")
            cur_book.edit_book(new_author, new_publication_year, new_genre)
            print(f"{book_title} book edited successfully!")
        
    def _delete_book(self, book_title):
        print("Deleting a Book...")
        if book_title not in self._books.keys():
            print("ERROR: there is no book with this title!")
        else:
            self._books.pop(book_title)
            self._books_quantity -= 1
            print(f"Book {book_title} deleted successfully!")
            
    def _parse_arguments(self):
        parser = argparse.ArgumentParser(description='Library Management System')
        
        parser.add_argument('-a', '--add', help='Add a book. Provide the book title')
        parser.add_argument('-l', '--list', choices=['all', 'author', 'genre'], help='Display books. Choices are (all) to show all books, (author) by author name and (genre) by genre')
        parser.add_argument('-e', '--edit', help='Edit a book. Provide the book title')
        parser.add_argument('-d', '--delete', help='Delete a book. Provide the book title')
        
        return parser

    def run_library(self):
        try:
            if os.path.exists("library_data.pkl"):
                with open("library_data.pkl", "rb") as pickle_file:
                    all_data = pickle.load(pickle_file)
                    self._books = all_data["books"]
                    self._books_by_author = all_data["books_by_author"]
                    self._books_by_genre = all_data["books_by_genre"]

            parser = self._parse_arguments()
            args = parser.parse_args()
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
        except Exception as e:
            print(e)
            print("ERROR: cannot load the library data from json file, "
                  "please run the library again")
            print("Exiting...")
            return
        
        try:
            all_data = {
                        "books": self._books, 
                        "books_by_author": self._books_by_author,
                        "books_by_genre": self._books_by_genre
                        }
            with open("library_data.pkl", "wb") as pickle_file:
                pickle.dump(all_data, pickle_file)
        except Exception:
            print("ERROR: cannot save the library data in json file")
        

    