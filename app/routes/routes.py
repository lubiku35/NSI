
from .webroutes import web_routes
from .apiroutes import api_routes

def init_app(app):
    app.register_blueprint(web_routes)
    app.register_blueprint(api_routes)
    