**Sauce Lab automation:**

**Pre-Requiste:**
Install python 3.12
Install Pycharm Community edition
run the  below commands from terminal/command window
    pip install pip
    pip install pytest
    pip install selenium

**Enable the pytest test runner by following the below steps**
Select the Edit Configuration under Run menu
Select + symbol -> Python Tests -> pytest option

**Pytest Execution commands:**
python -m pytest -v -s tests\{file_name}.py

for pytest execution, from command line/Terminal use the below command
To run all the test methods in the project (-s to print statements; -v for verbose)
    python -m pytest --browser=chrome    
To run the specific test case file
    python -m pytest tests/checkout_test.py --browser=chrome

**for Ordering**, install the below
"pip install pytest-ordering"

**To capture the reports,** 
Install "pip install pytest-html"

then run the below command:
python -m pytest tests/{testCaseFilename}.py -v -s --html=reports/{reportName}.html
**Example:**
python -m pytest tests/test_login.py -v -s --html=reports/loginReport.html

**To run the specific marker:**
python -m pytest -m login


**To run the test in parallel**, install thhe package "pip install pytest-xdist"
**Command**: python -m pytest -v -s tests\test_login.py -n 3
here -n 3 is the number  of workers/threads. We are running 3 threads in parallel

**Command to Execute with specific browser with thread**
**_Example_**: 
python -m pytest tests/test_loginClass.py -v -s --html=reports/loginReport.html -n 3 --browser=chrome