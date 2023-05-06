import os


from flask import Flask
from logging.config import dictConfig
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from stock.stock_api import api

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)


def create_app():
    app = Flask(__name__)
    environment_configuration = os.environ["CONFIGURATION_SETUP"]
    app.config.from_object(environment_configuration)
    jwt = JWTManager(app)

    limiter = Limiter(get_remote_address, app=app)

    app.register_blueprint(api, url_prefix="/stock")

    limiter.limit("10/minute")(api)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=3000)
