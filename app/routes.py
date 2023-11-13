from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('templates/register.html')
def home():
    return 'Welcome to the Bus Booking App'

@app.route('templates/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return 'Registration successful'
    return render_template('register.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            return 'Login successful'
        else:
            return 'Login failed'

    return render_template('login.html')
