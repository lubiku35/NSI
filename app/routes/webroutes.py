from flask import Blueprint, render_template

web_routes = Blueprint('web_routes', __name__)

@web_routes.route('/')
def index():
    return render_template('index.html')

@web_routes.route('/register')
def register():
    return render_template('register.html')

@web_routes.route('/login')
def login():
    return render_template('login.html')

@web_routes.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
