from src.connect_four_game import ConnectFourGame
from pytest import mark, fixture
from pprint import pprint


@fixture
def board():
    return ConnectFourGame()


@mark.context("testing Board initialisation")
class TestBoardInitialisation:
    @mark.it("creates the initial board with None values")
    def test_board_init(self, board):
        assert board.get_board == [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
        ]


@mark.context("Testing get_player method")
class TestGetPlayer:
    @mark.it("get's the current player playing - first player is 'x' ")
    def test_get_player_1(self, board):
        assert board.get_player == "x"


@mark.context("Testing play method")
class TestPlay:
    @mark.it("checks if the first play method call works")
    def test_play_1(self, board):
        assert board.get_player == "x"
        board.play(3)
        assert board.get_player == "o"
        assert board.get_board == [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, "x", None, None, None],
        ]

    @mark.it("should not play if the position given is not within the range")
    def test_play_2(self, board):
        returned_message = board.play(-1)
        assert board.get_player == "x"
        assert board.get_board == [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
        ]
        assert (
            returned_message
            == "Incorrect position please input a number between 0 and 6."
        )
        board.play(9)
        assert board.get_player == "x"
        assert board.get_board == [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
        ]
        assert (
            returned_message
            == "Incorrect position please input a number between 0 and 6."
        )

    @mark.it("returns no availablity when column is full")
    def test_play_3(self, board):
        board.play(3)
        board.play(3)
        board.play(3)
        board.play(3)
        board.play(3)
        board.play(3)
        # pprint(board.get_board)
        assert board.get_board == [
            [None, None, None, "o", None, None, None],
            [None, None, None, "x", None, None, None],
            [None, None, None, "o", None, None, None],
            [None, None, None, "x", None, None, None],
            [None, None, None, "o", None, None, None],
            [None, None, None, "x", None, None, None],
        ]
        returned_message = board.play(3)
        assert returned_message == "This position '3' is full."


@mark.context("testing if there is a horizontal win or not")
class TestHorizontalCheck:
    @mark.it("returns the correct winner")
    def test_horizontal_check_TLBR(self, board):
        test_board = [
            ["x", "x", "x", "x", None, None, None],
        ]
        result = board._horizontal_check(test_board)
        expected_winner = "x"
        assert expected_winner == result

        test_board = [
            [None, None, None, "o", "o", "o", "o"],
        ]
        result = board._horizontal_check(test_board)
        expected_winner = "o"
        assert expected_winner == result

        test_board = [
            ["o", "x", "o", "o", "o", "o", "x"],
        ]
        result = board._horizontal_check(test_board)
        expected_winner = "o"
        assert expected_winner == result

    @mark.it("returns False when there's no winner")
    def test_horizontal_check_2(self, board):
        test_board = [
            [None, None, None, None, None, None, None],
        ]
        result = board._horizontal_check(test_board)
        expected_winner = False
        assert expected_winner == result

        test_board = [
            ["o", "x", "o", "o", "x", "o", "x"],
        ]
        result = board._horizontal_check(test_board)
        expected_winner = False
        assert expected_winner == result


@mark.context("testing if there is a vertical win or not")
class TestVerticalCheck:
    @mark.it("returns the correct winner")
    def test_vertical_check_TLBR(self, board):
        test_board = [
            ["o", None],
            ["o", None],
            ["o", None],
            ["o", None],
            ["x", None],
            ["o", None],
            ["x", None],
        ]
        result = board._vertical_check(test_board)
        expected_winner = "o"
        assert expected_winner == result

        test_board = [
            [None, None],
            [None, None],
            [None, None],
            [None, None],
            ["o", None],
            ["o", None],
            ["o", None],
            ["o", None],
        ]
        result = board._vertical_check(test_board)
        expected_winner = "o"
        assert expected_winner == result

        test_board = [
            [None, None],
            [None, None],
            [None, None],
            [None, None],
            [None, "x"],
            [None, "x"],
            [None, "x"],
            [None, "x"],
        ]
        result = board._vertical_check(test_board)
        expected_winner = "x"
        assert expected_winner == result

    @mark.it("returns False when there's no winner")
    def test_horizontal_check_2(self, board):
        test_board = [
            ["x", "o"],
            ["o", "x"],
            ["x", "o"],
            ["x", "o"],
        ]
        result = board._vertical_check(test_board)
        expected_winner = False
        assert expected_winner == result

        test_board = [
            [None, None],
            [None, None],
            [None, None],
            [None, None],
        ]
        result = board._vertical_check(test_board)
        expected_winner = False
        assert expected_winner == result


