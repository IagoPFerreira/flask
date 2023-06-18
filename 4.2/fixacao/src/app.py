from flask import Flask, render_template
# from controllers.book_controller import book_controller

app = Flask(__name__)

app.template_folder = "views/templates"
app.static_folder = "views/statics"

# app.register_blueprint(book_controller, url_prefix="/")


@app.route("/", methods=["GET"])
def index():
    filmes = [
        {'titulo': 'O Poderoso Chefão', 'ano': 1972},
        {'titulo': 'Interestelar', 'ano': 2014},
        {'titulo': 'A Origem', 'ano': 2010},
        {'titulo': 'Clube da Luta', 'ano': 1999},
        {'titulo': 'Pulp Fiction', 'ano': 1994}
    ]
    return render_template("filmes.html", filmes=filmes)


# @app.route("/", methods=["GET"])
# def index():
# message = "Boas vindas!"
# return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
