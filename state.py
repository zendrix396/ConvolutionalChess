import chess

class State(object):
    def __init__(self): # initializer
        self.board = chess.Board()

    def serialize(self): # translator
        # board state to 257 bits conversion
        pass 
    def path(self): # path shower
        return list(self.board.legal_moves)
    
    def value(self): # brain
        # neural network
        return 1
    
if __name__=="__main__":
    s= State()
    print(s.edges())