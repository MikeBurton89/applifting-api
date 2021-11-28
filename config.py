import os


class Config():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


class DevConf(Config):
    DEBUG = True


class TestConf(Config):
    DEBUG = True
    TESTING = True


class ProdConf(Config):
    SQLALCHEMY_DATABASE_URI = None  # TODO add the address given by the hosting
