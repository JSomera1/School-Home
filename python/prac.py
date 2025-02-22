import csv
import json
import pytest


def to_json(e):
    return {
        "name": e['name'],
        "phone": e['phone']
    }

with open ('customers.csv', 'r') as fp:
    reader = csv.DictReader(fp)
    ls = []
    for i in reader:
        ls.append(to_json(i))
    with open('out.json', 'w') as ap:
        json.dump(ls, ap)