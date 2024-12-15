from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialise game board and current player
board = [' '] * 9
current_player = 'X'
results = {'X': 0, 'O': 0}

# NOTE: you cannot use this answer in Portfolio Part 2
def check_winner():
    """
    Check for a winner in the game.
    This function checks all possible winning combinations on the board.
    Returns:
        str or None: 
            - If a player has won, returns the marker ('X' or 'O') of the winning player.
            - If there is no winner yet, returns None.
    """
    winning_conditions = [[0, 4, 8], [2, 4, 6],  # diagonals
                          [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
                          [0, 1, 2], [3, 4, 5], [6, 7, 8]]  # rows

    for combo in winning_conditions:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            return board[combo[0]]

    return None


def tally_wins(winner):
    if winner:
        results[winner] += 1


def check_draw():
    """
    Check if current state is a draw.

    It's a draw if the board does not have any free moves and there is no winner.

    Returns:
        Todo ?
    """
    return ' ' not in board


@app.route('/')
def index():
    """
    Load the game board and display the current game state.

    Renders the 'index.html' template with the current state of the game including
    the board, the current player, and whether there's a winner or a draw.

    """
    winner = check_winner()
    draw = check_draw()
    return render_template('index.html', board=board, current_player=current_player, winner=winner, draw=draw, results=results)


@app.route('/play/<int:cell>')
def play(cell):
    """
    Updates the board with the current player's move if the selected cell is empty.
    """
    # breakpoint()
    global current_player
    if board[cell] == ' ':
        board[cell] = current_player
        winner = check_winner()
        if winner:
            tally_wins(winner)
        if not check_winner():
            current_player = 'O' if current_player == 'X' else 'X'
    return redirect(url_for('index'))


@app.route('/reset')
def reset():
    """
    Reset the game to the initial state.
    """
    global board, current_player
    board = [' '] * 9
    current_player = 'X'
    return redirect(url_for('index'))


app.run(debug=True)
