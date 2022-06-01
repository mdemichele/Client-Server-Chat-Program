# SOURCE: https://docs.python.org/3/library/socket.html
import socket 

HOST = "localhost"
PORT = 10892

# Create a new socket object for use
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to specified host and port 
    s.connect((HOST, PORT))
    
    continueConversation = True 
    print(f'Connected to {HOST} at port {PORT}.')
    print("Type \q to quit.")
    while continueConversation:
    
        # Prompt user for input 
        message = input(">>>> ")
        
        # Limit messages to 1024 bytes length 
        while len(message) > 900:
            print("\n")
            print("ERROR! Your message is too long. Type in something shorter please.")
            message = input(">>>> ")
        
        # close socket if \q is typed 
        if message == "\q":
            message = "The Client has left the conversation. Type \q to quit."
            byteMessage = bytes(message, 'ascii')
            s.sendall(byteMessage)
            continueConversation = False 
            s.close()
            
        # Send message to server and receive response back 
        else:
            byteMessage = bytes(message, 'ascii')
            s.sendall(byteMessage)
        
            # Receive response back from the server 
            response = s.recv(1024)
            print("SERVER: {}".format(response.decode('ascii')))
        