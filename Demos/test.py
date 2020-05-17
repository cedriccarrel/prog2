
newdata = pd.read_csv("Einnahmen3.csv", sep=";")
print(newdata)

print(newdata.loc[1, "col1"]) #übernahme

print(newdata.iloc[1, 1]) #position --> besser für iterrierung

newdata.iloc[1, 1] = 7

print(newdata)

newdata.to_csv("Einnahmen3.csv", sep=";")


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


from datetime import datetime
import json


def speichern(datei, key, value):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)


def aktivitaet_speichern(aktivitaet):
    datei_name = "aktivitaeten.json"
    zeitpunkt = datetime.now()
    speichern(datei_name, zeitpunkt, aktivitaet)
    return zeitpunkt, aktivitaet


def aktivitaeten_laden():
    datei_name = "aktivitaeten.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt


