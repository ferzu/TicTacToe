
BORDER = "---------"
DIMENSION = 3
COORDINATES = [[(1, 3), (2, 3), (3, 3)],
               [(1, 2), (2, 2), (3, 2)],
               [(1, 1), (2, 1), (3, 1)]]


# Game state ______________________________________________________________________________________
def game_state(board):
    winner = "__"
    if possible(board):
        w_horizontal = board_winner(board)
        w_vertical = board_winner(transposed_board(board))
        diag_1, diag_2 = get_diagonals(board)
        wd1 = diagonal_win(diag_1)
        wd2 = diagonal_win(diag_2)
        if w_horizontal:
            winner = w_horizontal
            return "{} wins".format(winner)
        elif w_vertical:
            winner = w_vertical
            return "{} wins".format(winner)
        elif wd1:
            winner = wd1
            return "{} wins".format(winner)
        elif wd2:
            winner = wd2
            return "{} wins".format(winner)
        else:
            winner = False
    if empty_cells(board) and not winner:
        return "Game not finished"
    elif not empty_cells(board) and not winner:
        return "Draw"
    else:
        return "Impossible"


# Input ______________________________________________________________________________________
def input_():
    exit_ = False
    values = ""
    while not exit_:
        print("Enter 9 values.")
        values = input()
        valid = True
        len_ = len(values)
        if len_ != 9:
            print("Enter 9 values. Valid characters: 'X', 'O', '_'")
        elif len_ == 9:
            for value in values:
                if value != "X" and value != "O" and value != "_":
                    print("Enter valid values. Valid characters: 'X', 'O', '_'")
                    valid = False
                    break
            if valid:
                exit_ = True
    return values


def update_values(old_values, position, player):
    values_list = [value for value in old_values]
    values_list[position] = player
    updated_values = "".join([str(value) for value in values_list])
    return updated_values


def input_coordinates():
    exit_ = True
    str_ = ""
    while exit_:
        print("Insert next move: number1 number2")
        str_ = input()
        if len(str_) > 3 or str_[1] != " ":
            print("Not valid.")
        else:
            exit_ = False
    return str_[0], str_[2]


# Coordinates ______________________________________________________________________________________
def valid_coordinates(coordinates, board):
    a, b = coordinates
    # print(a, b , type(coordinates))
    if not a.isdigit() or not b.isdigit():
        print("You should enter numbers!")
        return False
    else:
        a, b = int(a), int(b)
        coordinates = (a, b)
    if a < 1 or b < 1 or a > 3 or b > 3:
        print("Coordinates should be from 1 to 3!")
        return False
    elif occupied_cell(board, coordinates):
        print("This cell is occupied! Choose another one!")
        return False
    else:
        a, b = coordinates_translator(coordinates)
        return a, b


def coordinates_translator(coordinates):
    for i in range(0, DIMENSION):
        for j in range(0, DIMENSION):
            if COORDINATES[i][j] == coordinates:
                index = (i, j)
                return index


def index_of(coordinates):
    i1, i2 = coordinates
    position = 0
    for i in range(0, DIMENSION):
        for j in range(0, DIMENSION):
            position += 1
            if i == i1 and j == i2:
                return position - 1


# Board ______________________________________________________________________________________
def print_board(input_values):
    print(BORDER)
    for row in range(0, len(input_values), 3):
        print("| {} |".format(" ".join(input_values[row: row + 3])))
    print(BORDER)


def game_board(input_values):
    board = []
    cells = [cell for cell in input_values]
    for cell in range(0, len(input_values), 3):
        board.append(cells[cell: cell + 3])
    return board


def transposed_board(board):
    transposed = list(map(list, zip(*board)))
    return transposed


def board_winner(board):
    points = 1
    winner = ""
    for i in range(DIMENSION):  # To find 3 pieces x horizontal
        for j in range(DIMENSION - 1):
            winner = board[i][j]
            if board[i][j] == board[i][j + 1]:
                points += 1
        if points == 3 and not empty(winner):
            return winner
        else:
            points = 1
    return False


# Impossible ______________________________________________________________________________________
def impossible(board):
    points = 1
    winner = 0
    cell = ""
    for i in range(DIMENSION):
        for j in range(DIMENSION - 1):
            cell = board[i][j]
            if board[i][j] == board[i][j + 1]:
                points += 1
        if points == 3 and not empty(cell):
            winner += 1
            points = 1
        else:
            points = 1
    return winner


def possible(board):
    w1 = impossible(board)
    w2 = impossible(transposed_board(board))
    diag_1, diag_2 = get_diagonals(board)
    wd1 = diagonal_win(diag_1)
    wd2 = diagonal_win(diag_2)

    if w1 > 1 or w2 > 1 or big_difference(board):
        # print(w1, w2, gb.big_difference(board))
        return False
    elif w1 == 1 and w2 == 1:
        return False
    elif wd1 and wd2:
        return False
    elif (w1 == 1 or w2 == 1) and (wd1 or wd2):
        return False
    else:
        return True


def big_difference(board):
    count_x = 0
    count_o = 0
    for row in board:
        for cell in row:
            if cell == "X":
                count_x += 1
            elif cell == "O":
                count_o += 1

    difference = abs(count_o - count_x)
    # Rule: player 'X' and 'O' in turns, difference should be 1 or 0.
    if difference > 1:
        return True
    else:
        return False


# Diagonals ______________________________________________________________________________________
def get_diagonals(board):
    diag_1, diag_2 = [], []
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if i == j:
                diag_1.append(board[i][j])
            if i + j == DIMENSION - 1:
                diag_2.append(board[i][j])
    return diag_1, diag_2


def diagonal_win(diag):
    points = 1
    for i in range(0, len(diag) - 1):
        if diag[i] == diag[i + 1]:
            points += 1
    if points == 3 and diag[0] != "_":
        winner = diag[0]
        return winner
    else:
        return False


# Cells ______________________________________________________________________________________
def empty_cells(board):
    for row in board:
        for cell in row:
            if cell == "_":
                return True
    return False
    # x = "_"
    # return x in board


def empty(cell):
    if cell == "_":
        return True
    return False


def occupied_cell(board, coordinates):
    i, j = coordinates_translator(coordinates)
    if board[i][j] != "_":
        return True
    return False
