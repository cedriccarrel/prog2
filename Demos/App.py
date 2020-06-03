from flask import Flask, render_template, redirect, url_for, request
import json
from flask_mail import Message, Mail
import plotly.graph_objects as go
import plotly

app = Flask(__name__)


#E-Mail Konfiguration
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": 'testotester525@gmail.com',
    "MAIL_PASSWORD": 'Test123?'
}

app.config.update(mail_settings)
mail = Mail(app)


#Json laden für Ausgaben, Userdata
def lade_daten_aus_json (pfad, standard_wert = []):
    try:
        with open(pfad, 'r') as datei:
            return json.load(datei)
    except Exception:
        return standard_wert

#ins json schreiben
def schreibe_daten_in_json(pfad, daten):
    with open(pfad, 'w') as datei:
        json.dump(daten, datei, indent = 4)

#summe aller transaktionen
def total_transactions(transactions):
	sum = 0
	for transaction in transactions:
		sum = sum + transaction['ausgabebetrag']
	return sum

#summe aller Einnahmen
def total_salary(salaries):
	sum2 = 0
	for salary in salaries:
		sum2 = sum2 + salary['salary']
	return sum2

#def. um Diagram zu zeichnen
def zeichne_balken_diagram(x_daten, y_daten):
    fig = go.Figure(
        data=[go.Bar(x = x_daten, y = y_daten)],
        #layout_title_text="Ausgaben"
        )
    return plotly.offline.plot(fig, output_type="div")

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
	        "salary": float(result['salary']),
	        "budget": float(result['budget'])
	        }
		existing_sign_up.append(user_data_dictionary)
		schreibe_daten_in_json("user_data.json", existing_sign_up)
	
		print(existing_sign_up)
		#übergabe der berechnung von sum2 an Budget.html funktioniert noch nicht
		sum2 = total_salary(existing_sign_up)
		print(sum2)
		return redirect(url_for('dashboard'))
	return render_template ("sign_up.html")

#def um vergessenes Passwort durch Angabe von hinterlegter Mailadresse anzufordern
@app.route("/forgot_password",methods=['GET','POST'])
def forgot_password():
	data_mail=lade_daten_aus_json("user_data.json")
	if request.method == 'POST':
		mail_new = request.form['e_mail']
		for e in data_mail:
			if e['e_mail'].lower() == mail_new.lower():
				msg = Message(subject="Passwort vergessen",
				sender=app.config.get("MAIL_USERNAME"),#verweis nach oben (Zeile 16)
				recipients=[mail_new], # email welche eingegeben wurde und mit sign_up übereinstimmt
				body="Guten Tag! Hiermit können Sie Ihr Mail zurücksetzen" )
				mail.send(msg)
		return redirect(url_for('login'))
	return render_template("forgot_password.html")

#doppelte URL abfrage, für Dashboard mit /, oder /dashboard
@app.route("/", methods=['GET', 'POST'])
@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
	return render_template("dashboard.html")

@app.route("/tasks")
def graph():
	# Hole Daten für Diagramm und schreibe es in Variable
    grafik = lade_daten_aus_json("ausgaben.json")
    fig = go.Figure()
    x = "test"
    y_school = []
    y_food = []
    #fehler im get Befehl
    for i in grafik.get("ausgabehashtag", []):
            y_school.append(i["schule"])
            y_food.append(i["essen"])

    ausgaben_diagram = zeichne_balken_diagram(x, y_gewicht, "Ausgabenansicht")
    return render_template("tasks.html", ausgaben_diagram=ausgaben_diagram)

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

#passiert noch nix...
def load_salary():
	sum2 = total_salary(existing_sign_up)
	return render_template("budget.html", sum2=sum2)



if __name__ == "__main__":
	app.run(debug=True, port=5000)