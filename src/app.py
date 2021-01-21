from flask import Flask, url_for, render_template, request, redirect, session, abort
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = uuid.uuid4().hex
db = SQLAlchemy(app)


class User(db.Model):
    """ Create user table"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() # Hash password using bcrypt




def logged_in(func):
    def wrapper(*args, **kwargs):
        if not "logged_in" in session or not session["logged_in"]:
            abort(403)
        return func(*args, **kwargs)
    return wrapper



@app.route('/', methods=['GET', 'POST'])
def home():
    """ Session control"""
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if request.method == 'POST':
            username = getname(request.form['username'])
            return render_template('index.html', data=getfollowedby(username))
        return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login Form"""
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['username']
        passw = request.form['password']

        try:
            data = User.query.filter_by(username=name).first()
            if data is not None and bcrypt.checkpw(passw.encode(), data.password.encode()):
                session['logged_in'] = True
                return redirect(url_for('home'))
            else:
                return 'wrong username or password'
        except Exception as e:
            print(e)
            return "wrong username or password"
        finally:
            breakpoint()
            del passw



@app.route('/register/', methods=['GET', 'POST'])
def register():
    """Register Form"""
    if request.method == 'POST':
        new_user = User(
            username=request.form['username'],
            password=request.form['password']
        )
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
    return render_template('register.html')



# @app.route('/register/', methods=['POST'])
# def register():
#     """Register Form"""
#     new_user = User(
#         username=request.form['username'],
#         password=request.form['password'])
#     db.session.add(new_user)
#     db.session.commit()
#     return render_template('login.html')


@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('home'))


if __name__ == '__main__':

    app.debug = True
    db.create_all()
    app.run(host='0.0.0.0')
    