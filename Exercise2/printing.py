'''
Script: printing.py
By: NMC
Purpose: More efficient way to print something
Date: 10SEPT23
'''
#! /usr/bin/python3
#To break up code \n after the sentence

a = "Would you like breakfast!\n"
print("Good morning Niall, "  + a)

a = 5
b = 12
print("Good Monring, Niall. For breakfast, would you like {}?".format("Fruit"))
print("We have {} apples, {} bananas and a total of {} pieces available\n".format(a, b, a + b))

a = "Good"
b = "NMC"
c = "morning"   
print("Message is: {first} {second} {third}, {second}\n".format(first = a, second = c, third = b))

Number = 12345
Divisor = 333
Result = Number / Divisor
print("Result of {} divided by {} is {}".format(Number, Divisor, Result))
print("Limiting to a float with 4 decimal places would give {r:1.4f}\n".format(r = Result))

Number = 12345
Divisor = 333
Result = Number / Divisor
print("Result of {Number} divided by {Divisor} is {Result}\n")