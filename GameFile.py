import sys


# Start game and return score
def game():
    # We are creating field for game
    game_field = [[], [], []]
    for line in game_field:
        for number in range(3):
            line.append(0)
    winner = pvp(game_field)
    if winner == 3 or winner == 0:
        print('The game is drawn :)')
    else:
        print('Player' + str(winner) + ' win this game!')


# After each move we check the field for the winner
def checker(game_field):
    num = len(game_field)
    range_size = range(num)
    # check if The game is drawn
    check_game = 0
    for line in game_field:
        for value in line:
            if value == 1 or value == 2:
                check_game += 1
    if check_game == 9:
        return 3
    # check lines
    for line in game_field:
        check_p1, check_p2 = 0, 0
        for value in line:
            if value == 1 and check_p2 == 0:
                check_p1 += 1
            elif value == 2 and check_p1 == 0:
                check_p2 += 1
        if check_p1 == 3:
            return 1
        elif check_p2 == 3:
            return 2
    # check columns
    for i in range_size:
        check_p1, check_p2 = 0, 0
        for j in range(len(game_field[i])):
            if game_field[j][i] == 1 and check_p2 == 0:
                check_p1 += 1
            elif game_field[j][i] == 2 and check_p1 == 0:
                check_p2 += 1
        if check_p1 == 3:
            return 1
        elif check_p2 == 3:
            return 2
    # check diagonals
    # main diagonal
    check_p1, check_p2 = 0, 0
    for i in range_size:
        if game_field[i][i] == 1 and check_p2 == 0:
            check_p1 += 1
        elif game_field[i][i] == 2 and check_p1 == 0:
            check_p2 += 1
    if check_p1 == 3:
        return 1
    elif check_p2 == 3:
        return 2
    # the secondary diagonal
    check_p1, check_p2 = 0, 0
    for i in range_size:
        if game_field[i][num-1-i] == 1 and check_p2 == 0:
            check_p1 += 1
        elif game_field[i][num-1-i] == 2 and check_p1 == 0:
            check_p2 += 1
    if check_p1 == 3:
        return 1
    elif check_p2 == 3:
        return 2
    # If we doesn't find the winner
    return 0


# The Output
def field_output(game_field):
    for line in game_field:
        for value in line:
            if value == 1:
                sys.stdout.write('X  ')
            elif value == 2:
                sys.stdout.write('O  ')
            else:
                sys.stdout.write('.  ')
        print('')


# Move
def do_move(player, game_field):
    while True:
        greeting = 'Player' + str(player) + ':'
        move = input(greeting).split(',')
        if len(move) == 2:
            move[0] = int(float(move[0]))-1
            move[1] = int(float(move[1]))-1
            # Check the correctness of the input and is the cell occupied
            if move[0] >= 0 and move[0]< 3 and move[1] >= 0 and move[1] < 3 and game_field[move[0]][move[1]] == 0:
                game_field[move[0]][move[1]] = player
                return game_field
            else:
                print('Invalid input(the cell is already occupied, or you are out of bounds of the gaming field(1...3)')
        else:
            print('Invalid input(the cell is already occupied, or you are out of bounds of the gaming field(1...3)')


# P1 and P2 playing
def pvp(game_field):
    print('Field:')
    field_output(game_field)
    # The game continues until someone wins or no moves left
    while True:
        game_field = do_move(1, game_field)
        field_output(game_field)
        if checker(game_field) == 1 or checker(game_field) == 3:
            return checker(game_field)
        game_field = do_move(2, game_field)
        field_output(game_field)
        if checker(game_field) == 2 or checker(game_field) == 3:
            return checker(game_field)


# Launch point
if __name__ == "__main__":
    print("""This is a TIC-TAC-toe game. You can play against the computer or
against a second player. You take turns to select the desired cell specify the
row and column in which you want to make a mark according to the example.

Example: "1,2". (1 row, 2 column)

Other input forms will not be supported. Wish you a fun game!""")
    game()
