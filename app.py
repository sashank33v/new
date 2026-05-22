from flask import Flask, render_template, request, redirect

from models.library import Library

app = Flask(__name__)

library = Library()
library.load_books()


@app.route("/")
def home():
    all_books = library.view_books()
    available_books = list(library.available_books())

    return render_template(
        "index.html",
        total_books=len(all_books),
        available_books=len(available_books),
    )


@app.route("/books")
def books():

    all_books = library.view_books()

    return render_template("books.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add_book():

    if request.method == "POST":

        title = request.form["title"]
        author = request.form["author"]

        library.add_book(title, author)

        return redirect("/books")

    return render_template("add_book.html")


if __name__ == "__main__":
    app.run(debug=True)
