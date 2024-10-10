import logging
import pytest
import unittest

from pages.inventoryPage import InventoryPage
from pages.loginPage import LoginPage
from pages.checkoutPage import CheckoutPage
from pages.cartPage import CartPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CheckoutTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.lp = LoginPage(self.driver)
        self.ip = InventoryPage(self.driver)
        self.ch = CheckoutPage(self.driver)
        self.car = CartPage(self.driver)

    @pytest.mark.cart
    def test_verifyItemsinCart(self):
        print("*#" * 20)
        print("Verify Items in Cart")
        print("*#" * 20)
        self.lp.login("standard_user", "secret_sauce")
        self.ip.veriryInventoryHeader()
        assert self.ip.addItemIntoCart("Sauce Labs Bolt T-Shirt") == True
        assert self.ip.addItemIntoCart("Sauce Labs Bike Light") == True
        print(f"Cart Count: {self.ip.getCartCount()}")
        assert self.ip.getCartCount() == 2
        items = {
            "product1": {"name": "Sauce Labs Bolt T-Shirt", "price": "$15.99", "quantity": "1"},
            "product2": {"name": "Sauce Labs Bike Light", "price": "$9.99", "quantity": "1"},
        }
        self.car.verifyCart(items)
        self.car.clickContinueShoppingButton()
        assert self.ip.removeItemFromCart("Sauce Labs Bolt T-Shirt") == True
        assert self.ip.removeItemFromCart("Sauce Labs Bike Light") == True
        self.ip.logout()