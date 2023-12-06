'''
my_list = ["one", "two", "three"]
my_tuple = ("one", "two", "three")
print(type(my_list))
print(type(my_tuple))
'''

my_tuple = ("one", "two", "three", "one")
#How many times does "One" appear in the tuple
print(my_tuple.count("one"))
#At what position in the tuple can I first find "one"
print(my_tuple.index("one"))