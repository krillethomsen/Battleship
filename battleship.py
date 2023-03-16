from random import randint

board = []
counter = 5

for x in range(5):
    board.append(["O"] * 5)

def print_board(board_in):
    for row in board_in:
        print(" ".join(row))

print("Let's play Battleship!")
print_board(board)

def random_row(board_in):
    return randint(0, len(board_in) -1)

def random_col(ship_row):
    return randint(0, len(ship_row) -1)

ship_row = random_row(board)
ship_col = random_col(board[ship_row])

for turn in range(5):
    guess_row = int(input("\nGuess row: "))
    guess_col = int(input("Guess column: "))

    def check_board(guess_row, guess_col):
        board[ship_row][ship_col] = "S"
        if board[guess_row][guess_col] == "S":
            return True
        board[ship_row][ship_col] = "O"
        
    try:
        if check_board(guess_row-1, guess_col-1) == True:
            print("\nCongratulations! You sank the ship!")
            break

        elif board[guess_row-1][guess_col-1] == "X":
            print("\nYou already guessed that.\nTry again.")

        else:
            print("\nSorry, you missed.")
            print("{} attempts remaining.".format(counter -1))
            board[guess_row-1][guess_col-1] = "X"
            print_board(board)
            counter -= 1
    
    except IndexError:
        print("That's not even in the ocean. \nTry again: ")

if counter < 1:
    print("\nGAME OVER")
    board[ship_row][ship_col] = "S"

print_board(board)
