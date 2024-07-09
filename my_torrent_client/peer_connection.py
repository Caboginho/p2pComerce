# peer_connection.py
import socket
import threading

class PeerConnection:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = None
        self.connected = False

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip, self.port))
        self.connected = True
        print(f"Connected to peer {self.ip}:{self.port}")

    def send_message(self, message):
        if not self.connected:
            self.connect()
        self.sock.sendall(message.encode())
        print(f"Sent message to {self.ip}:{self.port}: {message}")

    def receive_message(self):
        if not self.connected:
            self.connect()
        response = self.sock.recv(1024).decode()
        print(f"Received message from {self.ip}:{self.port}: {response}")
        return response

    def close(self):
        if self.sock:
            self.sock.close()
        self.connected = False
        print(f"Disconnected from peer {self.ip}:{self.port}")

# Testando a PeerConnection
if __name__ == "__main__":
    peer_conn = PeerConnection("localhost", 6881)
    peer_conn.connect()
    peer_conn.send_message("Hello, peer!")
    response = peer_conn.receive_message()
    print(f"Response: {response}")
    peer_conn.close()
