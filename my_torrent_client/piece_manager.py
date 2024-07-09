# piece_manager.py
import hashlib

class PieceManager:
    def __init__(self, num_pieces):
        self.pieces = [{'index': i, 'downloaded': False, 'data': None} for i in range(num_pieces)]

    def verify_piece(self, piece_index, expected_hash):
        piece = self.pieces[piece_index]
        if piece['data'] is None:
            print(f"Piece {piece_index} has no data")
            return False
        piece_hash = hashlib.sha1(piece['data']).hexdigest()
        if piece_hash == expected_hash:
            print(f"Piece {piece_index} verified successfully")
            return True
        else:
            print(f"Piece {piece_index} verification failed")
            return False

    def get_missing_pieces(self):
        missing_pieces = [piece for piece in self.pieces if not piece['downloaded']]
        print(f"Missing pieces: {missing_pieces}")
        return missing_pieces

    def get_downloaded_pieces(self):
        downloaded_pieces = [piece for piece in self.pieces if piece['downloaded']]
        print(f"Downloaded pieces: {downloaded_pieces}")
        return downloaded_pieces

    def mark_piece_as_downloaded(self, piece_index, data):
        for piece in self.pieces:
            if piece['index'] == piece_index:
                piece['downloaded'] = True
                piece['data'] = data
                print(f"Piece {piece_index} marked as downloaded")

# Testando o PieceManager
if __name__ == "__main__":
    piece_manager = PieceManager(10)
    data = b"example data"
    piece_manager.mark_piece_as_downloaded(3, data)
    piece_manager.verify_piece(3, hashlib.sha1(data).hexdigest())
    piece_manager.get_missing_pieces()
    piece_manager.get_downloaded_pieces()
