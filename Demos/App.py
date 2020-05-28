from flask import Flask, render_template, redirect, url_for, request
import json

app = Flask(__name__)

def lade_daten_aus_json (pfad, standard_wert = []):
    #https://www.programiz.com/python-programming/json
    try:
        with open(pfad, 'r') as datei:
            return json.load(datei)
    except Exception:
        return standard_wert

def schreibe_daten_in_json(pfad, daten):
    #https://stackoverflow.com/questions/17043860/how-to-dump-a-dict-to-a-json-file
    with open(pfad, 'w') as datei:
        json.dump(daten, datei, indent = 4)

def total_transactions(transactions):
	sum = 0
	for transaction in transactions:
		sum = sum + transaction['ausgabebetrag']
	return sum



@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('dashboard'))
    return render_template("login.html", error=error)

@app.route("/sign_up2")
def sign_up():
	return render_template("sign_up2.html")

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

#definition für Übernahme aus newtransactions ins dict 
def load_newstransaction_form():
	result = None
	data = None
	existing_transaction = lade_daten_aus_json("ausgaben.json")
	if request.method == 'POST':
		result = request.form

		newtransaction_dictionary= {
			"titel": result['newtransaction'], 
			"currency": result['currency'],
	        "ausgabebetrag": float(result['ausgabebetrag']),
	        "ausgabedauerauftrag": result['ausgabedauerauftrag'],
	        "ausgabedatum": result['ausgabedatum'],
	        "ausgabefirma": result['ausgabefirma'],
	        "ausgabebeschreibung": result['ausgabebeschreibung'],
	        "ausgabehashtag": result['ausgabehashtag']
	        }
		existing_transaction.append(newtransaction_dictionary)
		schreibe_daten_in_json("ausgaben.json", existing_transaction)
	

	print(existing_transaction)
	sum = total_transactions(existing_transaction)

	return render_template("budget.html", data1=existing_transaction, sum=sum)



if __name__ == "__main__":
	app.run(debug=True, port=5000)