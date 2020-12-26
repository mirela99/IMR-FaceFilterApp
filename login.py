from flask import Flask, render_template, redirect, url_for, request

# Route for handling the login page logic
login = Flask(__name__,
        static_url_path='', 
        static_folder='static')
@login.route('/index', methods=['GET', 'POST'])
def logins():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('index.html', error=error)


@login.route('/login', methods=['GET', 'POST'])
def index():
    error = None
    return render_template('login.html', error=error)


if __name__ == '__main__':
    login.run(debug=True)