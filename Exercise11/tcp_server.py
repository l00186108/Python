'''
TCPServer by: NMC
Listens for packets on a particular address and port.
Alpha: 26OCT23
'''

# Import Modules.
import socket
import settings.tcp as settings

# Retrieving TCP settings from the 'settings' module
TCP_IP = settings.TCP["SERVER_TCP_IPv4"]
TCP_PORT = settings.TCP["SERVER_PORT"]
BUFFER_SIZE = 1024

print(f'This is the TCP server, it will open a port at {TCP_IP}:{TCP_PORT} and being listening')
print(f'Make sure the actual server IP address matches {TCP_IP} in the settings file')
print('This script has no error handling, by design')

# Now trying to connect to the server
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind the socket to IP address and port.
        s.bind((TCP_IP, TCP_PORT))
        print(f'Bound to {TCP_IP}:{TCP_PORT}')
        # Listen for incoming connections continuously
        while True:
            # Allow the maximum number of connections
            s.listen(1)
            # Accepting the connection
            conn, addr = s.accept()
            print(f'Connection address: {addr}')
            data = conn.recv(BUFFER_SIZE).decode()
            print(data)
            conn.send(data.encode())
# Handle socket errors 
except socket.error as e:
    print(f'Error: {e}')