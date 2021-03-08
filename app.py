from flask import Flask, render_template, make_response, jsonify, request

app = Flask(__name__)

PORT = 3200
HOST = '0.0.0.0'

INFO = {
    "language": {
        "es":"Spanish",
        "en": "English",
        "fr": "French",
    },
    "colors": {
        "r": "red",
        "g": "green",
        "b": "blue",
    },
    "clouds": {
        "IBM": "IBM CLOUD",
        "AMAZON": "AWS",
        "MICROSOFT": "AZURE",
        "GOOGLE": "GCP",
    }
}


@app.route("/")
def home():
    return "<h1 style='color:blue'>This is home</h1>"


@app.route("/temp")
def template():
    return render_template('index.html')


@app.route("/qstr")
def query_string():
    if request.args:
        req = request.args
        res = {}
        for key, value in req.items():
            res[key] = value
        res = make_response(jsonify(res), 200)
        return res
    res = make_response(jsonify({"error": "No query string"}), 400)
    return res


if __name__ == "__main__":
    print("Server Running in Port %s"%(PORT))
    app.run(host=HOST, port=PORT)
