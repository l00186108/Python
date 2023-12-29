'''
Script: oo1.py
By: NMC
Purpose: Simple Class by JOR, by convention, use camel case to name classes
Date: 25OCT23
'''

# Create a class 
class JORzClass():
    
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting):
        print("Running constructor for JORzClass")
        # Create attributes and set initial values
        self.message = my_greeting

    def my_method(self):
        print(self.message)

my_class1 = JORzClass("Morning JOR!")
my_class1.my_method()
print(type(my_class1))

# oo1.py

# Create a second class
class MyClass2:
    def __init__(self, my_message):
        print("Running constructor for MyClass2")
        self.message = my_message

    def my_method(self):
        print(self.message)

# Create an instance of MyClass1
my_class1 = MyClass1("Morning MyClass1!")
my_class1.my_method()

# Create an instance of MyClass2
my_class2 = MyClass2("Good evening from MyClass2!")
my_class2.my_method()