import time
from traceback import print_stack
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.seleniumDriver import SeleniumDriver
import logging

from pages.inventoryPage import InventoryPage
from pages.loginPage import LoginPage
from pages.cartPage import CartPage


class CheckoutPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.cartPage = CartPage(driver)

    # locators
    # Checkout-address-screen
    _firstNameLocator = "//input[@id='first-name']"
    _lastNameLocator = "//input[@id='last-name']"
    _zipPostalCodeLogator = "//input[@id='postal-code']"
    _cancelLocator = "//button[@id='cancel']"
    _continueLocator = "//input[@id='continue']"
    # Checkout-Confirm-screen
    _checkoutItemLocator = "//div[@class='inventory_item_name']"
    _paymentInformationLocator = "//div[@data-test='payment-info-value']"
    _shippingInformationLocator = "//div[@data-test='shipping-info-value']"
    _totalLocator = "//div[@data-test='total-label']"
    _checkoutCancelLocator = "//button[@id='cancel']"
    _finishLocator = "//button[@id='finish']"
    # Checkout-Complete-screen
    _completeLocator = "//span[@data-test='title']"
    _successMessageHeaderLocator = "//h2[@class='complete-header']"
    _backHomeLocator = "//button[@id='back-to-product']"

    def verifyCheckoutAddressTitle(self):
        self.headerText = self.cartPage.getCartTitleText()
        print(f"Cart title is {self.headerText}")
        assert self.headerText == "Checkout: Your Information"

    def verifyCheckoutOverviewTitle(self):
        self.headerText = self.cartPage.getCartTitleText()
        print(f"Cart title is {self.headerText}")
        assert self.headerText == "Checkout: Overview"

    def verifyCheckoutCompleteTitle(self):
        self.headerText = self.cartPage.getCartTitleText()
        print(f"Cart title is {self.headerText}")
        assert self.headerText == "Checkout: Complete!"

    def enterFirstname(self, name):
        self.clearField(self._firstNameLocator)
        self.sendKeys(name, self._firstNameLocator)

    def enterLastname(self, name):
        self.clearField(self._lastNameLocator)
        self.sendKeys(name, self._lastNameLocator)

    def enterZipcode(self, zip):
        self.clearField(self._zipPostalCodeLogator)
        self.sendKeys(zip, self._zipPostalCodeLogator)

    def clickContinueButton(self):
        self.elementClick(self._continueLocator, locatorType="xpath")

    def clickCancelButton(self):
        self.elementClick(self._cancelLocator, locatorType="xpath")

    def clickFinishButton(self):
        self.elementClick(self._finishLocator, locatorType="xpath")

    def clickBackButton(self):
        self.elementClick(self._backHomeLocator, locatorType="xpath")

    def enterAddressDetails(self, firstName, lastName, zipCode):
        self.enterFirstname(firstName)
        self.enterLastname(lastName)
        self.enterZipcode(zipCode)
        self.screenShot()
        self.clickContinueButton()

    def getSuccessMessage(self):
        self.waitForElement(self._successMessageHeaderLocator)
        element = self.driver.find_element(By.XPATH, self._successMessageHeaderLocator)
        return element.text

    def verifyOrderSuccessMessage(self):
        self.headerText = self.getSuccessMessage()
        print(f"Message is {self.headerText}")
        assert self.headerText == "Thank you for your order!"
        self.screenShot()

    def proceedToCheckout(self, items, firstName, lastName, zipCode):
        self.verifyCheckoutAddressTitle()
        self.enterAddressDetails(firstName, lastName, zipCode)
        self.verifyCheckoutOverviewTitle()
        self.cartPage.verifyItemsinCart(items)
        self.screenShot()
        self.clickFinishButton()

