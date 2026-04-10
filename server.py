import socket
import ssl
import threading
import time

HOST = "127.0.0.1"
PORT = 5000

# topic -> {client: expiry_time}
topics = {}

# socket -> username
clients = {}

lock = threading.Lock()

# 🔥 Throughput variables
message_count = 0
start_time = time.time()


# 🔹 Remove expired subscriptions
def clean_expired():
    current_time = time.time()

    with lock:
        for topic in list(topics.keys()):
            for client, expiry in list(topics[topic].items()):
                if current_time > expiry:
                    del topics[topic][client]


def handle_client(conn, addr):
    global message_count, start_time

    print(f"[CONNECTED] {addr}")

    try:
        # Receive username
        username = conn.recv(1024).decode()
        clients[conn] = username

        conn.send("CONNECTED".encode())
        print(f"[ACTIVE CLIENTS]: {len(clients)}")

        while True:
            msg = conn.recv(1024).decode()
            if not msg:
                break

            parts = msg.split(" ", 2)
            command = parts[0]

            # 🔹 SUBSCRIBE <topic> <days>
            if command == "SUBSCRIBE":
                topic = parts[1]
                days = int(parts[2]) if len(parts) > 2 else 1

                expiry_time = time.time() + (days * 86400)

                with lock:
                    if topic not in topics:
                        topics[topic] = {}
                    topics[topic][conn] = expiry_time

                conn.send(f"Subscribed to {topic} for {days} days".encode())

            # 🔹 UNSUBSCRIBE <topic>
            elif command == "UNSUBSCRIBE":
                topic = parts[1]

                with lock:
                    if topic in topics and conn in topics[topic]:
                        del topics[topic][conn]

                conn.send(f"Unsubscribed from {topic}".encode())

            # 🔹 PUBLISH <topic> <message> <timestamp>
            elif command == "PUBLISH":
                topic = parts[1]

                message_parts = parts[2].split()
                timestamp = float(message_parts[-1])
                message = " ".join(message_parts[:-1])

                clean_expired()

                with lock:
                    if topic in topics:
                        for subscriber in list(topics[topic].keys()):
                            try:
                                subscriber.send(
                                    f"[{topic}] {clients[conn]}: {message} {timestamp}".encode()
                                )
                            except:
                                pass
                message_count += 1
                elapsed_time = time.time() - start_time

                if elapsed_time > 0:
                    throughput = message_count / elapsed_time
                    print(f"[THROUGHPUT]: {throughput:.2f} msgs/sec")

            # 🔹 LIST
            elif command == "LIST":
                with lock:
                    topic_list = ", ".join(topics.keys())

                conn.send(f"Topics: {topic_list}".encode())

            else:
                conn.send("INVALID_COMMAND".encode())

    except:
        pass

    finally:
        conn.close()

        with lock:
            if conn in clients:
                del clients[conn]

        print(f"[DISCONNECTED] {addr}")
        print(f"[ACTIVE CLIENTS]: {len(clients)}")


def start_server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    secure_server = context.wrap_socket(server, server_side=True)

    print("[SERVER STARTED - WITH THROUGHPUT]")

    while True:
        conn, addr = secure_server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


start_server()