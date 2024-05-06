# LibraryManager

## Description

This is a library manager program that allows you to perform various operations on books.

## Table of Contents

- [Features](#Features)

- [Prerequisites](#Prerequisites)

- [Installation](#Installation)

- [Usage](#Usage)

## Features

- Add books: You can add new books to the library.
- Edit books: You can edit the details of existing books.
- Delete books: You can remove books from the library.
- List all books: You can view a list of all the books in the library.

## Prerequisites

Before running the library manager program, make sure you have the following prerequisites installed:

- Python 3: You need to have Python 3 installed on your system. You can download it from the official Python website: https://www.python.org/downloads/

- Git: You need to have Git installed on your system to clone the repository. You can download it from the official Git website: https://git-scm.com/downloads/

- Pip: Pip is the package installer for Python. It is usually installed by default with Python. You can check if it is installed by running the following command in your terminal:

    ```
    pip --version
    ```

    If it is not installed, you can install it by following the instructions on the official Pip website: https://pip.pypa.io/en/stable/installing/

Once you have installed these prerequisites, you can proceed with the steps mentioned in the "Getting Started" section to run the library manager program.

## Installation

To get started with the library manager program, follow these steps:

1. Clone the repository:<br>
git clone https://github.com/MohammadKhGh99/LibraryManager.git
2. Install the required dependencies:<br>
pip install -r requirements.txt

## Usage

<pre>
Usage: python main.py [-h] [-a ADD] [-l {all,author,genre}] [-e EDIT] [-d DELETE]

options:
  -h, --help            show this help message and exit
  -a ADD, --add ADD     Add a book. Provide the book title
  -l {all,author,genre}, --list {all,author,genre}
                        Display books. Choices are (all) to show all books, (author) by author name and (genre) by genre
  -e EDIT, --edit EDIT  Edit a book. Provide the book title
  -d DELETE, --delete DELETE
                        Delete a book. Provide the book title
</pre>