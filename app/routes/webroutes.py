from flask import Blueprint, render_template, request

from model.data_handler  import load_data, calculate_average

USER = "Guest"

web_routes = Blueprint('web_routes', __name__)

@web_routes.route('/')
def index():
    return render_template('index.html', user=USER)

@web_routes.route('/register')
def register():
    return render_template('register.html')

@web_routes.route('/login')
def login():
    return render_template('login.html')

@web_routes.route('/dashboard')
def dashboard():
    data =  load_data()
    
    items = request.args.get('items', default=len(data), type=int)
    if items < 1: items = 5
   
    data = data[:items]
   
    average_temp = round(calculate_average(data), 1)
    return render_template('dashboard.html', data=data, average_temp=average_temp)

@web_routes.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404