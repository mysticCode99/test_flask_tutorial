
from flask import url_for

from flask_site import app

with app.test_request_context():
    print( url_for('index') )
    print( url_for('about') )
    print( url_for('sign_in', username='fhjkd') )
