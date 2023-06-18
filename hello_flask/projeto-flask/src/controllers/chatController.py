from flask import Blueprint, request, render_template
from datetime import datetime
import random
from models.jokeModel import JokeModel
from models.messageModel import MessageModel

chatController = Blueprint("chatController", __name__)


# GET considerará usuário visitante, POST o usuário recebido do formulário
@chatController.route("/", methods=["GET", "POST"])
def continue_chat():
    username = request.form.get("username") or "Visitante"
    message = request.form.get("message")

    _save_message(message, _from=username, to="Trybot")
    # Prepara a resposta
    answer = _prepare_answer(username, message)
    _save_message(answer, _from="Trybot", to=username)

    # Retorna todas as mensagens que este usuário possui com o bot
    session_messages = _get_session_messages(username)
    return render_template(
        "chat.html", username=username, session_messages=session_messages
    )


# Métodos de serviços auxiliares
def _save_message(message, _from, to):
    if not message:
        return

    chat_message = MessageModel(
        {
            "message": message,
            "from": _from,
            "to": to,
            "time": datetime.now().strftime("%H:%M"),
        }
    )
    chat_message.save()


def _prepare_answer(name, message):
    if not message:
        return _answer_first(name)
    if "1" in message:
        return _answer_joke()
    return _answer_default()


def _answer_first(name):
    return f"Olá { name }, bem vindo a central de ajuda! Por hora posso te ajudar em algumas coisas 😄<br>1 - Contar uma piada"


def _answer_default():
    return random.choice(
        [
            "Interessante, me conte mais sobre isso.",
            "Compreendo como você se sente.",
            "Isso é algo com o qual muitas pessoas lidam.",
            "Como você está lidando com isso?",
            "Eu estou aqui para você, se precisar conversar.",
        ]
    )


def _answer_joke():
    joke = JokeModel.get_random() or JokeModel("Ainda não conheço piadas")
    return joke.to_dict()['joke']


def _get_session_messages(name):
    messages = MessageModel.find({"$or": [{"to": name}, {"from": name}]})
    return [message.to_dict() for message in messages]
