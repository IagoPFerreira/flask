from bson import ObjectId
from flask import Blueprint, jsonify, request
from models.jokeModel import JokeModel
from .statusHttp import StatusHttp

jokesController = Blueprint("blueprint", __name__)


def _get_all_jokes():
    jokes = JokeModel.find()
    return [joke.to_dict() for joke in jokes]


def _get_joke(id):
    return JokeModel.find_one({"_id": ObjectId(id)})


@jokesController.route("/", methods=["GET"])
def joke_index():
    jokes_list = _get_all_jokes()
    return jsonify(jokes_list), StatusHttp.OK


@jokesController.route("/random", methods=["GET"])
def joke_random():
    joke = JokeModel.get_random()
    return jsonify(joke.to_dict()), StatusHttp.OK


@jokesController.route("/", methods=["POST"])
def joke_post():
    new_joke = JokeModel(request.json)
    new_joke.save()
    return jsonify(new_joke.to_dict()), StatusHttp.CREATED


@jokesController.route("/<id>", methods=["PUT"])
def joke_update(id):
    joke = _get_joke(id)
    joke.update(request.json)
    return jsonify(joke.to_dict()), StatusHttp.OK


@jokesController.route("/<id>", methods=["GET"])
def joke_show(id):
    joke = _get_joke(id)
    return jsonify(joke.to_dict()), StatusHttp.OK


@jokesController.route("/<id>", methods=["DELETE"])
def joke_delete(id):
    joke = _get_joke(id)
    if joke is None:
        return jsonify({"error": "Joke not found"}), StatusHttp.NOT_FOUND
    else:
        joke.delete()
        return jsonify(joke.to_dict()), StatusHttp.NO_CONTENT
