# main.py
from peer_manager import PeerManager, Peer
from torrent_manager import TorrentManager
from piece_manager import PieceManager
from network_module import NetworkModule
from ui_module import UIModule

def main():
    peer_manager = PeerManager()
    torrent_manager = TorrentManager("exemplo.torrent",10)
    piece_manager = PieceManager(10)
    network_module = NetworkModule()
    ui_module = UIModule()

    # Adiciona lógica para iniciar o download e upload
    ui_module.add_torrent("exemplo.torrent")
    torrent_manager.start_download()

    # Adiciona peers para testar
    peer1 = Peer("192.168.1.1", 6881)
    peer_manager.add_peer("192.168.1.1", 6881)
    torrent_manager.add_peer("192.168.1.1", 6881)

    # Simula o progresso do download
    ui_module.display_progress(50)

if __name__ == "__main__":
    main()
