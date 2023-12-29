# Import the 'socket' module
import socket
# Import the 'time' module
import time
# Import the 'random' module
import random
# Import the 'udp' module from the 'Network.settings' package
import Network.settings.udp as settings
# Import the 'datetime' module for timestamp creation
from datetime import datetime


# Retrieve the server's IPv4 address and port from the 'settings' module
UDP_IP = settings.UDP["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]

# Print client information to the console
print(f'This is the UDP client, it will try to connect to a server at {UDP_IP}:{UDP_PORT} in the settings file.')
print('This script has error handling.')
# Start an infinite loop to try to connect
while True:
    # Create a UDP socket using the socket module
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            # Set the sensor ID to '1'
            sensor_id = "1"
            # Simulated temperature reading with random number generator
            temperature = int(random.uniform(0, 40)) 
            # Get the current timestamp in a certain format 
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Formatted timestamp
            # Create a string with sensor ID, Timestamp and temperature 
            data = f"{sensor_id},{timestamp},{temperature}"
            # Encode the data from string into bytes
            message = data.encode('utf-8')
            # Send the data to the Server
            s.sendto(message, (UDP_IP, UDP_PORT))
            # Pause and Send data every 10 seconds
            time.sleep(10)  
        except Exception as e:
            # Handle exception and print it error message
            print(f"An error occurred: {e}")