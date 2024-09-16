

class ResultsHandler:
    def __init__(self, board):
        self.board = board
        self.counter_x_player = 0
        self.counter_o_player = 0

    def check_winner(self):

        return None

    def check_draw(self):
        return ' ' not in self.board

    def results_counter(self, winner):
        if winner == 'X':
            print()
            self.counter_x_player += 1
            return self.counter_x_player
        elif winner == 'O':
            self.counter_o_player += 1
            return self.counter_o_player
