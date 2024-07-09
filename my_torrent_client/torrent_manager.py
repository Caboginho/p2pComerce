# torrent_manager.py
class TorrentManager:
    def __init__(self, torrent_file):
        self.torrent_file = torrent_file
        self.peers = []

    def add_peer(self, peer):
        self.peers.append(peer)

    def remove_peer(self, peer):
        if peer in self.peers:
            self.peers.remove(peer)

    def start_download(self):
        # Inicia o download do torrent
        pass

    def start_upload(self):
        # Inicia o upload do torrent
        pass
