# -----------------------------------------------------------------
# Entry point and, if name is changed, do set FLASK_APP = <name>.py
# -----------------------------------------------------------------

# Flask setup
from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
app = Flask(__name__)

# Regular python code
from pt.dir.class_file import ClassObj

def test_in_flask(nr):
    obj = ClassObj(nr)
    assert obj.get_attr() == nr
    return obj.get_attr()

number_test = test_in_flask(5)

# Routes
@app.route('/')
@app.route('/index')
@app.route('/index/<string:arg>')
def index(arg='five'):
    template = 'r_child.html'
    title = 'Child template'
    return render_template(template, title=title, nr=number_test)

# Link to port 80 in container
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)