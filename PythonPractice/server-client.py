import socket

class main:

    # Create socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")

    # Create port
    port = 33213

    # bind the port
    s.bind(('localhost', port))

    # Print confirmation message.
    print("Socket bound successfully.")

    # Listen for client response
    s.listen(5)

    # While loop until false
    while True:
        c, address = s.accept()
        print("Connection established with ", address)

        c.send(bytes("You are officially connected", 'utf-8'))

        # Terminate connection
        c.close()



