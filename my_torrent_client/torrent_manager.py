# torrent_manager.py
import random
from peer_manager import PeerManager
from piece_manager import PieceManager
from network_module import NetworkModule

class TorrentManager:
    def __init__(self, torrent_file, num_pieces):
        self.torrent_file = torrent_file
        self.peer_manager = PeerManager()
        self.piece_manager = PieceManager(num_pieces)
        self.network_module = NetworkModule()

    def add_peer(self, ip, port):
        self.peer_manager.add_peer(ip, port)

    def remove_peer(self, ip, port):
        self.peer_manager.remove_peer(ip, port)

    def start_download(self):
        print(f"Starting download for {self.torrent_file}")
        missing_pieces = self.piece_manager.get_missing_pieces()
        for piece in missing_pieces:
            self.download_piece(piece['index'])

    def download_piece(self, piece_index):
        peers = self.peer_manager.get_peers()
        if not peers:
            print("No peers available for download")
            return

        # Escolhe um peer aleatório para baixar a peça
        peer = random.choice(peers)
        if not peer.is_connected:
            self.peer_manager.connect_peer(peer.ip, peer.port)
        print(f"Downloading piece {piece_index} from peer {peer}")
        # Simula o download da peça
        piece_data = f"Data for piece {piece_index}".encode()  # Simulando dados da peça
        self.piece_manager.mark_piece_as_downloaded(piece_index, piece_data)

    def start_upload(self):
        print(f"Starting upload for {self.torrent_file}")
        peers = self.peer_manager.get_peers()
        for peer in peers:
            if not peer.is_connected:
                self.peer_manager.connect_peer(peer.ip, peer.port)
            self.upload_to_peer(peer)

    def upload_to_peer(self, peer):
        downloaded_pieces = self.piece_manager.get_downloaded_pieces()
        for piece in downloaded_pieces:
            data = piece['data']
            piece_index = piece['index']
            self.network_module.send_data(peer.ip, peer.port, data)
            print(f"Uploaded piece {piece_index} to peer {peer}")

# Testando o TorrentManager
if __name__ == "__main__":
    torrent_manager = TorrentManager("example.torrent", 10)
    torrent_manager.add_peer("localhost", 6881)
    torrent_manager.add_peer("localhost", 6882)
    torrent_manager.start_download()
    torrent_manager.start_upload()
