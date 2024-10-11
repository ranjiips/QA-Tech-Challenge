# Swagger Petstore API

## Objective
The Swagger Petstore API is a sample API provided by Swagger to demonstrate the capabilities of the Swagger framework and the OpenAPI Specification.

**API Endpoints:** 
The API provides a variety of endpoints for different operations, such as:
+ _/pet_: Manage pet information.
+ _/store/order_: Manage store orders.
+ _/user_: Manage user accounts.

### Key Test Cases:
1. **Pet Management:**
   * **Create Pet:** Verify that a new pet can be added to the store.
   * **Get Pet by ID:** Ensure that the correct pet details are returned for a given pet ID.
   * **Update Pet:** Check that pet details can be updated successfully.
   * **Delete Pet:** Confirm that a pet can be deleted from the store.
2. **Store Order Management:**
   * **Place Order:** Validate that an order can be placed for a pet.
   * **Get Order by ID:** Ensure that the correct order details are returned for a given order ID.
   * **Delete Order:** Verify that an order can be deleted from the store.
3. **User Management:**
   * **Create User:** Verify that a new user can be created.
   * **Get User by Username:** Ensure that the correct user details are returned for a given username.
   * **Update User:** Check that user details can be updated successfully.
   * **Delete User:** Confirm that a user can be deleted from the system.

# Project Overview
The primary objective of this project is to automate the API of the petstore using Python and Request. The goal is to ensure the website’s key functionalities, such as managing pets, store orders, and user accounts.

We are following the Page Object Model and **_Singleton pattern_** ensuring that only one instance of each page class is used throughout the tests. The test methods use the Singleton instances to perform actions and verifications

### Tools and Technologies:
+ **Request Library:** For automating the rest APIs.
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
- **Pet test cases:** 
```bash 
python -m pytest tests/pet_test.py -v -s --html=reports/petReport.html
```
- **Pet Store Test cases**
```bash 
python -m pytest tests/petStore_test.py -v -s --html=reports/petStoreReport.html
```
- **User Test cases**
```bash 
python -m pytest tests/user_test.py -v -s --html=reports/userReport.html
```


***Command Explanation***

When you run this command, **_pytest_** will:

+ Execute the tests in **_tests/pet_test.py_**.
+ Provide detailed output due to the **_-v_** option.
+ Show print statements and other outputs in the console because of the **_-s_** option.
+ Generate an HTML report of the test results and save it to **_reports/petReport.html_**.

**To run the test parallely, use the below command** 
```bash 
python -m pytest tests/pet_test.py -v -s -n 3 --html=reports/petReport.html
```
* **_-n 3_** Run the tests in parallel using 3 worker processes, which can speed up the execution.

**To run the specific marker/tag:**
```bash 
python -m pytest -m pet
```
