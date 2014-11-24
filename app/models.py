from . import db

class Artist(db.Model):
    """
    A favorite music artist.
    """
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    discog_url = db.Column(db.String(250))
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('activities.id'))
    emotion_id = db.Column(db.Integer, db.ForeignKey('activities.id'))

    def __repr__(self):
        return '<Artist {}>'.format(self.name)

class Activity(db.Model):
    """
    An activity, such as cycling or driving.
    """
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    artists = db.relationship('Artist', backref='artist')

    def __repr__(self):
        return '<Activity {}>'.format(self.name)


class Location(db.Model):
    """
    A location, such as Boone or Knoxville.
    """
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), unique=True)
    state = db.Column(db.String(2))
    artists = db.relationship('Artist', backref='artist')

    def __repr__(self):
        return '<Location {}, {}>'.format(self.city, self.state)

class Emotion(db.Model):
    """
    An emotion, such as excited or reflective.
    """
    __tablename__ = 'emotions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    artists = db.relationship('Artist', backref='artist')

    def __repr__(self):
        return '<Emotion {}>'.format(self.name)
