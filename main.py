from flask import Flask
from flask_mysqldb import MySQL
from flask import Blueprint, render_template, request, flash, session, redirect, url_for


app = Flask(__name__)

@app.route('/')
def landing():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')