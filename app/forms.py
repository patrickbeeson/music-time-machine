from flask.ext.wtf import Form
from wtforms import SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
#from wtforms.validators import DataRequired

from .models import Location, Emotion, Activity

def get_locations():
    return Location.query.all()

def get_emotions():
    return Emotion.query.all()

def get_activities():
    return Activity.query.all()


class ArtistForm(Form):
    """
    Form to refine query for artist based on location, activity and emotion.
    """
    locations = QuerySelectField(
        'locations',
        blank_text='choose location',
        query_factory=get_locations,
        allow_blank=True,
        #validators=[DataRequired()]
    )
    emotions = QuerySelectField(
        'emotions',
        blank_text='choose emotion',
        query_factory=get_emotions,
        allow_blank=True,
        #validators=[DataRequired()]
    )
    activities = QuerySelectField(
        'activities',
        blank_text='choose activity',
        query_factory=get_activities,
        allow_blank=True,
        #validators=[DataRequired()]
    )
    submit = SubmitField('Submit')
