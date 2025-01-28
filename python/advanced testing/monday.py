"""
three things to know 
1. fixtures 
an object that you create and is used by various unit test
2. mocks 
3. patching
"""

class person:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        return f"Hello. my name is {self.name}!"
    
    def say_goodbye(self):
        return "Goodbye!"