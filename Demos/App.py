from flask import Flask, render_template, redirect, url_for, request
import json
from flask_mail import Message, Mail #pip install Flask-Mail
import plotly #Library install via Conda --> Befehl: conda install plotly
import matplotlib.pyplot as plt #conda install -c conda-forge matplotlib
import plotly.graph_objects as go #somit wurde die Grafik angesprochen
from plotly.offline import plot 


app = Flask(__name__)


#E-Mail Konfiguration
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": 'oktofinance2.0@gmail.com',
    "MAIL_PASSWORD": 'Test123?'
}

#Instanz der Klasse Mail
app.config.update(mail_settings)

mail = Mail(app)


#json laden für Ausgaben, Userdata
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
def total_essen(transactions):
    sum_essen = 0
    for transaction in transactions:
        if transaction['ausgabehashtag'] == "essen":
            gefundener_hashtag = transaction['ausgabehashtag']
            find_betrag_essen = float(transaction['ausgabebetrag'])
            sum_essen = sum_essen + find_betrag_essen
            #print(sum_essen)
    return sum_essen

#berechnung summe je Hashtag welche im json "ausgaben.json" eingegeben wurden
def total_haushalt(transactions):
    sum_haushalt = 0
    for transaction in transactions:
        if transaction['ausgabehashtag'] == "haushalt":
            gefundener_hashtag = transaction['ausgabehashtag']
            find_betrag_haushalt = float(transaction['ausgabebetrag'])
            sum_haushalt = sum_haushalt + find_betrag_haushalt
            #print(sum_haushalt)
    return sum_haushalt

#berechnung summe je Hashtag welche im json "ausgaben.json" eingegeben wurden
def total_schule(transactions):
	sum_schule = 0
	for transaction in transactions:
		if transaction['ausgabehashtag'] == "schule":
			gefundener_hashtag = transaction['ausgabehashtag']
			find_betrag_schule = float(transaction['ausgabebetrag'])
			sum_schule = sum_schule + find_betrag_schule
			#print(sum_schule)
	return sum_schule

#berechnung summe je Hashtag welche im json "ausgaben.json" eingegeben wurden
def total_kleider(transactions):
	sum_kleider = 0
	for transaction in transactions:
	    if transaction['ausgabehashtag'] == "kleider":
	        gefundener_hashtag = transaction['ausgabehashtag']
	        find_betrag_kleider = float(transaction['ausgabebetrag'])
	        sum_kleider = sum_kleider + find_betrag_kleider
	        #print(sum_kleider)
	return sum_kleider

#berechnung summe je Hashtag welche im json "ausgaben.json" eingegeben wurden
def total_sport(transactions):
	sum_sport = 0
	for transaction in transactions:
	    if transaction['ausgabehashtag'] == "sport":
	        gefundener_hashtag = transaction['ausgabehashtag']
	        find_betrag_sport = float(transaction['ausgabebetrag'])
	        sum_sport = sum_sport + find_betrag_sport
	        #print(sum_sport)
	return sum_sport

def total_kommunikation(transactions):
	sum_kommunikation = 0
	for transaction in transactions:
	    if transaction['ausgabehashtag'] == "kommunikation":
	        gefundener_hashtag = transaction['ausgabehashtag']
	        find_betrag_kommunikation = float(transaction['ausgabebetrag'])
	        sum_kommunikation = sum_kommunikation + find_betrag_kommunikation
	        #print(sum_kommunikation)
	return sum_kommunikation

#berechnung summe je Hashtag welche im json "ausgaben.json" eingegeben wurden
def total_persönlich(transactions):
	sum_persönlich = 0
	for transaction in transactions:
	    if transaction['ausgabehashtag'] == "persönlich":
	        gefundener_hashtag = transaction['ausgabehashtag']
	        find_betrag_persönlich = float(transaction['ausgabebetrag'])
	        sum_persönlich = sum_persönlich + find_betrag_persönlich
	        #print(sum_persönlich)
	return sum_persönlich

#berechnung summe je Hashtag welche im json "ausgaben.json" eingegeben wurden
def total_freizeit(transactions):
	sum_freizeit = 0
	for transaction in transactions:
	    if transaction['ausgabehashtag'] == "freizeit":
	        gefundener_hashtag = transaction['ausgabehashtag']
	        find_betrag_freizeit = float(transaction['ausgabebetrag'])
	        sum_freizeit = sum_freizeit + find_betrag_freizeit
	        #print(sum_freizeit)
	return sum_freizeit

