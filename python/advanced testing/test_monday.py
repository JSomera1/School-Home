from monday import person
import pytest

@pytest.fixture # decorator
def bob(): # <-- this a fixture
    return person("Tim")

def test_name(bob): #using name as arguement 
    assert bob.name == "Tim"

def test_hello(bob):
    assert bob.say_hello() == 'Hello, my name is Tim!'

def test_goodbye(bob):
    assert bob.say_goodbye() == "Goodbye!"