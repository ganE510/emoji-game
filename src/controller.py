from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
import pymysql
import json

app = Flask(__name__)   # initial a flask as server
@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] == 'test@qq.com' and request.form['password']=='testtest':
            return redirect(url_for('hall',username='abc'))
        else:
            error = 'Invalid username/password'
    return render_template('signIn.html', error=error)

@app.route('/signup', methods=['POST','GET'])
def signUp():
    error = None
    if request.method == 'POST':
        if request.form['email']!='test@qq.com':
            return redirect(url_for('hall',username=request.form['nick']))
        else:
            error = 'Invalid username/password'
    return render_template('signUp.html', error=error)

@app.route('/hall')
def hall():
    return render_template('hall.html', username=request.args.get('username'))

@app.route('/onePlayer')
def onePlayer():
    return render_template('game-page.html')

@app.route('/twoPlayer')
def twoPlayer():
    return render_template('game2page.html')

if __name__ == '__main__':
    app.run(debug=True)
    app.run('0.0.0.0', 80)