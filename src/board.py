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

    def check_winner(self):
        # Winning combinations
        return None

    def check_draw(self):
        return ' ' not in self.Grid
