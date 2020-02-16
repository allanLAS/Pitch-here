
import os


class Config:
    """"""
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://allan:852456@localhost/pitch'
    SECRET_KEY = os.environ.get('SECRET_KEY')


   # simple mde configurations
   SIMPLEMDE_JS_IIFE = True
   SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    """"""
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://allan:852456@localhost/pitch'
    """"""

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}