import os
from dotenv import load_dotenv

load_dotenv()
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    CACHE_TYPE = "SimpleCache"
    DEBUG = True
    PROPAGATE_EXCEPTIONS = True
# # to connect to your computer, after root:, you can put your password between the colon and @

# class TestingConfig:
#     SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_SQLALCHEMY_DATABASE_URI')
#     CACHE_TYPE = "SimpleCache"
#     TESTING = True

# class DevelopmentConfig:
#     SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Groovin@localhost/LocalLynk'
#     CACHE_TYPE = "SimpleCache"
#     DEBUG = True