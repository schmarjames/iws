class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://schmarjames:4645Leclaire@iwstest.c4fzevenhymc.us-west-2.rds.amazonaws.com:3306/iwsdb"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://schmarjames:4645Leclaire@iwstest.c4fzevenhymc.us-west-2.rds.amazonaws.com:3306/iwsdb"
    SQLALCHEMY_ECHO = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://schmarjames:4645Leclaire@iwstest.c4fzevenhymc.us-west-2.rds.amazonaws.com:3306/iwsdb"
    SQLALCHEMY_ECHO = False
