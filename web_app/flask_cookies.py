
import os, sqlite3
from datetime import timedelta

from flask import ( 
                    Flask, render_template, redirect,
                    url_for, flash, make_response,
                    request, session,
                    g # Application Globals
                )

from config_provider import Singltone
from moderator import Moderator
from flask_db_provider import FBG_Provider

CONFIG_PROVIDER = Singltone()
MODERATOR = Moderator()
DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'sdfvresdbvrscrw85w7rsfv68w4rv'

app = Flask(__name__)

def set_navbar_links():
    CONFIG_PROVIDER.set_nav_link("Home", "/")
    # CONFIG_PROVIDER.set_nav_link("About", "/about")
    # CONFIG_PROVIDER.set_nav_link("Feedback", "/feedback")
    # CONFIG_PROVIDER.set_nav_link("Sign In", "/signin")
    # CONFIG_PROVIDER.set_nav_link("Login", "/login")

@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('error_page.html', cp=CONFIG_PROVIDER,
                           title_name='Error', err_txt='405 Method Not Allowed'), 405

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_page.html', cp=CONFIG_PROVIDER,
                           title_name='Error', err_txt='404 Not Found'), 404

@app.errorhandler(401)
def page_not_found(error):
    return render_template('error_page.html', cp=CONFIG_PROVIDER,
                           title_name='Error', err_txt='401 Unauthorized'), 401


@app.route('/')
@app.route('/index')
def index():
    return render_template('index_basic.html', cp=CONFIG_PROVIDER, title_name='Home')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    log = request.cookies.get('logged')
    
    res = app.make_response(f'<h1>User Logged</h1>{log}')
    res.set_cookie('logged', 'yes', 30*24*3600) # to save 30 days
    return res

@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    log = request.cookies.get('logged')
    
    res = app.make_response(f'<h1>User Logged Out</h1>{log}')
    res.set_cookie('logged', 'no', 30*24*3600) # to save 30 days
    return res




@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db



if __name__ == '__main__':
    set_navbar_links()
    # chrome://net-internals/#sockets
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config.update(
        dict(DATABASE=os.path.join(app.root_path, 'flsite.db'))
    )
    app.run(port=8000, debug=DEBUG)
    create_db()
