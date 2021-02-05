from os import system, name

gameBoard = []


def clear():
    # for windows 
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix') 
    else:
        _ = system('clear')


def print_game_board(list_of_signs):
    clear()

    i = 0
    j = 0
    print("#|0|1|2|")
    print('-' * 8)
    while i < 3:
        print(f"{i}|", end="")
        while j < 3:
            print(list_of_signs[i][j], end="|")
            j += 1
        print('\n' + '-' * 8)
        i += 1
        j = 0


def get_input():
    position = 0
    while True:
        try:
            position = int(input("Please enter your position 0-2: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    return position


def user_input():
    while True:
        positions = [get_input(), get_input()]

        if is_position_valid(positions):
            break
        else:
            print("Bad position")
    return positions


def is_it_draw():
    for oneList in gameBoard:
        if ' ' in oneList:
            return False
    else:
        print("It's a draw!")
        return True


def check_line():
    i = 0
    j = 0
    while j < 3:
        line = []
        while i < 3:
            line.append(gameBoard[i][j])
            i += 1
        if len(set(line)) == 1 and ' ' not in line:
            return True
        j += 1
        i = 0
    return False


def check_diagonal():
    first_cross = [gameBoard[0][0], gameBoard[1][1], gameBoard[2][2]]
    second_cross = [gameBoard[0][2], gameBoard[1][1], gameBoard[2][0]]
    if (len(set(first_cross)) != 1 or ' ' in first_cross) and (len(set(second_cross)) != 1 or ' ' in second_cross):
        return False
    return True


def check_row():
    for boardLine in gameBoard:
        if len(set(boardLine)) == 1 and ' ' not in boardLine:
            return True


def is_it_win(player_one):
    if check_row() or check_line() or check_diagonal():
        if player_one:
            print('x win')
            return True
        else:
            print('o win')
            return True
    return False


def is_position_valid(positions):
    # if position it's out of game boards returns false
    if (positions[0] < 0 or positions[0] > 2) or (positions[1] < 0 or positions[1] > 2):
        return False
    # if this cell is not empty then return false
    elif gameBoard[positions[0]][positions[1]] != ' ':
        return False
    else:
        return True


def play_game():
    # list of game plan
    global gameBoard
    gameBoard = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player_one = choose_players_signs()
    # Game is running till one player wins or game board is full and then it's a draw
    run_game(player_one)


def run_game(player_one):
    print("TIC TAC TOE GAME STARTS!")
    while True:
        positions = user_input()
        # put sign on cell selected by user if player one is true than it's a X otherwise O
        if player_one:
            gameBoard[positions[0]][positions[1]] = 'x'
        else:
            gameBoard[positions[0]][positions[1]] = 'o'

        # switch players
        print_game_board(gameBoard)
        if is_it_win(player_one):
            break
        player_one = not player_one

        if is_it_draw():
            break
    play_again()


def play_again():
    users_answer = (input("Do you want to play again? Y/N: ")).upper()
    if users_answer == 'Y':
        play_game()
    else:
        print("Thanks for playing!")


def choose_players_signs():
    question = "Player do you want to play like x or o?"
    # player one(X)
    while True:
        player_choice = input(question).lower()
        if player_choice == 'x':
            player_one = True
            break
        elif player_choice == 'o':
            player_one = False
            break
    clear()
    return player_one


play_game()
