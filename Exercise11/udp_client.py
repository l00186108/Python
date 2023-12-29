'''
UDPClient by: NMC
Send UDP packets to a particular address and port.
Alpha: 26OCT23
'''

# Import moduleS
import socket
import time
from datetime import datetime
import settings.udp as settings

# Retrieve the server's IPv4 address and port from the 'settings' module
UDP_IP = settings.UDP["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]

# Print client information to the console
print(f'This is the UDP client, it will try to connect to a server at {UDP_IP}:{UDP_PORT} in the settings file.')
print('This script has no error handling, by design')

# Start an infinite loop to try to connect
while True:
    # Create a UDP socket using the socket module
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # Set socket option to allow broadcast
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # Get the current timestamp in a certain format 
        message_text = f"ATU {datetime.now()}"
        message = message_text.encode('utf-8')
        # Send the data to the Server ip address and port
        s.sendto(message, (UDP_IP, UDP_PORT))
        print(f'Sent {message_text}')
        # Delay before the next iteration
        time.sleep(1)