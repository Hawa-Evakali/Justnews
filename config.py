import os

class Config:
    '''
    General configuration parent class
    '''
    CATEGORY_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_API_BASE_URL ='https://newsapi.org/v2/{}?apiKey={}&language=en'
    NEWS_API_KEY='24a12bd6288b4a8f896d082dadbedb45'
    SECRET_KEY="jkjj"



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}