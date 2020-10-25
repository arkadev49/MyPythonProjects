def State():
    print('---------')
    for i in range(3):
        print('|', end=" ")
        for j in range(3):
            print(board[i][j] + ' ', end='')
        print('|')
    print('---------')


def CheckWin(player):
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or (  # Checking  Diagonal 1
            board[0][2] == player and board[1][1] == player and board[2][0] == player) or (  # Checking Diagonal 2
            board[0][0] == player and board[0][1] == player and board[0][2] == player) or (  # Checking Row 1
            board[1][0] == player and board[1][1] == player and board[1][2] == player) or (  # Checking Row 2
            board[2][0] == player and board[2][1] == player and board[2][2] == player) or (  # Checking Row 3
            board[0][0] == player and board[1][0] == player and board[2][0] == player) or (  # Checking Column 1
            board[0][1] == player and board[1][1] == player and board[2][1] == player) or (  # Checking Column 2
            board[0][2] == player and board[1][2] == player and board[2][2] == player):  # Checking Column 3
        return True
    return False


def Count(player):
    count = 0
    for i in board:
        for j in i:
            if j == player:
                count += 1
    return count


def isDraw():
    for i in board:
        for j in i:
            if j == '_':
                return False
    return True


def Placeable(i, j):
    if board[i][j] == 'X' or board[i][j] == 'O':
        print('This cell is occupied! Choose another one!')
        return False
    return True


board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

while True:
    State()
    while True:
        try:
            i, j = input('Enter the coordinates: ').split()
            i = int(i)
            j = int(j)
        except ValueError:
            print('You should enter numbers!')
            continue

        if i < 1 or i > 3 or j < 1 or j > 3:
            print('Coordinates should be from 1 to 3!')
            continue

        elif not Placeable(i-1,j-1):
            continue

        else:
            break

    cx = Count('X')
    co = Count('O')
    if co >= cx:
        board[i-1][j-1] = 'X'
    else:
        board[i-1][j-1] = 'O'

    if CheckWin('X'):
        State()
        print('X wins')
        break
    elif CheckWin('O'):
        State()
        print('O wins')
        break
    elif Count('_') == 0:
        State()
        print('Draw')
        break
