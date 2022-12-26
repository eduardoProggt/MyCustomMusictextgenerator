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

text = ""

def addline():
	text = ""
	if random.randint(1, 3) == 3:
		text+= getRandomElement(line_standalone)
	else:
		text+= getRandomElement(line_begins) + getRandomElement(line_ends)

	return text +" \n"

def getRandomElement(line):
	return line[random.randint(0, len(line) - 1)]


for i in range(1,8):
	text += addline()

print(text)