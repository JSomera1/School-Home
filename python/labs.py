import pytest
from unittest.mock import patch, mock_open
from hangman import Game

def str2dict(str):
    dict = {}
    for i in str:
        if not i in dict:
            dict[i] = 1
        elif i in dict:
            dict[i] += 1
    return dict

def str2dict_plus(str):
    dict = {}
    str = list(str.lower())
    for i in str:
        if i == " ":
            pass
        elif not i in dict:
            dict[i] = 1
        elif i in dict:
            dict[i] += 1
    return dict 

def histogram(str):
    hst = str2dict_plus(str)
    star = "*"
    for i in hst:
        st = ""
        st += i
        for j in range(hst[i]):
            st += star
        print(st)


def obscure_text(str):
    new_str = str.replace("I", "1").replace("o", "0").replace("O", "0").replace("e", "3").replace("E","3").replace("l", "|").replace("a", "@")
    return new_str

def test_text(): #test is run with pytest and must be named test_* then tested function inside equal to a certain result
    assert obscure_text("Hello World") == "H3||0 W0r|d"

# def tistheseason():
#     return 'merry christmas'

# def test_season():
#     assert tistheseason() == 'merry christmas'


###object oriented programming

class mobian:
    def __init__(self,name,animal,age):
        self.name = name
        self.animal = animal
        self.age = age

    def __str__(self):
        return f"{self.name} is a {self.animal} and is {self.age} years old"
    
    def speak(self):
        return "I dont know what to say"
    
    def show_color(self):
        return f"I am {self.color}"
    
class hedgehog(mobian):
    def __init__(self,name,age,color):
        super().__init__(name,"hedgehog",age)
        self.color = color
    
    def speak(self):
        if self.name == "Sonic":
            return "Gotta go fast"
        elif self.name == "Shadow":
            return "I am the ultimate lifeform"
    
sonic = hedgehog("Sonic", 15, "blue")
shadow = hedgehog("Shadow", 50, "black")
print(sonic.show_color())
print(shadow.speak())

# @pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data="testword")
def test_game(mock_file):
    """Game object, 10 turns, word is testword"""
    assert mock_file == "testword"
    
