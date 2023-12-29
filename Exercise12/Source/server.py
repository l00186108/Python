# Import the 'socket' module
import socket
# Import the 'udp' module from the 'Network.settings' package
import Network.settings.udp as settings

# Retrieve the server's IPv4 address, port, and buffer size from the 'settings' module
UDP_IP = settings.UDP["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]
BUFFER_SIZE = 1024

# Print server information to the console
print(f'This is the UDP server, it will open a port at {UDP_IP}:{UDP_PORT} and begin listening')
print(f'Make sure the actual server IP address matches {UDP_IP} in the settings file')
print(f'Alerts will be saved to a file')
print('This script has error handling.')

# Create a UDP socket using the 'socket' module
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    try:
        # Enable broadcast mode for the socket
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # Bind socket to IP address and port
        s.bind((UDP_IP, UDP_PORT))
        print('Listening on', UDP_IP)
        # Start the infinite loop to continue listening for packets
        while True:
            # Recieve packets from the socket
            data, addr = s.recvfrom(BUFFER_SIZE)
            # Decode from bytes to string
            data = data.decode()
            # Split the received data into components using ',' as the delimiter
            sensor_id, timestamp, temperature = data.split(',')
            # Convert temperature to a integer for comparison
            temperature = int(temperature)
            # Check if the Temperature is less than 5
            if temperature <= 5:
                # Add the alert temperature text 
                alert_message = f"ALERT: Sensor ID {sensor_id} reports temperature below 5°C: {temperature}°C"
                print(alert_message)
                # Define the filename for the alert file
                alert_file = "alertsUnder5.txt"
                # Append the alert message to the alert file
                with open(alert_file, "a") as file:
                    file.write(f"Sensor ID: {sensor_id}, Timestamp: {timestamp}, Temperature: {temperature}\n")

            # Check if sensor is greater than 30
            elif temperature >= 30:
                alert_message = f"ALERT: Sensor ID {sensor_id} reports temperature above 30°C: {temperature}°C"
                print(alert_message)
                # Define the filename for the alert file
                alert_file = "alertsOver30.txt"
                # Append the alert message to the alert file
                with open(alert_file, "a") as file:
                    file.write(f"Sensor ID: {sensor_id}, Timestamp: {timestamp}, Temperature: {temperature}\n")
            # Otherwise just print out the sensor data to screen
            else:
                print(f"Received data from Sensor ID: {sensor_id}, Timestamp: {timestamp}, Temperature: {temperature}°C\n")
            # Define the filename for the log file based on the sensor ID
            log_file = f"Sensor{sensor_id}_logfile.txt"
            # Append to the log file
            with open(log_file, "a") as file:
                file.write(f"Sensor ID: {sensor_id}, Timestamp: {timestamp}, Temperature: {temperature}\n")
    # Handle exceptions and print an error message          
    except Exception as e:
        print(f"An error occurred: {e}")