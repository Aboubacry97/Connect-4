from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

player_names = {}

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/game')
def game():
    return render_template('game.html', player1=player_names.get('player1'), player2=player_names.get('player2'))

@app.route('/submit', methods=['POST'])
def submit():
    player1 = request.form['player1']
    player2 = request.form['player2']

    global player_names
    player_names['player1'] = player1
    player_names['player2'] = player2

    return redirect(url_for('game'))

if __name__ == '__main__':
    app.run()
