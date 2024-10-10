import logging
import pytest
import unittest

from pages.userDetails import UserDetails
from utilities.readConfig import ConfigReader

# Execution Command:
# python -m pytest tests/user_test.py -v -s --html=reports/userReport.html

@pytest.mark.user
class UserTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.baseURL = ConfigReader.getBaseURL()
        self.ud = UserDetails()

    @pytest.mark.createuser
    @pytest.mark.run(order=1)
    def test_createUser(self):
        print("*#" * 20)
        print("Create User operation")
        print("*#" * 20)
        createUserEndPointURL = ConfigReader.get_createUserEndpoint()
        self.ud.createUser(self.baseURL + createUserEndPointURL)

    @pytest.mark.getUser
    @pytest.mark.run(order=2)
    def test_getUser(self):
        print("*#" * 20)
        print("Get User Details")
        print("*#" * 20)
        createUserEndPointURL = ConfigReader.get_createUserEndpoint()
        self.ud.createUser(self.baseURL + createUserEndPointURL)
        getUserEndPointURL = ConfigReader.get_getUserByUserNameEndpoint()
        self.ud.getUserDetails(self.baseURL + getUserEndPointURL, "ranjith85")

    @pytest.mark.deleteUser
    @pytest.mark.run(order=3)
    def test_deleteUser(self):
        print("*#" * 20)
        print("Delete User Details")
        print("*#" * 20)
        createUserEndPointURL = ConfigReader.get_createUserEndpoint()
        self.ud.createUser(self.baseURL + createUserEndPointURL)
        deleteUserEndPointURL = ConfigReader.get_deleteUserByUserNameEndpoint()
        self.ud.deleteUserByUsername(self.baseURL + deleteUserEndPointURL, "ranjith85")

