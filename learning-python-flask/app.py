import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "some_secret"

# ROUTES
@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/about/<member_name>')
def about_member(member_name):
    member = {}
    
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member = member)
    
@app.route('/about')
def about():
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company_data=data)
    
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(request.form["name"]))
    return render_template("contact.html", page_title="Contact")
    
@app.route('/careers')
def careers():
    return render_template("careers.html", page_title="Careers")
    

# MAIN
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)