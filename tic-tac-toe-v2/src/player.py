class Player:
    def __init__(self, name, symbol, board=None):
        self.name = name
        self.symbol = symbol
        self.board = board #decides what board the player is playing at

    # TODO: get user name and symbol
    def start(self):
        try:
            self.name = input(str("Enter player name: "))
            self.symbol = input(str("Enter player symbol: "))
        except ValueError:
            print("Enter valid input")


    # TODO: get rows and column where the player wants to put symbol
    def play(self):
        pass


