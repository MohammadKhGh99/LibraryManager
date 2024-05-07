from library import Library
import argparse


def parse_arguments():
    """
    Parse command line arguments.

    Returns:
        ArgumentParser object: The parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description='Library Management System', usage="python main.py [-h] [-a ADD] [-l {all,author,genre}] [-e EDIT] [-d DELETE]")

    # add arguments
    parser.add_argument('-a', '--add', help='Add a book. Provide the book title')
    parser.add_argument('-l', '--list', choices=['all', 'author', 'genre'], help='Display books. Choices are (all) to show all books, (author) by author name and (genre) by genre')
    parser.add_argument('-e', '--edit', help='Edit a book. Provide the book title')
    parser.add_argument('-d', '--delete', help='Delete a book. Provide the book title')

    return parser


def main():
    library = Library()
    library.load_library_data()
    parser = parse_arguments()
    library.run_library(parser)
    library.save_library_data()


if __name__ == "__main__":
    main()