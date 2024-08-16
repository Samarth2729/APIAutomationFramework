# Python API Automation Framework 
### Tech Stack 
 - Python 3.12
 - Request - HTTP Request 
 - Pytest - Testing Framework
 - Reporting - ALlure report, Pytest XML
 - Test Data - CSV,Excel,JSON,Faker
 - Advance API Testcase - jsonschema
 - Parallel Execution - x distribute (xidist)

### How to install Packages

``` pip install requests pytest pytest-html faker allure-pytest jsonschema ```

### How to run your Testcase Parallel

``` pip install pytest-xidst```

### How to add the .gitignore File.

Copy the content from this to .gitignore file
https://www.toptal.com/developers/gitignore/api/pycharm

### How the run basic test case with allure report
``` tests/tests/crud/test_create_booking.py --alluredir=allure_result -s```



