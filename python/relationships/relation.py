class pet:
    def __init__ (self,name):
        self.name = name 

    def speak(self):
        print('sound')


class Dog(pet):
    def speak(self):
        #call speak on pet from the dog class
        #super calls from parent class 
        super().speak()
        print("woof")