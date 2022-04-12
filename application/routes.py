import json

from flask import render_template, request, jsonify

import service
from application import app

@app.route('/home', methods=['GET'])
def homepage():
    return render_template('layout.html', title="Home")


@app.route('/books/', methods=['GET'])
def show_books():
    error = ""
    books = service.get_all_books()
    #if len(books) == 0:
        #error = "There are no books to display"
    return render_template('book.html', books=books, message=error)

@app.route('/book/<int:BOOK_ID>', methods=['GET'])
def show_book(BOOK_ID):
    error = ""
    book = service.get_book_by_id(BOOK_ID)
    print(book.TITLE)
    if not book:
        return jsonify("There is no book with ID: " + str(BOOK_ID))
    return jsonify(book)

@app.route('/loan/<int:CUST_ID>', methods=['GET'])
def show_loans(CUST_ID):
    error = ""
    loans = service.get_loans_by_id(CUST_ID)
    if not loans:
        error = "There are no loans for customer with ID: " + str(CUST_ID)
    return render_template('show_loans.html', loans=loans, message=error, title="Book ID's currently on loan")

@app.route('/all/loans', methods=['GET'])
def show_books_on_loan():
    all_loans = service.get_books_on_loan()
    return render_template('show_loans.html', loans=loans)