import random
import time

def drawBoard(board):
    print(' ' + board[1] + '|' + board[2] + '|' + board[3])
    print('-------')
    print(' ' + board[4] + '|' + board[5] + '|' + board[6])
    print('-------')
    print(' ' + board[7] + '|' + board[8] + '|' + board[9])
    print('       ')

def initBoard():
    board = dict()
    board[1] = ' '
    board[2] = ' '
    board[3] = ' '
    board[4] = ' '
    board[5] = ' '
    board[6] = ' '
    board[7] = ' '
    board[8] = ' '
    board[9] = ' '
    return board

def isEnd(board):
    if board[1] == board[2] == board[3] != ' ':
        return board[1]
    elif board[4] == board[5] == board[6] != ' ':
        return board[4]
    elif board[7] == board[8] == board[9] != ' ':
        return board[7]
    elif board[1] == board[4] == board[7] != ' ':
        return board[1]
    elif board[2] == board[5] == board[8] != ' ':
        return board[2]
    elif board[3] == board[6] == board[9] != ' ':
        return board[3]
    elif board[1] == board[5] == board[9] != ' ':
        return board[1]
    elif board[3] == board[5] == board[7] != ' ':
        return board[3]
    elif freeSpaces == []:
        return 'Tie'
    else:
        return 'No'

freeSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def isFree(space):
    if space in freeSpaces:
        return True
    else:
        return False

def computerMove(board):
    if isFree(5):
        play = 5
    else:
        play = freeSpaces[0]
    canWin = False
    for space in freeSpaces:
        newBoardO = board.copy()
        newBoardO[space] = 'O'
        if isEnd(newBoardO) == 'O':
            play = space
            canWin = True
            break
    if canWin == False:
        for space in freeSpaces:
            newBoardX = board.copy()
            newBoardX[space] = 'X'
            if isEnd(newBoardX) == 'X':
                play = space
                break
    print('Computer chooses space ' + str(play))
    freeSpaces.remove(play)
    board[play] = 'O'
    drawBoard(board)
    end = isEnd(board)
    if end == 'X':
        playing = False
        print('You Win!')
        return None
    elif end == 'O':
        playing = False
        print('Computer Wins')
        return None
    elif end == 'Tie':
        playing = False
        print("It's a tie!")
        return None
    return board

def playerMove(board):
    play = 0
    while play == 0:
        print('What is your next move?')
        play = int(input())
        if isFree(play) == False:
            play = 0
            print('Invalid move, please pick again.')
    freeSpaces.remove(play)
    board[play] = 'X'
    drawBoard(board)
    end = isEnd(board)
    if end == 'X':
        playing = False
        print('You Win!')
        return None
    elif end == 'O':
        playing = False
        print('Computer Wins')
        return None
    elif end == 'Tie':
        playing = False
        print("It's a tie!")
        return None
    return board
a = initBoard()
a[3] = 'X'
a[5] = 'O'
a[6] = 'X'
a[9] = 'X'
print('here' + isEnd(a))
while True:
    print('Welcome to Tic-Tac-Toe!')
    board = initBoard()
    turn = random.choice(['You', 'Computer'])
    print(turn + ' will go first.')
    while True:
        if turn == 'You':
            board = playerMove(board)
            turn = 'Computer'
            if board == None:
                break
            time.sleep(0.3)
        elif turn == 'Computer':
            board = computerMove(board)
            turn = 'You'
            if board == None:
                break
            time.sleep(0.3)
    break
