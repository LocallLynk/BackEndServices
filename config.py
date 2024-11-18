import os

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    CACHE_TYPE = "SimpleCache"
    DEBUG = True

# to connect to your computer, after root:, you can put your password between the colon and @

class TestingConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_SQLALCHEMY_DATABASE_URI')
    CACHE_TYPE = "SimpleCache"
    TESTING = True