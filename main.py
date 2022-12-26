import random

line_begins= ["Alle Leute sagen zu mir",
"Es ist nicht so leicht",
"Kann es aber sein",
"Es ist mir egal",
"Auch wenn du denkst",
"Ohne nice"]

line_ends = [" bin so genial.", " bist so abgezeckt", " du wohnst in den Knast"]

line_standalone = [
"Zeig' ich dir den Mittelfinger"
"Bleib ich wie ich bin",
"Mach es ausm Kopf",
]

text = ""

def addline(text):
	if random.randint(1, 3) == 3:
		text+= line_standalone[random.randint(1, len(line_standalone)-1)]
	else:
		text+= line_begins[random.randint(1, len(line_begins)-1)] + line_ends[random.randint(1, len(line_ends)-1)]
	return text +"\n"
for i in range(1,8):
	text = addline(text)

print(text)