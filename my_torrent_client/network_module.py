# network_module.py
import socket

class NetworkModule:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_peer(self, ip, port):
        self.socket.connect((ip, port))

    def send_data(self, data):
        self.socket.sendall(data)

    def receive_data(self, buffer_size=1024):
        return self.socket.recv(buffer_size)
