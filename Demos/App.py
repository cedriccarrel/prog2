from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
import numpy as np


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

@app.route("/tasks")
def tasks():
	return render_template("tasks.html")

@app.route('/index/<name>')
def index(name):
	return render_template("index.html", name=name)

@app.route("/newtransactions")
def newtransactions():
	return render_template("newtransactions.html")

@app.route("/budget", methods =['POST', 'GET'])

#definition für Übernahme aus newtransactions ins dict und anschl. ins csv übertrgen
def load_newstransaction_form():
	result = None
	data = None
	if request.method == 'POST':
		result = request.form

		newtransaction_dictionary= {
		result['newtransaction']: {
			"currency": result['currency'],
	        "ausgabebetrag": result['ausgabebetrag'],
	        "ausgabedauerauftrag": result['ausgabedauerauftrag'],
	        "ausgabedatum": result['ausgabedatum'],
	        "ausgabefirma": result['ausgabefirma'],
	        "ausgabebeschreibung": result['ausgabebeschreibung'],
	        "ausgabehashtag": result['ausgabehashtag']
	        }
	       }
	data_new = pd.DataFrame(newtransaction_dictionary)
	#bei initialisierung muss diese Zeile aktiviert sein, anschliessend auskommentieren
	#data_new.to_csv("ausgaben.csv", index=True)
	data_old = pd.read_csv(r"ausgaben.csv", index_col=0)
	data = pd.concat([data_old, data_new], axis=1)
	data.to_csv("ausgaben.csv", index=True)
	data_new = pd.read_csv(r"ausgaben.csv", index_col=0)


	#pandas manipulation am df --> beträge auslesund rechnen
	betrag = data
	print(betrag)

	ausgabe_betrag = betrag.loc[betrag['Test30'] == 'schule']
	print(ausgabe_betrag)


	return render_template("budget.html", data1=data_new)


if __name__ == "__main__":
	app.run(debug=True, port=5000)