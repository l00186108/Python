'''
TCPClient by: NMC
Send TCP packets to a particular address and port.
Alpha: 26OCT23
'''

# Import Modules.
import socket
import time
from datetime import datetime
import settings.tcp as settings

# Retrieving TCP settings from the 'settings' module
TCP_IP = settings.TCP["SERVER_TCP_IPv4"]
TCP_PORT = settings.TCP["SERVER_PORT"]

print(f'This is the TCP client, it will try to connect to a server at {TCP_IP}:{TCP_PORT} in the settings file.')
print('This script has no error handling, by design')

# Set Buffer Size for recieving packets.
BUFFER_SIZE = 1024
while True:
    print(f'Trying to open a socket to {TCP_IP}:{TCP_PORT}')
    # Creating a socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Creating Timstamp then converting it.
        message_text = f"ATU {datetime.now()}"
        message = message_text.encode('utf-8')
        # Connecting to Server IP address and Port.
        s.connect((TCP_IP, TCP_PORT))
        # Messaging the server
        s.send(message)
        print(f'Sent {message_text} to {TCP_IP}:{TCP_PORT}')
        # Recieve data from server.
        data = s.recv(BUFFER_SIZE)
        print('Server echoed:', data)
        time.sleep(1)