
import os, sqlite3

from flask import ( 
                    Flask, render_template, redirect,
                    url_for, flash, make_response,
                    request, 
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
    db = get_db()
    dbase = FBG_Provider(db)
    rows = dbase.getMenu()
    rows.reverse()
    return render_template(
        'index_db_page.html', 
        cp=CONFIG_PROVIDER, 
        title_name='Home', 
        rows=rows
    )

@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    db = get_db()
    dbase = FBG_Provider(db)

    if request.method == 'POST':
        print(request.form)
        vals = []
        for key in ['translation', 'verb1', 'verb2', 'verb3']:
            vals.append(request.form.get(key))
        if None in vals:
            flash(f"'{vals}' haven't added", category='alert-danger')
        else:
            if dbase.addPost(*vals):
                flash(f"'{vals}' added", category='alert-info')
            else:
                flash(f"Couldn't add {vals}", category='alert-danger')
        del vals
    return redirect(url_for('index'))

@app.route('/api_responce')
def api_responce():
    context = 'hello'
    res = make_response(context)
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'flasksite'
    return res

@app.route('/api_responce1')
def api_responce1():
    img = None
    
    with app.open_resource( app.root_path + '/static/profile_pic.jpg', 'rb') as f:
        img = f.read()
    
    if img is None:
        return "None image"

    res = make_response(img)
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'flasksite'
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
