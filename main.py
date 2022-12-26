import random

line_begins= ["Alle Leute sagen zu mir",
"Es ist nicht so leicht",
"Kann es aber sein",
"Es ist mir egal",
"Auch wenn du denkst",
"Ohne nice"]

line_ends = [" bin so genial.", " bist so abgezeckt", " du wohnst in den Knast", " geh widder Heim"]

line_standalone = [
"Zeig\' ich dir den Mittelfinger",
"Bleib ich wie ich bin",
"Mach es ausm Kopf",
]

line_verbs = [
"labern",
"erzählen",
"glauben",
"ficken",
"tuten",
"blasen"
] 
text = ""

def addline():
	text = ""
	randint_for_line_type = random.randint(0, 20)
	if randint_for_line_type > 15:
		text+= getRandomElement(line_standalone)
	elif randint_for_line_type > 1:
		text+= getRandomElement(line_begins) + getRandomElement(line_ends)
	elif randint_for_line_type > 0:
		text+= "Was soll ich tun \nSoll ich "+getRandomElement(line_verbs)+" oder ruhn?"
	else:
		text+= getRandomElement(line_verbs) +", " +getRandomElement(line_verbs) +", "+getRandomElement(line_verbs) +" und zählen die Scheine" 
	return text +" \n"

def getRandomElement(line):
	return line[random.randint(0, len(line) - 1)]


for i in range(1,8):
	text += addline()

print(text)