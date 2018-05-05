
class Config(object):
    """
    Common configuration
    """

class DevConfig(object):
    """
    Development Configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProdConfig(object):
    """
    Production Configurations
    """
    DEBUG = False
    SQLALCHEMY_ECHO = False


app_config = {
    "dev": DevConfig,
    "prod": ProdConfig
}
