import configparser
import os
basedir = os.path.abspath(os.path.dirname(__file__))

config = configparser.ConfigParser()
config.read('/opt/settings/atfpoc.conf')

POSTGRES_DB_HOST = config['POSTGRES_DB']['POSTGRES_HOST']
POSTGRES_DB_PORT = config['POSTGRES_DB']['POSTGRES_PORT']
POSTGRES_DB_USERNAME = config['POSTGRES_DB']['POSTGRES_USERNAME']
POSTGRES_DB_PASSWORD = config['POSTGRES_DB']['POSTGRES_PASSWORD']
POSTGRES_DB_NAME = config['POSTGRES_DB']['POSTFRES_DB_NAME']
POSTGRES_DB_DRIVER = config['POSTGRES_DB']['POSTGRES_DRIVER']

API_HOST = config['API']['HOST']
API_PORT = config['API']['PORT']

LDAP_HOST = config['LDAP']['HOST']
LDAP_PORT = config['LDAP']['PORT']

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'Test1234'
    SQLALCHEMY_DATABASE_URI = POSTGRES_DB_DRIVER + '://' + POSTGRES_DB_USERNAME + ':' + POSTGRES_DB_PASSWORD \
                              + '@' + POSTGRES_DB_HOST + ':' + POSTGRES_DB_PORT + '/' + POSTGRES_DB_NAME

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True