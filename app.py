# -----------------------------------------------------------------
# Entry point. If name is changed, run set FLASK_APP = <name>.py
# -----------------------------------------------------------------

# External imports
import os

# Flask setup
from flask import Flask, render_template, request, send_file, session, redirect, url_for
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Internal imports
from pt.user_login.authentication import verify_login
from pt.dir.class_file import ClassObj

def test_in_flask(nr):
    obj = ClassObj(nr)
    assert obj.get_attr() == nr
    return obj.get_attr()

number_test = test_in_flask(5)

def verify_password(username, password):
    return True #TODO
    if verify_login(username, password):
        return True
    return False

# Routes
@app.route('/')
@app.route('/index')
@app.route('/index/<string:arg>')
@app.route('/login', methods=['GET', 'POST'])
@app.route('/login/<string:language>')
def index(language='en'):
    template = 'r_auth.html'
    if request.method and request.method == 'POST':
        valid = verify_password(request.form['email'], request.form['password'])
        if valid:
            session['logged_in'] = True
            return redirect(url_for('child')) 
        else:
            return render_template(template, msg='Falsches Login.')
    else:
        return render_template(template)


@app.route('/two_cols')
@app.route('/two_cols/<string:arg>')
def child(language='en'):
    if not session.get('logged_in'):
        return redirect(url_for("index")) 
    template = 'r_child.html'
    title = 'Two columns'
    return render_template(template, title=title, nr=number_test)

@app.route('/grid')
@app.route('/grid/<string:arg>')
def grid(language='en'):
    if not session.get('logged_in'):
        return redirect(url_for("index"))
    template = 'r_grid.html'
    title = 'Grid'
    return render_template(template, title=title, nr=number_test)

# Link to port 80 in container
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)