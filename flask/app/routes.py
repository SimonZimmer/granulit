from app import app
from app import db
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
import os
from app.forms import LoginForm, BioUpdateForm
from app.models import User, Bio


@app.route('/index')
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
    text = Bio().latest()
    return render_template('bio.html', data=dict(text))

@app.route('/impressum')
def impressum():
    return render_template('impressum.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('cms'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/cms', methods=['GET', 'POST'])
@login_required
def cms():
    form = BioUpdateForm()
    if form.validate_on_submit():
        flash(f'text: {form.text.data}')
        text = Bio(text=form.text.data)
        db.session.add(text)
        db.session.commit()
        return redirect(url_for('bio'))
    return render_template('cms.html', form=form)

