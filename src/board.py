class Board:
    def __init__(self, rows, cols):
        self.Rows = rows
        self.Columns = cols
        self.Grid = self.create_grid()

    def create_grid(self):
        grid = []
        for i in range(self.Rows):
            row = []
            for j in range(self.Columns):
                row.append(' ')
            grid.append(row)
        return grid

    def get_move(self, player, move):

        spaces = self.Rows * self.Columns
        grid_position = -1
        for i in range(self.Rows):
            for j in range(self.Columns):
                grid_position += 1
                if grid_position == move and self.Grid[i][j] != ' ':
                    self.Grid[i][j] = player

    def check_winner(self):
        # Winning combinations
        return None

    def check_draw(self):
        return ' ' not in self.Grid
