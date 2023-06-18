from flask import Flask, render_template
from data.musics import musics

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", musics=musics)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
