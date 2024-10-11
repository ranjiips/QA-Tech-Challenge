import time
from traceback import print_stack
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.seleniumDriver import SeleniumDriver
import logging

class LoginPage(SeleniumDriver):
    _instance = None

    def __new__(cls, driver):
        if cls._instance is None:
            cls._instance = super(LoginPage, cls).__new__(cls)
            cls._instance._initialize(driver)
        return cls._instance

    def _initialize(self, driver):
        self.driver = driver

    # locators
    _swaglabTitleLocator = "//div[@class='login_logo']"
    _usernameLocator = "//input[@id='user-name']"
    _passwordLocator = "//input[@id='password']"
    _submitbuttonLocator = "//input[@id='login-button']"
    _loginErrorLocator = "//div[@class='error-message-container error']/h3"


    def enterUsername(self, email):
        self.clearField(self._usernameLocator)
        self.sendKeys(email, self._usernameLocator)

    def enterPassword(self, password):
        self.clearField(self._passwordLocator)
        self.sendKeys(password, self._passwordLocator)

    def clickLoginButton(self):
        self.elementClick(self._submitbuttonLocator, locatorType="xpath")

    def login(self, userName="", password=""):
        self.headerText = self.getLoginPageHeaderText()
        print(f"Login Header text is {self.headerText}")
        assert self.headerText == "Swag Labs"
        self.enterUsername(userName)
        self.enterPassword(password)
        self.clickLoginButton()

    def getLoginPageHeaderText(self):
        self.waitForElement(self._swaglabTitleLocator, locatorType="xpath")
        element = self.driver.find_element(By.XPATH, self._swaglabTitleLocator)
        return element.text

    def getLoginErrorMessage(self):
        self.waitForElement(self._loginErrorLocator, locatorType="xpath")
        element = self.driver.find_element(By.XPATH, self._loginErrorLocator)
        return element.text
