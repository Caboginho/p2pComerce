# torrent_manager.py
import random
import threading
from peer_manager import PeerManager
from piece_manager import PieceManager
from peer_connection import PeerConnection

class TorrentManager:
    def __init__(self, torrent_file, num_pieces, update_ui_callback=None):
        self.torrent_file = torrent_file
        self.peer_manager = PeerManager()
        self.piece_manager = PieceManager(num_pieces)
        self.lock = threading.Lock()
        self.update_ui_callback = update_ui_callback

    def add_peer(self, ip, port):
        self.peer_manager.add_peer(ip, port)

    def remove_peer(self, ip, port):
        self.peer_manager.remove_peer(ip, port)

    def get_peers(self):
        return self.peer_manager.get_peers()

    def start_download(self):
        print(f"Starting download for {self.torrent_file}")
        self.update_piece_rarity()
        rarest_pieces = self.piece_manager.get_rarest_pieces()

        threads = []
        for piece_index in rarest_pieces:
            thread = threading.Thread(target=self.download_piece, args=(piece_index,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        if self.update_ui_callback:
            self.update_ui_callback("Download completed")

    def update_piece_rarity(self):
        peers = self.peer_manager.get_peers()
        for peer in peers:
            peer_conn = PeerConnection(peer.ip, peer.port)
            peer_conn.connect()
            peer_conn.send_message("REQUEST_PIECE_LIST")
            piece_list = peer_conn.receive_message().split()
            self.piece_manager.update_rarity(piece_list)
            peer_conn.close()

    def download_piece(self, piece_index):
        peers = self.peer_manager.get_peers()
        if not peers:
            print("No peers available for download")
            return

        peer = random.choice(peers)
        peer_conn = PeerConnection(peer.ip, peer.port)
        peer_conn.connect()
        peer_conn.send_message(f"REQUEST_PIECE {piece_index}")
        piece_data = peer_conn.receive_message()
        with self.lock:
            self.piece_manager.mark_piece_as_downloaded(piece_index, piece_data.encode())
        peer_conn.close()

        if self.update_ui_callback:
            self.update_ui_callback(f"Downloaded piece {piece_index}")

    def start_upload(self):
        print(f"Starting upload for {self.torrent_file}")
        peers = self.peer_manager.get_peers()

        threads = []
        for peer in peers:
            thread = threading.Thread(target=self.upload_to_peer, args=(peer,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        if self.update_ui_callback:
            self.update_ui_callback("Upload completed")

    def upload_to_peer(self, peer):
        peer_conn = PeerConnection(peer.ip, peer.port)
        peer_conn.connect()
        downloaded_pieces = self.piece_manager.get_downloaded_pieces()
        for piece in downloaded_pieces:
            data = piece['data']
            piece_index = piece['index']
            peer_conn.send_message(f"PIECE_DATA {piece_index} {data.decode()}")
            print(f"Uploaded piece {piece_index} to peer {peer.ip}:{peer.port}")

            if self.update_ui_callback:
                self.update_ui_callback(f"Uploaded piece {piece_index}")

        peer_conn.close()

# Testando o TorrentManager com múltiplas threads
if __name__ == "__main__":
    def update_ui_callback(message):
        print(message)

    torrent_manager = TorrentManager("exemplo.torrent", 10, update_ui_callback)
    torrent_manager.add_peer("192.168.1.1", 6881)
    torrent_manager.add_peer("192.168.1.1", 6882)
    torrent_manager.start_download()
    torrent_manager.start_upload()
