import os
import json
import requests
import urllib3
from asyncio.log import logger
from base.baseAPIs import BaseAPIs


class PetDetails(BaseAPIs):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PetDetails, cls).__new__(cls)
        return cls._instance

    def _initialize(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def addNewPet(self, url):
        headers = self.get_header_details()
        print(url)
        filePath = os.path.dirname(os.path.abspath(__file__))
        filePath = os.path.dirname(filePath) + r'\resources\addPetStore.json'
        with open(filePath, 'r') as f:
            pet_api = f.read()
            pet_api = pet_api.replace('CATEGORY_NAME', "Animals")
            pet_api = pet_api.replace('PET_NAME', "Cheetha")
            pet_api = pet_api.replace('URL_VALUE', "https://pixabay.com/photos/cheetah-animal-wildlife-mammal-3749168/")
            pet_api = pet_api.replace('TAG_NAME', "Runner")
            payload = str(pet_api)
            # print(payload)
            json_object = json.loads(payload)
            print(f'Add Pet payload: {payload}')
        response = self.post_api(headers, url, json_object)
        # print(response)
        idValue = response['id']
        return idValue

    def getPetById(self, url, petID):
        headers = self.get_header_details()
        url = url.replace('PET_ID', str(petID))
        print(url)
        response = self.get_response(headers, url)
        print(response)

        # Extract the required values
        data = json.loads(response)
        pet_id = data['id']
        category_name = data['category']['name']
        pet_name = data['name']
        status = data['status']

        # Print the extracted values
        print(f"Pet ID: {pet_id}")
        print(f"Category Name: {category_name}")
        print(f"Pet Name: {pet_name}")
        print(f"Status: {status}")

    def getPetByStatus(self, url, status):
        headers = self.get_header_details()
        url = url.replace('STATUS_VALUE', str(status))
        print(url)
        response = self.get_response(headers, url)
        # print(response)

        # Extract and print the required values
        data = json.loads(response)
        print("-" * 40)
        for item in data:
            pet_id = item['id']
            category_name = item['category']['name']
            pet_name = item['name']
            status = item['status']

            print(f"ID: {pet_id}")
            print(f"Category Name: {category_name}")
            print(f"Pet Name: {pet_name}")
            print(f"Status: {status}")
            print("-" * 40)



