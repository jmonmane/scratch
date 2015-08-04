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
import socket

MAX_BUFFER = 1024
# Create a Socket

myClientSocket = socket.socket()

# Get my local host address

localHost = socket.gethostname()

# Specify a local Port to attempt a connection

localPort = 5555

# Attempt a connection to my localHost and localPort

myClientSocket.connect((localHost, localPort))

# If connection is successful, wait for a reply

msg = myClientSocket.recv(MAX_BUFFER)
print msg

myClientSocket.close()




