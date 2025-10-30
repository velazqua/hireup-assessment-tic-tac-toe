# add your code to complete tic tac toe here
GAME_BOARD = [str(x) for x in range(10)]  # Ignore the first item for easier indexing.
PLAYERS = ['X', 'O']
def print_board():
    print(f"{GAME_BOARD[1]} | {GAME_BOARD[2]} | {GAME_BOARD[3]}")
    print("--+---+--")
    print(f"{GAME_BOARD[4]} | {GAME_BOARD[5]} | {GAME_BOARD[6]}")
    print("--+---+--")
    print(f"{GAME_BOARD[7]} | {GAME_BOARD[8]} | {GAME_BOARD[9]}")

def collect_valid_move(player):
    while True:
        move = input(f"Player {player}, enter your move (1-9): ")
        if not move.isdigit():
            print("Invalid input! Please enter a number between 1 and 9.")
            continue
        move = int(move)
        if move < 1 or move > 9:
            print("Out of bounds move! Try again.")
            continue
        if GAME_BOARD[move] in 'XO':
            print("This cell is already occupied! Try again.")
            continue
        return move

def reset_game():
    while True:
        print("Play again? (yes/no)")
        response = input().strip().lower()
        if response == 'yes':
            global GAME_BOARD
            GAME_BOARD = [str(x) for x in range(10)]
            print_board()
            return
        elif response == 'no':
            print("Goodbye!")
            exit()
        else:
            print("Invalid response! Please enter 'yes' or 'no'.")

def play_game():
    for player in PLAYERS:
        while True:
            move = collect_valid_move(player)
            GAME_BOARD[move] = player
            print_board()
            break
        # Check for a win condition
        winning_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                                (1, 4, 7), (2, 5, 8), (3, 6, 9),
                                (1, 5, 9), (3, 5, 7)]
        for combo in winning_combinations: 
            if GAME_BOARD[combo[0]] == GAME_BOARD[combo[1]] == GAME_BOARD[combo[2]] == player:
                print(f"Player {player} wins!")
                reset_game()
                break
        # Check for a draw condition
        if all(cell in 'XO' for cell in GAME_BOARD[1:]):
            print("It's a draw!")
            reset_game()
            break

while True:
    print_board()
    end_game = play_game()
    if end_game:
        break