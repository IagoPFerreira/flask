import datetime
from flask import Blueprint, render_template, request
homeController = Blueprint("homeController", __name__)


@homeController.route("/", methods=["GET", "POST"])
def index():
    username = ''
    saudacao = _get_saudacao()

    if request.method == 'POST':
        username = request.form.get("username")

    return render_template("index.html", username=username, saudacao=saudacao)


def _get_saudacao():
    hora_atual = datetime.datetime.now().hour
    if hora_atual < 6:
        return "Boa noite"
    if hora_atual < 12:
        return "Bom dia"
    if hora_atual < 18:
        return "Boa tarde"
    return "Boa noite"
