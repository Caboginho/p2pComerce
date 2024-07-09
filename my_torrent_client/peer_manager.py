# peer_manager.py
from network_module import NetworkModule

class Peer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.is_connected = False

    def __repr__(self):
        return f"{self.ip}:{self.port} - {'Connected' if self.is_connected else 'Disconnected'}"

class PeerManager:
    def __init__(self):
        self.peers = []
        self.network_module = NetworkModule()

    def add_peer(self, ip, port):
        peer = Peer(ip, port)
        self.peers.append(peer)
        print(f"Peer added: {peer}")

    def remove_peer(self, ip, port):
        peer_to_remove = None
        for peer in self.peers:
            if peer.ip == ip and peer.port == port:
                peer_to_remove = peer
                break
        if peer_to_remove:
            if peer_to_remove.is_connected:
                self.network_module.disconnect_from_peer(peer_to_remove.ip, peer_to_remove.port)
            self.peers.remove(peer_to_remove)
            print(f"Peer removed: {peer_to_remove}")
        else:
            print(f"Peer {ip}:{port} not found")

    def connect_peer(self, ip, port):
        for peer in self.peers:
            if peer.ip == ip and peer.port == port:
                if self.network_module.connect_to_peer(ip, port):
                    peer.is_connected = True
                return
        print(f"Peer {ip}:{port} not found")

    def disconnect_peer(self, ip, port):
        for peer in self.peers:
            if peer.ip == ip and peer.port == port:
                if self.network_module.disconnect_from_peer(ip, port):
                    peer.is_connected = False
                return
        print(f"Peer {ip}:{port} not found")

    def get_peers(self):
        return self.peers

# Testando o PeerManager
if __name__ == "__main__":
    peer_manager = PeerManager()
    peer_manager.add_peer("192.168.1.1", 6881)
    peer_manager.add_peer("192.168.1.1", 6882)
    print("Current peers:", peer_manager.get_peers())

    peer_manager.connect_peer("192.168.1.1", 6881)
    peer_manager.disconnect_peer("192.168.1.1", 6881)
    peer_manager.remove_peer("192.168.1.1", 6881)
    print("Current peers:", peer_manager.get_peers())
