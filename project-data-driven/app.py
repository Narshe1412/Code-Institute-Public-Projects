import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "task_manager"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())


if __name__ == "__main__":
    if(os.environ.get("WINDIR")):
        app.run(host="localhost", port=8888, debug=True)
    else:
        app.run(host=os.environ.get("IP"), port=int(
            os.environ.get("PORT")), debug=True)
