import os
import json
import requests
import urllib3
from asyncio.log import logger
from base.baseAPIs import BaseAPIs
from datetime import datetime, timezone

class UserDetails(BaseAPIs):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserDetails, cls).__new__(cls)
        return cls._instance

    def _initialize(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def createUser(self, url):
        headers = self.get_header_details()
        print(url)
        filePath = os.path.dirname(os.path.abspath(__file__))
        filePath = os.path.dirname(filePath) + r'\resources\createUser.json'
        with open(filePath, 'r') as f:
            user_api = f.read()
            user_api = user_api.replace('USER_NAME_VALUE', "ranjith85")
            user_api = user_api.replace('FIRST_NAME_VALUE', "Ranjith")
            user_api = user_api.replace('LAST_NAME_VALUE', "Kumar")
            user_api = user_api.replace('EMAIL_VALUE', "ranjith@gmail.com")
            user_api = user_api.replace('PASSWORD_VALUE', "Oct@2024")
            user_api = user_api.replace('PHONE_VALUE', "9876543210")
            payload = str(user_api)
            # print(payload)
            json_object = json.loads(payload)
            print(f'Create User payload: {payload}')

        response = self.post_api(headers, url, json_object)
        print('User created Successfully')
        # print(response)

    def deleteUserByUsername(self, url, userName):
        headers = self.get_header_details()
        url = url.replace('USER_NAME', str(userName))
        print(url)
        response = self.delete_api(headers, url)
        print(f'User name: {userName} deleted successfully')

    def getUserDetails(self, url, userName):
        headers = self.get_header_details()
        url = url.replace('USER_NAME', userName)
        print(url)
        response = self.get_response(headers, url)
        # print(response)

        # Extract the required values
        data = json.loads(response)
        username = data['username']
        firstName = data['firstName']
        lastName = data['lastName']
        email = data['email']
        phone = data['phone']

        # Print the extracted values
        print(f"User Name: {username}")
        print(f"First Name: {firstName}")
        print(f"Last Name: {lastName}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")




