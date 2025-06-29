import chess
import numpy as np
class State(object):
    def __init__(self, board=None): # initializer
        if board is None:
            self.board = chess.Board()
        else:
            self.board = board

    def serialize(self): # translator
        # board state to 257 bits conversion
        assert self.board.is_valid()
        bstate =np.zeros(64, np.uint8)
        piece_map = {"P":1, "N":2, "B":3, "R":4, "Q":5, "K":6,\
                             "p":9, "n":10, "b":11, "r":12, "q":13, "k":14}
        for i in range(64):
            piece = self.board.piece_at(i)
            if piece is not None:
                bstate[i] = piece_map[piece.symbol()]
        if self.board.has_queenside_castling_rights(chess.WHITE):
            # changing the number of rook from 4 to 7 (can castle)
            if bstate[0] == 4:
                bstate[0] = 7
        if self.board.has_kingside_castling_rights(chess.WHITE):
            if bstate[7] == 4:
                bstate[7] = 7
        if self.board.has_queenside_castling_rights(chess.BLACK):
            if bstate[56] == 8+4:
                bstate[56] = 8+7
        if self.board.has_kingside_castling_rights(chess.BLACK):
            if bstate[63] == 8+4:
                bstate[63] = 8+7
        if self.board.ep_square is not None:
            if bstate[self.board.ep_square] == 0:
                bstate[self.board.ep_square] = 8
        bstate = bstate.reshape(8,8)

        # binary state
        state = np.zeros((5,8,8), np.uint8)

        # columns converted to 4 bit binary 
        state[0] = (bstate>>3)&1
        state[1] = (bstate>>2)&1
        state[2] = (bstate>>1)&1
        state[3] = (bstate>>0)&1
        # 4th column is whose turn it is
        state[4] = int(self.board.turn)

        return state
    
    def path(self): # path shower
        return list(self.board.legal_moves)
    
    def value(self): # brain
        # neural network
        return 0
    
if __name__=="__main__":
    s= State()
    print(s.edges())