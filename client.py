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
    print("Type \\q to quit.")
    while continueConversation:
    
        # Prompt user for input 
        message = input(">>>> ")
        
        # Limit messages to 900 bytes length 
        while len(message) > 900:
            print("\n")
            print("ERROR! Your message is too long. Type in something shorter please.")
            message = input(">>>> ")
        
        # close socket if \q is typed 
        if message == "\\q":
            # Inform user that the connection will close 
            print("You've decided to quit. Goodbye!")
            
            # Send closing message to the server, so the server can successfully close connection on its end 
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
            
            # Close connection if server has quit 
            if response.decode('ascii') == '\\q':
                print("Server has decided to quit. Closing the connection!")
                continueConversation = False 
                s.close()
            else:
                print("SERVER: {}".format(response.decode('ascii')))
            
        