from flask import Flask, render_template, request
from game_of_life import GameOfLife


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    height, width = 25, 25
    if request.method == "POST":
        height = int(request.form['height'])
        width = int(request.form['width'])
    global game
    game = GameOfLife(height, width)
    return render_template("index.html")


@app.route("/live")
def live():
    game.form_new_generation()
    game.counter += 1
    return render_template("live.html", game=game)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
