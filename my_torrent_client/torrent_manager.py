from peer_manager import Peer
# torrent_manager.py

class TorrentManager:
    def __init__(self, torrent_file):
        self.torrent_file = torrent_file
        self.peers = []

    def add_peer(self, peer):
        self.peers.append(peer)
        print(f"Peer added to torrent: {peer}")

    def remove_peer(self, peer):
        if peer in self.peers:
            self.peers.remove(peer)
            print(f"Peer removed from torrent: {peer}")

    def start_download(self):
        print(f"Starting download for {self.torrent_file}")
        # Aqui você adicionará a lógica de download

    def start_upload(self):
        print(f"Starting upload for {self.torrent_file}")
        # Aqui você adicionará a lógica de upload

# Testando o TorrentManager
if __name__ == "__main__":
    torrent_manager = TorrentManager("example.torrent")
    peer1 = Peer("192.168.1.1", 6881)

    torrent_manager.add_peer(peer1)
    torrent_manager.start_download()
    torrent_manager.start_upload()
    torrent_manager.remove_peer(peer1)
