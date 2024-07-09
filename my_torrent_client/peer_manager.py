# peer_manager.py
class PeerManager:
    def __init__(self):
        self.peers = []

    def add_peer(self, peer):
        self.peers.append(peer)

    def remove_peer(self, peer):
        if peer in self.peers:
            self.peers.remove(peer)

    def get_peers(self):
        return self.peers
