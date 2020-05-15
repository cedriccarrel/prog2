import sqlite3 

connection = sqlite3.connect("daten2.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE einnahmen (
		sparziel FLOAT, sparzeitraum INTEGER, hashtagsparen TEXT,
		einnahmefirma FLOAT, einnahmebetrag FLOAT, einnahmedatum FLOAT,
		einnahmedauerauftrag TEXT, einnahmehashtag TEXT, einnahmebeschreibung TEXT
	)""")
	

cursor.execute("""CREATE TABLE ausgaben (
		ausgabenfirma FLOAT, ausgabenbetrag FLOAT, ausgabendatum FLOAT,
		ausgabendauerauftrag TEXT, ausgabenhashtag TEXT, ausgabenbeschreibung TEXT
	)""")

cursor.execute("""CREATE TABLE personalien (
		name TEXT, vorname TEXT, situation TEXT, email TEXT, passwort TEXT, username TEXT, 
		telefonnummer INTEGER, passwortvergessen TEXT
	)""")



try:
	cursor = connection.cursor()
	cursor.execute("""INSERT INTO einnahmen VALUES (
		500.00, 1, bmw, raiffeisen, 1000.00, 25.05, ja, lohn, saläreingang
	)""")
	connection.commit()

	cursor = connection.cursor()
	cursor.execute("""INSERT INTO ausgaben VALUES (
		lagerhaus, 40.00, 05.05, nein, verpflegung, mittag essen
	)""")
	connection.commit()

	cursor = connection.cursor()
	cursor.execute("""INSERT INTO personalien VALUES (
		pinto, jose, student, jpintomail, test123, jose_pinto, 0792697395, nein
	)""")
	connection.commit()

except:
	print("Ein Problem trat auf --> Rollback bis zum letzten commit")
	connection.rollback()



def view(sparziel=None):
	connection = db.connect("daten2.db")
	cursor = connection.cursor()
	if sparziel:
		sql = '''
		select * from einnahmen where sparziel = '{}'
		'''.format(sparziel)
		sql2 = '''
		select sum(einnahmebetrag) from einnahmen where sparziel = '{}'
		'''.format(sparziel)
	else:
		sql = '''
		select * from einnahmen
		'''.format(sparziel)
		sql2 = '''
		select sum(einnahmebetrag) from einnahmen
		'''.format(sparziel)
	cursor.execute(sql)
	cursor.execute(sql2)
	results = cursor.fetchall()
	total_amount = cursor.fetchone()[0]

	return total_amount, results