@mark.context(
    "testing if there is a diagonal win or not from top left to bottom right (TLBR)"
)
class TestDiagonalCheckTLBR:
    @mark.it("returns the correct winner and the start")
    def test_diagonal_check_tlbr_1(self, board):
        test_board = [
            ["x", None, None, None, None, None, None],
            [None, "x", None, None, None, None, None],
            [None, None, "x", None, None, None, None],
            [None, None, None, "x", None, None, None],
            [None, None, None, None, None, None, None],
        ]
        result = board._diagonal_check_TLBR(test_board)
        expected_winner = "x"
        assert expected_winner == result

    @mark.it("returns the correct winner if the next diagonal")
    def test_diagonal_check_tlbr_2(self, board):
        test_board = [
            [None, "x", None, None, None, None, None],
            [None, None, "x", None, None, None, None],
            [None, None, None, "x", None, None, None],
            [None, None, None, None, "x", None, None],
            [None, None, None, None, None, None, None],
        ]
        result = board._diagonal_check_TLBR(test_board)
        expected_winner = "x"
        assert expected_winner == result

    @mark.it("returns the correct winner if the final first diagonal")
    def test_diagonal_check_tlbr_3(self, board):
        test_board = [
            [None, None, None, "x", None, None, None],
            [None, None, None, None, "x", None, None],
            [None, None, None, None, None, "x", None],
            [None, None, None, None, None, None, "x"],
            [None, None, None, None, None, None, None],
        ]
        result = board._diagonal_check_TLBR(test_board)
        expected_winner = "x"
        assert expected_winner == result

    @mark.it("returns the correct winner next below diagonal")
    def test_diagonal_check_tlbr_4(self, board):
        test_board = [
            [None, None, None, "x", None, None, None],
            ["x", None, None, None, "x", None, None],
            [None, "x", None, None, None, "x", None],
            [None, None, "x", None, None, None, None],
            [None, None, None, "x", None, None, None],
        ]
        result = board._diagonal_check_TLBR(test_board)
        expected_winner = "x"
        assert expected_winner == result

    @mark.it("returns the correct winner final below diagonal")
    def test_diagonal_check_tlbr_5(self, board):
        test_board = [
            [None, None, None, "x", None, None, None],
            ["x", None, None, None, "x", None, None],
            [None, "x", None, "x", None, "x", None],
            [None, None, "x", None, "x", None, None],
            [None, None, None, None, None, "x", None],
            [None, None, None, None, None, None, "x"],
        ]
        result = board._diagonal_check_TLBR(test_board)
        expected_winner = "x"
        assert expected_winner == result

    @mark.it("returns the correct winner for 'o'")
    def test_diagonal_check_tlbr_6(self, board):
        test_board = [
            [None, None, None, "o", None, None, None],
            ["o", None, "x", None, "x", None, None],
            [None, "x", None, "o", None, "0", None],
            [None, None, "o", None, "o", None, None],
            [None, None, None, None, None, "o", None],
            [None, None, None, None, None, None, "o"],
        ]
        result = board._diagonal_check_TLBR(test_board)
        expected_winner = "o"
        assert expected_winner == result

    @mark.it("returns false if there's no diagonal win")
    def test_diagonal_check_tlbr_6(self, board):
        test_board = [
            [None, None, None, "o", None, None, None],
            ["o", None, "x", None, "x", None, None],
            [None, "x", None, "o", None, "0", None],
            [None, None, "o", None, "o", None, None],
            [None, None, None, None, None, "x", None],
            [None, None, None, None, None, None, "o"],
        ]
        result = board._diagonal_check_TLBR(test_board)
        expected_winner = False
        assert expected_winner == result


@mark.context(
    "testing if there is a diagonal win or not from top right to bottom left (TRBL)"
)
class TestDiagonalCheckTRBL:
    @mark.it("returns the correct winner from the start")
    def test_diagonal_check_trbl_1(self, board):
        test_board = [
            [None, None, None, None, None, None, "x"],
            [None, None, None, None, None, "x", None],
            [None, None, None, None, "x", None, None],
            [None, None, None, "x", None, None, None],
            [None, None, None, None, None, None, None],
        ]
        result = board._diagonal_check_TRBL(test_board)
        expected_winner = "x"
        assert expected_winner == result

    @mark.it("returns the correct winner next in line")
    def test_diagonal_check_trbl_2(self, board):
        test_board = [
            [None, None, None, "x", None, None, None],
            [None, None, "x", None, None, None, None],
            [None, "x", None, None, None, None, None],
            ["x", None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
        ]
        result = board._diagonal_check_TRBL(test_board)
        expected_winner = "x"
        assert expected_winner == result

    @mark.it("returns the correct winner next bottom line")
    def test_diagonal_check_trbl_3(self, board):
        test_board = [
            [None, None, None, None, None, "x", None],
            [None, None, None, None, None, None, "x"],
            [None, None, None, None, None, "x", None],
            [None, None, None, None, "x", None, None],
            [None, None, None, "x", None, None, None],
            [None, None, None, None, None, None, None],
        ]
        result = board._diagonal_check_TRBL(test_board)
        expected_winner = "x"
        assert expected_winner == result

    @mark.it("returns the correct winner final bottom line")
    def test_diagonal_check_trbl_4(self, board):
        test_board = [
            [None, None, None, None, None, None, None],
            [None, None, None, "x", None, None, None],
            [None, None, "x", None, None, None, None],
            [None, "x", None, None, None, None, None],
            ["x", None, None, None, None, None, None],
        ]
        result = board._diagonal_check_TRBL(test_board)
        expected_winner = "x"
        assert expected_winner == result

    @mark.it("returns the correct winner for 'o'")
    def test_diagonal_check_trbl_5(self, board):
        test_board = [
            [None, None, None, None, None, None, None],
            [None, None, None, "o", None, None, None],
            [None, None, "o", None, None, None, None],
            [None, "o", None, None, None, None, None],
            ["o", None, None, None, None, None, None],
        ]
        result = board._diagonal_check_TRBL(test_board)
        expected_winner = "o"
        assert expected_winner == result

    @mark.it("returns false when there's on diaginal win")
    def test_diagonal_check_trbl_6(self, board):
        test_board = [
            [None, None, None, None, None, None, None],
            [None, None, None, "x", None, None, None],
            [None, None, "x", None, None, None, None],
            [None, "x", None, None, None, None, None],
            [None, None, None, None, None, None, None],
        ]
        result = board._diagonal_check_TRBL(test_board)
        expected_winner = False
        assert expected_winner == result


class TestCheckWinner:
    def test_check_winner(self):
        pass