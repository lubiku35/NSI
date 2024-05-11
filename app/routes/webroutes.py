from flask import Blueprint, render_template, request, flash, session
import sys

from model.data_handler  import load_data, calculate_average
from model.register_handler import register_user as reg
from model.login_handler import login_user as log

# Manage user session via cookie
USER = "Guest"

web_routes = Blueprint('web_routes', __name__)

@web_routes.route('/')
def index():
    print(session.get('user'), file=sys.stderr)

    if session.get('user') is None:
        set_session(USER)
        return render_template('index.html', user=session.get('user'))
    else:
        return render_template('index.html', user=session.get('user'))

@web_routes.route('/register')
def register():
    if session.get('user') != "Guest":
        flash('You are already logged in', 'error')
        return render_template('index.html', user=session.get('user'))
    else:
        set_session(USER)    
        return render_template('register.html', user=session.get('user'))

@web_routes.route('/register', methods=['POST'])
def register_user():
    data = request.form.to_dict()
    is_registered = reg(data)

    if is_registered is True: 
        flash('User registered', 'success')
        return render_template('login.html')
    else: 
        flash(f'Registration Failed - {is_registered}', 'error')
        return render_template('register.html')


@web_routes.route('/login')
def login():
    if session.get('user') != "Guest":
        flash('You are already logged in', 'error')
        return render_template('index.html', user=session.get('user'))
    else:
        return render_template('login.html')


@web_routes.route('/login', methods=['POST'])
def login_user():
    data = request.form.to_dict()
    
    is_logged_in = log(data)
    
    if is_logged_in is True:
        flash('Login successful', 'success') 
        set_session(data.get('email'))
        # Redirect to dashboard
        return dashboard()
    else:
        flash(f'Login Failed - {is_logged_in}', 'error')
        set_session("Guest")
        return render_template('login.html', message=f'Login failed - {is_logged_in}')
    
@web_routes.route('/dashboard')
def dashboard():
    if session.get('user') == "Guest":
        flash(f'Please login to access the dashboard', 'error')
        return render_template('login.html')
    else:
        data = load_data()
        average_temp = round(calculate_average(data), 1)
        return render_template('dashboard.html', data=data, average_temp=average_temp)

@web_routes.route('/logout')
def logout():
    set_session("Guest")
    flash('You have been logged out', 'success')
    return render_template('index.html', user=session.get('user'))

@web_routes.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def set_session(user):
    session['user'] = user