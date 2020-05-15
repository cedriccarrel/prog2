import sqlite3 as db


def init():
	connection = db.connect("daten2.db")
	cursor = connection.cursor()
	sql = '''
	create table einnahmen (
		sparziel FLOAT, 
		sparzeitraum INTEGER, 
		hashtagsparen STRING,
		einnahmefirma FLOAT, 
		einnahmebetrag FLOAT, 
		einnahmedatum FLOAT,
		einnahmedauerauftrag STRING, 
		einnahmehashtag STRING, 
		einnahmebeschreibung STRING
		)
	'''
	cursor.execute(sql)
	connection.commit()

def log(sparziel, sparzeitraum, hashtagsparen, einnahmefirma, einnahmebetrag, einnahmedatum, einnahmedauerauftrag, einnahmehashtag, einnahmebeschreibung):
	connection = db.connect("daten2.db")
	cursor = connection.cursor()
	sql = '''
	insert into einnahmen values (
		{},
		{},
		'{}',
		{},
		{},
		{},
		'{}',
		'{}',
		'{}'
	)
	'''.format(sparziel, sparzeitraum, hashtagsparen, einnahmefirma, einnahmebetrag, einnahmedatum, einnahmedauerauftrag, einnahmehashtag, einnahmebeschreibung)
	cursor.execute(sql)
	connection.commit()


