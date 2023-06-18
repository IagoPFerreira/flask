from flask import Blueprint, render_template
from models.book_model import Book

book_controller = Blueprint("book_controller", __name__)


@book_controller.route("/", methods=["GET"])
def index():
    book = Book("O Hobbit", "J. R. R. Tolkien", 1937)
    return render_template("book.html", book=book)
