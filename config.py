import os

# TODO add testing and production config


class Config():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


class DevConf(Config):
    DEBUG = True
