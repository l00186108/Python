'''
Script: devices.py
By: NMC
Purpose: In any complex application, create a base class which will never be instantiated.
Date: 26OCT23
'''
# In any complex application, create a base class which will never be instantiated.
class Device():
    
    # Define a class object attribute, the same for any instance of the class
    pi = 3.142

    # Constructor, called whenever an instance of the class is created.
    def __init__(self) -> None:
        print("Running constructor for base class")
        # Create attributes and set initial values
        self.debug = False

    def run(self):
        raise NotImplementedError("This is an abstract class, do not instantiate")

    def calculate_crc(self, frame:str)->int: 
        print("Checking CRC from base")
        # Put real code in here, this is a dummy value for initial setup
        crc = 123456789
        return crc


"""
Child class Template by NMC
"""
# Create child class which can access the methods and properties of the base class
class Firewall(Device):

    # Constructor, called whenever an instance of the class is created.
    # Use parameter1 as a tag to identify the object
    def __init__(self, parameter1) -> None:
        # Call back to the parent class
        Device.__init__(self)
        print(f"Running constructor for {parameter1}")
        # Create attributes and set initial values
        self.parameter1 = parameter1
        self.test_message = ""
    
    def configure_firewall(self):
        print("Configuring Firewall")

    def calculate_crc(self, frame:str)->int: 
        print("Checking CRC from child")
        # Put real code in here, this is a dummy value for initial setup
        crc = 123456789
        return crc

# devices.py

class Switch(Device):
    def __init__(self, parameter1) -> None:
        Device.__init__(self)
        print(f"Running constructor for Switch {parameter1}")
        self.parameter1 = parameter1
        self.port_count = 24

    def configure_switch(self):
        print("Configuring Switch")

class LoadBalancer(Device):
    def __init__(self, parameter1) -> None:
        Device.__init__(self)
        print(f"Running constructor for Load Balancer {parameter1}")
        self.parameter1 = parameter1
        self.algorithm = "Round Robin"

    def configure_load_balancer(self):
        print("Configuring Load Balancer")