import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World ... again xD"


if __name__ == "__main__":
    if(os.environ.get("WINDIR")):
        app.run(host="localhost", port=8888, debug=True)
    else:
        app.run(host=os.environ.get("IP"), port=int(
            os.environ.get("PORT")), debug=True)
