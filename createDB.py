import sqlite3
from LineDataContainer import LineDataContainer
import os

if os.path.exists("database.db"):
	os.remove("database.db")

con = sqlite3.connect("database.db")
cur = con.cursor()

ldc = LineDataContainer('MCMdb.json')

#LINE BEGINNING
cur.execute("CREATE TABLE line_beginning(id, text)")
for i in range(0,len(ldc.line_beginnings)):
	line = ldc.line_beginnings[i]
	command = "INSERT INTO line_beginning VALUES ("+str(i)+", \""+line+"\")"
	print(command)
	cur.execute(command)

#LINE ENDING
cur.execute("CREATE TABLE line_ending(id, text, rhyme)")
for i in range(0,len(ldc.line_endings)):
	line = ldc.line_endings[i]
	rhyme = ldc.line_endings_rhymes[i]
	command = "INSERT INTO line_ending VALUES ("+str(i)+", \""+line+"\", \""+rhyme+"\")"
	print(command)
	cur.execute(command)

#LINE STANDALONE
cur.execute("CREATE TABLE line_standalone(id, text, rhyme)")
for i in range(0,len(ldc.line_standalones)):
	line = ldc.line_standalones[i]
	rhyme = ldc.line_standalones_rhymes[i]
	command = "INSERT INTO line_standalone VALUES ("+str(i)+", \""+line+"\", \""+rhyme+"\")"
	print(command)
	cur.execute(command)

#VERB
cur.execute("CREATE TABLE verb(id, text, type)")
for i in range(0,len(ldc.line_verbs)):
	line = ldc.line_verbs[i]
	vtype = "explicit"
	command = "INSERT INTO verb VALUES ("+str(i)+", \""+line+"\", \""+vtype+"\")"
	print(command)
	cur.execute(command)

for i in range(0,len(ldc.line_verbs_regular)):
	line = ldc.line_verbs_regular[i]
	vtype = "regular"
	command = "INSERT INTO verb VALUES ("+str(len(ldc.line_verbs)+i)+", \""+line+"\", \""+vtype+"\")"
	print(command)
	cur.execute(command)

#SUBSTANTIV
substIndex = 0
cur.execute("CREATE TABLE substantiv(id, text, type)")
for i in range(0,len(ldc.substantive_maennlich)):
	line = ldc.substantive_maennlich[i]
	vtype = "male"
	command = "INSERT INTO substantiv VALUES ("+str(substIndex)+", \""+line+"\", \""+vtype+"\")"
	print(command)
	cur.execute(command)
	substIndex += 1

for i in range(0,len(ldc.substantive_weiblich)):
	line = ldc.substantive_weiblich[i]
	vtype = "female"
	command = "INSERT INTO substantiv VALUES ("+str(substIndex)+", \""+line+"\", \""+vtype+"\")"
	print(command)
	cur.execute(command)
	substIndex += 1

for i in range(0,len(ldc.substantive_mehrzahl)):
	line = ldc.substantive_mehrzahl[i]
	vtype = "plural"
	command = "INSERT INTO substantiv VALUES ("+str(substIndex)+", \""+line+"\", \""+vtype+"\")"
	print(command)
	cur.execute(command)
	substIndex += 1

for i in range(0,len(ldc.substantive_neutrum)):
	line = ldc.substantive_neutrum[i]
	vtype = "neutrum"
	command = "INSERT INTO substantiv VALUES ("+str(substIndex)+", \""+line+"\", \""+vtype+"\")"
	print(command)
	cur.execute(command)
	substIndex += 1

cur.execute("CREATE TABLE people(id, text)")
for i in range(0,len(ldc.line_verbs)):
	line = ldc.people[i]
	command = "INSERT INTO people VALUES ("+str(i)+", \""+line+"\")"
	print(command)
	cur.execute(command)

con.commit()
con.close()