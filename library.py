import json
import os.path

from book import Book


class Library:
    
    def __init__(self, name):
        self._name = name
        # self._books = []
        self._books_quantity = 0
        # todo - all books have unique titles !
        self._books = dict()
        self._filters = {"a": "all", "t": "title", "h": "author name",
                         "p": "publication year", "g": "genre"}
        
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        self._name = new_name

    def get_books(self):
        return self._books

    def get_books_quantity(self):
        return self._books_quantity

    @staticmethod
    def create_library(name):
        return Library(name)

    def _add_book(self):
        print("Adding Book to Library...")
        book_title = input("Enter book title, (q) to quit: ")
        while book_title != "q":
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
                print(f"Book {book_title} Added Successfully!")
                print()
            else:
                print(f"ERROR: Book {book_title} is already in Library, "
                      f"try to add another book")
            
            book_title = input("Enter book title, (q) to quit: ")
        
    def _list_books(self):
        print("Displaying All Books...")
        displaying_method = input("How you want to display books?\n"
                                  "all (a), author (h) or by genre (g), "
                                  "(q) to quit: ")
        while displaying_method != "q":
            to_display_lst = None
            filter_by = None
            if displaying_method == "a":
                filter_by = "a"
                to_display_lst = self._books
            elif displaying_method == "h":
                filter_by = "h"
                to_display_lst = sorted(self._books, key=lambda x: x.author)
            elif displaying_method == "g":
                filter_by = "g"
                to_display_lst = sorted(self._books, key=lambda x: x.genre)
            else:
                print("Usage: you can just choose: (a) to show all books, "
                      "(h) by author name and (g) by genre!")
            print(to_display_lst)
            if to_display_lst:
                # displaying the list of books like what the user wants
                title_addon = ""
                if not filter_by:
                    title_addon = self._filters[filter_by]
                print(f"The Books: (filtering by {title_addon})")
                for book in self._books.values():
                    book.display_book()
                
            displaying_method = input("How you want to display books?\n"
                                      "all (a), title (t), author (h), "
                                      "publication year (p) or by genre (g), "
                                      "(q) to quit: ")
            
    def _edit_book(self):
        print("Editing a Book...")
        book_title = input("Enter book title to edit its details, (q) to "
                           "quit: ")
        while book_title != "q":
            if book_title not in self._books.keys():
                print("ERROR: there is no book with this title!")
            else:
                cur_book = self._books[book_title]
                print(f"Editing book {book_title}...")
                new_author = input("Enter new author name to edit or "
                                   "leave blank: ")
                new_publication_year = input("Enter new publication year "
                                             "to edit or leave blank: ")
                new_genre = input("Enter new genre to edit or leave blank: ")
                cur_book.edit_book(new_author, new_publication_year, new_genre)
                print(f"Book {book_title} edited successfully!")

            book_title = input("Enter book title to edit its details, (q) to "
                               "quit: ")
        
    def _delete_book(self):
        print("Deleting a Book...")
        book_title = input("Enter book title to delete, (q) to quit: ")
        while book_title != "q":
            if book_title not in self._books.keys():
                print("ERROR: there is no book with this title!")
            else:
                print(f"Deleting book {book_title}...")
                self._books.pop(book_title)
                self._books_quantity -= 1
                print(f"Book {book_title} deleted successfully!")

            book_title = input("Enter book title to delete, (q) to quit: ")
            
    def run_library(self):
        try:
            if os.path.exists("library_data.json"):
                self._books = json.loads("library_data.json")
            print(f"Hello to {self._name} Library")
            print("What do you want to do today?")
            option = input("Add Book (a), List Books (l), Edit Book (e), "
                           "Delete Book (d) and to Exit (q): ")
            while option != "q":
                if option == "a":
                    # Adding a book to the library
                    self._add_book()
                elif option == "l":
                    # Listing all books from the library
                    self._list_books()
                elif option == "e":
                    # Editing a book from the library
                    self._edit_book()
                elif option == "d":
                    # Deleting a book from the library
                    self._delete_book()
                else:
                    print(f"USAGE: invalid option ({option}) !")
                option = input("Add Book (a), List Books (l), Edit Book (e), "
                               "Delete Book (d) and to Exit (q): ")
        except Exception:
            print("ERROR: cannot load the library data from json file, "
                  "please run the library again")
            print("Exiting...")
            return
        
        try:
            json_file = open("library_json.json", "w")
            json.dump(self._books, json_file)
        except Exception:
            print("ERROR: cannot save the library data in json file")
        
            
if __name__ == "__main__":
    Library_name = input("Enter library name to create: ")
    library = Library(Library_name)
    library.run_library()
    