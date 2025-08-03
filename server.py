import socket

s = socket.socket()

print("Socket created.")

s.bind(('localhost', 9900))

s.listen(3)

print("Waiting for connection.")

while True:
    c, address = s.accept()
    name = c.recv(1024).decode()

    print(f"Connected to {address} with {name}")

    c.send(bytes(f"Welcome to demo, {name}", "utf-8"))

    c.close()

    print("Connection closed.")
