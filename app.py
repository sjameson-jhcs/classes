# *********************************
# ****** SECTION 1 - CLASSES ******
# *********************************

# A "Class" is like a blueprint for an object
# Objects can be many different things
# In a grade tracking program objects might be: Course, Period, Teacher, Student, Gradable Assignment, Comment, Etc.
# In Mario objects might be: Mario, Level, Enemy, Power Up (like star or mushroom), Hittable Block, Etc.
# In banking software objects might be: Customer, Account, Deposit, Withdrawal, Etc.


# Note: Classes are normally named with capital letters with no spaces. But that is not required, just recommended.
class UnknownStudent:
    name = "Unknown"
    age = "Unknown"


# Now that the blueprint exists we can create an INSTANCE of the class
first_student = UnknownStudent()
first_student.name = "John Smith"
first_student.age = 15
print(f"The student's name is {first_student.name} and he is {first_student.age} years old.")


# ********************************************
# ****** SECTION 2 - CONSTRUCTOR METHOD ******
# ********************************************

# A method is what we call a function that belongs to a class.
# A CONSTRUCTOR method runs when a new instance is created.
# The purpose of a constructor is to setup any initial values for a new instance.
# A constructor in python uses the name: __init__

# NOTE: It is considered good practice to always have a constructor even if it does nothing.
class Student:
    # NOTE: For constructor input parameters I like to start them with an underscore.
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age


# second_student = Student(_name="Jane", _age="Doe")
# print(f"The student's name is {second_student.name} and her age is {second_student.age}.")


# ***************************************
# ****** SECTION 3 - OTHER METHODS ******
# ***************************************

# A class can (and usually does) have other methods besides the constructor
class Dog:

    def __init__(self, _name, _breed, _color):
        self.name = _name
        self.breed = _breed
        self.color = _color
        self.position = 0

    def run(self, distance=1):
        self.position += distance
        print(f"{self.name} ran {distance} meters and is now at position {self.position}.")

    def bark(self):
        if self.breed == "Lab":
            print("Woof")
        elif self.breed == "Terrier":
            print("Yap")
        else:
            print("Bark")

    def get_color(self):
        return self.color


# my_dog = Dog(_name="Ellie", _breed="Lab", _color="Yellow")
# my_dog.run(5)
# my_dog.run(-2)
# my_dog.bark()
# print(f"My dog is {my_dog.color}.")


# *************************************
# ****** SECTION 3 - INHERITANCE ******
# *************************************

# For the sake of organization it is often useful to have one class inherit another.
# Usually the parent class is something generic and the child is one type of the parent class

class Animal:
    def __init__(self):
        self.position = 0
        self.speed = 0
        self.noise = "[silence]"

    def run(self):
        self.position += self.speed
        print(f"The animal ran {self.speed} meters and is now at position {self.position}.")

    def make_noise(self):
        print(self.noise)


class Jaguar(Animal):
    def __init__(self):
        self.position = 0
        self.speed = 10
        self.noise = "growwwl"


class Horse(Animal):
    def __init__(self):
        self.position = 0
        self.speed = 8
        self.noise = "neigggh"


class Snake(Animal):
    def __init__(self):
        self.position = 0
        self.speed = 1
        self.noise = "hssss"

    def run(self):
        self.position += self.speed
        print(f"The snake slithered {self.speed} meters and is now at position {self.position}.")

# jax = Jaguar()
# jax.run()
# jax.make_noise()
#
# harvey = Horse()
# harvey.run()
# harvey.make_noise()
#
# steve = Snake()
# steve.run()
# steve.make_noise()

# ******************************************************
# ****** SECTION 4 - S.O.L.I.D. DESIGN PRINCIPLES ******
# ******************************************************

# S.O.L.I.D is an acronym. If we follow the 5 recommendations our code
#   will be easier to modify and maintain in the future

# S - Single Responsibility: Classes should have a singular purpose. If you try to do everything in onc class it
#                            gets cluttered and difficult to maintain.

# O - Open for extension, Closed for modification: A class should be able to be added onto at a later time,
#                            In general it should be generic enough that future situations don't cause you to
#                            change existing code in the class.

# L - Liskov Substitution: Any inherited class should be substitutable with its parent class. In our example above
#                            a Horse should be able to do whatever an Animal can do.

# I - Interface Segregation: This one basically says that if a child class doesn't fit in the parent class then
#                            make a new parent class. (For example if I wanted an animal like snail it might need
#                            its own parent class becuase it doesn't make noise and it doesnt really run).

# D - Dependency Inversion: Means that child classes can (and should) depend on their parent classes to define
#                            Their behavior. But a parent should never be dependent on a child class. For example,
#                            an Animal should not have any of their behavior defined by a snake because snake is
#                            an Animal. You could have a jaguar react to a snake, but not a generic Animal.
