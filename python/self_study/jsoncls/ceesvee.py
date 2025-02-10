import csv
import json

#with open(filename, encoding) as varname:
    #csv.reader Or DictReader to read as dictionary
with open("file.csv", encoding="utf-8") as fp:
    reader = csv.reader(fp) # or DictReader
    for row in reader:
        print(row)


#Writing CSV files 
example = {"name": "Tim", "grade": 25}
fields = list(example.keys())
#using w to "write"
with open("output.csv", "w", encoding="utf-8", newline="") as fp:
    writer = csv.DictWriter(fp, fieldnames=fields)
    writer.writeheader()
    writer.writerow(example)

"""
JSON -> JavaScript Object Notation
Pros -> 
- lightwaight and very flexible, langauge independant, easy ro read and write, flat
Cons ->
- Very flexible (no validation), no comments, Hard to "debug"


JSON in python 
https://docs.python.org/3/library/json.html
"""


# with open("input.json") as ap:
#     json.load(ap)

#JSON should be in triple quotes
value = """["JSON list", {"keyword": "value"}]"""
#loads takes in json string to python readable content 
data = json.loads(value)

#using w to write again
with open("output.json", "w") as ap:
    #json writing requires json.loads() and the variable of the time 
    json.dump(data, ap)

print(json.dumps(data))


#method usually mean class 
class ser: 
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def to_dict(self):
        #convert the object's state into a dictionary 
        #when calling loads, must be a string 
        fo = json.loads("""{ 
            "name":"name",
            "age":"age"
        }""")
        return fo
    
    def to_json(self):
        with open("method.json", "w") as wr:
            #dump uses json string while dumps allows for python readable
            json.dump(self.to_dict(), wr)

    #writing a class method to take a json string and turns into an objecy
    @classmethod
    def from_json(cls, json_str):
        #conver a json string into an instance of serialable
        data =  json.loads(json_str)
        return data
    

#example usage 
person = ser("Sean", 18)
person.to_json()

json_str = '{"name": "Bob", "age": 25 }'
person2 = ser.from_json(json_str)
print(person2)
