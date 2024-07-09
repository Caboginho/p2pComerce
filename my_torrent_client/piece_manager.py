# piece_manager.py
class PieceManager:
    def __init__(self, pieces):
        self.pieces = pieces

    def verify_piece(self, piece_index):
        # Verifica a integridade da peça usando o hash
        pass

    def get_missing_pieces(self):
        # Retorna uma lista de peças que ainda não foram baixadas
        return [piece for piece in self.pieces if not piece['downloaded']]
 
 