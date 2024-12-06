from src.connect_four_game import ConnectFourGame
from pprint import pprint
import os

def main():
    game = ConnectFourGame()
    print("\nWelcome to Connect Four!\n")
    winner = game.check_winner
    while winner is False:
        print(game.check_winner)
        message = ""
        print("############################################\n")
        pprint(game.get_board)
        print("   0  ,  1  ,  2  ,  3  ,  4  ,  5  ,  6  \n")
        position = input(f"Player '{game.get_player}' Please enter the position you would like to play: \n")
        try: 
            message = game.play(int(position))
        except (TypeError, ValueError):
            print("############################################\n\n",f"INVALID '{position}' Please input a number between 0 and {game._max_width}\n")
        if message:
            print(message)
        winner = game.check_winner
    pprint(game.get_board)
    print("   0  ,  1  ,  2  ,  3  ,  4  ,  5  ,  6  \n") 
    print(f"Congraulations! The winners is : {winner}")


def cls():
    os.system('cls' if os.name=='nt' else 'clear')



if __name__ == "__main__":
    main()