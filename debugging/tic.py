#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if (
            board[0][col] == board[1][col] ==
            board[2][col] != " "
        ):
            return board[0][col]

    # Check diagonals
    if (
        board[0][0] == board[1][1] ==
        board[2][2] != " "
    ):
        return board[0][0]

    if (
        board[0][2] == board[1][1] ==
        board[2][0] != " "
    ):
        return board[0][2]

    return None


def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        try:
            row = int(
                input(
                    "Enter row (0, 1, or 2) for player "
                    + player + ": "
                )
            )

            col = int(
                input(
                    "Enter column (0, 1, or 2) for player "
                    + player + ": "
                )
            )

            # Check range
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid row or column. Try again.")
                continue

            # Check if spot is free
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            # Place move
            board[row][col] = player

            # Check winner
            winner = check_winner(board)

            if winner:
                print_board(board)
                print("Player " + winner + " wins!")
                break

            # Check draw
            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch player
            if player == "X":
                player = "O"
            else:
                player = "X"

        except ValueError:
            print("Invalid input. Please enter numbers only.")


tic_tac_toe()
