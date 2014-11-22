class Config(object):
    DEBUG = False
    TESTING = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USERNAME = 'patrickbeeson'
    MAIL_PASSWORD = '6ElevenBicycleC0'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    ADMINS = ['patrickbeeson@gmail.com']
    SERVER_EMAIL_ADDRESS = 'noreply@patrickbeeson.com'
    SECRET_KEY = "\xce0\x95I\x99o\x12\x97\xd6\x85\xdf\xb8z\x03\x13\xc8'?\xeb\xcc\xfb\xe9\xf4\xe5"


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://pbeeson_madlibs:PortlandOR@localhost/madlibs'


class ProductionConfig(Config):
    DEBUG = False
    MAIL_SERVER = ''
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_PORT = 465
    MAIL_USE_SSL = True
