# ui_module.py

class UIModule:
    def __init__(self):
        pass

    def display_progress(self, progress):
        print(f"Download Progress: {progress}%")

    def add_torrent(self, torrent_file):
        print(f"Torrent added: {torrent_file}")

# Testando o UI Module
if __name__ == "__main__":
    ui_module = UIModule()
    ui_module.add_torrent("exemplo.torrent")
    ui_module.display_progress(50)
