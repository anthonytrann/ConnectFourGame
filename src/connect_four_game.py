from pprint import pprint
class ConnectFourGame:
    
    def __init__(self, rows: int = 6, columns: int = 7):
        self.board = []
        self._player_x = True
        self.winner = False
        self._max_height = rows - 1
        self._max_width = columns - 1 
        self._board_dict = {i : 0 for i in range(columns)}
        for _ in range(rows):
            self.board.append([None for _ in range(columns)])

    @property
    def get_board(self):
        # pprint(self._board_dict)
        return self.board

    @property
    def get_player(self):
        if self._player_x is True:
            return "x"
        else:
            return "o"

    def play(self, position: int):
        message = ""
        if position >= 0 and position <= self._max_width:
            next_available_row = self._max_height - self._board_dict[position]
            if next_available_row >= 0:
                self.board[next_available_row][position] = self.get_player
                self._board_dict[position] += 1
                self._player_x = not self._player_x
            else:
                message = f"This position '{position}' is full."
        else:
            message = f"Incorrect position please input a number between 0 and {self._max_width}."
        return message

    def _horizontal_check(self, current_board):
        counter = -1
        in_a_row = 1
        for row in current_board:
            counter = row[0]
            for i in range(1, len(row)):
                if counter == row[i] and counter is not None:
                    in_a_row += 1
                else:
                    in_a_row = 1
                    counter = row[i]
                if in_a_row == 4:
                    return counter
                # print(counter, in_a_row)
        return False

    def _vertical_check(self, current_board):
        counter = -1
        in_a_row = 1
        for j in range(0, len(current_board[0])):
            counter = current_board[0][j]
            for i in range(len(current_board)):
                if counter == current_board[i][j] and counter is not None:
                    in_a_row += 1
                else:
                    in_a_row = 1
                    counter = current_board[i][j]
                if in_a_row == 4:
                    return counter
        return False
        

    def _diagonal_check_TLBR(self, current_board):
        counters = ["x", "o"]
        in_a_row = 1
        y = 0
        x = 0
        for counter in counters:
            while not (x > (len(current_board) - 3)):
                while not (y > (len(current_board[0]) - 3)):
                    i = x
                    j = y
                    counter = current_board[i][j]
                    for _ in range(3):
                        i += 1
                        j += 1
                        if j < len(current_board[0]) and i < len(current_board):
                            if counter == current_board[i][j] and counter is not None:
                                in_a_row += 1
                            else:
                                in_a_row = 1
                            if in_a_row == 4:
                                return counter
                    y += 1
                x += 1
                y = 0
        return False

    def _diagonal_check_TRBL(self, current_board):
        counters = ["x", "o"]
        in_a_row = 1
        y = len(current_board[0]) - 1
        x = 0
        for counter in counters:
            while not (x > (len(current_board) - 3)):
                while not (y < 3):
                    print(x, y, "this is x and y")
                    i = x
                    j = y
                    counter = current_board[i][j]
                    for _ in range(3):
                        i += 1
                        j -= 1
                        if j < len(current_board[0]) and i < len(current_board):
                            if counter == current_board[i][j] and current_board[i][j] is not None:
                                in_a_row += 1
                            else:
                                in_a_row = 1
                            if in_a_row == 4:
                                print(x, y)
                                print(i, j)
                                return counter
                    y -= 1
                x += 1
                y = len(current_board[0]) - 1
        return False

    @property
    def check_winner(self):
        checks = [
            self._horizontal_check(self.board),
            self._vertical_check(self.board),
            self._diagonal_check_TLBR(self.board),
            self._diagonal_check_TRBL(self.board),
        ]
        print(checks)
        if "x" in checks:
            return "x"
        elif "o" in checks:
            return "o"
        else:
            return False




# def main():
#     game = ConnectFourGame()
#     game.get_board


# if __name__ == '__main__':
#     main()