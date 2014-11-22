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
