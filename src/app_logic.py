from flask import render_template, redirect, url_for
from results_handler import ResultsHandler


class AppLogic:
    def __init__(self, app):
        self.app = app
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.result_handler = ResultsHandler(self.board)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def index():
            winner = self.result_handler.check_winner()
            draw = self.result_handler.check_draw()
            x_wins = 0
            o_wins = 0
            return render_template('index.html', board=self.board,
                                   current_player=self.current_player, winner=winner, draw=draw,
                                   x_wins=x_wins, o_wins=o_wins)

        @self.app.route('/play/<int:cell>')
        def play(cell):
            if self.board[cell] == ' ':
                self.board[cell] = self.current_player
                if not self.result_handler.check_winner():
                    self.current_player = 'O' if self.current_player == 'X' else 'X'
            return redirect(url_for('index'))

        @self.app.route('/reset')
        def reset():
            # self.board = [' '] * 9
            self.board = self.result_handler.reset()
            self.current_player = 'X'
            return redirect(url_for('index'))

