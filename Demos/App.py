from flask import Flask, render_template, redirect, url_for, request
import daten
import datenbank

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('dashboard'))
    return render_template('login.html', error=error)

@app.route("/sign_up")
def sign_up():
	return render_template("sign_up.html")

@app.route("/")
@app.route("/dashboard")
def dashboard():
	return render_template("dashboard.html")

@app.route("/newtransactions")
def newtransactions():
	return render_template("newtransactions.html")

@app.route("/tasks")
def tasks():
	return render_template("tasks.html")

@app.route("/budget")
def budget():
	return render_template("budget.html")

@app.route('/index/<name>')
def index(name):
	return render_template("index.html", name=name)
	
	
if __name__ == "__main__":
	app.run(debug=True, port=5000)