#definition für berechnung summe aller einnahmen, welche im json "user_data.json" eingegeben wurden
def total_salary(salaries):
	sum2 = 0
	for i in salaries:
		sum2 = sum2 + i['salary']
	return sum2

#def. für berechnung summe des budgets, welche im json "user_data.json" definiert und eingegeben wurde
def total_budget(budgets):
	sum_budget = 0
	for e in budgets:
		sum_budget = sum_budget + e['budget']
	return sum_budget

#def für Berechnung des aktuellen budgetschwellenwertes
def aktuelles_budget(budgets):
	all_budget = lade_daten_aus_json("user_data.json")
	all_transactions = lade_daten_aus_json("ausgaben.json")
	aktuelles_budget = float(total_budget(all_budget))
	aktuelle_ausgaben = float(total_transactions(all_transactions))
	neues_budget = float(aktuelles_budget) - float(aktuelle_ausgaben)
	if float(neues_budget) <= 0.0:
		#print("Budget überschritten")
		#print(neues_budget)
		return neues_budget


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
		mail = result['e_mail']
		for address in existing_sign_up:
			error2 = None
			if address['e_mail'] == mail:
				error2 = 'Mail already exists. Please try another.'
				return render_template("sign_up.html", error2=error2)
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
		sum2 = total_salary(existing_sign_up)
		sum_budget = total_budget(existing_sign_up)
		return redirect(url_for('dashboard'))
	return render_template ("sign_up.html")

#def um vergessenes Passwort durch Angabe von hinterlegter Mailadresse anzufordern
@app.route("/forgot_password",methods=['GET','POST'])
def forgot_password():
	data_mail=lade_daten_aus_json("user_data.json")
	if request.method == 'POST':
		mail_new = request.form['e_mail']
		for e in data_mail: #sucht in json nach "E-Mail Adresse"
			if e['e_mail'].lower() == mail_new.lower(): #wenn E-Mail Adresse übereinstimmt"
				liste_username = e["username"]
				liste_password = e["password"]
				msg = Message(subject="Passwort vergessen",
				sender=app.config.get("MAIL_USERNAME"),#verweis nach oben (Zeile 16)
				recipients=[mail_new], # email welche eingegeben wurde und mit sign_up übereinstimmt
				body="Guten Tag " + liste_username + "!" + " Ihr Passwort lautet: " + liste_password)
				print(liste_username,liste_password)
				mail.send(msg)
		return redirect(url_for('login'))
	return render_template("forgot_password.html")

@app.route("/settings", methods=['GET', 'POST'])
def settings():
	return render_template("settings.html")

#doppelte URL abfrage, für Dashboard mit /, oder /dashboard
@app.route("/", methods=['GET', 'POST'])
@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
	all_budget = lade_daten_aus_json("user_data.json")
	all_transactions = lade_daten_aus_json("ausgaben.json")
	aktuelles_budget = total_budget(all_budget)
	aktuelle_ausgaben = total_transactions(all_transactions)
	aktueller_lohn = total_salary(all_budget)
	#anzeige Username im Dashboard
	for e in all_budget: 
		username = e['username']
	#Berechnung Lohn und Ausgabenverhältnis in Prozent
	lohn_verhaeltnis = aktueller_lohn - aktuelle_ausgaben
	if aktuelle_ausgaben == 0:
		prozent_print_lohn = 0
		count = 0
		neues_budget = 0
		aktuelles_budget = 0
		prozent_print = 0
		prozent_print2 = 0
		return render_template("dashboard.html", prozent_print_lohn=prozent_print_lohn, count=count, neues_budget=neues_budget, 
		aktuelles_budget=aktuelles_budget, prozent_print=prozent_print, username=username, prozent_print2=prozent_print2)
	else:
		prozent = (lohn_verhaeltnis*100)/aktuelle_ausgaben 
	if prozent >= 0:
		prozent_print_lohn = str(prozent) + " " + "%"
	else:
		prozent_print_lohn = "100%"
	#für Berechnung Anzahl erfasster Tasks in New Transactions
	count = 0
	for i in all_transactions:  
		anzahl = i['ausgabehashtag']
		count = count + 1
	#für prozentberechnungsanzeigen im Dashboard - Berechnung in% wie viel vom def. Budget ausgegeben wurde
	neues_budget = aktuelles_budget - aktuelle_ausgaben
	prozent = (neues_budget*100)/aktuelles_budget 
	if prozent >= 0:
		prozent_print = str(prozent) + " " + "%"
	else:
		prozent_print = "100%"
	# für prozentberechnungsanzeigen im Dashboard - Berechnung in% wie viel vom def. Budget NOCH ausgegeben werden kann
	prozent2 = (aktuelles_budget*100)/neues_budget
	if prozent2 >= 0:
		prozent_print2 = str(prozent2) + " " + "%"
	else:
		prozent_print2 = "0%"
	return render_template("dashboard.html", prozent_print_lohn=prozent_print_lohn, count=count, neues_budget=neues_budget, 
		aktuelles_budget=aktuelles_budget, prozent_print=prozent_print, username=username, prozent_print2=prozent_print2)

