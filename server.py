from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'yeetyoink'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['yourname']=request.form['yourname']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment']=request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')



if __name__=="__main__":
    app.run(debug=True)
