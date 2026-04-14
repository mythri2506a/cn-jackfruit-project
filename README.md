# CN Jackfruit Project – Publish-Subscribe Notification System

## 📌 Project Overview

This project implements a **Publish–Subscribe Notification System** using Python socket programming.

It allows multiple clients to communicate through a central server using topic-based messaging.

---

## 🛠 Technologies Used

* Python
* Socket Programming (TCP)
* Threading
* SSL/TLS (Secure Communication)

---

## ⚙️ Features

* Multi-client support
* Topic-based publish–subscribe model
* Real-time message delivery
* SSL/TLS secure communication
* Efficient message routing

---

## 📂 Project Structure

server.py → Server handling connections and routing
client.py → Base client communication module
publisher.py → Sends messages to topics
subscriber.py → Subscribes and receives messages
generate_cert.py → Generates SSL certificates
server.crt / server.key → SSL certificate files

---

## 🔄 Client Design

The client-side is modular:

* `client.py` handles basic socket connection logic
* `publisher.py` sends messages
* `subscriber.py` receives messages

This improves modularity and code reuse.

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/mythri2506a/cn-jackfruit-project.git
cd cn-jackfruit-project
```

### 2. Install dependencies

```bash
pip install cryptography
```

### 3. Generate SSL certificates (if not present)

```bash
python generate_cert.py
```

---

## ▶️ How to Run

### Step 1: Start Server

```bash
python server.py
```

---

### Step 2: Start Subscriber

Open a new terminal:

```bash
python subscriber.py
```

Enter username and topic.

---

### Step 3: Start Publisher

Open another terminal:

```bash
python publisher.py
```

Enter publisher name, topic, and message.

---

## 🔄 Example

Subscriber:
Alice → subscribes to sports

Publisher:
Bob → publishes "Match started"

Output:
[sports] Bob: Match started

---

## 🔐 Security

Communication is secured using **SSL/TLS encryption**.

---

## ⚡ Optimization

* Dictionary-based lookup (O(1))
* Topic-based routing (no unnecessary broadcasting)
* Multi-threading for concurrency

---

## ⚠️ Limitations

* No unsubscribe feature
* No message storage
* Duplicate subscriptions possible

---

## 📌 Future Improvements

* Add unsubscribe functionality
* Prevent duplicate subscriptions
* Add database support
* Add authentication

---

## 👨‍💻 Author

Mythri
CN Jackfruit Project
