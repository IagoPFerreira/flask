from flask import Blueprint, render_template
from models.musicModel import MusicModel

musics_controller = Blueprint("music", __name__)


def _get_all_musics():
    musics = MusicModel.find()
    return [music.to_dict() for music in musics]


@musics_controller.route("/")
@musics_controller.route("/home")
def home():
    musics = _get_all_musics()
    print(musics)
    return render_template("home.html", musics=musics)


@musics_controller.route("/random")
def random_music():
    music = MusicModel.get_random()
    return render_template("home.html", musics=[music.to_dict()])
