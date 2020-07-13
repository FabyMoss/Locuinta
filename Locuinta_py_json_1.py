import json
from json import JSONEncoder
class Poze:
    def __init__(self, URL: str, nr_ord = int, desc = str):
        self.URL = URL
        self.nr_ord = nr_ord
        self.desc = desc
    def get_URL(self):
        return self.URL
    def get_nr_ord(self): 
        return self.nr_ord
    def get_desc(self): 
        return self.desc

class PozeEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

url1 = input('Introduceti link-ul URL: ')
nr_ord1 = int(input('Introduceti numarul de ordine: '))
desc1 = input('Introduceti o descriere scurta a pozei: ')
obj1 = Poze(url1, nr_ord1, desc1)
al = open("locuinta.json", "a")
#print(PozeEncoder().encode(obj1))

pozeJSONData = json.dumps(obj1, indent=4, cls=PozeEncoder)
print(pozeJSONData)
json.dump(pozeJSONData, al)

#pozeJSON = json.loads(pozeJSONData)
#print(pozeJSON)

al.close()









