# Subscriber module
# Add subscriber implementation here
import socket
import threading

HOST = "127.0.0.1"
PORT = 5000


def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            print(msg)
        except:
            break


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Enter username: ")
client.send(username.encode())

print(client.recv(1024).decode())

thread = threading.Thread(target=receive_messages, args=(client,))
thread.start()

while True:
    topic = input("Enter topic to subscribe: ")
    msg = f"SUBSCRIBE {topic}"
    client.send(msg.encode())