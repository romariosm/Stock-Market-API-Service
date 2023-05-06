class Config(object):
    """Base config."""

    DEBUG = False
    TESTING = False
    STOCK_API = "X86NOH6II01P7R24"
    SECRET_KEY = "super_secret"


class ProductionConfig(Config):
    FLASK_ENV = "PROD"


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = "DEV"


class TestingConfig(Config):
    DEBUG = True
    FLASK_ENV = "TESTING"
