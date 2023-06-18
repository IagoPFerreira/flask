# from flask import Flask
from os import environ
from waitress import serve
# from controllers.music_controller import musics_controller

# app = Flask(__name__)

# app.template_folder = 'views/templates'
# app._static_folder = 'views/static'

# app.register_blueprint(musics_controller, url_prefix="/")


# def start_server(host="0.0.0.0", port=8000):
#     if environ.get("FLASK_ENV") == "dev":
#         return app.run(debug=True, host=host, port=port)
#     else:
#         serve(app, host=host, port=port)


# if __name__ == "__main__":
#     start_server()

from flask import Flask
from controllers.music_controller import musics_controller

app = Flask(__name__)

app.template_folder = 'views/templates'
app._static_folder = 'views/static'

app.register_blueprint(musics_controller, url_prefix="/")


def start_server(host="0.0.0.0", port=8000):
    if environ.get("FLASK_ENV") == "dev":
        return app.run(debug=True, host=host, port=port)
    else:
        serve(app, host=host, port=port)


if __name__ == "__main__":
    start_server()


# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=8080)
