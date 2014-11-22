import os
from flask import Flask
from . import app

app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def home():
    """
    When Patrick was living in <location>, <activity> and feeling <emotion>
    these were his top five artists.
    """
    return "Nothing to see here. Move along."
