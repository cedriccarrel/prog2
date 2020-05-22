
#read headers
#df.columns
#print(df.head(5))

#read ech column
#print(df['Name'][0:5])
#print(df[['Name', 'Type1', 'HP']])
#print(df.name)

#read ech row
#print(df.iloc[1:4])
#for index, row in df.iterrwos():
#	print(index, row['Name'])
#df.loc[df['Type 1']== 'Fire'] --> eingrenzen mit variablen
#df.loc[(df['Type 1']== 'Fire') & (df['Type 2']== 'Poison') ] -->2 variablen --  


#read a specific location (r, c)
#print(df.iloc[2, 1])


#df.describe -->gibt daten zusammengefasst aus

#df.sort_values(['Type1', 'HP'], ascending=False) --> sortieren
#df['Total'] = df['HP'] + df['Attack'] --> rechnen und in neue spalte
#df['Total'] = df.iloc[:,4:10].sum(axis=1) --> neue anordnung der spalten und zusammengezaählt

#df.to_csv('modified.csv', index=false)
#df.to_excel('modified.xlsx', index=false)--> als excel