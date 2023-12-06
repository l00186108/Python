my_list = []
my_string = "Morning Folks!"
for letter in my_string:
    my_list.append(letter)

print(my_list)

#Produces the same outcome from different code
my_string = "Morning Folks!"
my_list = [letter for letter in my_string]
print(my_list)

my_list = [number for number in range(0,20)]
print(my_list)

my_list = [number * 10 for number in range(0,20)]
print(my_list)

my_list = [number * 10 for number in range(0,20) if number < 10]
print(my_list)

conversion = 0.3048
my_depth_in_feet = [12.3, 13.8, 15.3, 12.1, 8.8]
my_depth_in_meters = [(round(depth * conversion, 2)) for depth in my_depth_in_feet] 
print(my_depth_in_meters)