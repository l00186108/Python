'''
UDPServer by: NMC
Listens for packets on a particular address and port.
Alpha: 13FEB22
'''
# Import modules. 
import socket
import settings.udp as settings

# Retrieve the server's IPv4 address, port, and buffer size from the 'settings' module
UDP_IP = settings.UDP["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]
BUFFER_SIZE = 1024

# Print INfo to Console.
print(f'This is the UDP server, it will open a port at {UDP_IP}:{UDP_PORT} and being listening')
print(f'Make sure the actual server IP address matches {UDP_IP} in the settings file')
print('This script has no error handling, by design')

# Create a UDP socket using the 'socket' module
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # Enable broadcast mode for the socket
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # Bind socket to IP address and port
    s.bind( (UDP_IP, UDP_PORT) )
    # Print Info of Port.
    print('Listening on', UDP_IP)
    # Start the infinite loop to continue listening for packets
    while True:
        # Recieve packets from the socket
        data, addr = s.recvfrom(BUFFER_SIZE)
        # Decode from bytes to string
        data = data.decode()
        print(addr, data)