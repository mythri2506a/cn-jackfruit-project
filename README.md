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



server.py → Server handling connections and message routing  
client.py → Combined client module supporting both publishing and subscribing  
generate_cert.py → Generates SSL certificate  
server.crt / server.key → SSL certificate files  

---



## 🔄 Client Design

The client-side functionality is combined into a single file:

- `client.py` supports both publishing and subscribing
- Users can choose to send messages or subscribe to topics
- This simplifies the architecture and improves usability


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
python server.py

### Step 2: Start Client
python client.py

Users can:
- Enter username
- Choose to publish messages
- Subscribe to topics
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
