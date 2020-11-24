import game_basics as gb
BORDER = "---------"
DIMENSION = 3
player = ""
player_x = True
values = "_________"
result = "Game not finished"
valid_move = False

# Initializing
gb.print_board(values)
game_board = gb.game_board(values)  # 2.1 making matrix from board

while result == "Game not finished":

    # Insert move
    while not valid_move:
        move = gb.input_coordinates()
        valid_move = gb.valid_coordinates(move, game_board)
    c1, c2 = valid_move

    # Updating matrix
    if values == "_________" or player_x:
        game_board[c1][c2] = "X"
        player = "X"
        player_x = False
    else:
        game_board[c1][c2] = "O"
        player = "O"
        player_x = True

    # Output board
    output_values = gb.update_values(values, gb.index_of(valid_move), player)
    gb.print_board(output_values)

    # Game state
    result = gb.game_state(game_board)
    print(result)
    if result == "Impossible":
        player_x = True
        values = "_________"
        print("Restart the game.")
    valid_move = False
    values = output_values
