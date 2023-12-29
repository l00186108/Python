'''
Script: oo2.py
By: NMC
Purpose: Simple Class 
Date: 25OCT23
'''

class MyTemplate():
    # # Constructor, called whenever an instance of the class is created.
    # def __init__(self) -> None:
    #     print("Constructor ran")
    # Define class object attributes, they are the same for all instances of the class
    class_object_attribute1 = 6378137
    class_object_attribute2 = 6356752
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        print("Constructor ran")
        # Take in an argument and assign it to a meaningful attribute name
        self.attr1 = attribute1
        self.attr2 = attribute2

    def my_method1(self):
        if self.attr2:
            print(f"Good morning {self.attr1}")
        else:
            print(f"No greeting {self.attr1}")

    def my_method2(self, my_name:str):
        if self.attr2:
            print(f"Good morning {my_name}")
        else:
            print(f"No greeting {my_name}")

# Instantiate the class
#my_object = MyTemplate()
# Instantiate the class and pass values for the constructor
my_object = MyTemplate("John", True)

# Check the type of the object
print(type(my_object))

# Access and print the attribute 'attr1' of the object
print("Name: " + my_object.attr1)

# Access and print the attribute 'attr1' again with a different message
print("Name of the User is  " + my_object.attr1)

# Access the class object attributes
print(my_object.class_object_attribute1, my_object.class_object_attribute2)

# Call the 'my_method1' method
my_object.my_method1()

# Call the 'my_method2' method with a custom name
my_object.my_method2("Slartibartfast")