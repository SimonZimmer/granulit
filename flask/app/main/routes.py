from app.main import bp
from app import db
from flask import render_template, flash, redirect, url_for
from flask_login import login_required
import os
from app.main.forms import ContentUpdateForm
from app.models import User, Content


@bp.route('/index')
@bp.route('/')
def index():
    return render_template('base.html')


@bp.route('/audio')
def audio():
    content = Content().latest() if Content().latest() else Content()
    return render_template('main/audio.html', data=dict(content))


@bp.route('/video')
def video():
    imageDirPath = "app/static/images"
    images = []
    if os.path.exists(imageDirPath):
        images = [image for image in os.listdir(imageDirPath) if image.endswith(".jpg")]
    content = Content().latest() if Content().latest() else Content()
    return render_template('main/video.html', images=images, data=dict(content))


@bp.route('/contact')
def contact():
    content = Content().latest() if Content().latest() else Content()
    return render_template('main/contact.html', data=dict(content))


@bp.route('/bio')
def bio():
    content = Content().latest() if Content().latest() else Content()
    return render_template('main/bio.html', data=dict(content))


@bp.route('/impressum')
def impressum():
    content = Content().latest() if Content().latest() else Content()
    return render_template('main/impressum.html', data=dict(content))


@bp.route('/cms', methods=['GET', 'POST'])
@login_required
def cms():
    form = ContentUpdateForm()
    if form.validate_on_submit():
        content = Content(bio=form.bio.data,
                          releases=form.releases.data,
                          podcasts=form.podcasts.data,
                          videos=form.videos.data,
                          contact=form.contact.data,
                          impressum=form.impressum.data)
        db.session.add(content)
        db.session.commit()
        flash('changes updated successfully.')
        return redirect(url_for('main.cms'))
    else:
        try:
            form.bio.data = Content().latest().bio
            form.releases.data = Content().latest().releases
            form.podcasts.data = Content().latest().podcasts
            form.videos.data = Content().latest().videos
            form.contact.data = Content().latest().contact
            form.impressum.data = Content().latest().impressum
        except:
            pass

    return render_template('main/cms.html', form=form)
