# connection_manager.py
import socket
import threading

class ConnectionManager:
    def __init__(self, peer_id, port=6881):
        self.peer_id = peer_id
        self.port = port
        self.connections = []

    def start_server(self):
        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()

    def run_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', self.port))
            s.listen()
            print(f"Server listening on port {self.port}")
            while True:
                conn, addr = s.accept()
                self.connections.append(conn)
                threading.Thread(target=self.handle_client, args=(conn, addr)).start()

    def handle_client(self, conn, addr):
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received from {addr}: {data.decode()}")
            conn.sendall(data)
        conn.close()
        print(f"Connection with {addr} closed")

    def connect_to_peer(self, ip, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            self.connections.append(s)
            threading.Thread(target=self.handle_client, args=(s, (ip, port))).start()

    def send_message(self, message):
        for conn in self.connections:
            conn.sendall(message.encode())
