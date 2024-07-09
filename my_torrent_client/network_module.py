# network_module.py
import socket

class NetworkModule:
    def __init__(self):
        self.connections = {}

    def connect_to_peer(self, ip, port):
        try:
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn.connect((ip, port))
            self.connections[(ip, port)] = conn
            print(f"Connected to {ip}:{port}")
            return True
        except Exception as e:
            print(f"Failed to connect to {ip}:{port} - {e}")
            return False

    def disconnect_from_peer(self, ip, port):
        conn = self.connections.get((ip, port))
        if conn:
            conn.close()
            del self.connections[(ip, port)]
            print(f"Disconnected from {ip}:{port}")
            return True
        else:
            print(f"No active connection to {ip}:{port}")
            return False

    def send_data(self, ip, port, data):
        conn = self.connections.get((ip, port))
        if conn:
            conn.sendall(data.encode())
            print(f"Data sent to {ip}:{port}: {data}")
        else:
            print(f"No active connection to {ip}:{port}")

    def receive_data(self, ip, port, buffer_size=1024):
        conn = self.connections.get((ip, port))
        if conn:
            data = conn.recv(buffer_size).decode()
            print(f"Data received from {ip}:{port}: {data}")
            return data
        else:
            print(f"No active connection to {ip}:{port}")
            return None

# Testando o Network Module
if __name__ == "__main__":
    network_module = NetworkModule()
    if network_module.connect_to_peer("192.168.1.1", 6881):
        network_module.send_data("192.168.1.1", 6881, "Hello, peer!")
        network_module.receive_data("192.168.1.1", 6881)
        network_module.disconnect_from_peer("192.168.1.1", 6881)
