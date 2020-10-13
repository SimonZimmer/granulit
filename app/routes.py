from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('header.html')

@app.route('/audio')
def audio():
    return render_template('audio.html')

@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/bio')
def bio():
    return render_template('bio.html')
