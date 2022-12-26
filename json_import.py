import json

f = open('MCMdb.txt')

data = json.load(f)

print(data['Verben'])