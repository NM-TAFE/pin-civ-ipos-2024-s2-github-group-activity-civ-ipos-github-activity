
class ResultsHandler:
    def __init__(self, board):
        self.board = board
        self.counter_x_player = 0
        self.counter_o_player = 0
        self.board_size = len(self.board)
        self.empty = ' '
        self.DIAGONAL_WIN_CONDITION = [(0, 4, 8), (2, 4, 6)]

    def check_draw(self):
        if self.empty not in self.board:
            return True

    def check_winner(self):
        for row in range(0, 7, 3):
            if self.board[row] == self.board[row + 1] == self.board[row + 2] != self.empty:
                return self.board[row]

        for column in range(0, 3, 1):
            if self.board[column] == self.board[column + 3] == self.board[column + 6] != self.empty:
                return self.board[column]

        for wc in self.DIAGONAL_WIN_CONDITION:
            if self.board[wc[0]] == self.board[wc[1]] == self.board[wc[2]] != self.empty:
                return self.board[wc[0]]

    def reset(self):
        # Reset the board to empty spaces and set the current player to 'X'
        self.board = [' ' for _ in range(9)]
        return self.board

