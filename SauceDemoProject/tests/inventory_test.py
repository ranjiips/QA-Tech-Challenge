import logging
import pytest
import unittest

from pages.inventoryPage import InventoryPage
from pages.loginPage import LoginPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class InventoryTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.lp = LoginPage(self.driver)
        self.ip = InventoryPage(self.driver)

    @pytest.mark.run(order=1)
    def test_getItemNames(self):
        print("*#" * 20)
        print("Get items as list")
        print("*#" * 20)
        self.lp.login("standard_user", "secret_sauce")
        self.ip.veriryInventoryHeader()
        itemNames = self.ip.getItemName()
        print("Item Names: ", itemNames)
        assert len(itemNames) > 0
        self.ip.logout()

    @pytest.mark.run(order=2)
    def test_verifyValidItems(self):
        print("*#" * 20)
        print("Verify item in the list")
        print("*#" * 20)
        self.lp.login("standard_user", "secret_sauce")
        self.ip.veriryInventoryHeader()
        assert self.ip.isItemListed("Sauce Labs Bolt T-Shirt") == True
        self.ip.logout()

    @pytest.mark.run(order=3)
    def test_verifyInValidItems(self):
        print("*#" * 20)
        print("Verify InValid item in the list")
        print("*#" * 20)
        self.lp.login("standard_user", "secret_sauce")
        self.ip.veriryInventoryHeader()
        assert self.ip.isItemListed("Sauce Labs Bolt Shorts") == False
        self.ip.logout()

    @pytest.mark.run(order=4)
    def test_addItemIntoCart(self):
        print("*#" * 20)
        print("Add Item into Cart")
        print("*#" * 20)
        self.lp.login("standard_user", "secret_sauce")
        self.ip.veriryInventoryHeader()
        assert self.ip.addItemIntoCart("Sauce Labs Bolt T-Shirt") == True
        assert self.ip.addItemIntoCart("Sauce Labs Bike Light") == True
        print(f"Cart Count: {self.ip.getCartCount()}")
        assert self.ip.getCartCount()==2
        self.ip.logout()

    @pytest.mark.run(order=5)
    def test_removeItemFromCart(self):
        print("*#" * 20)
        print("Remove Item from Cart")
        print("*#" * 20)
        self.lp.login("standard_user", "secret_sauce")
        self.ip.veriryInventoryHeader()
        print(f"Cart Count: {self.ip.getCartCount()}")
        assert self.ip.removeItemFromCart("Sauce Labs Bolt T-Shirt") == True
        assert self.ip.removeItemFromCart("Sauce Labs Bike Light") == True
        self.ip.logout()
