import socket as soc

# Create new socket
s = soc.socket()

# Define port
port = 33213

# Connect with server
s.connect(('localhost', port))

print(s.recv(1024).decode())

# Print confirmation message
print("Connection established.")



