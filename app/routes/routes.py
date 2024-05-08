
from .webroutes import web_routes

def init_app(app):
    app.register_blueprint(web_routes)
    