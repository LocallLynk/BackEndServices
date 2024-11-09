class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:rootroot1!@localhost/LocalLynk'
    CACHE_TYPE = "SimpleCache"
    DEBUG = True

# to connect to your computer, after root:, you can put your password between the colon and @