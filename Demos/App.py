from flask import Flask, render_template, redirect, url_for, request
import json
from flask_mail import Message, Mail
import plotly #Library install via Conda --> Befehl: conda install plotly
import matplotlib.pyplot as plt
import plotly.graph_objects as go #somit wurde die Grafik angesprochen
from plotly.offline import plot 


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
#Instanz der Klasse Mail
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

#berechnung summe je Hashtag welche im json "ausgaben.json" eingegeben wurden
def total_hashtags(transactions):
	sum_essen = 0
	sum_haushalt = 0
	sum_schule = 0
	sum_kleider = 0
	sum_sport = 0
	sum_freizeit = 0
	sum_kommunikation = 0
	sum_persönlich = 0
	for transaction in transactions:
	    if transaction['ausgabehashtag'] == "essen":
	        gefundener_hashtag = transaction['ausgabehashtag']
	        find_betrag_essen = float(transaction['ausgabebetrag'])
	        sum_essen = sum_essen + find_betrag_essen
	        #print(sum_essen)
	    if transaction['ausgabehashtag'] == "haushalt":
	        gefundener_hashtag = transaction['ausgabehashtag']
	        find_betrag_haushalt = float(transaction['ausgabebetrag'])
	        sum_haushalt = sum_haushalt + find_betrag_haushalt
	        #print(sum_haushalt)
	    if transaction['ausgabehashtag'] == "schule":
	        gefundener_hashtag = transaction['ausgabehashtag']
	        find_betrag_schule = float(transaction['ausgabebetrag'])
	        sum_schule = sum_schule + find_betrag_schule
	        #print(sum_schule)
	    if transaction['ausgabehashtag'] == "kleider":
	        gefundener_hashtag = transaction['ausgabehashtag']
	        find_betrag_kleider = float(transaction['ausgabebetrag'])
	        sum_kleider = sum_kleider + find_betrag_kleider
	        #print(sum_kleider)
	    if transaction['ausgabehashtag'] == "sport":
	        gefundener_hashtag = transaction['ausgabehashtag']
	        find_betrag_sport = float(transaction['ausgabebetrag'])
	        sum_sport = sum_sport + find_betrag_sport
	        #print(sum_sport)
	    if transaction['ausgabehashtag'] == "kommunikation":
	        gefundener_hashtag = transaction['ausgabehashtag']
	        find_betrag_kommunikation = float(transaction['ausgabebetrag'])
	        sum_kommunikation = sum_kommunikation + find_betrag_kommunikation
	        #print(sum_kommunikation)
	    if transaction['ausgabehashtag'] == "persönlich":
	        gefundener_hashtag = transaction['ausgabehashtag']
	        find_betrag_persönlich = float(transaction['ausgabebetrag'])
	        sum_persönlich = sum_persönlich + find_betrag_persönlich
	        #print(sum_persönlich)
	    if transaction['ausgabehashtag'] == "freizeit":
	        gefundener_hashtag = transaction['ausgabehashtag']
	        find_betrag_freizeit = float(transaction['ausgabebetrag'])
	        sum_freizeit = sum_freizeit + find_betrag_freizeit
	        #print(sum_freizeit)
	return sum_kleider, sum_persönlich, sum_kommunikation, sum_sport, sum_schule, sum_haushalt, sum_essen, sum_freizeit


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
    #anschrift = users["username"][1]
    #print(anschrift)
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
	for i in data_mail:
		liste_username = (i.get('username'))
		print(liste_username)
	if request.method == 'POST':
		mail_new = request.form['e_mail']
		#user_password = request.json('password')
		for e in data_mail:
			if e['e_mail'].lower() == mail_new.lower():
				msg = Message(subject="Passwort vergessen",
				sender=app.config.get("MAIL_USERNAME"),#verweis nach oben (Zeile 16)
				recipients=[mail_new], # email welche eingegeben wurde und mit sign_up übereinstimmt
				body="Guten Tag!" + " " + liste_username + " " + "Ihr Passwort lautet:") #+ user_password# + "!")
				mail.send(msg)
		return redirect(url_for('login'))
	return render_template("forgot_password.html")

#doppelte URL abfrage, für Dashboard mit /, oder /dashboard
@app.route("/", methods=['GET', 'POST'])
@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
	return render_template("dashboard.html")

@app.route("/tasks") #anzeige der Ausgaben
def viz():
	#load data from user_date.json
	data_grafic = lade_daten_aus_json("ausgaben.json")


	# create data
	labels = ['groupA', 'groupB', 'groupC', 'groupD']
	values = [12, 11, 3, 30]
	#create figure
	fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.7)])
	div = plot(fig, output_type="div") #create div from figure and send to render template as div
	return render_template('tasks.html', viz_div=div)

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
	sum_essen = total_hashtags(existing_transaction)
	sum_haushalt = total_hashtags(existing_transaction)
	sum_schule = total_hashtags(existing_transaction)
	sum_kleider = total_hashtags(existing_transaction)
	sum_sport = total_hashtags(existing_transaction)
	sum_freizeit = total_hashtags(existing_transaction)
	sum_kommunikation = total_hashtags(existing_transaction)
	sum_persönlich = total_hashtags(existing_transaction)

	return render_template("budget.html", data1=existing_transaction, sum=sum, sum_essen=sum_essen, sum_haushalt=sum_haushalt, 
		sum_schule=sum_schule, sum_kleider=sum_kleider, sum_sport=sum_sport, sum_freizeit=sum_freizeit, 
		sum_kommunikation=sum_kommunikation,sum_persönlich=sum_persönlich)

#passiert noch nix...
def load_salary():
	sum2 = total_salary(existing_sign_up)
	return render_template("budget.html", sum2=sum2)



if __name__ == "__main__":
	app.run(debug=True, port=5000)