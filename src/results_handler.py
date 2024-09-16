
class ResultsHandler:
    def __init__(self, board):
        self.board = board
        self.board_size = len(self.board)

    def check_winner(self):
        if self._check_rows():
            return True
        if self._check_columns():
            return True
        if self._check_diagonals():
            return True
        return False
    def check_draw(self):
        counter = 0
        for row in self.board:
            if all(cell != " " for cell in row):
                counter += 1
        if counter == self.board_size:
            print("It's a tie! Game over.")
            return True
        else:
            return False

    def _check_diagonals(self):
        diagonal_value = self.board[0][0]
        if diagonal_value != " ":
            if all(self.board[i][i] == diagonal_value for i in range(self.board_size)):
                return True
        diagonal_value_reverse = self.board[0][self.board_size - 1]
        if diagonal_value_reverse != " ":
            if all(self.board[i][self.board_size - 1 - i] == diagonal_value_reverse for i in range(self.board_size)):
                return True
        return False

    def _check_rows(self):
        for row in self.board:
            if row[0] != " " and all(cell == row[0] for cell in row):
                return True
            return False

    def _check_columns(self):
        for column in range(self.board_size):
            if self.board[0][column] != " " and all(
                    self.board[row][column] == self.board[0][column] for row in range(self.board_size)):
                return True
            return False