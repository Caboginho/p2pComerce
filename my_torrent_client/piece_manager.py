# piece_manager.py

class PieceManager:
    def __init__(self, pieces):
        self.pieces = [{'index': i, 'downloaded': False} for i in range(pieces)]

    def verify_piece(self, piece_index):
        # Aqui você implementará a lógica para verificar a integridade da peça
        print(f"Verifying piece {piece_index}")

    def get_missing_pieces(self):
        missing_pieces = [piece for piece in self.pieces if not piece['downloaded']]
        print(f"Missing pieces: {missing_pieces}")
        return missing_pieces

# Testando o PieceManager
if __name__ == "__main__":
    piece_manager = PieceManager(10)
    piece_manager.verify_piece(3)
    piece_manager.get_missing_pieces()
