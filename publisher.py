# Publisher module
# Add publisher implementation here
import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Enter publisher name: ")
client.send(username.encode())

print(client.recv(1024).decode())

while True:
    topic = input("Topic: ")
    message = input("Message: ")

    msg = f"PUBLISH {topic} {message}"

    client.send(msg.encode())