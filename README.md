# Client Server Chat Program
A client-server chat program. The purpose of the project is to explore the process of transmitting data via a socket connection. 

The project is built in Python and utilizes the socket module. There is one server, which communicates with only one client at a time. The client and server may communicate as long as the socket connections are open. 

# Lessons Learned 
- Learned about communication between a server and client using sockets 
- Learned how to create a client-server connection using Python 

# User Guide

To start the server, type `python server.py`. The server should start and wait for the message for the client. While the server is waiting, the program will simply hang there.

To start the client, open a new terminal window and type `python client.py`. The client should start and will ask for input. The input prompt will be `>>>>`. Enter text directly after the prompt. 

To quit the program, type `\q` in either the server or the client program when it is their turn to write input.

# TODOs: 
- Allow server to exit even if the client doesn't input anything. 
- input validation. Right now, the program isn't safe at all. Validation checks are definitely necessary. 