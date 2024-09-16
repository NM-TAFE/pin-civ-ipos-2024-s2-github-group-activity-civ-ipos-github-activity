from flask import Flask, render_template, request, redirect, url_for
from game import Game
from board import Board


app = Flask(__name__)

# Initialise game board and current player
game = Game()
board = Board(3, 3)

# NOTE: you cannot use this answer in Portfolio Part 2

@app.route('/')
def index():
    winner = board.check_winner()
    draw = board.check_draw()
    current_player = game.CurrentPlayer
    return render_template('index.html', board=board, current_player=current_player, winner=winner, draw=draw)


@app.route('/play/<int:cell>')
def play(cell):
    # breakpoint()

    if board[cell] == ' ':
        board[cell] = game.CurrentPlayer
        if not board.check_winner():
            game.CurrentPlayer = 'O' if game.CurrentPlayer == 'X' else 'X'
    return redirect(url_for('index'))


@app.route('/reset')
def reset():

    # board = Board(3, 3)
    # current_player = 'X'
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
