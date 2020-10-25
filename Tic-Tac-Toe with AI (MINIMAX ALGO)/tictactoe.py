import random
import math


def is_game_over():
    return True if CheckWin('X') or CheckWin('O') or Count('_') == 0 else False


def minimax(depth, maximizingPlayer, player):
    if is_game_over():
        return static_eval(player)
    if maximizingPlayer:
        maxEval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = player
                    evaluation = minimax(depth + 1, False, player)
                    board[i][j] = '_'
                    maxEval = max(maxEval, evaluation)
        return maxEval
    else:
        minEval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O' if player == 'X' else 'X'
                    evaluation = minimax(depth + 1, True, player)
                    board[i][j] = '_'
                    minEval = min(minEval, evaluation)
        return minEval


def static_eval(player):
    if CheckWin(player):
        return 1
    elif CheckWin('O' if player == 'X' else 'X'):
        return -1
    else:
        return 0


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


def PlaceEasy():
    unfilled_places = [(x, y) for x in range(3) for y in range(3) if not (board[x][y] == 'X' or board[x][y] == 'O')]
    choice = random.choice(unfilled_places)
    return choice[0], choice[1]


def PlaceUser():
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

        elif not Placeable(3 - j, i - 1):
            continue

        else:
            break
    return 3 - j, i - 1


def two_in_row(player):
    for i in range(3):
        if board[i].count(player) == 2:
            for j in range(3):
                if board[i][j] == '_':
                    return i, j
    return False


def PlaceMedium(player):
    self = two_in_row(player)
    opp = two_in_row('X' if player == 'O' else 'O')
    if self:
        return self
    elif opp:
        return opp
    else:
        return PlaceEasy()


def PlaceHard(player):
    if cx == 0 and co == 0:
        return PlaceEasy()
    max_score = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player
                score = minimax(0, False, player)
                board[i][j] = '_'
                if score > max_score:
                    max_score = score
                    max_i = i
                    max_j = j
    return max_i, max_j


while True:
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    # inp = input('Enter cells: ')
    #
    # board =[[_ for _ in inp[:3]],[_ for _ in inp[3:6]],[_ for _ in inp[6:9]]]
    co = 0
    cx = 0

    while True:
        command = input('Input command: ')
        if command.startswith('start'):
            if not len(command.split()) == 3:
                print('Bad parameters!')
            else:
                break
        elif command == 'exit':
            exit(0)
        else:
            print('Bad parameters!')

    user1 = command.split()[1]
    user2 = command.split()[2]

    game_over = False
    while True:
        State()
        if cx - co != 1 or (cx == 0 and co == 0):
            if user1 == 'user':
                r, c = PlaceUser()
            else:
                if user1 == 'easy':
                    r, c = PlaceEasy()
                elif user1 == 'medium':
                    r, c = PlaceMedium('X')
                else:
                    r, c = PlaceHard('X')
                print('Making move level "{}"'.format(user1))
            board[r][c] = 'X'
            cx += 1
        else:
            if user2 == 'user':
                r, c = PlaceUser()
            else:
                if user2 == 'easy':
                    r, c = PlaceEasy()
                elif user2 == 'medium':
                    r, c = PlaceMedium('O')
                else:
                    r, c = PlaceHard('O')
                print('Making move level "{}"'.format(user2))
            board[r][c] = 'O'
            co += 1

        # cx = Count('X')
        # co = Count('O')
        # if co >= cx:
        #     board[3 - j][i - 1] = 'X'
        # else:
        #     board[3 - j][i - 1] = 'O'
        if cx >= 3 or co >= 3:
            if CheckWin('X'):
                State()
                print('X wins')
                game_over = True
            elif CheckWin('O'):
                State()
                print('O wins')
                game_over = True
            elif Count('_') == 0:
                State()
                print('Draw')
                game_over = True
            if game_over:
                break
    print()
