from flask import Flask


app = Flask(__name__)

@app.route("/home")
def welcome():
    return "hello"


@app.route("/home/<name>")
def welcome_with_name(name):
    return "hi " + name


if __name__ == "__main__":
    app.run(debug=True)