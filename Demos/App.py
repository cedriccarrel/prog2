from flask import Flask, render_template, redirect, url_for, request
import json

app = Flask(__name__)

def lade_daten_aus_json (pfad, standard_wert = []):
    try:
        with open(pfad, 'r') as datei:
            return json.load(datei)
    except Exception:
        return standard_wert

def schreibe_daten_in_json(pfad, daten):
    with open(pfad, 'w') as datei:
        json.dump(daten, datei, indent = 4)

def total_transactions(transactions):
	sum = 0
	for transaction in transactions:
		sum = sum + transaction['ausgabebetrag']
	return sum

def total_salary(salaries):
	sum_salary = 0
	for salary in salaries:
		sum_salary = sum_salary + salary['salary']
	return sum_salary

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    users = lade_daten_aus_json("user_data.json")
    if request.method == 'POST':
    	username = request.form['username']
    	passwort = request.form['password']
    	for user in users:
    		if user['username'].lower() == username.lower() and user['password'].lower() == passwort.lower():
    			return redirect(url_for('dashboard'))
    	error = 'Invalid Credentials. Please try again.'
    return render_template("login.html", error=error)

@app.route("/sign_up", methods=['GET', 'POST'])
#def um daten aus sign up form in dict und json zu laden
def load_sign_up_form():
	result = None
	data = None
	existing_sign_up = lade_daten_aus_json("user_data.json")
	if request.method == 'POST':
		result = request.form

		user_data_dictionary = {
			"username": result['username'],
	        "e_mail": result['e_mail'],
	        "password": result['password'],
	        "confirm_password": result['confirm_password'],
	        "salary": result['salary'],
	        "budget": result['budget']
	        }
		existing_sign_up.append(user_data_dictionary)
		schreibe_daten_in_json("user_data.json", existing_sign_up)
	
		print(existing_sign_up)
		return redirect(url_for('dashboard'))
	return render_template ("sign_up.html")

@app.route("/forgot_password")
def forgot_password():
	return render_template("forgot_password.html")

@app.route("/", methods=['GET', 'POST'])
@app.route("/dashboard", methods=['GET', 'POST'])
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

	print(existing_sign_up)
	sum_salary = total_salary(existing_sign_up)

	return render_template("budget.html", data1=existing_transaction, sum=sum, sum_salary=sum_salary)



if __name__ == "__main__":
	app.run(debug=True, port=5000)