'''
Script: main.py
By: NMC
Purpose: Main class to run the devices with the specified imports
Date: 26OCT23
'''
from devices import Firewall, Switch, LoadBalancer

# # Create a firewall instance
# firewall27 = Firewall("firewall27")
# # Configure it
# firewall27.configure_firewall()

# # Create a firewall instance
# firewall28 = Firewall("firewall28")
# # Verify a CRC
# firewall28.calculate_crc("dummy data")

# Create instances of different devices
firewall27 = Firewall("firewall27")
firewall28 = Firewall("firewall28")
switch1 = Switch("switch1")
load_balancer1 = LoadBalancer("lb1")

# Test their methods
firewall27.configure_firewall()
firewall28.calculate_crc("dummy data")
switch1.configure_switch()
load_balancer1.configure_load_balancer()