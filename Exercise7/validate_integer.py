'''
Script: validate_integer.py
By: NMC
Purpose: Create a file and write some text to it. Then function returns a string representing the result of endurance validation
Date: 2OCT23
'''
from re import A

# def validate_integer():
#     # Loop forever
#     while True:
#         try:
#             user_input = int(input("Enter an integer value: "))
#         except:
#             # Bad value, 
#             print("Error")
#             continue
#         else:
#             print("Valid input")
#             # Good value, exit the loop
#             break
#         finally:
#             # Continue
#             print("This message shows every time, regardless of the programme flow")
    

# validate_integer()

def calculate_endurance(fuel, fuel_consumption):
    try:
        if fuel_consumption == 0:
            raise ValueError("Fuel consumption cannot be zero")
        
        endurance = fuel / fuel_consumption
        return endurance
    except ZeroDivisionError:
        return "Division by zero error. Fuel consumption cannot be zero."
    except ValueError as e:
        return str(e)
    except Exception as e:
        return "An error occurred: " + str(e)

# Example usage:
fuel_litres = 100.0
fuel_consumption_per_minute = 0.0

endurance = calculate_endurance(fuel_litres, fuel_consumption_per_minute)
print("Remaining Endurance:", endurance)


# Take an input number as a string and convert it to an integer
my_value = int(input("Enter an integer greater than 0 :"))

if my_value <= 0:
    raise Exception("Values must be > 0")
else:
    print("Validation checks passed")