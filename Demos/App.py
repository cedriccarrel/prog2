from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == "POST":
		ziel_person = request.form['vorname']
		output = "willkommen auf der Webseite" + ziel_person + "!!!"
		return output
	return render_template("login.html")

@app.route('/login2')
def login2():
	return render_template("login2.html")

@app.route('/index/<name>')
def index(name):
	return render_template("index.html", name=name)

@app.route('/bacon')
def bacon():
	import mysql.connector

	mydb = mysql.connector.connect(
		host="localhost",
		user="yourusername",
		passwd="yourpassword"
	)

	mycursor = mydb.cursor()
	mycursor.execute("CREATE DATABASE mydatabase")

@app.route("/")
@app.route("/<user>")
def angabe(user=None):
	return render_template("user.html", user=user)


@app.route("/shopping")
def shopping():
	food =["Chesse", "Tuna", "Beef", "Bacon"]
	return render_template("shopping.html", food=food)


@app.route('/post/<int:post_id>')
def show_post(post_id):
	return "Post ID is %s" % post_id

@app.route("/profile/<name>")
def profile(name):
	return render_template("profile.html", name=name)

if __name__ == "__main__":
	app.run(debug=True, port=5000)