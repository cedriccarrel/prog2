#test file

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