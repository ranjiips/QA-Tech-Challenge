import logging
import pytest
import unittest

from pages.inventoryPage import InventoryPage
from pages.loginPage import LoginPage

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
        self.lp.login("standard_user", "secret_sauce")
        self.ip.veriryInventoryHeader()
        self.ip.logout()

    @pytest.mark.login
    def test_invalidUser(self):
        print("*#" * 20)
        print("In valid Credentials Test case")
        print("*#" * 20)
        self.lp.login("locked_out_user", "secret_sauce")
        errorText = self.lp.getLoginErrorMessage()
        print(f"Error message: {errorText}")

