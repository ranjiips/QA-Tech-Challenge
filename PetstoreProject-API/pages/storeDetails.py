import os
import json
import requests
import urllib3
from asyncio.log import logger
from base.baseAPIs import BaseAPIs
from datetime import datetime, timezone

class PetStoreDetails(BaseAPIs):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PetStoreDetails, cls).__new__(cls)
        return cls._instance

    def _initialize(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def orderPetFromStore(self, url, petID, orderQty):
        headers = self.get_header_details()
        print(url)
        filePath = os.path.dirname(os.path.abspath(__file__))
        filePath = os.path.dirname(filePath) + r'\resources\oderPet.json'
        shipDate = self.getShipDate()
        with open(filePath, 'r') as f:
            pet_api = f.read()
            pet_api = pet_api.replace('PET_ID_VALUE', str(petID))
            pet_api = pet_api.replace('ORDER_QUANTITY', str(orderQty))
            pet_api = pet_api.replace('SHIP_DATE_VALUE', str(shipDate))
            pet_api = pet_api.replace('ORDER_STATUS', "placed")
            payload = str(pet_api)
            # print(payload)
            json_object = json.loads(payload)
            logger.info(f'Order Pet payload: {payload}')

        response = self.post_api(headers, url, json_object)
        print('Order placed Successfully')
        idValue = response['id']
        return idValue

    def getShipDate(self):
        # Get the current date and time in UTC
        now = datetime.now(timezone.utc)
        # Format the date string
        date_string = now.strftime("%Y-%m-%dT%H:%M:%S.%f%z")
        return date_string

    def deleteOrderById(self, url, orderID):
        headers = self.get_header_details()
        url = url.replace('ORDER_ID', str(orderID))
        print(url)
        response = self.delete_api(headers, url)
        print(f'Order id {orderID} deleted successfully')



