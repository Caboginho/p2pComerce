# torrent_manager.py
import os
import time
import random
import hashlib

class Peer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.pieces = []

class TorrentManager:
    def __init__(self, torrent_file, piece_count, update_ui_callback=None):
        self.torrent_file = torrent_file
        self.piece_count = piece_count
        self.peers = []
        self.downloaded_pieces = []
        self.uploaded_pieces = []
        self.update_ui_callback = update_ui_callback

    def add_peer(self, ip, port):
        self.peers.append(Peer(ip, port))

    def remove_peer(self, ip, port):
        self.peers = [peer for peer in self.peers if not (peer.ip == ip and peer.port == port)]

    def get_peers(self):
        return self.peers

    def get_downloaded_pieces(self):
        return self.downloaded_pieces

    def get_uploaded_pieces(self):
        return self.uploaded_pieces

    def start_download(self):
        for i in range(self.piece_count):
            time.sleep(random.uniform(0.1, 0.5))  # Simulate download time
            piece = self.download_piece(i)
            if self.verify_piece(piece):
                self.downloaded_pieces.append(piece)
                if self.update_ui_callback:
                    self.update_ui_callback(f"Downloaded and verified piece {i}")
            else:
                if self.update_ui_callback:
                    self.update_ui_callback(f"Failed to verify piece {i}, retrying download")
                piece = self.download_piece(i)
                if self.verify_piece(piece):
                    self.downloaded_pieces.append(piece)
                    if self.update_ui_callback:
                        self.update_ui_callback(f"Downloaded and verified piece {i} after retry")
        if self.update_ui_callback:
            self.update_ui_callback("Download complete")

    def start_upload(self):
        for i in range(self.piece_count):
            if i < len(self.downloaded_pieces):
                time.sleep(random.uniform(0.1, 0.5))  # Simulate upload time
                piece = self.downloaded_pieces[i]
                self.uploaded_pieces.append(piece)
                if self.update_ui_callback:
                    self.update_ui_callback(f"Uploaded piece {i}")
        if self.update_ui_callback:
            self.update_ui_callback("Upload complete")

    def download_piece(self, index):
        data = f"Data of piece {index}"
        piece = {'index': index, 'data': data, 'hash': self.calculate_hash(data)}
        return piece

    def verify_piece(self, piece):
        calculated_hash = self.calculate_hash(piece['data'])
        return calculated_hash == piece['hash']

    def calculate_hash(self, data):
        sha1 = hashlib.sha1()
        sha1.update(data.encode('utf-8'))
        return sha1.hexdigest()
