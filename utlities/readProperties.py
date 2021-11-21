import configparser

config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class ReadConfig():

    @staticmethod
    def getApplicationUrl():
        baseUrl=config.get('common info','baseUrl')
        return baseUrl

    @staticmethod
    def getApplicationUserName():
        username = config.get('common info', 'userName')
        return username

    @staticmethod
    def getLoginPassword():
        password = config.get('common info', 'password')
        return password