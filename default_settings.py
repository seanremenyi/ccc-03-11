import os

class Config(object):
    # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://app:testing@localhost:5432/library_api"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = "postgresql+psycopg2://app:testing@localhost:5432/library_api"
        
        if not value:
            raise ValueError("DB_URI is not set!")
    
        return value
    
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True

environment = os.getenv("FLASK_ENV")

if environment == "production":
    app_config =ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()