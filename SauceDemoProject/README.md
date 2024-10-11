# Swag Lab Web Automation

## Objective

The primary objective of this project is to automate the testing of the SauceDemo website using Selenium WebDriver and Python. The goal is to ensure the website’s key functionalities, such as user authentication, product management, and checkout processes, perform as expected under various scenarios.

### Scope:
The scope of this project includes:

- **User Authentication:** Testing login and logout functionalities with various user roles.
- **Product Management:** Verifying product listings, details, and interactions such as adding/removing items from the cart.
- **Checkout Process:** Ensuring the checkout process, including payment and order confirmation, works correctly.
- **Error Handling:** Testing the system’s response to invalid inputs and user actions.


## Features to be Tested:
### Login Functionality:
* Valid login with standard user credentials.
* Handling of locked-out users.
* Error messages for invalid login attempts.
### Product Verification:
* Verify product details are displaying.
* Verify Item is listed in the product screen.
* Verify Invalid Item is listed in the product screen.
* Adding and removing products from the cart.
### Cart Operations:
* Verifying items in the cart.
* Persisting cart state across sessions.
### Checkout Process:
* Navigating through the checkout process.
* Verifying items in the cart.
* Validating payment and order confirmation steps.
* Verify the messages.

# Project Overview
This automation project aims to ensure that the SauceDemo website functions correctly and provides a seamless user experience by identifying and addressing any issues through automated testing.

We are following the Page Object Model and **_Singleton pattern_** ensuring that only one instance of each page class is used throughout the tests. The test methods use the Singleton instances to perform actions and verifications

### Tools and Technologies:
+ **Selenium WebDriver:** For automating web browser interactions.
+ **Python:** As the programming language for writing test scripts.
+ **Pytest:** For managing and executing test cases.
+ **ConfigParser:** For managing configuration settings.
+ **CI/CD Integration:** To enable continuous testing and integration.
+ **HTML Reports:** To capture the execution reports in HTML format.

### Pre-Requiste:
- Install python 3.12
- Install Pycharm Community edition- 
- Install Git

## Getting Started
Once you met all the pre-requiste requirements, follow the below commands

* Create a local folder as per your wish to clone the project [Ex: Project]
* Open Git Bash from the folder
* Clone the project by using the command
```bash 
https://github.com/ranjiips/QA-Tech-Challenge.git 
```
* To make sure you have the latest code, run the below git command
```bash 
git fetch
git pull origin
```
* Install the required libraries from the file "requirements.txt"
* Enable the pytest test runner by following the below steps**
  * > Select the Edit Configuration under Run menu
  * > Select + symbol -> Python Tests -> pytest option

Once all the setup completes, then start execute the test cases by following the below execution commands

**Pytest Execution commands:**
- **Login test cases:** 
```bash 
python -m pytest tests/login_test.py -v -s --html=reports/loginReport.html  --browser=chrome
```
- **Product Page Test cases**
```bash 
python -m pytest tests/inventory_test.py -v -s --html=reports/inventoryReport.html  --browser=chrome
```
- **Cart Validation Test cases**
```bash 
python -m pytest tests/cart_test.py -v -s --html=reports/cartReport.html  --browser=chrome
```
- **Checkout Test cases**
```bash 
python -m pytest tests/checkout_test.py -v -s --html=reports/checkoutReport.html  --browser=chrome
```

***Command Explanation***

When you run this command, **_pytest_** will:

+ Execute the tests in **_tests/checkout_test.py_**.
+ Provide detailed output due to the **_-v_** option.
+ Show print statements and other outputs in the console because of the **_-s_** option.
+ Generate an HTML report of the test results and save it to **_reports/checkoutReport.html_**.
+ Use Chrome as the browser for the tests, as specified by the **_--browser=chrome_** option.

**To run the test parallely, use the below command** 
```bash 
python -m pytest tests/inventory_test.py -v -s -n 3 --html=reports/inventoryReport.html  --browser=chrome
```

* **_-n 3_** Run the tests in parallel using 3 worker processes, which can speed up the execution.

**To run the specific marker/tag:**
```bash 
python -m pytest -m login
```
