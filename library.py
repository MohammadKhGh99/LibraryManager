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

    def _add_book(self, book_title):
        print("Adding Book to Library...")

        # book_title = input("Enter book title, (q) to quit: ")
        # while book_title != "q":
        if book_title not in self._books.keys():
            author_name = input(f"Enter author name of book {book_title},"
                                f" (q) to quit: ")
            publication_year = input(f"Enter publication year of book"
                                        f" {book_title}, (q) to quit: ")
            genre = input(f"Enter genre of book {book_title}, (q) to quit: ")
            
            new_book = Book.create_book(book_title, author_name,
                                        publication_year, genre)
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
            # book_title = input("Enter book title, (q) to quit: ")
        
    def _list_books(self, option):
        print("Displaying All Books...")
        # displaying_method = input("How you want to display books?\n"
        #                           "all (a), author (h) or by genre (g), "
        #                           "(q) to quit: ")
        # while displaying_method != "q":
        # to_display_lst = None
        # filter_by = None
        if option == "all":
            # filter_by = "a"
            # to_display_lst = self._books
            self._display_table.title = "All Books in Library"
            for book in self._books.values():
                self._display_table.add_row(*book.display_book())
        elif option == "author":
            # filter_by = "h"
            # to_display_lst = sorted(self._books, key=lambda x: x.author)
            self._display_table.title = "All Books in Library, Filtered by Author Name"
            for book in self._books_by_author.values():
                self._display_table.add_row(*book.display_book())
        elif option == "genre":
            # filter_by = "g"
            # to_display_lst = sorted(self._books, key=lambda x: x.genre)
            self._display_table.title = "All Books in Library, Filtered by Genre"
            for book in self._books_by_genre.values():
                self._display_table.add_row(*book.display_book())
        # else:
        #     print("Usage: you can just choose: (a) to show all books, "
        #             "(h) by author name and (g) by genre!")
            
        # if to_display_lst:
        #     # displaying the list of books like what the user wants
        #     title_addon = ""
        #     if not filter_by:
        #         title_addon = self._filters[filter_by]

        #     print(f"The Books: (filtering by {title_addon})")
        console = Console()
        console.print(self._display_table)
                
            # displaying_method = input("How you want to display books?\n"
            #                           "all (a), title (t), author (h), "
            #                           "publication year (p) or by genre (g), "
            #                           "(q) to quit: ")
            
    def _edit_book(self, book_title):
        print("Editing a Book...")
        # book_title = input("Enter book title to edit its details, (q) to "
        #                    "quit: ")
        # while book_title != "q":
        if book_title not in self._books.keys():
            print("ERROR: there is no book with this title!")
        else:
            cur_book = self._books[book_title]
            # print(f"Editing {book_title} book...")
            new_author = input("Enter new author name to edit or "
                                "leave blank: ")
            new_publication_year = input("Enter new publication year "
                                            "to edit or leave blank: ")
            new_genre = input("Enter new genre to edit or leave blank: ")
            cur_book.edit_book(new_author, new_publication_year, new_genre)
            print(f"{book_title} book edited successfully!")

            # book_title = input("Enter book title to edit its details, (q) to "
            #                    "quit: ")
        
    def _delete_book(self, book_title):
        print("Deleting a Book...")
        # book_title = input("Enter book title to delete, (q) to quit: ")

        # while book_title != "q":
        if book_title not in self._books.keys():
            print("ERROR: there is no book with this title!")
        else:
            # print(f"Deleting book {book_title}...")
            self._books.pop(book_title)
            self._books_quantity -= 1
            print(f"Book {book_title} deleted successfully!")

            # book_title = input("Enter book title to delete, (q) to quit: ")
            
    def _parse_arguments(self):
        parser = argparse.ArgumentParser(description='Library Management System')
        
        parser.add_argument('-a', '--add', help='Add a book. Provide the book title')
        parser.add_argument('-l', '--list', choices=['all', 'author', 'genre'], help='Display books. Choices are (a) to show all books, (h) by author name and (g) by genre')
        parser.add_argument('-e', '--edit', help='Edit a book. Provide the book title')
        parser.add_argument('-d', '--delete', help='Delete a book. Provide the book title')
        
        return parser

    def run_library(self):
        try:
            if os.path.exists("library_data.pkl"):
                with open("library_data.pkl", "rb") as pickle_file:
                    # data = pickle_file.read()
                    print("hi")
                    # if data:
                    all_data = pickle.load(pickle_file)
                    self._books = all_data["books"]
                    self._books_by_author = all_data["books_by_author"]
                    self._books_by_genre = all_data["books_by_genre"]
                    # else:
                    #     print("INFO: there is no data in the library json file")

            parser = self._parse_arguments()
            args = parser.parse_args()
            if not any(vars(args).values()):
                parser.print_help()
                return
            # option = input("Add Book (a), List Books (l), Edit Book (e), "
            #                "Delete Book (d) and to Exit (q): ")
            # while option != "q":
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
            # else:
            #     print(f"USAGE: invalid option ({option}) !")
                # option = input("Add Book (a), List Books (l), Edit Book (e), "
                            #    "Delete Book (d) and to Exit (q): ")
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
        

    