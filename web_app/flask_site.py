
from datetime import timedelta

from flask import ( 
                    Flask, render_template, 
                    url_for, request, flash,
                    redirect, session, abort
                )

from config_provider import Singltone
from moderator import Moderator

CONFIG_PROVIDER = Singltone()
MODERATOR = Moderator()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdfvresdbvrscrw85w7rsfv68w4rv'

def set_navbar_links():
    CONFIG_PROVIDER.set_nav_link("Home", "/")
    CONFIG_PROVIDER.set_nav_link("About", "/about")
    CONFIG_PROVIDER.set_nav_link("Feedback", "/feedback")
    CONFIG_PROVIDER.set_nav_link("Sign In", "/signin")
    CONFIG_PROVIDER.set_nav_link("Login", "/login")

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', cp=CONFIG_PROVIDER, title_name='Home')

@app.route('/about')
def about():
    return render_template('about.html', cp=CONFIG_PROVIDER, title_name='About')

# @app.route('/signin', methods = ['POST'])
@app.route('/signin', methods = ["GET", "POST"])
def signin():
    print(url_for('signin'))
    if request.method != 'POST':
        pass
    else:
        print('POST ->', request.form)
        print('GET ->', request.args)
    return render_template('signin.html', cp=CONFIG_PROVIDER, title_name='Sign In')

@app.route('/feedback', methods=["GET"])
def feedback():
    print('GET ->', request.args)
    if request.method != 'GET':
        pass
    elif not request.args:
        pass
    else:
        comment_txt = request.args["comment"]
        if comment_txt:
            flash(f"'{comment_txt}' revived", category='alert-info')
        else:
            flash("Empty comment", category='alert-danger')
    return render_template('feedback.html', cp=CONFIG_PROVIDER, title_name='Feedback')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('profile', username=session['username']))
    elif request.method != 'POST':
        flash('Please fill all fields', category='alert-danger')
    elif 'user' not in request.form.keys():
        flash('Please fill Username fields', category='alert-danger')
    elif 'pw' not in request.form.keys():
        flash('Please fill Password fields', category='alert-danger')
    elif request.form['user'] == 'artur' and request.form['pw'] == '1234':
        session['username'] = request.form['user']
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=2)
        return redirect(url_for('profile', username=session['username']))
    else:
        flash('Incorrect Username or Password', category='alert-danger')
    return render_template('login.html', cp=CONFIG_PROVIDER, title_name='Login')

@app.route('/profile/<username>')
def profile(username):
    if username != session['username']:
        abort(401)
    return render_template('profile.html', cp=CONFIG_PROVIDER, title_name='Login',
                           fst_name='Artur', snd_name='Margaryan')

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

@app.route('/learn_english/<task>')
def learn_english(task):
    print(task)
    return render_template('learn_english.html', cp=CONFIG_PROVIDER, title_name='Learn Words',
                           fst_name='Artur', snd_name='Margaryan')

@app.route('/add_verb', methods=["GET"])
def add_verb():
    print('GET ->', request.args)
    if request.method != 'GET':
        pass
    elif not request.args:
        flash("Verbs haven't been added", category='alert-danger')
        pass
    else:
        print(request.args)
        Moderator.insert_data('irregular_verbs', request.args)
        flash("Verbs are added", category='alert-info')
    return render_template('learn_english.html', cp=CONFIG_PROVIDER, title_name='Learn Words')

if __name__ == '__main__':
    set_navbar_links()
    # chrome://net-internals/#sockets
    app.run(port=8000, debug=True)
