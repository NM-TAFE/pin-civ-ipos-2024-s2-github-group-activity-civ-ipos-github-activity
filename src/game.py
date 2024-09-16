class Game:

    def __init__(self):
        self.board = [' '] * 9
        self.players = None

    def check_winner(self):
        # Winning combinations
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != ' ':
                return self.board[a]
            return None


    def check_draw():
        return ' ' not in board

    def play(self, cell):
        ...