'''
Copyright (c) 2014 Chet Hosmer

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.

'''
# 
# Setup a Simple listening Socket
# and obtain one connection
# send a message to the connector
# and then close the connection
#

import socket

# Create Socket

myServerSocket = socket.socket()

# Get my local host address

localHost = socket.gethostname()

# Specify a local Port to accept connections on

localPort = 5555

# Bind mySocket to localHost and the specified localPort

myServerSocket.bind((localHost, localPort))

# Begin Listening for connections

myServerSocket.listen(1)

# Wait for a connection request
# Note this is a synchronous Call
# meaning the program will halt until
# a connection is received.
# Once a connection is received
# we will accept the connection and obtain the 
# ipAddress of the connector

print 'Python-Forensics .... Waiting for Connection Request'

conn, clientInfo = myServerSocket.accept()

# Print a message to indicate we have received a connection

print 'Connection Received From: ', clientInfo

# Send a message to connector using the connection obj 'conn'

conn.send('Connection Confirmed: '+ 'IP: ' + clientInfo[0] + '  Port: ' + str(clientInfo[1]))


          
    
