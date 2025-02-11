import pytest
import json 
import csv
from unittest.mock import mock_open, patch

def contain():
    def test_this():
        name = 1 
        assert name == 1

    @pytest.fixture
    def example_fixture():
        fix = 1
        return fix

    #fixture is called before the code and can be used without recalling it every time
    def test_with_fixture(example_fixture):
        assert example_fixture == 1

    #fixture can be called any number of times 
    def test_fix(example_fixture):
        assert example_fixture == 1



    @patch("builtins.input", side_effect=["abc", "def"])
    def test_example(mock_input):
        #cannot iterate throug the mock list 
        test1 = input()
        assert test1 == "abc"
        test2 = input()
        assert test2 == "def"

#writing into json and csv


"""example = {"name": "Tim", "grade": 25}
fields = list(example.keys())
#using w to "write"
with open("output.csv", "w", encoding="utf-8", newline="") as fp:
    writer = csv.DictWriter(fp, fieldnames=fields)
    writer.writeheader()
    writer.writerow(example)
"""
with open("output.csv", encoding="utf-8") as ap:
    read = csv.DictReader(ap)
    # Items are already in an object and need to be iterated through 
    for i in read:
        print(i)

stringson = """["string", 21, {"name":"dict", "list":[1,2,3]}]"""
data = json.loads(stringson)

with open("sonic.json", "w") as tp:
    json.dump(data, tp)
