# peer_manager.py

class Peer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __repr__(self):
        return f"{self.ip}:{self.port}"

class PeerManager:
    def __init__(self):
        self.peers = []

    def add_peer(self, peer):
        self.peers.append(peer)
        print(f"Peer added: {peer}")

    def remove_peer(self, peer):
        if peer in self.peers:
            self.peers.remove(peer)
            print(f"Peer removed: {peer}")

    def get_peers(self):
        return self.peers

# Testando o PeerManager
if __name__ == "__main__":
    peer_manager = PeerManager()
    peer1 = Peer("192.168.1.1", 6881)
    peer2 = Peer("192.168.1.2", 6882)

    peer_manager.add_peer(peer1)
    peer_manager.add_peer(peer2)
    print("Current peers:", peer_manager.get_peers())

    peer_manager.remove_peer(peer1)
    print("Current peers:", peer_manager.get_peers())
