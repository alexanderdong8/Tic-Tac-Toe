"""
Tic Tac Toe Player
"""

import math

from cv2 import BORDER_ISOLATED

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countx = 0
    county = 0
    for row in board:
        for item in row:
            if item == "X":
                countx += 1
            elif item == "Y":
                county += 1
    
    if countx>county:
        return "O"
    elif county>countx:
        return "X"
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] != "X" or board[row][column] != "O":
                actions.add((row, column))

    return actions

    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    newboard = board

    if player(board) == "X":
        newboard[action[0]][action[1]] = "X"
    elif player(board) == "O":
        newboard[action[0]][action[1]] = "O"
    
    return newboard
            


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """


    c = ["X","O"]
    for p in c:
        if board[0][0]== board[0][1]== board[0][2] == p:
            return p
        if board[1][0]== board[1][1]== board[1][2] == p:
            return p
        if board[2][0]== board[2][1]== board[2][2] == p:
            return p
        if board[0][0]== board[1][0]== board[2][0] == p:
            return p
        if board[0][1]== board[1][1]== board[2][1] == p:
            return p
        if board[0][2]== board[1][2]== board[2][2] == p:
            return p
        if board[0][0]== board[1][1]== board[2][2] == p:
            return p
        if board[0][2]== board[1][1]== board[2][0] == p:
            return p
    return None



    """
    for row in board:
        if not("O" in row):
            return "X"
        elif not ("X" in row):
            return "O"

    countx = 0
    counto = 0  

    for x in range(3):
        for y in range(3):
            if board[y][x] == "X":
                countx+=1

            if board[y][x] == "O":
                counto+=1

            if countx == 3:
                return "X"
            
            if counto == 3:
                return "O"

        countx = 0
        counto = 0
    
    countxx = 0
    countoo = 0
    for x in range(3):
        if board[x][x] == "X":
            countxx += 1
        if board[x][x] == "O":
            countoo += 1
        if countxx == 3:
            return "X"
        if countoo == 3:
            return "O"

    return None
    """



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) == "X" or winner(board) == "O":
        return True
    else:
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == "X":
        return 1
    
    elif winner(board) == "O":
        return -1
    
    else:
        return 0
    
def max_value(board):
    if terminal(board):
        return utility(board)
    v = -2
    key
    for action in actions(board):
        prev = v
        min = min_value(result(board, action))
        v = max(v, min[0])
        if v > prev:
            key = action

    return v, key

def min_value(board):
    if terminal(board):
        return utility(board)
    v = 2
    key
    for action in actions(board):
        prev = v
        max = max_value(result(board, action))
        v = min(v, max[0])
        if v > prev:
            key = action
    
    return v, key

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == "X":
        return max_value(board)[1]

    if player(board) == "O":
        return min_value(board)[1]
    
    

                




