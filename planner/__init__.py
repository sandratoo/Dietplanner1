from ssl import VERIFY_ALLOW_PROXY_CERTS
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] ="secretkey"

    from .views import views
    app.register_blueprint(views)

    from .auth import auth
    app.register_blueprint(auth, url_prefix="/auth/")

    return app