@app.route("/tasks") #anzeige der Ausgaben als Grafik
def viz():
	#load data from user_data.json
	data_grafic = lade_daten_aus_json("ausgaben.json")
	sum_essen = total_essen(data_grafic)
	sum_haushalt = total_haushalt(data_grafic)
	sum_schule = total_schule(data_grafic)
	sum_kleider = total_kleider(data_grafic)
	sum_sport = total_sport(data_grafic)
	sum_freizeit = total_freizeit(data_grafic)
	sum_kommunikation = total_kommunikation(data_grafic)
	sum_persönlich = total_persönlich(data_grafic)

	# create data --> werden aus user_data.json ausgelesen (s. funktionen oben) und in diese Variablen geladen
	labels = ['Essen', 'Haushalt', 'Schule', 'Kleider', 'Sport', 'Freizeit', 'Kommunikation', 'Persönlich']
	values = [sum_essen, sum_haushalt, sum_schule, sum_kleider, sum_sport, sum_freizeit, sum_kommunikation, sum_persönlich]
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
	anzeige_budget = lade_daten_aus_json("user_data.json") 
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
	
	#Einzeln berechnete Werte, werden hier angesprochen, damit sie anschl. gerendert werden können
	sum = total_transactions(existing_transaction)
	sum2 = total_salary(anzeige_budget)
	sum_budget = total_budget(anzeige_budget)
	neues_budget = aktuelles_budget(anzeige_budget)
	sum_essen = total_essen(existing_transaction)
	sum_haushalt = total_haushalt(existing_transaction)
	sum_schule = total_schule(existing_transaction)
	sum_kleider = total_kleider(existing_transaction)
	sum_sport = total_sport(existing_transaction)
	sum_freizeit = total_freizeit(existing_transaction)
	sum_kommunikation = total_kommunikation(existing_transaction)
	sum_persönlich = total_persönlich(existing_transaction)

	#Logik = wenn das Budget aufgebraucht wurde, wird ein Mail an den User versendet
	for e in anzeige_budget:
		mail_alert = e['e_mail']
		username_alert = e['username'] 
		if neues_budget <= 0.0:
			msg = Message(subject="BUDGET ALERT!",
			sender=app.config.get("MAIL_USERNAME"),#verweis nach oben (Zeile 16)
			recipients=[mail_alert], # email welche eingegeben wurde und mit sign_up übereinstimmt
			body="Hallo" + " " + username_alert + " " + "Ihr definiertes Budget ist aufgebraucht. Das aktuelle Saldo liegt aktuell bei:" + " " + str(neues_budget) + ".")
			mail.send(msg)
		else:
			return render_template("budget.html", data1=existing_transaction, sum=sum, sum2=sum2, sum_budget=sum_budget, neues_budget=neues_budget, 
				sum_essen=sum_essen, sum_haushalt=sum_haushalt, sum_schule=sum_schule, sum_kleider=sum_kleider, sum_sport=sum_sport, 
				sum_freizeit=sum_freizeit, sum_kommunikation=sum_kommunikation, sum_persönlich=sum_persönlich)

if __name__ == "__main__":
	app.run(debug=True, port=5000)