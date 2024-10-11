import configparser
import os

configReader = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), '..', 'configfiles', 'config.ini')
configReader.read(config_path)

class ConfigReader:
    @staticmethod
    def getBaseURL():
        url=configReader.get('api_info', 'baseURl')
        return url

    @staticmethod
    def getContentType():
        contentType = configReader.get('api_info', 'contentType')
        return contentType

    @staticmethod
    def getAuthorizationCode():
        authorizationCode = configReader.get('api_info', 'authorizationCode')
        return authorizationCode

    @staticmethod
    def get_addPetEndpoint():
        endPoint=configReader.get('petStore','addPetEndpoint')
        return endPoint

    @staticmethod
    def get_updateExistingPetEndpoint():
        endPoint=configReader.get('petStore','updateExistingPetEndpoint')
        return endPoint

    @staticmethod
    def get_findPetByStatusEndpoint():
        endPoint=configReader.get('petStore','findPetByStatusEndpoint')
        return endPoint

    @staticmethod
    def get_findPetByIDEndpoint():
        endPoint = configReader.get('petStore', 'findPetByIDEndpoint')
        return endPoint

    @staticmethod
    def get_deletePetByIDEndpoint():
        endPoint = configReader.get('petStore', 'deletePetByIDEndpoint')
        return endPoint

    @staticmethod
    def get_placeOrderEndpoint():
        endPoint = configReader.get('petOrderStore', 'placeOrder')
        return endPoint

    @staticmethod
    def get_deleteOrderEndpoint():
        endPoint = configReader.get('petOrderStore', 'deleteOrder')
        return endPoint

    @staticmethod
    def get_createUserEndpoint():
        endPoint = configReader.get('userOperations', 'createUser')
        return endPoint

    @staticmethod
    def get_getUserByUserNameEndpoint():
        endPoint = configReader.get('userOperations', 'getUserByUserName')
        return endPoint

    @staticmethod
    def get_deleteUserByUserNameEndpoint():
        endPoint = configReader.get('userOperations', 'deleteUserByUserName')
        return endPoint

    @staticmethod
    def get_loginUserEndpoint():
        endPoint = configReader.get('userOperations', 'loginUser')
        return endPoint

    @staticmethod
    def get_logoutUserEndpoint():
        endPoint = configReader.get('userOperations', 'logoutUser')
        return endPoint
