# ui.py
import tkinter as tk
from tkinter import messagebox
from torrent_manager import TorrentManager
import threading

class TorrentClientUI:
    def __init__(self, root, torrent_manager):
        self.root = root
        self.torrent_manager = torrent_manager
        self.create_widgets()

    def create_widgets(self):
        self.root.title("Torrent Client")

        self.torrent_label = tk.Label(self.root, text="Torrent File:")
        self.torrent_label.grid(row=0, column=0, padx=10, pady=10)

        self.torrent_entry = tk.Entry(self.root)
        self.torrent_entry.grid(row=0, column=1, padx=10, pady=10)

        self.add_peer_button = tk.Button(self.root, text="Add Peer", command=self.add_peer)
        self.add_peer_button.grid(row=1, column=0, padx=10, pady=10)

        self.remove_peer_button = tk.Button(self.root, text="Remove Peer", command=self.remove_peer)
        self.remove_peer_button.grid(row=1, column=1, padx=10, pady=10)

        self.start_download_button = tk.Button(self.root, text="Start Download", command=self.start_download)
        self.start_download_button.grid(row=1, column=2, padx=10, pady=10)

        self.start_upload_button = tk.Button(self.root, text="Start Upload", command=self.start_upload)
        self.start_upload_button.grid(row=1, column=3, padx=10, pady=10)

        self.log_text = tk.Text(self.root, state='disabled', width=80, height=20)
        self.log_text.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        self.progress_label = tk.Label(self.root, text="Progress:")
        self.progress_label.grid(row=3, column=0, padx=10, pady=10)

        self.progress_bar = tk.Canvas(self.root, width=300, height=20, bg='white')
        self.progress_bar.grid(row=3, column=1, columnspan=3, padx=10, pady=10)
        self.progress = 0

        self.peers_label = tk.Label(self.root, text="Connected Peers:")
        self.peers_label.grid(row=4, column=0, padx=10, pady=10)

        self.peers_listbox = tk.Listbox(self.root, width=50, height=10)
        self.peers_listbox.grid(row=4, column=1, columnspan=3, padx=10, pady=10)
        self.peers_listbox.bind('<<ListboxSelect>>', self.show_peer_details)

        self.update_peers_list()

    def add_peer(self):
        peer_ip = "localhost"  # Ajuste conforme necessário
        peer_port = 6881  # Ajuste conforme necessário
        self.torrent_manager.add_peer(peer_ip, peer_port)
        self.log_message(f"Added peer {peer_ip}:{peer_port}")
        self.update_peers_list()

    def remove_peer(self):
        selected_peer = self.peers_listbox.curselection()
        if selected_peer:
            peer_info = self.peers_listbox.get(selected_peer)
            ip, port = peer_info.split(':')
            self.torrent_manager.remove_peer(ip, int(port))
            self.log_message(f"Removed peer {peer_info}")
            self.update_peers_list()
        else:
            messagebox.showwarning("Warning", "No peer selected to remove")

    def start_download(self):
        torrent_file = self.torrent_entry.get()
        self.torrent_manager.torrent_file = torrent_file
        self.log_message(f"Starting download for {torrent_file}")
        download_thread = threading.Thread(target=self.torrent_manager.start_download)
        download_thread.start()

    def start_upload(self):
        torrent_file = self.torrent_entry.get()
        self.torrent_manager.torrent_file = torrent_file
        self.log_message(f"Starting upload for {torrent_file}")
        upload_thread = threading.Thread(target=self.torrent_manager.start_upload)
        upload_thread.start()

    def log_message(self, message):
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, message + '\n')
        self.log_text.config(state='disabled')
        self.log_text.see(tk.END)

    def update_progress(self, message):
        self.log_message(message)
        if "Downloaded piece" in message or "Uploaded piece" in message:
            self.progress += 1
            self.progress_bar.delete("progress")
            self.progress_bar.create_rectangle(0, 0, self.progress * 30, 20, fill='blue', tags="progress")

    def update_peers_list(self):
        self.peers_listbox.delete(0, tk.END)
        peers = self.torrent_manager.get_peers()
        for peer in peers:
            self.peers_listbox.insert(tk.END, f"{peer.ip}:{peer.port}")

    def show_peer_details(self, event):
        selected_peer = self.peers_listbox.curselection()
        if selected_peer:
            peer_info = self.peers_listbox.get(selected_peer)
            ip, port = peer_info.split(':')
            # Mostrar detalhes do peer (essa parte pode ser expandida conforme necessário)
            messagebox.showinfo("Peer Details", f"IP: {ip}\nPort: {port}")

# Testando a interface de usuário
if __name__ == "__main__":
    root = tk.Tk()
    torrent_manager = TorrentManager("example.torrent", 10, update_ui_callback=None)
    app = TorrentClientUI(root, torrent_manager)

    def update_ui_callback(message):
        app.update_progress(message)

    torrent_manager.update_ui_callback = update_ui_callback

    root.mainloop()
