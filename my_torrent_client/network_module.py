# network_module.py
import socket

class NetworkModule:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_peer(self, ip, port):
        try:
            self.socket.connect((ip, port))
            print(f"Connected to {ip}:{port}")
        except Exception as e:
            print(f"Failed to connect to {ip}:{port} - {e}")

    def send_data(self, data):
        self.socket.sendall(data.encode())
        print(f"Data sent: {data}")

    def receive_data(self, buffer_size=1024):
        data = self.socket.recv(buffer_size).decode()
        print(f"Data received: {data}")
        return data

# Testando o Network Module
if __name__ == "__main__":
    network_module = NetworkModule()
    network_module.connect_to_peer("localhost", 6881)
    network_module.send_data("Hello, peer!")
    network_module.receive_data()
