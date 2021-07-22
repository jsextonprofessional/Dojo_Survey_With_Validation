from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
from model import User

app = Flask(__name__)
app.secret_key = 'yeetyoink'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def insert_user():
    if not User.registration_validation(request.form):
        return redirect('/')
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    User.insert_user(request.form)
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html', name = session['name'], location = session['location'], language = ['language'], comment = session['comment'])

if __name__=="__main__":
    app.run(debug=True)
