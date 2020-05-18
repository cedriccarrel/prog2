
newdata = pd.read_csv("Einnahmen3.csv", sep=";")
print(newdata)

print(newdata.loc[1, "col1"]) #übernahme

print(newdata.iloc[1, 1]) #position --> besser für iterrierung

def result():
    try:
        if request.method == 'POST':
            result = request.form
            newdata = pd.read_csv("Einnahmen.csv", sep=";")
            newdata.iloc[[0, 1]] = result['Name']
            newdata.iloc[[1, 1]] = result['Vorname']
            newdata.to_csv("Einnahmen.csv", sep=";")

    except FileNotFoundError:
        vorlage = {'name': [4, 6], 'vorname': [5, 7]}
        liste = pd.DataFrame(data=vorlage)
        liste.to_csv("Einnahmen.csv", sep=";")
        if request.method == 'POST':
            result = request.form
            newdata = pd.read_csv("Einnahmen.csv", sep=";")
            newdata.iloc[1, 1] = result['Name']
            newdata.iloc[1, 2] = result['Vorname']
            newdata.to_csv("Einnahmen.csv", sep=";")

    return render_template("budget.html", result=result)


 einnahmen (
		sparziel FLOAT, sparzeitraum INTEGER, hashtagsparen TEXT,
		einnahmefirma FLOAT, einnahmebetrag FLOAT, einnahmedatum FLOAT,
		einnahmedauerauftrag TEXT, einnahmehashtag TEXT, einnahmebeschreibung TEXT
	)
	
ausgaben (
		ausgabenfirma FLOAT, ausgabenbetrag FLOAT, ausgabendatum FLOAT,
		ausgabendauerauftrag TEXT, ausgabenhashtag TEXT, ausgabenbeschreibung TEXT
	)

personalien (
		name TEXT, vorname TEXT, situation TEXT, email TEXT, passwort TEXT, username TEXT, 
		telefonnummer INTEGER, passwortvergessen TEXT
	)



