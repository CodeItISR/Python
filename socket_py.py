# ip : 0-255    253.18.124.1
# port : 0 - 2^16
#       0 - 1023 saved ports , Example : 22 ssh , 80 http
#       1024 - 65535

import socket

# Create a socket object
server_socket = socket.socket()

# Get the local host ip
host = socket.gethostname()

# Bind the ip with the port
server_socket.bind((host, 20000))

# queue of 5 connection
server_socket.listen(5)

while (True):
    # Set the connection
    # c as a client socket object , addr as the ip and port from client
    c, addr = server_socket.accept()
    print('Got connection from : ' + str(addr))

    # Wait to receve a message, decode it from byte to string
    message = c.recv(1024)
    message = 'Hello ' + message.decode('UTF-8')

    print('Sending ' + message)
    # Send the message and encode it
    c.send(message.encode('UTF-8'))

    # close the connection
    c.close()

# close the server connection
server_socket.close()

#==========================
# Client

import socket

client_socket = socket.socket()

host = socket.gethostname()

# Connect to the local host ip in port 20000
client_socket.connect((host, 20000))

message = input('Please enter your name : ')

client_socket.send(message.encode('UTF-8'))

message = (client_socket.recv(1024)).decode('UTF-8')
print(message)

client_socket.close()

