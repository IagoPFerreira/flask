from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<H2>Hello World!</H2>'


@app.route("/api/")
def api_hello_world():
    return jsonify({'mensagem': 'Hello World!'})



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9000)
