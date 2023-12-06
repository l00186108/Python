'''
iterable_variable = [1,2,3,4,5,6]

for item in iterable_variable:
    # For each item, execute this code block
    print(item)

'''
'''
iterable_variable = [1,2,3,4,5,6]

for item in iterable_variable:
    if item %2 != 0:
        print(item)
'''
'''
iterable_variable = [1,2,3,4,5,6]
total = 0

for item in iterable_variable:
    total = total + item

print(total)
'''
# Define a string to iterate over
for this_letter in "John ORaw":
    # Specify which letter to test for
    if this_letter == "J":
        # Found the test letter
        print(f"Woo hoo, found a {this_letter}!")
        # Exit the current loop
        break
    else:
        # Didn't find the test letter
        print(f"Aww man, I didn't want a {this_letter}!")
