# External dependencies
from flask import Flask, request, render_template, redirect, url_for, session

# Internal dependencies
from routes.routes import init_app

app = Flask(__name__)
app.secret_key = 'secret'
init_app(app)


# Main Method
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
    session.clear()