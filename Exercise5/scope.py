my_string = "global"

def my_function():
    my_string = "enclosing"
    def nested_function():
        my_string = "local"
        print(my_string)
    nested_function()
    return my_string

# Print the variable my_string
print(my_string)
# Print the output of the function, my_function
print(my_function())

my_string = "global"

def my_function():
    global my_string
    print(f"At the moment, my_string is: {my_string}")
    my_string = "mangled!"

my_function()
print(f"Now the global value of my_string is: {my_string}")