from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html', title = 'Contact')

@app.route("/about")
def about():
    # return render_template('about.html', title = 'About')
    return "<h1 style='color: red;'>About Page</h1>"

@app.route("/projects")
def projects():
    return render_template('projects.html', title = 'Projects')

