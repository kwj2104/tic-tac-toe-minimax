from board import Board

if __name__ == "__main__":
    b = Board()
    player = 2

    while True:
        is_complete, is_tie = b.check_board()
        if is_complete:
            break

        if player == 2:
            player = 1
        else:
            player = 2

        while True:
            try:
                player_input = int(input("Player %d : Enter your move\n" % player))
                if 1 <= player_input <= 9:
                    row, column = (player_input - 1) // 3, (player_input - 1) % 3
                    if b.board[row][column] == 0:
                        break
                    else:
                        print("Position already taken - try again")
                else:
                    print("Position index out of range - try again")
            except Exception:
                print("Input was not a digit - try again")

        b.board = (row, column, player, player)
        b.display_board()

    if not is_tie:
        print("Winner is %s" % player)
    else:
        print("Tie Game")



