from src.connect_four_game import ConnectFourGame
from pprint import pprint
import os


def main():
    game = ConnectFourGame()
    print("\nWelcome to Connect Four!\n")
    winner = game.check_winner
    is_full = False
    while winner is False and is_full is False:
        message = ""
        print("############################################################\n")
        print_board(game.get_board)

        position = input(
            f"Player '{game.get_player.strip()}' Please enter the position you would like to play: \n"
        )
        try:
            message = game.play(int(position) - 1)
        except (TypeError, ValueError):
            print(
                "############################################################\n\n",
                f"INVALID '{position}' Please input a number between 0 and {game._max_width}\n",
            )
        if message:
            print(message)
        winner = game.check_winner
        is_full = game.check_board_is_full

    if winner is not False:
        print_board(game.get_board)
        print(f"Congraulations! The winners is : {winner.strip()}")
    else:
        print_board(game.get_board)
        print("There is no winner")


def print_board(board):
    counter = 0
    for row in board:
        row_str = "|"
        for item in row:
            if not item:
                row_str += "  None |"
            else:
                row_str += f"  {item}   |"  
        print("------------------------------------------------------------")
        print(row_str, counter)
        counter += 1
    print("============================================================")
    print("|   1   |   2   |   3   |   4   |   5   |   6   |   7   |\n")


def cls():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()
