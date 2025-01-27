#object oriented programming 

class warframe:
    #instantiate the object. arguements passed into init function
    #self works by reading assigned value such as variable set to object 
    def __init__(self, name, ability):
        #defines attribute
        self.name = name
        self.ability = ability
        pass
    def jump(self):
        print("boing")

    # alternative instead printing `object.name`
    def get_name(self):
        return self.name
    
    def get_ability(self):
        return self.ability
    
    #altering attributes 
    # changing attribute name does change assigned variable name
    def set_name(self, name):
        self.name = name 

# arguments can be anything 
Ash = warframe("Ash", 1)

#similarly called to javascript objects 
# print(Ash.name)
print(Ash.get_ability())

#calling attribute change 
Ash.set_name('Excalibur')
# checking that it changed 
print(Ash.get_name())

#calling value 
Ash.jump()


#multiple classes/ communication between classes 
class student:
    def __init__(self, name, age, grade):
        self.name = name 
        self.age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade 
    
class course:
    def __init__(self, name, max_students):
        self.name = name 
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True 
        return False 
    
    #using inner object in a function to determine grade
    def get_average_grade(self):
        value = 0 
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)
    
s1 = student("Tim", 19, 95)
s2 = student("Bill", 19, 75)
s3 = student("Jill", 19, 65)

course = course("Science", 2)
# adding an object to another object
course.add_student(s1)
course.add_student(s2)

# calling positional atttribute. Since inside is an object, you can call the objects' attribute as seen below
print(course.students[0].name)

# calling 
print(course.get_average_grade())


#inheritance
#class specific things 

#generalization
class pet:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')
    def speak(self):
        print("I dont know what to say")

# adding inheritance for upper level class
class cat(pet):
    def __init__ (self, name, age, color):
        #referencing superclass (parent), choose function then pass in arguments
        super().__init__(name,age)
        self.color = color
    def speak(self):
        print("meow")
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')


class fish(pet):
    pass

p = pet("Tim", 19)
p.show()
# child classes can call generaled functions. If same name, specific class function overrides the parent function
c = cat('Bill', 34, "Blue")
c.show()
#example of generalization for class calling 
f  = fish('Jill', 6)
f.speak()

#class attributes
class person:
    # defined for the entire class (not specific to an instance)
    number_of_people = 0 

    def __init__(self, name):
        self.name = name
        person.add_person()

    #class methods - called on the class itself so it can return attribute. no accesss to individual instances
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

#attribute is general therefor all classes share them
p1 = person('John')

p2 = person('Johnny')
print(person.number_of_people_())


#static methods
class Math:
    #dont change anything
    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def pr():
        print("run")

print(Math.add5(5))
Math.pr()
