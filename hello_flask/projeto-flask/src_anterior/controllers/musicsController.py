from flask import Blueprint, jsonify, request
from models.musicModel import MusicModel
from .statusHttp import StatusHttp

musicsController = Blueprint("music", __name__)


def _get_all_musics():
    musics = MusicModel.find()
    return [music.to_dict() for music in musics]


@musicsController.route("/", methods=["POST"])
def music_post():
    new_music = MusicModel(request.json)
    new_music.save()
    return jsonify(new_music.to_dict()), StatusHttp.CREATED


@musicsController.route("/random", methods=["GET"])
def music_random():
    music = MusicModel.get_random()
    return jsonify(music.to_dict()), StatusHttp.OK


# @musicsController.route("/", methods=["GET"])
# def music_index():
#     musics_list = _get_all_musics()
#     return jsonify(musics_list), StatusHttp.OK
