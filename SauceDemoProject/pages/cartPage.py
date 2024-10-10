import time
from traceback import print_stack
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.seleniumDriver import SeleniumDriver
import logging

from pages.inventoryPage import InventoryPage
from pages.loginPage import LoginPage
# from pages.checkoutPage import CheckoutPage


class CartPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _cartLocator = "//div[@id='shopping_cart_container']/a"
    _cartTitleLocator = "//span[@class='title']"
    _cartContinueShoppingButtonLocator = "//button[@id='continue-shopping']"
    _cartCheckoutButtonLocator = "//button[@id='checkout']"
    _cartItemPrice = "//div[text()='ITEM_NAME']/ancestor::div[@class='cart_item_label']//div[@class='inventory_item_price']"
    _cartQuantityLocator = "//div[text()='ITEM_NAME']/ancestor::div[@class='cart_item']/div[@class='cart_quantity']"

    def verifyItemsinCart(self, itemDetails):
        # self.clickCartIcon()
        # self.waitForElement(self._cartTitleLocator)
        # self.verifyCartTitle()
        item_names = list(itemDetails.keys())
        for productname in item_names:
            itemName = itemDetails[productname]["name"]
            itemPrice = itemDetails[productname]["price"]
            itemQuantity = itemDetails[productname]["quantity"]
            print(f"Product name: {itemName}, Price: {itemPrice}, Quantity: {itemQuantity}")

            priceLocator = self._cartItemPrice.replace("ITEM_NAME", itemName)
            qtylocator = self._cartQuantityLocator.replace("ITEM_NAME", itemName)

            self.waitForElement(priceLocator)
            element = self.driver.find_element(By.XPATH, priceLocator)
            itemPriceInCart = element.text
            print(f"Price from cart: {itemPriceInCart}")

            self.waitForElement(qtylocator)
            element = self.driver.find_element(By.XPATH, qtylocator)
            itemQtyInCart = element.text
            print(f"Quantity from cart: {itemQtyInCart}")

            assert itemPrice==itemPriceInCart
            assert itemQuantity==itemQtyInCart
        self.screenShot()



    def clickCartIcon(self):
        self.waitForElement(self._cartLocator)
        self.elementClick(self._cartLocator)

    def clickContinueShoppingButton(self):
        self.waitForElement(self._cartContinueShoppingButtonLocator)
        self.elementClick(self._cartContinueShoppingButtonLocator)

    def clickCheckoutButton(self):
        self.waitForElement(self._cartCheckoutButtonLocator)
        self.elementClick(self._cartCheckoutButtonLocator)

    def getCartTitleText(self):
        self.waitForElement(self._cartTitleLocator)
        element = self.driver.find_element(By.XPATH, self._cartTitleLocator)
        return element.text

    def verifyCartTitle(self):
        self.headerText = self.getCartTitleText()
        print(f"Cart title is {self.headerText}")
        assert self.headerText == "Your Cart"

    def verifyCart(self, items):
        self.clickCartIcon()
        self.waitForElement(self._cartTitleLocator)
        self.verifyCartTitle()
        self.verifyItemsinCart(items)
        self.screenShot()


    