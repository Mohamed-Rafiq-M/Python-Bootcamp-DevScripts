import random

print("\t\tTIC-TAC-TOE")
player_1 = input("\n1st Player Name : ").upper()
player_2 = input("2nd Player Name : ").upper()
players = [player_1, player_2]

def display_board(board):
    print(f'''
          \t\t     POSITIONS\n
          \t{board[7]}|{board[8]}|{board[9]}  \t  \t7 | 8 | 9
          \t---+---+---            ---+---+---    
          \t{board[4]}|{board[5]}|{board[6]}  \t=>\t4 | 5 | 6
          \t---+---+---            ---+---+---     
          \t{board[1]}|{board[2]}|{board[3]}  \t  \t1 | 2 | 3
          ''')

def valid_input():
    while True:
        place_marker = input("Enter the Position number : ")
        if place_marker != " ":
            if place_marker.isdigit():
                if int(place_marker) in range(1, 10):
                    return int(place_marker)
                print("Invalid Position")
            else:
                print("Enter numbers between 1-9")
                continue

def valid_position(turn, board, player):
    print(f"{turn} chance")
    position = valid_input()
    while True:
        if board[position] == '   ':
            board[position] = ' ' + dict(player)[turn] + ' '
            display_board(board)
            break
        else:
            print("The position is already filled")
            position = valid_input()

def check_win(board):
    check = 0
    if board[1] == board[2] == board[3] != '   ' or board[4] == board[5] == board[6] != '   ' or board[7] == board[8] == board[9] != '   ' or board[1] == board[4] == board[7] != '   ' or board[2] == board[5] == board[8] != '   ' or board[3] == board[6] == board[9] != '   ' or board[1] == board[5] == board[9] != '   ' or board[3] == board[5] == board[7] != '   ':
        check = 1

    return check

def match(board, mark, player):
    mark_1, mark_2 = mark[random.randint(0, 1)]
    player_turn = 0 if mark_1 == 'X' else 1
    print(f"\t{player[player_turn][0]} plays first")
    display_board(board)
    for i in range(9):
        if not i % 2:
            turn = player[player_turn][0]
            valid_position(turn, board, player)
        else:
            turn = player[not player_turn][0]
            valid_position(turn, board, player)
        if i >= 4:
            if check_win(board):
                display_board(board)
                print(f"\tCongratulation !!!\n\t{turn} WON the Match")
                break
        if i == 8:
            print("It's a Tie")

def main():
    mark = [('O', 'X'), ('X', 'O')]
    replay = "yes"
    while replay == "yes":
        board = ['', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']
        print("\nLet the Match Begin !!!\nBest of Luck to both the Players !!!")
        num = random.randint(0, 1)
        player = [(players[num], 'X'), (players[not num], 'O')]
        print(f"\n\t{players[num]} is X and {players[not num]} is O")
        match(board, mark, player)
        replay = input("\nDo you want to play again? (yes/no)\n").lower()

if __name__ == '__main__':
    main()
    print("\n\t\tThanks for playing !!!")
