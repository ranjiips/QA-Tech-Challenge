import time
from traceback import print_stack
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.seleniumDriver import SeleniumDriver
import logging

from pages.loginPage import LoginPage


class InventoryPage(SeleniumDriver):
    _instance = None

    def __new__(cls, driver):
        if cls._instance is None:
            cls._instance = super(InventoryPage, cls).__new__(cls)
            cls._instance._initialize(driver)
        return cls._instance

    def _initialize(self, driver):
        self.driver = driver

    # locators
    _inventoryMenuLocator="//button[@id='react-burger-menu-btn']"
    _logoutLocator="//a[@id='logout_sidebar_link']"
    _productLocator="//span[@class='title']"
    _productListLocator="//div[@data-test='inventory-item-name']"
    _cartCountLocator="//span[@class='shopping_cart_badge']"
    _swaglabHeaderLocator = "//div[@class='app_logo']"
    _cartButton = "//div[text()='ITEM_NAME']/ancestor::div[@class='inventory_item_label']/following-sibling::div/button"

    def clickHamburgerMenu(self):
        self.elementClick(self._inventoryMenuLocator, locatorType="xpath")

    def clickLogoutLink(self):
        self.waitForElement(self._logoutLocator, locatorType="xpath")
        self.elementClick(self._logoutLocator, locatorType="xpath")

    def logout(self):
        self.clickHamburgerMenu()
        self.clickLogoutLink()
        self.loginObj = LoginPage(self.driver)
        self.headerText = self.loginObj.getLoginPageHeaderText()
        print(f"Successfully logged out. Login screen loaded with text is {self.headerText}")

    def veriryInventoryHeader(self):
        self.headerText = self.getInventroyHeaderText()
        print(f"Inventory Header text is {self.headerText}")
        assert self.headerText == "Swag Labs"

    def getInventroyHeaderText(self):
        self.waitForElement(self._swaglabHeaderLocator, locatorType="xpath")
        element = self.driver.find_element(By.XPATH, self._swaglabHeaderLocator)
        return element.text

    def getItemName(self):
        elementList = self.driver.find_elements(By.XPATH, self._productListLocator)
        itemNames = []
        for ele in elementList:
            itemNames.append(ele.text)
        return itemNames

    def isItemListed(self, itemName):
        itemNames = self.getItemName()
        return any(item == itemName for item in itemNames)

    def addItemIntoCart(self, item):
        locator = self._cartButton.replace("ITEM_NAME",item)
        self.scrollToElement(locator)
        element = self.driver.find_element(By.XPATH, locator)
        if element.text == "Add to cart":
            self.elementClick(locator, locatorType="xpath")
            return True
        else:
            return False

    def removeItemFromCart(self, item):
        locator = self._cartButton.replace("ITEM_NAME",item)
        self.scrollToElement(locator)
        element = self.driver.find_element(By.XPATH, locator)
        if element.text == "Remove":
            self.elementClick(locator, locatorType="xpath")
            return True
        else:
            return False

    def getCartCount(self):
        self.waitForElement(self._cartCountLocator, locatorType="xpath")
        element = self.driver.find_element(By.XPATH, self._cartCountLocator)
        return int(element.text)




