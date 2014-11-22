import os
import json
from flask import Flask
from flask import render_template, jsonify, flash

from . import app
from .forms import ArtistForm
from .models import Artist, ArtistSchema

app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    When Patrick was living in <location>, <activity> and feeling <emotion>
    these were his top five artists.
    """
    form = ArtistForm()
    if form.validate_on_submit():
        location = form.locations.data
        activity = form.activities.data
        emotion = form.emotions.data
        artists = Artist.query.filter_by(location=location).filter_by(activity=activity).filter_by(emotion=emotion).all()
        #serializer = ArtistSchema(many=True)
        #result = serializer.dump(artists)
        #return jsonify({'artists': result.data})
        if artists:
            return render_template('index.html', form=form, artists=artists)
        else:
            flash('Yeah. This combination of things never happened. Try again.')
            return render_template('index.html', form=form)
    return render_template('index.html', form=form)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
