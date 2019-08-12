import flask
import os




app = flask.Flask(__name__)

@app.route("/")
def index():
    print(os.getcwd())
    return flask.render_template("index.html")

def run():
    app.run()