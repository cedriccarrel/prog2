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

@app.route('/login3')
def login3():
	return render_template("login3.html")

@app.route('/index/<name>')
def index(name):
	return render_template("index.html", name=name)

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
	
if __name__ == "__main__":
	app.run(debug=True, port=5000)