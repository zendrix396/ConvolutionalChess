import os
import chess.pgn
from state import State
for fn in os.listdir('data'):
    pgn = open(os.path.join('data', fn))
    while 1:
        try: 
            game = chess.pgn.read_game(pgn)
        except:
            break
        value = {"1-0":1, "0-1":-1, "1/2-1/2":0}[game.headers['Result']]
        board = game.board()
        for i, move in enumerate(game.mainline_moves()):
            board.push(move)
            # extract the boards
            print(State(board).serialize())
            exit()
    break