from flask import Flask, request
from flask import jsonify
from dotenv import dotenv_values

from controllers import operation

app = Flask(__name__)
config = dotenv_values(".env")


@app.route("/")
def server_info():
    return config.get("AUTHOR", "Vanek") + "'s server"


@app.route("/author")
def author():
    author = {
        "name": "Goriachev Ivan",
        "course": 2,
        "age": 19,
    }
    return jsonify(author)


@app.route("/sum")
def runner():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'sum': operation(a, b)})


if __name__ == "__main__":
    app.run(
        debug=config.get("Debug", "False") == "True",
        port=config.get("PORT", 5000),
    )
