from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, request


# Route for handling the login page logic

login = Flask(__name__,
              static_url_path='',
              static_folder='static')

# login.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////my-test.db'
db = SQLAlchemy(login)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()


@login.route('/index', methods=['GET', 'POST'])
def logins():
    error = None
    if request.method == 'POST':
        if not User.query.filter_by(username=request.form['username'], password=request.form['password']).first(): # request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('index.html', error=error)


@login.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        if User.query.filter_by(username=request.form['username']).first(): # request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Username already used'
        else:
            new_user = User(username=request.form['username'], password=request.form['password'])
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('index.html', error=error)


@login.route('/login', methods=['GET', 'POST'])
def index():
    error = None
    return render_template('login.html', error=error)


if __name__ == '__main__':
    login.run(debug=True)


