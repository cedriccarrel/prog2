from flask import Flask, render_template, redirect, url_for, request
import preise
import daten

app = Flask(__name__)


@app.route("/speichern/<aktivitaet>")
def speichern(aktivitaet):
    zeitpunkt, aktivitaet = daten.aktivitaet_speichern(aktivitaet)

    return "Gespeichert: " + aktivitaet + " um " + str(zeitpunkt)


@app.route("/liste")
def auflisten():
    aktivitaeten = daten.aktivitaeten_laden()

    aktivitaeten_liste = ""
    for key, value in aktivitaeten.items():
        zeile = str(key) + ": " + value + "<br>"
        aktivitaeten_liste += zeile

    return aktivitaeten_liste


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == "POST":
		erste_zahl = request.form['zahl1']
		zweite_zahl = request.form['zahl2']
		ergebnis = float(erste_zahl) + float(zweite_zahl)
		return str(ergebnis)
	return render_template("login.html")

@app.route("/<preis>")
def rabatt(preis):
	preis_mit_rabatt = preise.rabatt_berechnen(preis)
	return "Der neue Preis ist" + str(preis_mit_rabatt)

@app.route("/budget")
def budget():
	dinger = ["Eins", "Zwei", "Drei"]
	number = 6
	return render_template("budget.html", dinger=dinger, number=number)

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