from flask import Flask
from datetime import datetime
import os
from flask import render_template, request, redirect, url_for

app  = Flask(__name__)

menu = {
            "/certifications": "My certifications",
            "/about": "About me"
        }

@app.route('/')
def index():
    return render_template("main.html", menu=menu,
                           operating_system=os.name,
                           user_agent=request.user_agent,
                           time=datetime.now().strftime("%H:%M:%S"))


@app.route("/about")
def about():
    return render_template("about.html", menu=menu,
                           operating_system=os.name,
                           user_agent=request.user_agent,
                           time=datetime.now().strftime("%H:%M:%S"))


@app.route("/certifications")
def certifications():
    return render_template("certifications.html", menu=menu,
                           operating_system=os.name,
                           user_agent=request.user_agent,
                           time=datetime.now().strftime("%H:%M:%S"))


@app.route("/portfolio")
def portfolio():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)