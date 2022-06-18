import pickle
import chess
with open('final.pkl','rb') as f:  # Python 3: open(..., 'rb')
    qValues= pickle.load(f)
import numpy as np
import random
def get_move1(fen):
    board = chess.Board(fen)
    possibleMoves = list(board.legal_moves )
    q = [qValues[(fen, action)] for action in possibleMoves]
    k =np.max(q)
    temp = np.where(q == k)[0]

    return str(possibleMoves[temp[random.randint(0,len(temp)-1)]])

