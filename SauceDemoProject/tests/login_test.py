import logging
import pytest
import unittest

from pages.inventoryPage import InventoryPage
from pages.loginPage import LoginPage
# from utilities.readConfig import ReadConfig
from utilities.readConfig import ConfigReader

# Execution Command:
# python -m pytest tests/login_test.py -v -s --html=reports/loginReport.html  --browser=chrome

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.lp = LoginPage(self.driver)
        self.ip = InventoryPage(self.driver)

    @pytest.mark.login
    def test_validLogin(self):
        print("*#" * 20)
        print("Valid Login Test case")
        print("*#" * 20)
        username = ConfigReader.get_Username()
        password = ConfigReader.get_Password()
        self.lp.login(username, password)
        self.ip.veriryInventoryHeader()
        self.ip.logout()

    @pytest.mark.login
    def test_invalidUser(self):
        print("*#" * 20)
        print("In valid Credentials Test case")
        print("*#" * 20)
        username = ConfigReader.get_LockedUsername()
        password = ConfigReader.get_Password()
        self.lp.login(username, password)
        errorText = self.lp.getLoginErrorMessage()
        print(f"Error message: {errorText}")

