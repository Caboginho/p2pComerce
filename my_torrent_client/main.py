# main.py
from peer_manager import PeerManager
from torrent_manager import TorrentManager
from piece_manager import PieceManager
from network_module import NetworkModule
from ui_module import UIModule

def main():
    peer_manager = PeerManager()
    torrent_manager = TorrentManager("example.torrent")
    piece_manager = PieceManager([])
    network_module = NetworkModule()
    ui_module = UIModule()

    # Adiciona lógica para iniciar o download e upload
    ui_module.add_torrent("example.torrent")
    torrent_manager.start_download()

if __name__ == "__main__":
    main()
