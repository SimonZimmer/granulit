from app import app
from flask import render_template
import os


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/audio')
def audio():
    return render_template('audio.html')

@app.route('/video')
def video():
    images = [image for image in os.listdir("./app/static/images") if image.endswith(".jpg")]
    return render_template('video.html', images=images)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/bio')
def bio():
    return render_template('bio.html')

@app.route('/impressum')
def impressum():
    return render_template('impressum.html')
