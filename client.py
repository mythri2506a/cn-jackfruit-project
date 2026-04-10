import socket
import ssl
import threading
import time

HOST = "127.0.0.1"
PORT = 5000


def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                received_time = time.time()

                parts = msg.split()

                try:
                    timestamp = float(parts[-1])
                    clean_msg = " ".join(parts[:-1])

                    print("\n\n" + clean_msg)

                    latency = received_time - timestamp
                    print(f"Latency: {latency:.4f} sec")

                except:
                    print("\n\n" + msg)

                print("\n> ", end="", flush=True)

        except:
            break


# SSL setup
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_client = context.wrap_socket(client)

secure_client.connect((HOST, PORT))


# Username
username = input("Enter username: ")
secure_client.send(username.encode())

print(secure_client.recv(1024).decode())


# Start receiver thread
threading.Thread(target=receive_messages, args=(secure_client,), daemon=True).start()


# Print menu ONCE
print("\nCommands:")
print("SUBSCRIBE <topic> <days>")
print("UNSUBSCRIBE <topic>")
print("PUBLISH <topic> <message>")
print("LIST")
print("EXIT")


# Command loop
while True:
    cmd = input("\n> ")

    if cmd == "EXIT":
        break

    if cmd.startswith("PUBLISH"):
        timestamp = time.time()
        cmd = cmd + " " + str(timestamp)

    secure_client.send(cmd.encode())