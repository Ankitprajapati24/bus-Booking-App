from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key
if __name__ == '__main__':
    app.run(debug=True)


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

# Dummy database to store registered users (replace with a real database)
users_db = []

@app.route('/register.html')
def home():
    return 'Welcome to the Bus Booking App'

@app.route('/register', methods=['GET', 'POST'])
def register():
    # ...

    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data, method='sha256')
        users_db.append({'username': username, 'password': password})
        return redirect(url_for('registration_success'))
    return render_template('register.html', form=form)

@app.route('/registration_success')
def registration_success():
    return 'Registration successful!'

if __name__ == '__main__':
    app.run(debug=True)
