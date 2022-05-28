# SOURCE: https://docs.python.org/3/library/socket.html
import socket 

# Declare variables for the host name and port number 
HOST = "localhost"
PORT = 10023

# Create a listening socket 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    # Bind socket to host and port 
    s.bind((HOST, PORT))
    
    # Let the server listen for new connections indefinitely
    while True:
        # Listen for one connection at a time 
        s.listen(1)
        print("Listening for connections on port {}...".format(PORT))
        # Accept a connection (conn is the new socket object)
        conn, addr = s.accept()
        
        # Read the socket request 
        data = conn.recv(1024)
        print("RECIEVED <<<<<<<<<")
        print(data.decode('ascii'))
        
        # Close conn socket object 
        conn.close()