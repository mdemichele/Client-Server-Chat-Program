# SOURCE: https://docs.python.org/3/library/socket.html
import socket 

# Declare variables for the host name and port number 
HOST = "localhost"
PORT = 10892

# Create a listening socket 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    # Bind socket to host and port 
    s.bind((HOST, PORT))
    print("Listening for connections on port {}...".format(PORT))
    print("Type \q to quit.")
    # Listen for one connection at a time 
    s.listen(1)
        
    # Accept a connection (conn is the new socket object)
    conn, addr = s.accept()
    
    continueConversation = True 

    while continueConversation:
        # Read the message from the socket 
        data = conn.recv(1024)
        print("CLIENT: {}".format(data.decode('ascii')))
        
        # Prompt response from server 
        response = input(">>>> ")
        
        # Check that the message is less than 1024 bytes 
        while len(response) > 900:
            print("\n")
            print("ERROR! Your message is too long. Type in something shorter please.")
            response = input(">>>> ")
        
        # Close conn socket object and exit loop
        if response == "\q":
            byteResponse = bytes("Server has left the conversation...Quit by typing \q.", 'ascii')
            conn.sendall(byteResponse)
            continueConversation = False  
            conn.close()
        # Send response back to client
        else:
            byteResponse = bytes(response, 'ascii')
            conn.sendall(byteResponse)
        