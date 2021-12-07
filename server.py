from flask import Flask, render_template, request, redirect, session 
import random
app = Flask(__name__)
app.secret_key = 'shhh this is a secret'

@app.route('/')
def index():
    if 'playing' not in session:
        session['playing'] = True
    if 'rand_num' not in session:
        session['rand_num'] = random.randint(1,100)
        print(session['rand_num'])
        print(type(session['rand_num']))

    return render_template('index.html')

@app.route('/guess', methods=["POST"])
def guess():
    session['player_guess']=request.form['number']
    player_guess = int(session['player_guess'])

    if player_guess > session['rand_num']:
        session['color'] = 'red'
        session['message'] = 'Too High, Try Again'

    elif player_guess < session['rand_num']:
        session['color'] = 'red'
        session['message'] = 'Too Low, Try Again'

    else:
        session['color'] = 'greenyellow'
        session['message'] = 'Correct!'
        session['playing'] = False

    return redirect('/')

@app.route('/destroy', methods=['POST'])
def destroy():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)