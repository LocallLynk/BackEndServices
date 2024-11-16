class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'postgresql://localadminlynk:3RiB0oXyTnknc86nw4kOR2QtZqWYqdDF@dpg-csn5guggph6c73ftfvh0-a.ohio-postgres.render.com/locallynk'
    CACHE_TYPE = "SimpleCache"
    DEBUG = True

# to connect to your computer, after root:, you can put your password between the colon and @

class TestingConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    CACHE_TYPE = "SimpleCache"
    TESTING = True