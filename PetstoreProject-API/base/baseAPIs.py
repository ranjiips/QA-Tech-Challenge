import json
import os
from asyncio.log import logger
import certifi
import requests
from _pytest.outcomes import fail

from utilities.readConfig import ConfigReader

class BaseAPIs:

    def get_header_details(self):
        contentType = ConfigReader.getContentType()
        authCode = ConfigReader.getAuthorizationCode()
        headers = {"Content-Type": f"{contentType}", "Authorization": f"{authCode}"}
        return headers

    def post_api(self, header, url, apiData):
        try:
            # Send the POST request
            response = requests.post(url, json=apiData, headers=header, verify=False)
            # Check if the response was successful
            if response.status_code == 200:
                print(response.status_code)
                print('POST Message Successfully')
                return response.json()
            else:
                print("Error:", response.status_code, response.text)
                logger.info(f'POST request Failed with status code: {response.status_code} ')
                raise ValueError(f'POST request Failed with status code: {response.status_code}')
        except requests.exceptions.RequestException as e:
            logger.info('Failed to POST the payload')
            print("Error message:", e)

    def put_api(self, header, url, apiData):
        try:
            # Send the put request
            response = requests.put(url, json=apiData, headers=header, verify=False)
            # Check if the response was successful
            if response.status_code == 200:
                print(response.status_code)
                logger.info('Put Message Successfully')
                return response.json()
            else:
                print("Error:", response.status_code, response.text)
                logger.info(f'Put request Failed with status code: {response.status_code} ')
                raise ValueError(f'Put request Failed with status code: {response.status_code}')
        except requests.exceptions.RequestException as e:
            logger.info('Failed to Put the payload')
            print("Error message:", e)

    def get_response(self, header, url):
        try:
            response = requests.get(url, headers=header, verify=False)
            if response.status_code != 200:
                print(f'GET request Failed with status code: {response.status_code}')
                data = json.loads(response.text)
                fail(f"Error message: {data['message']}")
            elif response.status_code == 200:
                print('Successfully pull the value')
            return response.text
        except requests.exceptions.RequestException as e:
            logger.info('Failed to get the response')
            print("Error message:", e)

    def delete_api(self, header, url):
        try:
            response = requests.delete(url, headers=header, verify=False)
            if response.status_code != 200:
                print(f'Delete request Failed with status code: {response.status_code}')
                data = json.loads(response.text)
                fail(f"Error message: {data['message']}")
            elif response.status_code == 200:
                print('Successfully deleted the value')
            return response.text
        except requests.exceptions.RequestException as e:
            logger.info('Failed to delete the value')
            print("Error message:", e)


