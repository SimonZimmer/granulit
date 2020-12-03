from app import app
from flask import render_template, flash, redirect
import os
from app.forms import LoginForm


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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)

