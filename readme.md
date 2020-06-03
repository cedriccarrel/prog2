# Projekt: Oktofinance 2.0
## Ausgangslage / Problemstellung
Die bestehenden Spar und Budgetfunktionen im E-Banking sind nicht sexy und machen einfach keinen Spass. Die meisten Leute kennen diese Funktionen nicht einmal, da das E-Banking kein Ort ist, an dem man sich länger als nötig aufhalten möchte.

Ein weiteres Problem besteht darin, dass der Zeitpunkt, an dem man darauf hingewiesen wird, dass man jetzt spätestens sparen muss, in diesen Tools nicht akkurat ist. Das Geld ist meist schon ausgegeben, bis man sich Ende Monat wieder im E-Banking einloggt und den dortigen Sparplaner aufruft.
Vielen Menschen fehlt die Motivation ihr Budget zu planen. Der damit verbundene Aufwand (Transaktionen kategorisieren, Sparziele festlegen, Analysen etc.) schreckt einen Grossteil der potenziellen Nutzer ab.

## Projektidee
Wir wollen, eine Web-App programmieren, die durch Einfachheit und Nuterfreundlichkeit besticht. Dies soll die Nutzer motivieren, sich mit dem Sparen auseinanderzusetzen. Wir möchten ihnen dabei helfen, finanzielle Entscheide besser treffen zu können. 

Sparziele sollen keine weit entfernten Träume mehr darstellen, sondern Realität werden.

Ziel des Projektes ist eine Budgetplanungs-Applikation zu bauen, mit welcher man sein Budget für verschiedene anstehende Ausgaben (z.B. Lebensmittel, Ferien, Kleider, Arztrechnungen etc.) des täglichen Lebens planen kann. Wir haben uns für eine Web-App entschieden, damit Sparen wieder spass macht und man mit Freude sein Budget plant.

## Funktionen
Der Nutzer kreiert über die Sign Up-Funktion einen Account. Dieser enthält Username, Passwort, E-Mail-Adresse, Budgetziel und Einkommen. Diese Daten fliessen danach in das Dashboard des Users ein.
Sobald der User registriert ist, kann er sich über die Loginfunktion einloggen. Falls er sein Passwort vergessen hat, lässt sich dieses über die Forgotten Password-Funktion zurücksetzen.

Über die Funktion "New Transactions" kann der Nutzer Zahlungen und Ausgaben eingegeben welche direkt vom Budget abgerechnet werden.

Im Dashboard wird einem grafisch angezeigt, wieviel man in den einzelnen Budgetposten im aktuellen Monat oder Jahr noch ausgeben darf. 
Weiter wird das Sparpotenzial grafisch dargestellt und dem Nutzer werden mögliche Budget-Swaps (Verschiebungen zwischen Konten und Ausgabeposten) angezeigt. 
Dadurch ist eine Übersicht über das Budget, die getätigten Zahlungen und das aktuelle Vermögen gewährleistet.

## Workflow
![Ablaufdiagramm](./Prog2_Ablaufdiagramm_V1.jpg)

### Dateneingabe
Im Sign Up (Registrierung) wird der User folgende Daten eingeben können:
- Username, E-Mail-Adresse, Passwort, monatliches Einkommen, Gesamtbudget

Im Login (Anmeldung) wird der User folgende Daten eingeben:
- Username, Passwort

In "New Transactions":
- Angabe Budget pro Ausgabenposten - In welchen Bereichen ist wie viel Budget vorhanden?
- Eingabe der offenen Ausgaben und Rechnungen per Scan, manueller Angabe oder Upload als PDF-File
- Definition von kurz- und langfristigen Sparzielen
- Eingabe, wann die Steuerrechnung ausgefüllt wird
- Angabe des Sparzwangs (Stark, Mittel und leicht)

### Datenverarbeitung / Speicherung
- User Daten werden als json-Datei abgespeichert und sind persistent.
- Transaktionsdaten werden auch als json-Datei abgespeichert und sind persistent.

### Datenausgabe
- Übersicht aller Ausgaben als Kuchendiagramm
- Übersicht des aktuellen Budgets als Balkendiagramm
- Anzeige Ausgabenverlauf im Liniendiagramm
- Anzeige Sparpotential als Balkendiagramm - wird im Budget grün dargestellt
