from flask import Flask, render_template, request, redirect
from repositories import book_repository, author_repository
from models.books import Book
from flask import Blueprint

books_blueprint = Blueprint("Books", __name__)


# INDEX
# GET '/books'
@books_blueprint.route("/books")
def books():
    book = book_repository.select_all()
    return render_template("/books/index.html", all_books = book)

# NEW
# GET '/books/new'

# CREATE

# SELECT ALL

#  SHOW
@books_blueprint.route("/books/<id>", methods=['GET'])
def show_task(id):
    book = book_repository.select(id)
    return render_template('books/show.html', book = book )

# DELETE_ID
@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete(id):
    book_repository.delete(id)
    return redirect("/books")
