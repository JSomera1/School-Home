import json


value = """["JSON list", {"keyword": "value"}]"""
data = json.loads(value)

with open("output.json", "w") as fp:
    json.dump(data, fp)
print(json.dumps(data))