'''
Script: plint1.py
By: NMC
Purpose: Pylint Tests.
Date: 12DEC23
''' 
# Note: Before running the tests, ensure that you have installed pylint by running "pip install pylint" in the terminal.

# Initializing variables
a = 1
b = 2
c = "JOR"

# printing the sum of integers a and b
print(a+b)

# Attempting to print the sum of integer a and an undefined variable B
# Uncommenting this line will cause a NameError
# print(a + B)

# Attempting to concatenate integer a with string c
# Uncommenting this line will cause a TypeError
# print(a + c)