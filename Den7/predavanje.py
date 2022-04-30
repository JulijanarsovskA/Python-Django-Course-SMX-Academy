import requests
import json

req = requests.get("http://api.open-notify.org/iss-now.json")
data = json.loads(req.text)
#print(data)

req2 = requests.get("http://api.open-notify.org/astros.json")
data2 = json.loads(req2.text) # data2 e dictionary
#print(data2)

names = data2['people'] #  names e lista
#print(names)

for name in names:
    print("Astronaut {} e del od ekipazot na {}".format(name['name'], name['craft']))
   

