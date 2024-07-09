# torrent_manager.py
import random
from peer_manager import PeerManager
from piece_manager import PieceManager
from peer_connection import PeerConnection

class TorrentManager:
    def __init__(self, torrent_file, num_pieces):
        self.torrent_file = torrent_file
        self.peer_manager = PeerManager()
        self.piece_manager = PieceManager(num_pieces)

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
        peer_conn = PeerConnection(peer.ip, peer.port)
        peer_conn.connect()
        peer_conn.send_message(f"REQUEST_PIECE {piece_index}")
        piece_data = peer_conn.receive_message()
        self.piece_manager.mark_piece_as_downloaded(piece_index, piece_data.encode())
        peer_conn.close()

    def start_upload(self):
        print(f"Starting upload for {self.torrent_file}")
        peers = self.peer_manager.get_peers()
        for peer in peers:
            peer_conn = PeerConnection(peer.ip, peer.port)
            peer_conn.connect()
            self.upload_to_peer(peer_conn)
            peer_conn.close()

    def upload_to_peer(self, peer_conn):
        downloaded_pieces = self.piece_manager.get_downloaded_pieces()
        for piece in downloaded_pieces:
            data = piece['data']
            piece_index = piece['index']
            peer_conn.send_message(f"PIECE_DATA {piece_index} {data.decode()}")
            print(f"Uploaded piece {piece_index} to peer {peer_conn.ip}:{peer_conn.port}")

# Testando o TorrentManager
if __name__ == "__main__":
    torrent_manager = TorrentManager("example.torrent", 10)
    torrent_manager.add_peer("localhost", 8000)
    torrent_manager.add_peer("localhost", 8080)
    torrent_manager.start_download()
    torrent_manager.start_upload()
