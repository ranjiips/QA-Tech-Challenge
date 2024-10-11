import configparser
import os

configReader = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), '..', 'configfiles', 'config.ini')
configReader.read(config_path)

class ConfigReader:
    @staticmethod
    def getApplicationURL():
        url=configReader.get('settings', 'url')
        return url

    @staticmethod
    def get_Username():
        username=configReader.get('settings','username')
        return username

    @staticmethod
    def get_Password():
        password=configReader.get('settings','password')
        return password

    @staticmethod
    def get_LockedUsername():
        username=configReader.get('settings','lockedUser')
        return username
