#magic methods/dunder methods 

"""
Everything is an object 
type(class) is an object 

dunder methods aer surrounded by __ and are built in methods 
    - thye run withou being called explicitly 
"""

#
class Person:
    def __init__(self, name):
        self._name = name
    #str is returned when the class is printed without specification print(obj.name)
    def __str__(self):
        return f"Person: {self._name}"
    

"""
More useful methods 

str for printing 

len for length -> this can return anything 

getitem allows instance[value] (like positional notation) 

call allows instance()

contains -> testing something in the instance

iter -> uses instance as an iterator

next -> returns next value of the iteration


Dunder "math"

add using instance + something 
sub using instance - something 
mul using instance * something 
pow using instance ** something 
mod using instance % something 
eq using instance == something 
lt using instance < something. needed for sorting!
le using instance <= something 
gt using instance > something 
"""

#implementing __lt__
class Score:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __lt__(self, other):
        if type(other) is not type(self):
            raise TypeError("Unsupported type")
        # We compare the score attribute
        return self.score < other.score
    

#collection in a list 
class HighScores:
    def __init__(self):
        self._scores = list()
    # We would need to manage scores here, or use aggregation
    def __len__(self):
        return len(self._scores)
    

#operatro for sorting 
menu = [
    ("Pizza", 10),
    ("Pizza slice", 3),
    ("Fountain drink", 2),
    ("Cookie", 4),
]
# Each element in the menu is a tuple (~list)
# We want to sort on the item with index 1
sorted(menu, key=operator.itemgetter(1))


#with dictionaries
menu = [
    { "name": "pizza", "price": 10, "in stock": 10 },
    { "name": "drink", "price": 2, "in stock": 50 },
    { "name": "cookie", "price": 4, "in stock": 20 },
    { "name": "pizza slice", "price": 3, "in stock": 15 },
]
#sorting by a specific key 
sorted(menu, key=operator.itemgetter('price'))

#sorting object
hiscores = [
    Score(name="Tim", score=20),
    Score(name="John", score=0),
    Score(name="Sarah", score=100),
]
# Sorting on the name attribute
sorted(hiscores, key=operator.attrgetter('name'))

#collections with __getitem__
class HighScores:
    def __init__(self):
    # This is a list of scores
        self._scores = list()
    def __len__(self):
        return len(self._scores)
    def __getitem__(self, idx):
        return self._scores[idx]
    hiscores = HighScores()
# Add scores to the instance, and then:
print(hiscores[0].scores) # First score in the list
print(hiscores[-1].scores) # Last score in the list