# SOURCE: https://docs.python.org/3/library/socket.html
import socket 

HOST = "localhost"
PORT = 10023

# Create a new socket object for use
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to specified host and port 
    s.connect((HOST, PORT))
    
    # Send GET request 
    s.sendall(b'Are we connected?')
    print("Message Sent")
    # Receive the message back from the server 
    data = s.recv(1024)
    
# Print the resulting message from the server in the terminal 
print(data.decode('ascii'))