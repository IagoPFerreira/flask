from flask import Flask
from controllers.jokesController import jokesController
# from controllers.musicsController import musicsController
from controllers.homeController import homeController
from controllers.chatController import chatController
from os import environ
from waitress import serve

app = Flask(__name__)

app.static_folder = "views/static"
app.template_folder = "views/templates"

app.register_blueprint(jokesController, url_prefix="/jokes")
# app.register_blueprint(musicsController, url_prefix="/musics")
app.register_blueprint(homeController, url_prefix="/")
app.register_blueprint(chatController, url_prefix="/chat")


def start_server(host="0.0.0.0", port=8000):
    if environ.get("FLASK_ENV") == "dev":
        return app.run(debug=True, host=host, port=port)
    else:
        serve(app, host=host, port=port)


if __name__ == "__main__":
    start_server()
