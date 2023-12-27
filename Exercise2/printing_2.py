'''
Script: printing_2.py
By: NMC
Purpose: Printing the first 2 characters of a string and other printable characters
Date: 10SEPT23
'''
#!/usr/bin/python3

__author__ = "Niall McCann"
__contact__ = "L00186108@atu.ie"
__copyright__ = "Copyright $YEAR, JOR"
__date__ = "10SEPT23"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "Production"
__version__ = "12.0"
# At the end of code it print out the message "Good morning, NM Breakfast!"
print("Good morning, NMC", end = " ")
print("Breakfast!\n")

print("Good morning, NMC\nWould you like some Breakfast\n")
# At the end of code it should be 47 characters long
a = "Good morning, NMC\nWould you like some Breakfast?"
print(len(a))

my_string = "Almost finished now folks!"
my_upper = my_string.upper()
my_lower = my_string.lower()
print(f"Original string: {my_string}")
print(f"Uppercased string: {my_upper}")
print(f"Lowercased string: {my_lower}\n")

text_with_spaces = "    Niall McCann        "
text_without_spaces = text_with_spaces.strip()
print("Original = {}".format(text_with_spaces))
print(text_without_spaces)

print("\n")
text_with_brackets = "(Niall McCann)"
text_without_brackets = text_with_brackets.strip('(')
text_without_brackets = text_without_brackets.strip(')')
print("Original = {}".format(text_with_brackets))
print(text_without_brackets)